# File: git_pull
# Author: Theo Technicguy
# Interpreter: Python 3.9
# Ext: py
# Licenced under GPU GLP v3. See LICENCE file for information.
# -----------------------

import datetime
import json
import logging
import os
import subprocess

from flask import Flask

# ---------- START Program Constants ----------
__version__ = "1.0.2"
__author__ = "Theo Technicguy"
# ---------- END Program Constants ----------

logging.basicConfig(
    filename=__file__ + ".log",
    level=logging.DEBUG,
    format="%(levelname)s at %(asctime)s: %(message)s",
    filemode="w",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)

logging.info(f"Running on version {__version__}.")

WORK_DIR = os.path.dirname(__file__)
CFG_PATH = os.path.join(WORK_DIR, "git_pull.cfg")
logging.debug(f"Config file expected at {CFG_PATH}")

with open(CFG_PATH) as file:
    cfg = json.load(file)
logging.debug(f"Config file contents: {json.dumps(cfg)}")

app = Flask(cfg["repository"])


@app.route("/", methods=["POST"])
def _pull():
    pull = subprocess.run("git pull", shell=True, capture_output=True)
    return f"Pulled on {datetime.datetime.now()} with result {pull.stdout.decode()}"


app.run(host=cfg["ip"], port=cfg["port"])
