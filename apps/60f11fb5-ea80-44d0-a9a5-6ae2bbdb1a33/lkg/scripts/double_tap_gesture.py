import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('double_tap', 'btn_double_tap')
    context.verify(grep="Double Tap Successful")
