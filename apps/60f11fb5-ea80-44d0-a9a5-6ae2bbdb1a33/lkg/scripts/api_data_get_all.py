import requests, json
import logging
log = logging.getLogger(__name__)

def run(context):
    # get_app_id = requests.get("http://localhost:12543/api/v1/dashboard")
    # app_id_data = get_app_id.json().get("data",[])
    # app_string = json.dumps(app_id_data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', app_string) 
    # log.info('=====================data request======================')
    # log.info(app_id_data)
    # log.info('======================json dumps======================')
    # log.info(app_string)
    # context.verify(grep="Blogen")
    # context.perform_gesture("tap", "lnk_dynamic")
    # context.get_all_elements()

    get_labeler_objects = requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/crawls/20211220142248/labeler_objects")
    objects_data = get_labeler_objects.json().get("data",[])
    objects_string = json.dumps(objects_data)
    log.info('=====================data request======================')
    log.info(objects_data)
    log.info('======================json dumps======================')
    log.info(objects_string) #makes JSON object returned in line 9 into string
    context.perform_gesture('text_entry_no_submit','inp_test_info', objects_string) 

    # context.verify(grep="")
    # context.perform_gesture("click", "lnk_dynamic")

    # get_labels = requests.get("")
    # data = get_labels.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)

    # context.perform_gesture("click", "lnk_dynamic")

    # get_test_runs = requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/test_runs")
    # data = get_test_runs.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)

    # context.perform_gesture("click", "lnk_dynamic")

    # get_test_run_ids = requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/test_runs/20211220123921")
    # data = get_test_run_ids.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)    
    
    # context.perform_gesture("click", "lnk_dynamic")


    # get_test_results_case_id = requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/test_results/20211220123921:Postman - Get - Test Runs - cb7524ed-2821-4281-96ad-26c209a94168")
    # data = get_test_results_case_id.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)

    # context.perform_gesture("click", "lnk_dynamic")

    # get_tests= requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/tests")
    # data = get_tests.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)

    # context.perform_gesture("click", "lnk_dynamic")

    # get_builds = requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/builds")
    # get_builds_data = get_builds.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)

    # context.perform_gesture("click", "lnk_dynamic")

    # get_latest_test_run = requests.get("http://localhost:12543/api/v1/c/testai/apps/web/60f11fb5-ea80-44d0-a9a5-6ae2bbdb1a33/latest_test_run")
    # data = get_latest_test_run.json().get("data",[])
    # json_string = json.dumps(data) #makes JSON object returned in line 9 into string
    # context.perform_gesture('text_entry_no_submit','inp_test_info', json_string) 
    # log.info('=====================data request======================')
    # log.info(data)
    # log.info('======================json dumps======================')
    # log.info(json_string)