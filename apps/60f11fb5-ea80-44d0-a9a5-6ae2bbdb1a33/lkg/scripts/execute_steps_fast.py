import logging
import time

log = logging.getLogger(__name__)


def run(context):
    
    driver = context.get_driver()  
    first = context.find_element('btn_first') 
    first_x = first.get('x')
    first_y = first.get('y')
    first_w = first.get('width')
    first_h = first.get('height')
    first_cx = int(first_x + (first_w / 2))
    first_cy = int(first_y + (first_h / 2))
    log.info('====================output first button info====================')
    log.info(type(first_cx))
    log.info(type(first_cy))

    second = context.find_element('btn_second') 
    second_x = second.get('x')
    second_y = second.get('y')
    second_w = second.get('width')
    second_h = second.get('height')
    second_cx = int(second_x + (second_w / 2))
    second_cy = int(second_y + (second_h / 2))

    third = context.find_element('btn_third') 
    third_x = third.get('x')
    third_y = third.get('y')
    third_w = third.get('width')
    third_h = third.get('height')
    third_cx = int(third_x + (third_w / 2))
    third_cy = int(third_y + (third_h / 2))

    input_text = context.find_element('inp_text') 
    input_text_x = input_text.get('x')
    input_text_y = input_text.get('y')
    input_text_w = input_text.get('width')
    input_text_h = input_text.get('height')
    input_text_cx = int(input_text_x + (input_text_w / 2))
    input_text_cy = int(input_text_y + (input_text_h / 2))

    modal = context.find_element('btn_modal') 
    modal_x = modal.get('x')
    modal_y = modal.get('y')
    modal_w = modal.get('width')
    modal_h = modal.get('height')
    modal_cx = int(modal_x + (modal_w / 2))
    modal_cy = int(modal_y + (modal_h / 2))

          # click btn_first
    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(first_cx, first_cy)
            }])
    time.sleep(0)
        # click btn_second
    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(second_cx,second_cy)
            }])
    time.sleep(0)    
    # click btn_one_time
    driver.session.execute_command('DoubleClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(third_cx,third_cy)
            }])
    time.sleep(0)

    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(modal_cx,modal_cy)
            }])
    time.sleep(1)

    close = context.find_element('icn_close') 
    close_x = close.get('x')
    close_y = close.get('y')
    close_w = close.get('width')
    close_h = close.get('height')
    close_cx = int(close_x + (close_w / 2))
    close_cy = int(close_y + (close_h / 2))

    log.info('====================output close modal info====================')
    log.info(close_cx)
    log.info(close_cy)

    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(close_cx,close_cy)
            }])
    time.sleep(1)

    disappear = context.find_element('btn_disappear') 
    disappear_x = disappear.get('x')
    disappear_y = disappear.get('y')
    disappear_w = disappear.get('width')
    disappear_h = disappear.get('height')
    disappear_cx = int(disappear_x + (disappear_w / 2))
    disappear_cy = int(disappear_y + (disappear_h / 2))

    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(disappear_cx,disappear_cy)
            }])
    time.sleep(1)
    context.get_all_elements()
    log.info('===========================verifying================')
    context.verify(labels=["btn_disappear_tapped"])
    
    # write the properties out for reference in the log output
    # log.info('====================output first button info====================')
    # log.info(first_cx)
    # log.info(first_cy)
    # log.info('====================output second button info====================')
    # log.info(second_cx)
    # log.info(second_cy)
    # log.info('====================output third button info====================')
    # log.info(third_cx)
    # log.info(third_cy)
    # log.info('====================output input field info====================')
    # log.info(input_text_cx)
    # log.info(input_text_cy)
    # log.info('====================output modal info====================')
    # log.info(modal_cx)
    # log.info(modal_cy)
    # log.info('====================disappear info====================')
    # log.info(disappear_cx)
    # log.info(disappear_cy)

