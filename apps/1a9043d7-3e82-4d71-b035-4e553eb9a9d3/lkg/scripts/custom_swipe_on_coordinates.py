import logging

log = logging.getLogger(__name__)


def run(context):
    context.perform_gesture_on_coord('swipe_custom', {'start_x': 1000, 'start_y': 1400, 'end_x': 100, 'end_y': 1400, 'duration': 3000})
