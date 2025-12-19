# GPT Director Project Plan

## Overview
The GPT Director acts as the central orchestrator for the **SeniorPetsCare** online store. It coordinates decisions across five specialized GPTs—Product & Catalogue, SEO & Content, UX & Conversion, Logistics & Operations, and Finance & Pricing—ensuring alignment with high-level business rules. The director reads from shared state files and writes daily decision summaries to maintain transparency.

## Responsibilities
1. **Collect and interpret state data**
   - Load JSON files from the `/state` directory: `products.json`, `seo.json`, `ux.json`, `logistics.json`, and `finance.json`.
   - Each file describes the current status of its respective department (e.g., approved products, SEO performance metrics, UX improvement backlog, stock levels, financial margins).

2. **Apply decision rules**
   - Follow the guidelines in `rules/director_rules.md`:
     - Execute low im‭pact tasks autonomously (non‭financial, non‭reputational, non‭legal).
     - Seek human approval when proposing large investments, significant price changes, high‭risk product additions, or sensitive branding decisions【181017396637729†L4-L11】.
   - Prioritize conversion over aesthetics and focus on solving problems for senior pets: mobility, rest, hygiene, alimentation, and cognition【181017396637729†L14-L17】.

3. **Generate daily reports**
   - Summarize actions taken, decisions made, and outstanding approvals in `decisions/daily_reports.md`.
   - Include key metrics: number of products promoted, paused or discarded; SEO updates applied; UX improvements deployed; logistics alerts (e.g., low stock); financial decisions (price adjustments or margin issues).

4. **Interface with specialized GPTs**
   - Issue tasks to each department GPT by updating their respective state files or by triggering their internal processes.
   - Resolve conflicts when recommendations from different GPTs clash (e.g., a product with high profit but poor SEO appeal) and document the rationale.

5. **Notify user when needed**
   - Send notifications for approvals or exceptions that require human attention. Use the criteria in the rules file to minimize unnecessary interruptions.

## Implementation Suggestions
- **Language and environment**: Use Python for the orchestration script due to its robust JSON support and ease of file operations.
- **Script location**: Add a new directory (e.g., `/director`) in the repository for Python code. The main script could be `director.py`.
- **Data loading**: Use `json` module to load state files and parse them into dictionaries.
- **Decision logic**: Implement functions such as `evaluate_products(state)`, `update_seo(state)`, `optimize_ux(state)`, `monitor_logistics(state)`, and `adjust_pricing(state)` that return recommendations or actions.
- **Report generation**: At the end of each run, write a Markdown report to `decisions/daily_reports.md`. Append the new report to keep a history of actions.
- **Automation**: Use a GitHub Action to run `director.py` on a schedule (e.g., daily at midnight). The action can commit updated state and reports back to the repository. This ensures that decisions are logged without manual intervention.

## Example Skeleton (`director.py`)
```
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
```
This skeleton demonstrates how to load product state, run simple evaluation logic, and write a report. The actual decision logic must be expanded to incorporate SEO, UX, logistics, and finance states and follow the rules specified in `director_rules.md`.

## Next Steps
1. **Enhance data structures**: Extend each state file to include relevant metrics (e.g., sales volume, conversion rates, stock levels, margins).
2. **Implement detailed evaluation functions**: Write decision logic for each department following business rules and best practices.
3. **Set up GitHub Action**: Configure an action in `.github/workflows/director.yml` to run the script daily and commit changes.
4. **Test and iterate**: Run the script manually, review decisions, and refine the rules and logic to align with business objectives.
