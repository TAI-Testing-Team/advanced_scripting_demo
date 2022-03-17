def run(context):
# Resetting a value to create initial conditions for test
    script_vals = context.get_test_script_vals()
    script_vals['new_value_name'] = 'valuetwo'