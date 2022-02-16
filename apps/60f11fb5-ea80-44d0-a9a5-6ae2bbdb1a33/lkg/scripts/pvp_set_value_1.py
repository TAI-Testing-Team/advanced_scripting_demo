def run(context):
# Can place a value for later use within a subsequently executed script.
    script_vals = context.get_test_script_vals()
    script_vals['new_value_name'] = 'valueone'

    # Can retrieve a value within a subsequently executed script.
    # script_vals = context.get_test_script_vals()
    # new_value = script_vals['new_value_name']