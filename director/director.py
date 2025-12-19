import json
from datetime import date

STATE_DIR = 'state'
DECISIONS_FILE = 'decisions/daily_reports.md'

# Load state files
def load_state(filename):
    with open(f'{STATE_DIR}/{filename}', 'r', encoding='utf-8') as f:
        return json.load(f)

# Evaluate products: placeholder logic
def evaluate_products(products_state):
    actions = []
    for product in products_state.get('products', []):
        # Example rule: if sales < threshold and margin < threshold -> discard
        if product.get('sales', 0) < 10 and product.get('margin', 0) < 0.05:
            actions.append({'product_id': product['id'], 'action': 'discard', 'reason': 'low performance'})
        # Additional rules can go here
    return actions

# Generate report
def generate_report(actions_by_department):
    lines = []
    lines.append(f"## Report for {date.today().isoformat()}\n")
    for dept, actions in actions_by_department.items():
        lines.append(f"### {dept}\n")
        if not actions:
            lines.append("No actions taken.\n")
        else:
            for action in actions:
                lines.append(f"- {action}\n")
        lines.append("\n")
    return "\n".join(lines)

def main():
    # Load all state files
    products_state = load_state('products.json')
    # Additional states: seo_state, ux_state, etc.

    # Evaluate decisions
    product_actions = evaluate_products(products_state)
    actions_by_department = {
        'Product': product_actions,
        # Add other departments here
    }

    # Write report
    report = generate_report(actions_by_department)
    with open(DECISIONS_FILE, 'a', encoding='utf-8') as f:
        f.write(report)

if __name__ == '__main__':
    main()
