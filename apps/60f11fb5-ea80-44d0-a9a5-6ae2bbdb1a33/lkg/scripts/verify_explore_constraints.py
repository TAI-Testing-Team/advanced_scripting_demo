import logging
import os

def run(context):
    if context.element_exists('scrn_home', dynamic=False)== True or context.element_exists('scrn_find_element', dynamic=False)== True or context.element_exists('scrn_dynamic', dynamic=False)== True or context.element_exists('scrn_tap_parameterization', dynamic=False)== True or context.element_exists('scrn_input_parameterization', dynamic=False)== True or context.element_exists('scrn_basic_gestures', dynamic=False)== True or context.element_exists('scrn_wait', dynamic=False)== True or context.element_exists('scrn_verify', dynamic=False)== True or context.element_exists('scrn_profile', dynamic=False)== True or context.element_exists('scrn_logout', dynamic=False)== True :
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
    else:
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')