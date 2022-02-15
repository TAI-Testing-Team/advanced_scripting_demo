import logging


def run(context):
        context.verify(grep="CamelCase String")
        context.perform_gesture('tap', 'btn_exact_case')