import logging

log = logging.getLogger(__name__)

# This script performs a gesture on an element, even if the element has changed - in text or color for example
# In the example below, we are tapping on a button, the dynamic=True flag allows it to recognize the element, even if it has changed


def run(context):
    context.perform_gesture('double_tap', 'btn_change', dynamic=True)


