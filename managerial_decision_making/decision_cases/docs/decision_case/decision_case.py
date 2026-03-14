"""Doc runtime hooks for decision_case."""

class DocRuntime:
    doc_key = "decision_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'approve', 'reject', 'close', 'archive']
