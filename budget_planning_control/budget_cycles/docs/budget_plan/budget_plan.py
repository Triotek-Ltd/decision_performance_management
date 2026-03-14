"""Doc runtime hooks for budget_plan."""

class DocRuntime:
    doc_key = "budget_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'activate', 'close', 'archive']
