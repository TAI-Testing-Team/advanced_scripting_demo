import logging


def run(context):
        context.verify(grep="This is the String.")
        context.perform_gesture('tap', 'btn_current_case')