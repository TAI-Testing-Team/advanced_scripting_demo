import logging
import time

def run(context):

    context.wait_for_template_match(['btn_wait_for_tmp'], score_threshold=0.95, grayscale=False, canny=False, scale_invariant=False)  
    context.perform_gesture('tap', 'btn_wait_for_tmp')
