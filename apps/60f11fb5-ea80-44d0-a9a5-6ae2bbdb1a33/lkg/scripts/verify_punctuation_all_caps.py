import logging


def run(context):
        context.verify(grep="ALL CAPS. STRING", grep_count=0)
        context.perform_gesture('tap', 'btn_punctuation')