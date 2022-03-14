import logging

log = logging.getLogger(__name__)

def tapstep(context):
    context.perform_gesture('tap', 'lnk_find_element')
    # context.get_all_elements()