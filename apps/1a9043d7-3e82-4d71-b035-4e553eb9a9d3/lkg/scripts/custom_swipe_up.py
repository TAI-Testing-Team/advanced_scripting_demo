import logging

log = logging.getLogger(__name__)


def run(context):
    context.perform_gesture_on_coord('swipe_custom', {'start_x': 540, 'start_y': 1700, 'end_x': 540, 'end_y': 300, 'duration': 2000})