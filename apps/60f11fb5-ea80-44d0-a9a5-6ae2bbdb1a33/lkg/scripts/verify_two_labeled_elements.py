import logging


def run(context):
    context.verify(labels=["btn_accept", "btn_ok"])
    context.perform_gesture('tap', 'btn_verified')