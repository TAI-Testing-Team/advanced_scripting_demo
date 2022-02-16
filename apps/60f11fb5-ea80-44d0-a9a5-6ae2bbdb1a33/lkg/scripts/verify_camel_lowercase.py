import logging


def run(context):
        context.verify(grep="LoWeRCaSe StRinG")
        context.perform_gesture('tap', 'btn_camel_case')