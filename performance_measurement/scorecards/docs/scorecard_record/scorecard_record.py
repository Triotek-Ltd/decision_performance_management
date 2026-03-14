"""Doc runtime hooks for scorecard_record."""

class DocRuntime:
    doc_key = "scorecard_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'finalize', 'archive']
