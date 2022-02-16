'''
This script swipes up until a label is found for a default max of 10 swipes, modify the max as needed.
Replace the 4 labeled_element and 3 img_green_hoodie with appropriate values.
Set the start_x, start_y, end_x, end_y values as needed.
The duration is how long the swipe will take from the start to the end point, larger number is a slower swipe.
'''

import logging
import time
import os

log = logging.getLogger(__name__)

MAX_SWIPES = 10


def run(context):
    labeled_element = False
    attempts = 0

    labeled_element = element_exists(context, 'img_green_hoodie')
    
    while not labeled_element and attempts <= MAX_SWIPES:
        attempts += 1
        context.perform_gesture_on_coord('swipe_custom', {'start_x': 540, 'start_y': 1700, 'end_x': 540, 'end_y': 700, 'duration': 2000})
        labeled_element = element_exists(context, 'img_green_hoodie')

    context.verify(['img_green_hoodie'])


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0