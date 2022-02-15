import logging


def run(context):
        context.verify(grep="ALL CAPS STRING")
        context.perform_gesture('tap', 'btn_exact_case')