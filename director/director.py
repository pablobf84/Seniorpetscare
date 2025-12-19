import json
import os
from datetime import datetime
from integrations.telegram.notify import send_telegram

STATE_DIR = "state"
SNAPSHOT_FILE = os.path.join(STATE_DIR, "shopify_snapshot.json")
ACTIONS_FILE = os.path.join("decisions", "actions_pending.json")
REPORT_FILE = os.path.join("decisions", "daily_reports.md")


def load_snapshot() -> dict:
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"products": []}


def propose_actions(snapshot: dict, max_actions: int = 10) -> list:
    actions = []
    products = snapshot.get("products", [])
    for product in products:
        for variant in product.get("variants", {}).get("nodes", []):
            if not variant.get("sku"):
                # Construct a simple SKU using the last 6 characters of the variant ID.
                # Use single quotes inside the f-string to avoid conflicts with outer quotes.
                new_sku = f"SKU-{variant['id'][-6:]}"[:63]
                actions.append({
                    "type": "FIX_SKU",
                    "product_id": product["id"],
                    "variant_id": variant["id"],
                    "new_sku": new_sku,
                    "reason": "Variant without SKU"
                })
            if len(actions) >= max_actions:
                break
        if len(actions) >= max_actions:
            break
    return actions


def save_actions(actions: list, approved: bool = False) -> None:
    os.makedirs(os.path.dirname(ACTIONS_FILE), exist_ok=True)
    with open(ACTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at_utc": datetime.utcnow().isoformat() + "Z",
            "actions": actions,
            "approved": approved,
        }, f, ensure_ascii=False, indent=2)


def append_report(summary: str) -> None:
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(summary + "\n")


def main() -> None:
    snapshot = load_snapshot()
    products_count = len(snapshot.get("products", []))
    actions = propose_actions(snapshot, max_actions=int(os.environ.get("DIRECTOR_MAX_ACTIONS", 10)))
    save_actions(actions, approved=False)
    timestamp = datetime.utcnow().isoformat() + "Z"
    # Create a human-readable summary for the report and Telegram
    summary = (
        f"🧠 <b>GPT Director</b> ({timestamp})\n"
        f"📦 Productos en snapshot: <b>{products_count}</b>\n"
        f"🛠️ Acciones propuestas: <b>{len(actions)}</b>\n"
        f"🔒 Modo seguro: <b>NO se aplica nada sin aprobación</b>\n"
        f"📄 Revisa: decisions/actions_pending.json"
    )
    append_report(summary)
    send_telegram(summary)


if __name__ == "__main__":
    main()
