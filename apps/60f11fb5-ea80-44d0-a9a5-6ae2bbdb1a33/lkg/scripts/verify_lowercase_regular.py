import logging


def run(context):
        context.verify(grep="regular string")
        context.perform_gesture('tap', 'btn_lowercase')