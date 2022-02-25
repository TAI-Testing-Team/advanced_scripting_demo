import logging

log = logging.getLogger(__name__)


def run(context):
    def dismiss_modal():
        if _modal_exists(context):
            context.perform_gesture('tap', 'btn_no_thanks')

    # Add precondition that checks for the existence of a modal dialog.
    # The precondition logic dismisses the dialog.
    context.preconditions.append(dismiss_modal)

    # Prior to executing each step, the precondition function will be executed.
    # This ensures the modal dialog is dismissed prior to gesture execution.
    # context.perform_gesture('tap', 'btn_free')
    context.perform_gesture('tap', 'btn_paid')



def _modal_exists(context):
    driver = context.get_driver()
    try:
        driver.find_element('sign_up_modal')
        return True
    except:
        return False