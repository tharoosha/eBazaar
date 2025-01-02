from .deal_finding_agent import Deal_Finding_Agent
import re
import json

class Comparison_Agent:
    def __init__(self, deals, user_constraints):
        self.deal_agent = Deal_Finding_Agent(deals, user_constraints)

    def get_best_deal(self):
        best_deal = self.deal_agent.build().kickoff().raw
        match = re.search(r'\{.*\}', best_deal, re.DOTALL)
        if match:
            json_content = match.group()
            try:
                best_deal = json.loads(json_content)
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("No JSON content found.")
        return best_deal


