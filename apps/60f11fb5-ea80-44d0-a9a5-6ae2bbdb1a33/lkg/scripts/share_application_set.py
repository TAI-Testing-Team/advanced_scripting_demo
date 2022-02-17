
import logging, requests

log = logging.getLogger(__name__)

def run(context):

# 1: capture data from the current screen:

    # get text values from a pricing table. 
    # use `dynamic=True` to allow capture of an element where the text might change,
    # as with shopping cart totals, new user IDs, etc...
    screen_element_text = context.find_element('screen_element', dynamic=True).get('text')

# 2: access context datastore and add data for use in subsequent test steps:

    # access the internal test case datastore (part of the `context` object)
    script_vals = context.get_test_script_vals()

    # add element data to the TC datastore for use in subsequent steps
    script_vals['screen_data'] = screen_element_textd