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
        while i <= 50:
            for device in testbed:
                # ---------------------------------------
                # Execute learn for various functions
                # ---------------------------------------
                # Interface
                self.learned_interface = ParseLearnFunction.parse_learn(steps, device, "interface")
                # ---------------------------------------
                # Create JSON, YAML, CSV, MD, HTML, HTML Mind Map files from the Parsed Data
                # ---------------------------------------         
                with steps.start('Store data',continue_=True) as step:              
                    # Learned interface
                    if self.learned_interface is not None:
                        today = datetime.datetime.now()
                        date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

                        Mgmt0_IO_blender_template = env.get_template('Mgmt0_IO_Bar_Graph_blender.j2')                    
                        Mgmt0_IO_blender = Mgmt0_IO_blender_template.render(Mgmt0=self.learned_interface['Mgmt0'],date=date_time)

                        with open("Camelot/Mgmt0_Graphs/%s_Mgmt0_IO_Bar_Graph_blender.json" % device.alias, "w") as fh:
                            fh.write(Mgmt0_IO_blender)
                            fh.close()

                        Mgmt0_Input_blender_template = env.get_template('Mgmt0_Input_Line_Graph_blender.j2')
                        Mgmt0_Input_blender = Mgmt0_Input_blender_template.render(Mgmt0=self.learned_interface['Mgmt0'],date=date_time)

                        with open("Camelot/Mgmt0_Graphs/%s_Mgmt0_Input_Line_Graph_blender.json" % device.alias) as f:
                            original_input_counter = json.load(f)
                            f.close

                        original_input_counter.append(Mgmt0_Input_blender)

                        Mgmt0_New_Input_blender_template = env.get_template('No_Quotes.j2')
                        Mgmt0_New_Input_blender = Mgmt0_New_Input_blender_template.render(new_list=original_input_counter)
    

                        with open("Camelot/Mgmt0_Graphs/%s_Mgmt0_Input_Line_Graph_blender.json" % device.alias, "w") as fh:
                            fh.write(Mgmt0_New_Input_blender)
                            fh.close()

                        Mgmt0_Output_blender_template = env.get_template('Mgmt0_Output_Line_Graph_blender.j2')
                        Mgmt0_Output_blender = Mgmt0_Output_blender_template.render(Mgmt0=self.learned_interface['Mgmt0'],date=date_time)

                        with open("Camelot/Mgmt0_Graphs/%s_Mgmt0_Output_Line_Graph_blender.json" % device.alias) as f:
                            original_output_counter = json.load(f)
                            f.close

                        original_output_counter.append(Mgmt0_Output_blender)

                        Mgmt0_New_Output_blender_template = env.get_template('No_Quotes.j2')
                        Mgmt0_New_Output_blender = Mgmt0_New_Output_blender_template.render(new_list=original_output_counter)

                        with open("Camelot/Mgmt0_Graphs/%s_Mgmt0_Output_Line_Graph_blender.json" % device.alias, "w") as fh:
                            fh.write(Mgmt0_New_Output_blender)
                            fh.close()
                        i += 1                            