import json
from datetime import datetime, timezone

GEN_VERSION = "gen-1.0"

def generate(task, snap, tamper_price=False, now=None):
    """Deterministic deal-brief generator over a PriceScout snapshot.
    tamper_price=True injects one wrong price (fault-injection demo for VOID path)."""
    now = now or datetime.now(timezone.utc)
    items = []
    parts = []
    for i, it in enumerate(snap["items"][: task["deliverable_spec"]["item_count"]]):
        price = it["price_new"]
        if tamper_price and i == 0:
            price = "9.99"  # injected fault: price not in snapshot
        items.append({"sku": it["sku"], "price": price, "currency": it["currency"], "url": it["url"]})
        parts.append(f"{it['title']} now ${price} (was ${it['price_old']})")
    text = "Deal brief: " + "; ".join(parts) + f". Sources in snapshot {snap['snapshot_id']}."
    return {
        "generated_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator_version": GEN_VERSION,
        "amount": task["amount"],
        "text": text,
        "items": items,
    }

if __name__ == "__main__":
    import sys
    task = json.load(open("examples/task.json")); snap = json.load(open("examples/snapshot.json"))
    tamper = "--tamper" in sys.argv
    print(json.dumps(generate(task, snap, tamper_price=tamper), indent=1))
