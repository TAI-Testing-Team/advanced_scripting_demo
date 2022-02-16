import logging


def run(context):
        context.verify(grep="REGULAR STRING")
        context.perform_gesture('tap', 'btn_all_caps')