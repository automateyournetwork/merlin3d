import bpy
import json

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\Mgmt0_Graphs\\DevNet_Sandbox_Nexus9k_Mgmt0_IO_Bar_Graph_blender.json') as f:
    mgmt0_counters = json.load(f)

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\Mgmt0_Graphs\\DevNet_Sandbox_Nexus9k_Mgmt0_Input_Line_Graph_blender.json') as f:
    mgmt0_input_rate = json.load(f)

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\Mgmt0_Graphs\\DevNet_Sandbox_Nexus9k_Mgmt0_Output_Line_Graph_blender.json') as f:
    mgmt0_output_rate = json.load(f)

bpy.data.objects['Cylinder.001'].material_slots[0].material = bpy.data.materials['Input']
bpy.data.objects['InputLine'].material_slots[0].material = bpy.data.materials['Input']
bpy.data.objects['Cylinder.002'].material_slots[0].material = bpy.data.materials['Output']
bpy.data.objects['OutputLine'].material_slots[0].material = bpy.data.materials['Output']

print(mgmt0_counters)
