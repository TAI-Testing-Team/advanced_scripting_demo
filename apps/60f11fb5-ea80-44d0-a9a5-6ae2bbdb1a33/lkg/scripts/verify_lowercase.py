import logging


def run(context):
        context.verify(grep="this is the string.")
        context.perform_gesture('tap', 'btn_lowercase')