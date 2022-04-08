import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_home')
    context.verify(labels="mnu_options")
