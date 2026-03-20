"""Action handler seed for performance_exception:assign."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "performance_exception"
ACTION_ID = "assign"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['raised', 'reviewed', 'correcting', 'escalated'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['kpi_definition', 'scorecard_record', 'management_action_item'], 'borrowed_fields': ['threshold', 'metric context from kpi_definition'], 'inferred_roles': ['hr officer']}, 'actors': ['hr officer'], 'action_actors': {'create': ['hr officer'], 'assign': ['hr officer'], 'review': ['hr officer'], 'close': ['hr officer'], 'archive': ['hr officer']}}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['raised', 'reviewed', 'correcting', 'escalated'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
