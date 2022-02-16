import logging


def run(context):
    context.verify(labels=["btn_accept", "btn_modal_button"], label_count=1)
    context.perform_gesture('tap', 'btn_accept')