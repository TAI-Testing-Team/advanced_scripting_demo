'''
This script swipes up until a label is found for a default max of 10 swipes, you can modify as needed.
Available swipe actions are: swipe_up, swipe_down, swipe_left, swipe_right.
Replace 4 <your_common_name> and 3 <your_label_name> items wit your values.
You can set the start_x, start_y, end_x, end_y values.
The duration is how long the swipe will take from the start to the end point, larger number is a slower swipe.
'''

import logging
import time
import os

log = logging.getLogger(__name__)

MAX_SWIPES = 10


def run(context):
    home_button = False
    attempts = 0

    home_button = element_exists(context, 'lnk_home')
    
    while not home_button and attempts <= MAX_SWIPES:
        attempts += 1
        context.perform_gesture('swipe_down', '')
        home_button = element_exists(context, 'lnk_home')

    context.verify(['lnk_home'])


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0

