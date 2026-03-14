"""Action registry seed for project_plan."""

from __future__ import annotations


DOC_ID = "project_plan"
ALLOWED_ACTIONS = ['create', 'review', 'approve', 'activate', 'revise', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'active', 'revised'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'approved', 'active', 'revised'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'active', 'revised'], 'transitions_to': 'approved'}, 'activate': {'allowed_in_states': ['draft'], 'transitions_to': 'active'}, 'revise': {'allowed_in_states': ['draft', 'approved', 'active', 'revised'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'approved', 'active', 'revised'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
