'''
This script will find the properties for an element so they can be used as needed. 
In this case the x and y coordinates and height and width are stored.
The coordinates of the element's center point are then determined and a tap action is executed
The script also prints out the values to the terminal output so they can be checked in the logs if needed.
Change "careers" to a common name related to your element.
Change <YOUR_LABEL_NAME> to the label name used in the test.ai GUI, either a standard or template match label.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    # find the properties for the element
    elem_properties = context.find_element('btn_change')
    
    # put the properties into variables that can be used
    elem_properties_x = elem_properties.get('x')
    elem_properties_y = elem_properties.get('y')
    elem_properties_w = elem_properties.get('width')
    elem_properties_h = elem_properties.get('height')
    tag_name = elem_properties.get('tag_name')
    text = elem_properties.get('text')
    attributes = elem_properties.get('attributes')
    flags = elem_properties.get('flags')
    
    # write the properties out for reference in the log output
    log.info('====================output find element====================')
    log.info('flags')
    log.info('focused')
    log.info('scrollablble')

    log.info('====================end find element====================')

    all_elem_properties = 'The X Value is ' + str(elem_properties_x) + ', The Y Value is ' + str(elem_properties_y) + ', The W Value is ' + str(elem_properties_w) + ', The H Value is ' + str(elem_properties_h) + '\n The tag name is ' + tag_name + ', The text is ' + text + '\n The attributes are ' + str(attributes) + '\n The flag attributes are ' + str(flags) 
    context.perform_gesture('text_entry_no_submit', 'inp_test_info', all_elem_properties)