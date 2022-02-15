import logging


def run(context):
        context.verify(grep="Regular String")
        context.perform_gesture('tap', 'btn_exact_case')