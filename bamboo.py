#!/usr/bin/env python

from workflow import Workflow3
from workflow.util import set_config
import requests
import sys
from dotenv import load_dotenv
import os 

load_dotenv()

def main(wf):
    api_key = os.environ.get('apiKey')
    url = 'https://api.bamboohr.com/api/gateway.php/signalai/v1/employees/directory'
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers, auth=(api_key, 'x'))
    wf.logger.debug(r.json())
    

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))