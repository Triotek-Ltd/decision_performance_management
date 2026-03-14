"""Doc runtime hooks for kpi_definition."""

class DocRuntime:
    doc_key = "kpi_definition"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'approve', 'archive']
