import logging


def run(context):
        context.verify(grep="LOWERCASE STRING")
        context.perform_gesture('tap', 'btn_all_caps')