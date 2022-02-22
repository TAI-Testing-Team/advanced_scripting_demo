import logging
import os

def run(context):
    if  context.verify(labels=["scrn_home"]) or context.verify(labels=["scrn_basic_gestures"]) or context.verify(labels=["scrn_find_element"]) or context.verify(labels=["scrn_verify"]) or context.verify(labels=["scrn_profile"]) or context.verify(labels=["scrn_input_parameterization"]) or context.verify(labels=["scrn_tap_parameterization"]) or context.verify(labels=["scrn_wait"]) or context.verify(labels=["scrn_dynamic"]) or context.verify(labels=["scrn_conditions"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
    else:
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')