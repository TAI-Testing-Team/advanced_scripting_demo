import logging

log = logging.getLogger(__name__)

def run(context):
    def execute_before_each_explore_step():
        driver = context.get_driver();
        driver.get('http://blogen-inc.surge.sh/index.html')
        context.get_all_elements()
        driver.execute_command('ResizeCommand', [800, 600])
        context.verify(labels=["lnk_find_element_800_600"])
        context.verify(labels=["lnk_find_element"], label_count=0)
        driver.execute_command('ResizeCommand', [1920, 1080]) 
        context.perform_gesture('tap','lnk_find_element')
        context.perform_gesture('text_entry', 'inp_ta_element_info', "Run Before Explore Steps Successful!!!")
        driver.execute_command('RefreshCommand', [])
    context.explore(5, before_each_step=execute_before_each_explore_step, ignore_element_errors=True)