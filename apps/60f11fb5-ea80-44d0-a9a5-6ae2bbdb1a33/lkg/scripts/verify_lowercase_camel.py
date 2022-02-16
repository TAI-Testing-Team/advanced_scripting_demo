import logging


def run(context):
        context.verify(grep="camelcase string")
        context.perform_gesture('tap', 'btn_lowercase')