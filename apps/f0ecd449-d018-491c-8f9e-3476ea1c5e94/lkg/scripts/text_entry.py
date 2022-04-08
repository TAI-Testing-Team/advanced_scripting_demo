import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry', 'inp_search','dark blue')
    context.verify(labels="tle_dark_blue_jeans")