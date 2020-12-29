# File: git_pull
# Author: Theo Technicguy
# Interpreter: Python 3.9
# Ext: py
# Licenced under GPU GLP v3. See LICENCE file for information.
# -----------------------

import json
import os
import subprocess

from flask import Flask

# ---------- START Program Constants ----------
__version__ = "1.0.1"
__author__ = "Theo Technicguy"
# ---------- END Program Constants ----------

WORK_DIR = os.path.dirname(__file__)
CFG_PATH = os.path.join(WORK_DIR, "git_pull.cfg")

with open(CFG_PATH) as file:
    cfg = json.load(file)

app = Flask(cfg["repository"])


@app.route("/", methods=["POST"])
def _pull():
    subprocess.run("git pull", shell=True)
    return "pulled"


app.run(host=cfg["ip"], port=cfg["port"])
