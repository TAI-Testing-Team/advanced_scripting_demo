import logging


def run(context):
        context.verify(grep="underscore_string")
        context.perform_gesture('tap', 'btn_underscore')