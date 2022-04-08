import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry_no_submit', 'inp_search','dark blue')
    context.verify(labels="lbl_dark_blue_jeans_suggestion")
