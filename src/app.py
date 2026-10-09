#!/usr/bin/env python3
"""ProofPay demo app (D2): order -> authorize -> generate -> 9 checks -> capture/void.
Demo mode: payment state machine mirrors the sandbox-verified D1 flow
(authorize 201 / capture 201 COMPLETED / void 204 VOIDED on 2026-10-09).
Set PAYPAL_CLIENT_ID/PAYPAL_CLIENT_SECRET env to wire live sandbox calls later."""
import json, html, os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
sys.path.insert(0, os.path.dirname(__file__))
from check import check
from generate import generate

BASE = os.path.join(os.path.dirname(__file__), "..")
TASK = json.load(open(os.path.join(BASE, "examples/task.json")))
SNAP = json.load(open(os.path.join(BASE, "examples/snapshot.json")))
STATE = {}  # task_id -> {status, generated, results, decision, tamper}

CSS = "body{font-family:system-ui;max-width:760px;margin:40px auto;padding:0 16px;color:#14213d}h1{font-size:24px}.card{border:1px solid #ddd;border-radius:12px;padding:20px;margin:16px 0}.ok{color:#0a7d2c}.bad{color:#c0392b}.light{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:8px}button{background:#0070e0;color:#fff;border:0;border-radius:8px;padding:10px 18px;font-size:15px;cursor:pointer}code{background:#f2f2f2;padding:2px 6px;border-radius:4px}.muted{color:#666;font-size:13px}"

BANNER = "<p class=muted style='border:1px dashed #999;border-radius:8px;padding:8px 12px'><b>Local demo</b> — this run executes on your machine; no live charge happens here. The payment evidence behind it comes from a separately verified PayPal sandbox run (2026-10-09).</p>"
def page(title, body):
    return f"<!doctype html><html lang=en><meta charset=utf-8><title>{title} · ProofPay</title><style>{CSS}</style><h1>ProofPay</h1>{BANNER}{body}</html>".encode()

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def send_html(self, body, title="ProofPay"):
        self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
        self.wfile.write(page(title, body))
    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        if u.path == "/":
            t = TASK
            body = f"""<div class=card><h2>1 · Order &amp; freeze</h2>
            <p>Service: <b>AI deal brief</b> from PriceScout snapshot <code>{t['snapshot_id']}</code> ({len(SNAP['items'])} items)</p>
            <p>Amount: <b>${t['amount']['value']} {t['amount']['currency']}</b> · Deliverable: {t['deliverable_spec']['item_count']} items, ≤{t['deliverable_spec']['max_chars']} chars</p>
            <p class=muted>Your money is only <b>authorized (frozen)</b> now. It is captured only if the AI output passes all 9 objective checks — otherwise the authorization is voided and you pay nothing.</p>
            <form method=post action=/order><label><input type=checkbox name=tamper value=1> Fault injection: make the AI use a wrong price (demo of the VOID path)</label>
            <p><button>Place order &amp; freeze ${t['amount']['value']}</button></p></form></div>"""
            self.send_html(body, "Order")
        elif u.path == "/review":
            tid = q.get("task", [""])[0]; st = STATE.get(tid)
            if not st: self.send_html("<p>Unknown task.</p>"); return
            lights = "".join(f"<p><span class=light style='background:{'#0a7d2c' if v else '#c0392b'}'></span>{html.escape(k)} — <b class={'ok' if v else 'bad'}>{'PASS' if v else 'FAIL'}</b></p>" for k, v in st["results"])
            dec = st["decision"]
            body = f"""<div class=card><h2>2 · Generated brief &amp; verification</h2>
            <p><i>{html.escape(st['generated']['text'])}</i></p>{lights}
            <p>Decision: <b class={'ok' if dec=='CAPTURE' else 'bad'}>{'9/9 passed → CAPTURE' if dec=='CAPTURE' else 'A check failed → VOID (you pay nothing)'}</b></p>
            <form method=post action=/settle?task={tid}><button>{'Capture $'+TASK['amount']['value'] if dec=='CAPTURE' else 'Void authorization'}</button></form></div>"""
            self.send_html(body, "Review")
        elif u.path == "/receipt":
            tid = q.get("task", [""])[0]; st = STATE.get(tid)
            if not st: self.send_html("<p>Unknown task.</p>"); return
            if st["status"] == "CAPTURED":
                body = f"""<div class=card><h2>3 · Payment receipt</h2><p class=ok><b>Paid ${TASK['amount']['value']} {TASK['amount']['currency']}</b> — capture COMPLETED</p>
                <p>Task <code>{tid}</code> · the brief passed all 9 checks, so the frozen authorization was captured.</p>
                <p class=muted>Payment evidence (separate PayPal sandbox run, 2026-10-09): authorize 201 → capture 201 COMPLETED. This local demo run did not move money.</p></div>"""
            else:
                fails = ", ".join(k for k, v in st["results"] if not v)
                body = f"""<div class=card><h2>3 · Authorization voided</h2><p class=bad><b>You pay $0.00</b> — authorization VOIDED</p>
                <p>Task <code>{tid}</code> · failed checks: <b>{html.escape(fails)}</b>. The frozen funds were released; no capture happened.</p>
                <p class=muted>Payment evidence (separate PayPal sandbox run, 2026-10-09): authorize 201 → void 204 → VOIDED. This local demo run did not move money.</p></div>"""
            body += "<p><a href='/'>← New order</a></p>"
            self.send_html(body, "Receipt")
        else:
            self.send_response(404); self.end_headers()
    def do_POST(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        length = int(self.headers.get("Content-Length", 0)); form = parse_qs(self.rfile.read(length).decode())
        if u.path == "/order":
            tid = TASK["task_id"]
            tamper = form.get("tamper", [""])[0] == "1"
            gen = generate(TASK, SNAP, tamper_price=tamper)
            results = check(TASK, SNAP, gen)
            decision = "CAPTURE" if all(v for _, v in results) else "VOID"
            STATE[tid] = {"status": "AUTHORIZED", "generated": gen, "results": results, "decision": decision, "tamper": tamper}
            self.send_response(303); self.send_header("Location", f"/review?task={tid}"); self.end_headers()
        elif u.path == "/settle":
            tid = q.get("task", [""])[0]; st = STATE.get(tid)
            if st: st["status"] = "CAPTURED" if st["decision"] == "CAPTURE" else "VOIDED"
            self.send_response(303); self.send_header("Location", f"/receipt?task={tid}"); self.end_headers()
        else:
            self.send_response(404); self.end_headers()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    print(f"ProofPay demo on http://127.0.0.1:{port}")
    HTTPServer(("127.0.0.1", port), H).serve_forever()
