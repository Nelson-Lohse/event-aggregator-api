from flask import Blueprint, jsonify
from services import mock_event_service

bp = Blueprint('main', __name__)




@bp.route('/')
def get_events():
    events = mock_event_service.get_mock_events()
    return jsonify(events)