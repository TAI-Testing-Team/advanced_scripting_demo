import logging
import time

log = logging.getLogger(__name__)

def run(context):
    
	context.perform_gesture('tap', 'btn_tap')
	context.verify(grep="Tap Successful")
	context.perform_gesture('double_tap', 'btn_double_tap')
	context.verify(grep="Double Tap Successful")	

	context.perform_gesture('swipe_up', '')
	context.verify(grep="Copyright")
	context.perform_gesture('swipe_down', '')
	context.verify(grep="Double Tap Successful")	
	
	context.perform_gesture('text_entry_no_submit', 'inp_text_entry_no_submit', 'Bot Gestures All Script Text')
	context.verify(grep="Bot Gestures All Script Text")
	context.perform_gesture('text_entry', 'inp_text_entry', 'Completed!!')
	context.verify(grep="Bot Gestures All Script Text", grep_count=0)
	
