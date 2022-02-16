import logging


def run(context):
        context.verify(grep="a_m1xed-$tring")
        context.perform_gesture('tap', 'btn_mixed_string')