"""Doc runtime hooks for project_task."""

class DocRuntime:
    doc_key = "project_task"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'block', 'close', 'archive']
