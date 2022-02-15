import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('swipe_down', '')
    context.verify(grep="Double Tap Successful")