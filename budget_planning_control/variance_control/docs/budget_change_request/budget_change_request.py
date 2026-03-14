"""Doc runtime hooks for budget_change_request."""

class DocRuntime:
    doc_key = "budget_change_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'reject', 'close', 'archive']
