"""Doc runtime hooks for project_plan."""

class DocRuntime:
    doc_key = "project_plan"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'activate', 'revise', 'archive']
