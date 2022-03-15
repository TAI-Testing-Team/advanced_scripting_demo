import logging

log = logging.getLogger(__name__)

def typetext(context):
    context.perform_gesture('tap', 'lnk_dynamic')
    context.perform_gesture('text_entry', 'inp_test_info', 'This is the text I want to enter from external script libraries.')