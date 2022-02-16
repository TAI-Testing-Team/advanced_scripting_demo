import logging


def run(context):
        context.verify(grep="dash-string")
        context.perform_gesture('tap', 'btn_dash')