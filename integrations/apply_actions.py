import os
import json
import urllib.request
from typing import Dict, Any, List
from integrations.design.apply_design import main as apply_design_main

# This is a stub implementation for applying actions to Shopify.
# It reads decisions/actions_pending.json and, if approved, iterates
# through actions and applies safe modifications via the Shopify API.


def load_actions(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_log(message: str) -> None:
    os.makedirs("decisions", exist_ok=True)
    with open("decisions/apply_log.md", "a", encoding="utf-8") as f:
        f.write(message + "\n")


def shopify_rest(endpoint: str, method: str = "GET", payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
    store = os.environ.get("SHOPIFY_STORE")
    token = os.environ.get("SHOPIFY_ADMIN_TOKEN")
    version = os.environ.get("SHOPIFY_API_VERSION", "2025-01")
    if not store or not token:
        raise RuntimeError("Missing SHOPIFY_STORE or SHOPIFY_ADMIN_TOKEN environment variables")
    url = f"https://{store}.myshopify.com/admin/api/{version}/{endpoint}"
    data_bytes: bytes | None = None
    headers = {"X-Shopify-Access-Token": token, "Content-Type": "application/json"}
    if payload is not None:
        data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def apply_actions(actions: List[Dict[str, Any]]) -> None:
    for action in actions:
        action_type = action.get("type")
        # Example: implement safe action types
        if action_type == "FIX_SKU":
            variant_id = action.get("variant_id")
            new_sku = action.get("new_sku", "")
            if not variant_id or not new_sku:
                continue
            endpoint = f"variants/{variant_id}.json"
            payload = {"variant": {"id": variant_id, "sku": new_sku}}
            resp = shopify_rest(endpoint, method="PUT", payload=payload)
            save_log(f"Updated SKU for variant {variant_id}: {resp}")
        else:
            save_log(f"Unsupported action type: {action_type}")


def main() -> None:
    actions_path = "decisions/actions_pending.json"
    if not os.path.exists(actions_path):
        save_log("No actions_pending.json found.")
        return
    data = load_actions(actions_path)
    if not data.get("approved"):
        save_log("Actions not approved. Nothing applied.")
        return
    actions = data.get("actions", [])
    if not actions:
        save_log("No actions to apply.")
        return
    apply_actions(actions)
        apply_design_main()

        save_log("Finished applying actions.")


if __name__ == "__main__":
    main()
