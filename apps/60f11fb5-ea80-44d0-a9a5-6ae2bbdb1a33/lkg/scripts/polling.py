import logging

log = logging.getLogger(__name__)


def run(context):

    def wait_for_job_complete():
        jobs_table = context.find_element('jobs_table')

        # Verify there is exactly one row on the job table.
        assert len(jobs_table['rows']) == 1, 'Row count mismatch'

        # Verify the text on the first column within the first row.
        assert jobs_table['rows'][0][0] == 'There are currently no jobs scheduled or running.'

    # Wait up to 180 seconds for the job to complete, sleeping for 15 seconds in between each attempt.
    # Exits early if the condition is met before 180 seconds have elapsed.
    context.wait(wait_for_job_complete, 180, sleep_in_between=15)