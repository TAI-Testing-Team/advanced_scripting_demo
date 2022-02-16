import logging


def run(context):
        context.verify(grep="ch@racter $tring")
        context.perform_gesture('tap', 'btn_special_characters')