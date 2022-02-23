import logging
import os

def run(context):
    
    screenhome = context.element_exists('scrn_home', dynamic=False)
    
    
    
    
    
    
    
    if screenhome==True:
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
    else:
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')