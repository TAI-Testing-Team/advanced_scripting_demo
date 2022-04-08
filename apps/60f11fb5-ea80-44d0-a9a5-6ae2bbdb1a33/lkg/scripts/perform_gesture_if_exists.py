import logging

log = logging.getLogger(__name__)

# This script checks to make sure the element EXISTS and if it does, then it performs a gesture on that element. 
# In this example, it's a tap gesture and it's acting on a button (btn_confirm)

def run(context):
    context.perform_gesture_if_exists('double_tap', 'btn_confirm')
