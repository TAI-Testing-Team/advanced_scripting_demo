#Built to see how fast or how much time individual perform gestures take versue execute steps fast commands.

import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_first')
    context.perform_gesture('tap', 'btn_second')
    context.perform_gesture('tap', 'btn_third')
    context.perform_gesture('tap', 'inp_text')
    context.perform_gesture('tap', 'btn_modal')
    context.perform_gesture('tap', 'btn_close')

