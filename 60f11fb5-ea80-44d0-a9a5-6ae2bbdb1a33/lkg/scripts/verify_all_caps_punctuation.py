import logging


def run(context):
        context.verify(grep="TEST'S STRING")
        context.perform_gesture('tap', 'btn_all_caps')