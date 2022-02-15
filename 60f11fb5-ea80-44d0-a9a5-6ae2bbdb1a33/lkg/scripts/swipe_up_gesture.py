import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('swipe_up', '')
    context.verify(grep="Copyright")

