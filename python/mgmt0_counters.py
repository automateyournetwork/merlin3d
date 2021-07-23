import requests
import json

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\Mgmt0_Graphs\\DevNet_Sandbox_Nexus9k_Mgmt0_IO_Bar_Graph_blender.json') as f:
    mgmt0_counters = json.load(f)

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\Mgmt0_Graphs\\DevNet_Sandbox_Nexus9k_Mgmt0_Input_Line_Graph_blender.json') as f:
    mgmt0_input_rate = json.load(f)

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\Mgmt0_Graphs\\DevNet_Sandbox_Nexus9k_Mgmt0_Output_Line_Graph_blender.json') as f:
    mgmt0_output_rate = json.load(f) 

print(mgmt0_counters)
