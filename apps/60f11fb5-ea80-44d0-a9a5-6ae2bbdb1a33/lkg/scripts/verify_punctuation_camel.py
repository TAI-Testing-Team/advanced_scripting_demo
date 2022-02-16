import logging


def run(context):
        context.verify(grep="CamelCase! String", grep_count=0)
        context.perform_gesture('tap', 'btn_punctuation')