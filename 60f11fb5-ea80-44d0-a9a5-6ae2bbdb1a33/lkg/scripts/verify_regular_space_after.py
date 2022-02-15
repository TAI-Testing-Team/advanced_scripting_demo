import logging


def run(context):
        context.verify(grep="Regular String  ", grep_count=0)
        context.perform_gesture('tap', 'btn_space_after')