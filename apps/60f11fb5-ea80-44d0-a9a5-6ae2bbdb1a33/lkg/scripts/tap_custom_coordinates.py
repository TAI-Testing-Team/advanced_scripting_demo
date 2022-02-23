import logging

log = logging.getLogger(__name__)

def run(context):
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

