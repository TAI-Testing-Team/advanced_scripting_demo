import logging


def run(context):
        context.verify(grep="lowercase string")
        context.perform_gesture('tap', 'btn_exact_case')