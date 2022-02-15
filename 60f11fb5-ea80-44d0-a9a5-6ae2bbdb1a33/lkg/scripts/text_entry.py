import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry', 'inp_text_entry','Completed your test!')
    context.verify(grep="Here is some text!", grep_count=0)