"""Doc runtime hooks for variance_report."""

class DocRuntime:
    doc_key = "variance_report"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'publish', 'archive']
