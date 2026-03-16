"""Action handler seed for risk_evaluation_record:confirm."""

from __future__ import annotations


DOC_ID = "risk_evaluation_record"
ACTION_ID = "confirm"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'accepted'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['decision_case', 'decision_option', 'performance_exception'], 'borrowed_fields': ['decision', 'option context from linked records'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'review': ['case owner'], 'confirm': ['case owner'], 'archive': ['case owner']}}

def handle_confirm(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
