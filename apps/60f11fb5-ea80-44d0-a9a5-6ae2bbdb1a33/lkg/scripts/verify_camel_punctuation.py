import logging


def run(context):
        context.verify(grep="TeSt'S StRiNg")
        context.perform_gesture('tap', 'btn_camel_case')