import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_tap')
    context.verify(grep="Tap Successful")
