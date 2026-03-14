"""Doc runtime hooks for project_record."""

class DocRuntime:
    doc_key = "project_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'archive']
