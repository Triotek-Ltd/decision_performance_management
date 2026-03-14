"""Doc runtime hooks for project_status_report."""

class DocRuntime:
    doc_key = "project_status_report"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'publish', 'archive']
