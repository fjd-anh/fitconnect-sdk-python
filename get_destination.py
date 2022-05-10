#!/usr/bin/env poetry run

from datetime import datetime
from fitconnect import FITConnectClient, Environment
from read_config import read_config_sender
from strictyaml import load, Map, Str, Int, Seq, YAMLError
from strictyaml import Enum as YAMLEnum
import json
import logging

# configure logging. Uncomment to enable logging. Python's default logging level
# is WARN.
logging.basicConfig()
logging.getLogger('fitconnect').level = logging.INFO

# read config_file
config = read_config_sender('conf/sender.yaml')

# initialize SDK
fitc = FITConnectClient(Environment[config['sdk']['environment']], config['sdk']['client_id'], config['sdk']['client_secret'])

response = fitc.get_destination(config['destination_id'])
print(json.dumps(response.json(), indent=2))
