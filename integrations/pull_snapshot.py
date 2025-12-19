import os
import json
import urllib.request
from datetime import datetime

def shopify_graphql(query: str, variables=None) -> dict:
    """Execute a GraphQL query against Shopify's Admin API.

    Expects environment variables SHOPIFY_STORE, SHOPIFY_ADMIN_TOKEN and
    SHOPIFY_API_VERSION to be defined. Returns the parsed JSON response.
    """
    store = os.environ.get("SHOPIFY_STORE")
    token = os.environ.get("SHOPIFY_ADMIN_TOKEN")
    version = os.environ.get("SHOPIFY_API_VERSION", "2025-01")
    if not store or not token:
        raise RuntimeError("Missing SHOPIFY_STORE or SHOPIFY_ADMIN_TOKEN environment variables")

    url = f"https://{store}.myshopify.com/admin/api/{version}/graphql.json"
    payload = json.dumps({"query": query, "variables": variables or {}}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "X-Shopify-Access-Token": token,
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> None:
    """Pull a snapshot of products and their variants from Shopify and save to state."""
    query = """
    query {
      products(first: 50) {
        nodes {
          id
          title
          handle
          status
          vendor
          productType
          tags
          variants(first: 50) {
            nodes {
              id
              title
              sku
              price
              availableForSale
            }
          }
        }
      }
    }
    """
    data = shopify_graphql(query)
    snapshot = {
        "fetched_at_utc": datetime.utcnow().isoformat() + "Z",
        "products": data.get("data", {}).get("products", {}).get("nodes", []),
        "errors": data.get("errors", []),
    }
    os.makedirs("state", exist_ok=True)
    with open("state/shopify_snapshot.json", "w", encoding="utf-8") as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
