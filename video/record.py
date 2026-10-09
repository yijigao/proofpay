import asyncio, os
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8080"
OUT = os.path.join(os.path.dirname(__file__), "clips")
os.makedirs(OUT, exist_ok=True)

async def captions(page, text):
    await page.evaluate("""(t)=>{
      let d=document.getElementById('cap');
      if(!d){d=document.createElement('div');d.id='cap';
        d.style='position:fixed;left:0;right:0;bottom:0;background:rgba(10,20,40,.88);color:#fff;font:600 26px system-ui;padding:18px 28px;z-index:9999;line-height:1.35';
        document.body.appendChild(d);}
      d.textContent=t;}""", text)

S=2.3
async def run():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        ctx = await browser.new_context(viewport={"width":1280,"height":800},
                                        record_video_dir=OUT, record_video_size={"width":1280,"height":800})
        page = await ctx.new_page()
        # ---- CAPTURE path ----
        await page.goto(BASE + "/")
        await captions(page, "Pay first and hope the AI output is right? ProofPay freezes your money instead — it is only paid when the output checks out.")
        await page.wait_for_timeout(int(S*5000))
        await captions(page, "The buyer orders an AI deal brief for $10. PayPal AUTHORIZE freezes the funds — nothing is captured yet.")
        await page.wait_for_timeout(int(S*4000))
        await page.click("text=Place order")
        await page.wait_for_timeout(int(S*1500))
        await captions(page, "The AI generated the brief from a frozen PriceScout snapshot. Nine objective checks now run — count, length, source binding, price, currency, freshness, deadline, amount, dedup.")
        await page.wait_for_timeout(int(S*6000))
        await captions(page, "9 of 9 checks pass — so the frozen authorization is captured.")
        await page.wait_for_timeout(int(S*3500))
        await page.click("text=Capture")
        await page.wait_for_timeout(int(S*1500))
        await captions(page, "Paid $10.00 — capture COMPLETED. This exact flow was verified in the PayPal sandbox: authorize 201, capture 201 COMPLETED.")
        await page.wait_for_timeout(int(S*5000))
        # ---- VOID path ----
        await page.goto(BASE + "/")
        await captions(page, "Now the failure case: we inject a fault and make the AI quote a wrong price.")
        await page.wait_for_timeout(int(S*4000))
        await page.check("input[name=tamper]")
        await page.wait_for_timeout(int(S*1200))
        await page.click("text=Place order")
        await page.wait_for_timeout(int(S*1500))
        await captions(page, "One red light — the price does not match the snapshot. A single failed check voids the whole authorization.")
        await page.wait_for_timeout(int(S*5000))
        await page.click("text=Void authorization")
        await page.wait_for_timeout(int(S*1500))
        await captions(page, "You pay $0.00 — authorization VOIDED (sandbox-verified: void 204). The buyer gets the failed-item list, not a surprise charge.")
        await page.wait_for_timeout(int(S*5000))
        await captions(page, "ProofPay reuses the PriceScout feed and a rule-gate verification pattern. Open source, MIT — judges can run it with no credentials. Amount-to-live-order binding is a documented v1 gap; we show what is verified, and what is not.")
        await page.wait_for_timeout(int(S*6000))
        await ctx.close()
        await browser.close()

asyncio.run(run())
print("recorded to", OUT)
