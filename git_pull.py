# File: git_pull
# Author: Theo Technicguy
# Interpreter: Python 3.9
# Ext: py
# Licenced under GPU GLP v3. See LICENCE file for information.
# -----------------------

import json
import subprocess

from flask import Flask

# ---------- START Program Constants ----------
__version__ = "1.0.0"
__author__ = "Theo Technicguy"
# ---------- END Program Constants ----------

with open("git_pull.cfg") as file:
    cfg = json.load(file)

app = Flask(cfg["repository"])


@app.route("/", methods=["POST"])
def _pull():
    subprocess.run("git pull", shell=True)
    return "pulled"


app.run(host=cfg["ip"], port=cfg["port"])
