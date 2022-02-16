import logging
import os

def run(context):
    if element_exists(context, 'inp_radio_no_active'):
        context.verify(labels=[inp_radio_no_active])
    elif:
        element_exists(context, 'div_btn_clicked'):
        context.verify(labels=[div_btn_clicked])
    elif:
        element_exists(context, 'ddi_first_option'):
        context.verify(labels=[div_btn_clicked])