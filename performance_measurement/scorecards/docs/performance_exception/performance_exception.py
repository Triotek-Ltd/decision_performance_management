"""Doc runtime hooks for performance_exception."""

class DocRuntime:
    doc_key = "performance_exception"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'correct', 'escalate', 'close', 'archive']
