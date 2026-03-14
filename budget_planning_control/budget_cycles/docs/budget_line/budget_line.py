"""Doc runtime hooks for budget_line."""

class DocRuntime:
    doc_key = "budget_line"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'adjust', 'archive']
