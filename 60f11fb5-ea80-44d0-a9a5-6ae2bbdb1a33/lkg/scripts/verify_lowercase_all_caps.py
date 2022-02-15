import logging


def run(context):
        context.verify(grep="all caps")
        context.perform_gesture('tap', 'btn_lowercase')