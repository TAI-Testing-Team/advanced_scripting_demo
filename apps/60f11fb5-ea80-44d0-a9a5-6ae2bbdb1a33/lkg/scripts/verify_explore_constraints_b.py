import logging
import os

def run(context):
    if context.verify(labels=["scrn_home"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
    
    elif context.verify(labels=["scrn_basic_gestures"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ')        
    
    elif context.verify(labels=["scrn_tap_parameterization"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    elif context.verify(labels=["scrn_wait"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    elif context.verify(labels=["scrn_dynamic"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    elif context.verify(labels=["scrn_verify"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    elif context.verify(labels=["scrn_basic_gestures"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    elif context.verify(labels=["scrn_input_parameterization"]):
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ')     
    
    else:   
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')