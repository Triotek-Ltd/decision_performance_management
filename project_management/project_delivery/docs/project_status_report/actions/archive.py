"""Action handler seed for project_status_report:archive."""

from __future__ import annotations


DOC_ID = "project_status_report"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'published'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['project_record', 'project_plan', 'project_task'], 'borrowed_fields': ['project identity', 'owner from project_record'], 'inferred_roles': ['operations coordinator']}, 'actors': ['operations coordinator'], 'action_actors': {'create': ['operations coordinator'], 'review': ['operations coordinator'], 'publish': ['operations coordinator'], 'archive': ['operations coordinator']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
