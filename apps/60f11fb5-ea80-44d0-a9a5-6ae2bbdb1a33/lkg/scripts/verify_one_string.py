import logging


def run(context):
        context.verify(grep="Verify My Existence")
        context.perform_gesture('tap', 'btn_verified')