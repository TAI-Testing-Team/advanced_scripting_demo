'''
This script allows the bot to interact with an element somewhere other than the center.
Useful if a checkbox is chopped only with its' associated label text so the checkbox is on the far right of the element image.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'btn_offset', additional_params={'offset': {'x': 20, 'y': 50}}) 


    # OLD CODE FROM OLD TRIES for reference

    # log.info('=================================offset=================')
    # log.info('button cx is '+ str(btn_offset_cx))
    # log.info('button cy is '+ str(btn_offset_cy))
    # log.info('button x is '+ str(btn_offset_x))
    # log.info('button y is ' + str(btn_offset_y))
    # log.info('=================================offset=================')

    # driver = context.get_driver()
    # btn_offset = context.find_element('btn_offset') 
    # btn_offset_x = btn_offset.get('x')
    # btn_offset_y = btn_offset.get('y')
    # btn_offset_w = btn_offset.get('width')
    # btn_offset_h = btn_offset.get('height')
    # btn_offset_cx = btn_offset_x + (btn_offset_w / 2)
    # btn_offset_cy = btn_offset_y + (btn_offset_h / 2)