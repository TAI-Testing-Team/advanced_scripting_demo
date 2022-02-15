import logging


def run(context):
        context.verify(grep="THIS IS THE STRING")
        context.perform_gesture('tap', 'btn_all_caps')