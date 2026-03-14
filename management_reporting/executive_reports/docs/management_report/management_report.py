"""Doc runtime hooks for management_report."""

class DocRuntime:
    doc_key = "management_report"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'publish', 'archive']
