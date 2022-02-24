import logging
log = logging.getLogger(__name__)
import os

def run(context):
    #verified=context.verify(grep="Please Select One")
    home_screen = context.element_exists("txt_please_select_test_start")
    basic_gestures = context.element_exists("btn_double_tap")
    find_element = context.element_exists("inp_slider")
    verify_screen = context.element_exists("btn_verify_one_string")
    wait_for_label = context.element_exists("btn_wait_for_label")
    tap_parameterization = context.element_exists("btn_tap_one")
    input_parameterization = context.element_exists("btn_sign_in")
    dynamic = context.element_exists("btn_next")
    log.info("=======================Verified=========================")
    #log.info(element)
    log.info("=======================Verified=========================")
    #if verified == True: 
    
    if home_screen==True or basic_gestures==True or find_element==True or verify_screen==True or wait_for_label==True or tap_parameterization==True or input_parameterization==True or dynamic==True:   
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verified')
    
    else:   
        context.perform_gesture('tap', 'lnk_find_element')
        context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', 'Explore mode bot constraints verification failed ')