"""Doc runtime hooks for executive_review."""

class DocRuntime:
    doc_key = "executive_review"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'schedule', 'complete', 'close', 'archive']
