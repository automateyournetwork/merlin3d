# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import os
import sys
import datetime
import yaml
import time
import json
import shutil
import logging
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from jinja2 import Environment, FileSystemLoader
from general_functionalities import ParseShowCommandFunction, ParseLearnFunction, ParseConfigFunction, ParseDictFunction

# ----------------
# Get logger for script
# ----------------

log = logging.getLogger(__name__)

# ----------------
# Template Directory
# ----------------

template_dir = 'templates/cisco/nxos'
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect(learn_hostname=True)

# ----------------
# Test Case #1
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        i = 1
        while i <= 500:
            for device in testbed:
                # ---------------------------------------
                # Execute learn for various functions
                # ---------------------------------------
                # Interface
                self.parsed_show_ip_int_brief = ParseShowCommandFunction.parse_show_command(steps, device, "show ip interface brief")
                # ---------------------------------------
                # Create JSON, YAML, CSV, MD, HTML, HTML Mind Map files from the Parsed Data
                # ---------------------------------------         
                with steps.start('Store data',continue_=True) as step:              
                    # Learned interface
                    if self.parsed_show_ip_int_brief is not None:

                        today = datetime.datetime.now()
                        date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

                        IP_Int_Brief_blender_template = env.get_template('IP_Int_Brief_blender.j2')                    
                        IP_Int_Brief_blender = IP_Int_Brief_blender_template.render(date=date_time,ip_int_brief=self.parsed_show_ip_int_brief['interface'])
                    
                        with open("Camelot/IP_Interface_Brief/%s_IP_Interface_Brief.json" % device.alias, "w") as fh:
                            fh.write(IP_Int_Brief_blender)
                            fh.close()

                        i += 1                            