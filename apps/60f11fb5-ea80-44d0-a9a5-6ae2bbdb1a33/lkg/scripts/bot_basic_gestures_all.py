import logging

log = logging.getLogger(__name__)

MAX_SWIPES = 10

def run(context):
    
	context.perform_gesture('tap', 'btn_tap')
	context.verify(grep="Tap Successful")
	context.perform_gesture('double_tap', 'btn_double_tap')
	context.verify(grep="Double Tap Successful")	

	context.perform_gesture('swipe_up', '')
	context.verify(grep="Posuere ac ut consequat semper viverra")
	context.perform_gesture('swipe_down', '')
	context.verify(grep="Double Tap Successful")	
	
	context.perform_gesture('text_entry_no_submit', 'inp_text_entry_no_submit', 'Bot Gestures All Script Text')
	context.verify(grep="Bot Gestures All Script Text")
	context.perform_gesture('text_entry', 'inp_text_entry', 'Completed!!')
	context.verify(grep="Bot Gestures All Script Text", grep_count=0)

	mixed_string = False
	attempts = 0

	mixed_string = element_exists(context, 'btn_coordinate_tap')
	
	while not mixed_string and attempts <= MAX_SWIPES:
		attempts += 1
		context.perform_gesture('swipe_up', '')
		mixed_string = element_exists(context, 'btn_coordinate_tap')

	
	context.verify(['btn_coordinate_tap'])
	coordinate_tap_info = context.find_element('btn_coordinate_tap')
    # put the properties into variables that can be used
	cord_x = coordinate_tap_info.get('x')
	cord_y = coordinate_tap_info.get('y')
	cord_w = coordinate_tap_info.get('width')
	cord_h = coordinate_tap_info.get('height')
	cord_cx = cord_x + (cord_w / 2)
	cord_cy = cord_y + (cord_h / 2)
	log.info('=========================info======================')
	log.info(cord_x)
	log.info(cord_y)
	log.info(cord_w)
	log.info(cord_h)
	log.info('=======coordinate tap=========')
	log.info(cord_cx)
	log.info(cord_cy)
	log.info('=========================info======================')
	context.perform_gesture_on_coord('tap', {'x': cord_cx, 'y': cord_cy})
	context.verify(grep="Coordinate Tap Successful")

def element_exists(context, label):
	labels_per_elem = context.find_elements_with_label(label)
	return labels_per_elem and len(labels_per_elem.keys()) > 0


