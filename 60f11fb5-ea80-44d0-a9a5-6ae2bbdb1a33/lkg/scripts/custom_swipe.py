import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture_on_coord('swipe_custom', {'start_x': 0, 'start_y': 0, 'end_x': 200, 'end_y': 200, 'duration': 2000})