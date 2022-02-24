import logging
import time

log = logging.getLogger(__name__)


def run(context):
    
    driver = context.get_driver()
    # first = context.find_element('btn_first') 
    # first_x = first.get('x')
    # first_y = first.get('y')
    # first_w = first.get('width')
    # first_h = first.get('height')
    # first_cx = first_x + (first_w / 2)
    # first_cy = first_y + (first_h / 2)

    # second = context.find_element('btn_second') 
    # second_x = second.get('x')
    # second_y = second.get('y')
    # second_w = second.get('width')
    # second_h = second.get('height')
    # second_cx = second_x + (second_w / 2)
    # second_cy = second_y + (second_h / 2)

    # third = context.find_element('btn_third') 
    # third_x = third.get('x')
    # third_y = third.get('y')
    # third_w = third.get('width')
    # third_h = third.get('height')
    # third_cx = third_x + (third_w / 2)
    # third_cy = third_y + (third_h / 2)





    # input_text = context.find_element('inp_text') 
    # input_text_x = input_text.get('x')
    # input_text_y = input_text.get('y')
    # input_text_w = input_text.get('width')
    # input_text_h = input_text.get('height')
    # input_text_cx = input_text_x + (input_text_w / 2)
    # input_text_cy = input_text_y + (input_text_h / 2)

    # modal = context.find_element('btn_modal') 
    # modal_x = modal.get('x')
    # modal_y = modal.get('y')
    # modal_w = modal.get('width')
    # modal_h = modal.get('height')
    # modal_cx = modal_x + (modal_w / 2)
    # modal_cy = modal_y + (modal_h / 2)    

    # disappear = context.find_element('btn_disappear') 
    # disappear_x = disappear.get('x')
    # disappear_y = disappear.get('y')
    # disappear_w = disappear.get('width')
    # disappear_h = disappear.get('height')
    # disappear_cx = disappear_x + (disappear_w / 2)
    # disappear_cy = disappear_y + (disappear_h / 2)     

    
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

        

        # click btn_one_time
    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(590, 301)
            }])
    time.sleep(0)

        # click btn_one_time
    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(960, 301)
            }])
    time.sleep(0)
    
    # click btn_one_time
    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(1329, 301)
            }])
    time.sleep(0)


    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(496, 511)
            }])
    time.sleep(1)




    # close = context.find_element('icn_close') 
    # close_x = close.get('x')
    # close_y = close.get('y')
    # close_w = close.get('width')
    # close_h = close.get('height')
    # close_cx = close_x + (close_w / 2)
    # close_cy = close_y + (close_h / 2)

    # log.info('====================output close modal info====================')
    # log.info(close_cx)
    # log.info(close_cy)

    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(1185, 57)
            }])
    time.sleep(1)

    driver.session.execute_command('ClickCommand', [{
                'type': 'coordinates',
                'value': '{},{},SCREENSHOT'.format(564, 607)
            }])
    time.sleep(1)
    context.get_all_elements()
    log.info('===========================verifying================')
    # context.verify(labels=["btn_disappear_tapped"])
    # # double click btn_keypad_5
    # driver.session.execute_command('DoubleClickCommand', [{
    #             'type': 'coordinates',
    #             'value': '{},{},SCREENSHOT'.format(close_cx, close_cy)
    #         }])
    # time.sleep(2)
    
#     driver.session.execute_command('TextEntryCommand', [{
#             'type': 'coordinates',
#             'value': '{},{},SCREENSHOT'.format(input_text_cx, input_text_cy),
#             'grep': 'hello'
#         }])
# time.sleep(0)
