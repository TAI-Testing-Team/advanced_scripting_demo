import logging


def run(context):
        context.verify(grep="gmail.com", grep_count=0)
        context.perform_gesture('tap', 'btn_verified')