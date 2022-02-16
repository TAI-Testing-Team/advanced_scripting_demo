import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry_no_submit', 'inp_text_entry_no_submit','Here is some text!')
    context.verify(grep="Here is some text!", grep_count=1)
