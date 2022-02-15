import logging


def run(context):
        context.verify(grep="No Place Like")
        context.perform_gesture('tap', 'btn_verified')