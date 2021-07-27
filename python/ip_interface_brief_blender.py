import bpy
import json

with open('\\\wsl$\\Ubuntu\\home\\capobj\\merlin3d\\Camelot\\IP_Interface_Brief\\DevNet_Sandbox_Nexus9k_IP_Interface_Brief.json') as f:
    ip_interface_brief = json.load(f)

for count, item in enumerate(ip_interface_brief, start=1):
    if count <= 9:
        if item[8] == "HEALTHY":
            bpy.data.objects['NIC.00%s' % count].material_slots[0].material = bpy.data.materials['UP']
            bpy.data.objects['indicator.00%s' % count].material_slots[0].material = bpy.data.materials['indicator_up']
            bpy.data.objects['message_label.00%s' % count].material_slots[0].material = bpy.data.materials['UP']
            bpy.data.objects['message_value.00%s' % count].material_slots[0].material = bpy.data.materials['UP']            
            bpy.data.objects['status_label.00%s' % count].material_slots[0].material = bpy.data.materials['UP']
            bpy.data.objects['status_value.00%s' % count].material_slots[0].material = bpy.data.materials['UP']
        elif item[8] == "NOT HEALTHY":
            bpy.data.objects['NIC.00%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['indicator.00%s' % count].material_slots[0].material = bpy.data.materials['indicator_down']            
            bpy.data.objects['message_label.00%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['message_value.00%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['status_label.00%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['status_value.00%s' % count].material_slots[0].material = bpy.data.materials['DOWN']

        if item[0].startswith("Vlan"):
            bpy.data.objects['Interface_Name_Text.00%s' % count].material_slots[0].material = bpy.data.materials['VLAN_Interface']

        if item[0].startswith("Lo"):
            bpy.data.objects['Interface_Name_Text.00%s' % count].material_slots[0].material = bpy.data.materials['Loopback_Interface']     
        
        if item[0].startswith("Eth"):
            bpy.data.objects['Interface_Name_Text.00%s' % count].material_slots[0].material = bpy.data.materials['Ethernet_Interface']
    else:
        if item[8] == "HEALTHY":
            bpy.data.objects['NIC.0%s' % count].material_slots[0].material = bpy.data.materials['UP']
            bpy.data.objects['indicator.0%s' % count].material_slots[0].material = bpy.data.materials['indicator_up']            
            bpy.data.objects['message_label.0%s' % count].material_slots[0].material = bpy.data.materials['UP']            
            bpy.data.objects['message_value.0%s' % count].material_slots[0].material = bpy.data.materials['UP']
            bpy.data.objects['status_label.0%s' % count].material_slots[0].material = bpy.data.materials['UP']
            bpy.data.objects['status_value.0%s' % count].material_slots[0].material = bpy.data.materials['UP']
        elif item[8] == "NOT HEALTHY":
            bpy.data.objects['NIC.0%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['indicator.0%s' % count].material_slots[0].material = bpy.data.materials['indicator_down']            
            bpy.data.objects['message_label.0%s' % count].material_slots[0].material = bpy.data.materials['DOWN']            
            bpy.data.objects['message_value.0%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['status_label.0%s' % count].material_slots[0].material = bpy.data.materials['DOWN']
            bpy.data.objects['status_value.0%s' % count].material_slots[0].material = bpy.data.materials['DOWN']

        if item[0].startswith("Vlan"):
            bpy.data.objects['Interface_Name_Text.0%s' % count].material_slots[0].material = bpy.data.materials['VLAN_Interface']

        if item[0].startswith("Lo"):
            bpy.data.objects['Interface_Name_Text.0%s' % count].material_slots[0].material = bpy.data.materials['Loopback_Interface']     
        
        if item[0].startswith("Eth"):
            bpy.data.objects['Interface_Name_Text.0%s' % count].material_slots[0].material = bpy.data.materials['Ethernet_Interface']        
        