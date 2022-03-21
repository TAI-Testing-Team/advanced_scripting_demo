def run(context):
    def before_each_step():
        context.verify(labels=["icn_cart"])   
    context.explore(3, before_each_step=before_each_step, ignore_element_errors=True)