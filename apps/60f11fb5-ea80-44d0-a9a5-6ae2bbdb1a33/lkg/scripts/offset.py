'''
This script allows the bot to interact with an element somewhere other than the center.
Useful if a checkbox is chopped only with its' associated label text so the checkbox is on the far right of the element image.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_change', additional_params={'offset': {'x': 95, 'y': 0}}) 