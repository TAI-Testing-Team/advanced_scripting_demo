# import requests, json
# import logging
# log = logging.getLogger(__name__)

# def run(context):

#    driver = context.get_driver()
#    resources = driver.execute_async_script('''
#        var done = arguments[0];
#        $.ajax({
#              type: "GET",
#              url: "http://localhost:12543/api/v1/dashboard",
#              dataType: "json",
#              contentType: "application/json; charset=utf-8",
#              success: function(data) { done(data); }
#            });
#    ''')
# #    resp = requests.get("http://localhost:12543/api/v1/dashboard")
# #    data = resp.json().get("data",[])
# #    json_string = json.dumps(data) #makes JSON object returned in line 9 into string

#    log.info('=====================info======================')
#    log.info(resources)
#    log.info('=====================info======================')

# #    context.perform_gesture('text_entry_no_submit','inp_test_info', resources) 

#    return resources


def run(context):
   items = get_shopping_cart_items(context)
   # Write custom assertions, or perhaps make more API calls...

def get_shopping_cart_items(context):
   driver = context.get_driver()
   resources = driver.execute_async_script('''
      var done = arguments[0];
      $.ajax({
            type: "GET",
            url: "http://localhost:12543/api/v1/dashboard",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            success: function(data) { done(data); }
         });
   ''')
   return resources


   