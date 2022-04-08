import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('double_tap', 'icn_favorite')
    context.verify(labels='icn_favorite_selected', label_count=0)
