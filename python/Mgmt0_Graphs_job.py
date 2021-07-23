'''
To run the job:

$ pyats run job Mgmt0_Graphs_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml

'''

import os
from genie.testbed import load

def main(runtime):

    # ----------------
    # Load the testbed
    # ----------------
    if not runtime.testbed:
        # If no testbed is provided, load the default one.
        # Load default location of Testbed
        testbedfile = os.path.join('testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
        testbed = load(testbedfile)
    else:
        # Use the one provided
        testbed = runtime.testbed

    # Find the location of the script in relation to the job file
    testscript = os.path.join(os.path.dirname(__file__), 'Mgmt0_Graphs.py')

    # run script
    runtime.tasks.run(testscript=testscript, testbed=testbed)