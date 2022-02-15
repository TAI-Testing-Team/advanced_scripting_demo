import logging


def run(context):
        context.verify(grep="AlL CaPs")
        context.perform_gesture('tap', 'btn_camel_case')