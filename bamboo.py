#!/usr/bin/env python

from workflow import Workflow3
from workflow.util import set_config
import requests
import sys
import os

# uncomment the below if you want to use a .env file for subdomain and apiKey
#from dotenv import load_dotenv
#load_dotenv()

def fetchEmployees():
    api_key = os.environ.get('apiKey')
    subdomain = os.environ.get('subdomain')
    url = f"https://api.bamboohr.com/api/gateway.php/{subdomain}/v1/employees/directory"
    headers = {'Accept': 'application/json'}
    r = requests.get(url, headers=headers, auth=(api_key, 'x'))
    return(r.json()['employees'])

def main(wf):
    employees = wf.cached_data('employees', data_func=fetchEmployees, max_age=86400)
    #wf.add_item(employees[0]['displayName'])
    #map(lambda x: wf.logger.debug(x['displayName']), employees)
    #map(lambda x: wf.add_item(x['displayName']), employees)
    for employee in employees:
        wf.add_item(employee['displayName'], subtitle=f"{employee['jobTitle']} ({employee['department']}) - {employee['workEmail']}",
                    copytext=f"{employee['displayName']} <{employee['workEmail']}>", quicklookurl=employee['photoUrl'], arg=employee['photoUrl'],
                    valid=True)
    wf.send_feedback()
    

if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))