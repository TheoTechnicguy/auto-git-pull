# File: git_pull
# Author: Theo Technicguy
# Interpreter: Python 3.9
# Ext: py
# Licenced under GPU GLP v3. See LICENCE file for information.
# -----------------------

import datetime
import json
import os
import subprocess

from flask import Flask

# ---------- START Program Constants ----------
__version__ = "1.0.2"
__author__ = "Theo Technicguy"
# ---------- END Program Constants ----------

WORK_DIR = os.path.dirname(__file__)
CFG_PATH = os.path.join(WORK_DIR, "git_pull.cfg")

with open(CFG_PATH) as file:
    cfg = json.load(file)

app = Flask(cfg["repository"])


@app.route("/", methods=["POST"])
def _pull():
    subprocess.run(f"cd {WORK_DIR} && git pull", shell=True)
    return f"Pulled at {datetime.datetime.now()}"


app.run(host=cfg["ip"], port=cfg["port"])
