import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture_on_coord('tap', {'x': 509, 'y': 650})
    context.verify(grep="Coordinate Tap Successful")

