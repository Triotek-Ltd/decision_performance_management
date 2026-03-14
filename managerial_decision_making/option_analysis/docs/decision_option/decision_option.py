"""Doc runtime hooks for decision_option."""

class DocRuntime:
    doc_key = "decision_option"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'select', 'reject', 'archive']
