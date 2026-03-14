"""Doc runtime hooks for management_action_item."""

class DocRuntime:
    doc_key = "management_action_item"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'track', 'close', 'archive']
