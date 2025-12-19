import os
import json


def main():
    actions_file = "decisions/actions_pending.json"
    if not os.path.exists(actions_file):
        return
    with open(actions_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    actions = data.get("actions", [])
    design_actions = [a for a in actions if a.get("type", "").startswith("DESIGN")]
    if design_actions:
        log_path = "decisions/apply_log.md"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(log_path, "a", encoding="utf-8") as log_file:
            for action in design_actions:
                log_file.write(f"- Applied design action: {action}\n")


if __name__ == "__main__":
    main()
