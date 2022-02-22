import logging
import os

labels = ['scrn_home', 'scrn_find_elements', 'scrn_wait', 'scrn_basic_gestures', 'scrn_verify', 'scrn_input_parameterization','scrn_tap_parameterization']
#want to use for loop here instead of if elif else or statements
for label in labels: 
    def run(context):
        if context.element_exists(label, dynamic=False) == True:
            context.perform_gesture('tap', 'lnk_find_element')
            context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
        else:
            context.perform_gesture('tap', 'lnk_find_element')
            context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')
    # how to use if statement? If label is in labels then xxxx??? 