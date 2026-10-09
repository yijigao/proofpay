import sys, json, urllib.request, urllib.error, base64
def api(method, path, token=None, body=None, cid=None, sec=None):
    url='https://api-m.sandbox.paypal.com'+path
    data=json.dumps(body).encode() if body is not None else (b'grant_type=client_credentials' if token is None else None)
    req=urllib.request.Request(url, method=method, data=data)
    if token is None:
        req.add_header('Authorization','Basic '+base64.b64encode(f"{cid}:{sec}".encode()).decode())
        req.add_header('Content-Type','application/x-www-form-urlencoded')
    else:
        req.add_header('Authorization','Bearer '+token); req.add_header('Content-Type','application/json')
    try:
        with urllib.request.urlopen(req, timeout=25) as r: return r.status, json.loads(r.read().decode() or '{}')
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode() or '{}')
        except Exception: return e.code, {}
lines=[l.strip() for l in sys.stdin.read().splitlines() if l.strip()]
cid, sec = lines[0], lines[1]
s, tok = api('POST','/v1/oauth2/token', cid=cid, sec=sec)
print('oauth', s, bool(tok.get('access_token'))); at=tok.get('access_token')
if not at: sys.exit(0)
# Order A intent AUTHORIZE
sA, oA = api('POST','/v2/checkout/orders', token=at, body={"intent":"AUTHORIZE","purchase_units":[{"reference_id":"proofpay-A","amount":{"currency_code":"USD","value":"10.00"}}]}, )
print('create_AUTH_A', sA, oA.get('id',''), oA.get('status',''), str(oA.get('name',''))[:40])
if oA.get('id'):
    sAu, rAu = api('POST', f"/v2/checkout/orders/{oA['id']}/authorize", token=at, body={})
    print('authorize_A', sAu, rAu.get('status',''), str(rAu.get('name', rAu.get('message','')))[:80])
