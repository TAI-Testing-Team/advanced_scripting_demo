def run(context):
   def dismiss_modal():
       if _survey_iframe_exists(context):
           context.perform_gesture('tap', 'no_thanks_button')

   # Add precondition that checks for the existence of a modal dialog.
   # The precondition logic dismisses the dialog.
   context.preconditions.append(dismiss_modal)

   # Prior to executing each step, the precondition function will be executed.
   # This ensures the modal dialog is dismissed prior to gesture execution.
   context.perform_gesture('tap', 'deals_menu')
   context.perform_gesture('tap', 'laptop_deals_menu')


def _survey_iframe_exists(context):
   try:
       context.get_driver().find_element_by_id('iframeSurvey')
       return True
   except:
       return False