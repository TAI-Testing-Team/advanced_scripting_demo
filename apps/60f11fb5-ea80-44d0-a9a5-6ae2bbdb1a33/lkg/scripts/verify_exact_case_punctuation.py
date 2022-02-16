import logging


def run(context):
        context.verify(grep="Test's String")
        context.perform_gesture('tap', 'btn_exact_case')