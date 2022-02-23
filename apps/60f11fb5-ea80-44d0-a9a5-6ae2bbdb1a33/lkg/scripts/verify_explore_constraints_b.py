import logging
log = logging.getLogger(__name__)
import os

def run(context):
    #verified=context.verify(grep="Please Select One")
    home_screen = context.element_exists("txt_please_select_test_start")
    basic_gestures = context.element_exists("btn_double_tap")
    find_element = context.element_exists("txt_please_select_test_start")
    log.info("=======================Verified=========================")
    log.info(element)
    log.info("=======================Verified=========================")
    #if verified == True: 
    if home_screen==True or basic_gestures==True or find_element==True:
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
    
    # elif context.verify(labels=["scrn_basic_gestures"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ')        
    
    # elif context.verify(labels=["scrn_tap_parameterization"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    # elif context.verify(labels=["scrn_wait"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    # elif context.verify(labels=["scrn_dynamic"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    # elif context.verify(labels=["scrn_verify"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    # elif context.verify(labels=["scrn_basic_gestures"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ') 
    
    # elif context.verify(labels=["scrn_input_parameterization"]):
    #     context.perform_gesture('tap', 'lnk_find_element')
    #     context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified ')     
    
    else:   
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')