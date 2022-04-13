import logging

is_secure = False
is_http_only = True

def run(context):
	driver=context.get_driver()
    # is_secure and is_http_only are booleans
	driver.execute_command('AddCookieCommand', ['NAME', '2', '/', 'http:www.google.com', '2-16-2022', is_secure, is_http_only])

# We do not have a test for this script yet until we build our full stack app.


# # import requests

# # url = "https://httpbin.org/cookies"

# # cookies = {'location': 'New York'}

# # r = requests.get(url, cookies=cookies)


# [{'session': False, 'httpOnly': True, 'secure': True, 'name': 'NID', 'value': '511=P_EQFKA54TxZTrfrxeLEJItli5F_9sSMiCdrB4YM-BPdlsVbLQnNBB3HyOM02ABE-A3d6ikzH52b9ucw5jZBTUF01elHDrSDeFLxN35c2S0ApIK-R93m1EWlmBsS0aPUpfwcvER1ivGPGDm5g-M8Ct_8xyEk_PLrLyRKInTNG3w', 'path': '/', 'domain': '.google.com', 'expiration': [2022, 8, 16, 10, 8, 37]}, {'session': False, 'httpOnly': False, 'secure': True, 'name': '1P_JAR', 'value': '2022-02-14-14', 'path': '/', 'domain': '.google.com', 'expiration': [2022, 3, 16, 10, 8, 43]}]