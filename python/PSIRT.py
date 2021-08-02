# ----------------
# Copyright
# ----------------
# Written by John Capobianco, August 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import datetime
import json
from jinja2 import Environment, FileSystemLoader

# ----------------
# Template Directory
# ----------------

template_dir = "templates/cisco/PSIRT"
env = Environment(loader=FileSystemLoader(template_dir))

# ----------------
# Load Sample JSON
# ----------------

with open('templates/cisco/PSIRT/Sample_PSIRT.json') as f:
    raw_psirt = json.load(f)
    f.close()

today = datetime.datetime.now()
date_time = today.strftime("%m/%d/%Y, %H:%M:%S")

# ----------------
# Template to Blender Array of Arrays
# ----------------

PSIRT_blender_template = env.get_template("PSIRT_Blender.j2")
PSIRT_blender = PSIRT_blender_template.render(date=date_time,PSIRT=raw_psirt['advisories'])

# ----------------
# Save new File
# ----------------

with open("Camelot/PSIRT/PSIRT.json", "w") as fh:
    fh.write(PSIRT_blender)
    fh.close()