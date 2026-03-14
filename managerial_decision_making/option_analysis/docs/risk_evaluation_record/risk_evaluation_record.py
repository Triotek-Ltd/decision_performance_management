"""Doc runtime hooks for risk_evaluation_record."""

class DocRuntime:
    doc_key = "risk_evaluation_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'confirm', 'archive']
