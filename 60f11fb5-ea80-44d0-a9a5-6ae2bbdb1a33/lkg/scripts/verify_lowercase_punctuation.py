import logging


def run(context):
        context.verify(grep="test's string")
        context.perform_gesture('tap', 'btn_lowercase')