"""Action handler seed for management_action_item:create."""

from __future__ import annotations


DOC_ID = "management_action_item"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['opened', 'assigned', 'in_progress'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['management_report', 'executive_review', 'team_checkin', 'performance_exception'], 'borrowed_field_context': ['source issue or decision context from management_report or executive_review'], 'inferred_roles': ['Reviewer']}, 'actors': ['Reviewer'], 'action_actors': {'create': ['Reviewer'], 'assign': ['Reviewer'], 'track': ['Reviewer'], 'close': ['Reviewer'], 'archive': ['Reviewer']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
