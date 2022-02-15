import logging


def run(context):
        context.verify(grep="CAMELCASE STRING")
        context.perform_gesture('tap', 'btn_all_caps')