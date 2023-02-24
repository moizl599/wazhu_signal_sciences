from SigSciApiPy.SigSci import *
import os.path
import json

# setup sigsci api module
sigsci = SigSciAPI()

# required variables
sigsci.email = "moiz.lakdawala@workjam.com"
sigsci.corp = "workjam"
sigsci.site = "gcp-prod"
sigsci.api_token = "fa003294-5c0d-48ac-be69-67fe01e2b55a"
tags = ['SQLI', 'XSS']
sigsci.from_time = "-7d"

# check if temp file already exists, if so then delete it
'''
if os.path.isfile(sigsci.file):
    os.remove(sigsci.file)

if sigsci.authenticate():
    sigsci.get_agent_metrics()

with open(sigsci.file) as json_file:
    agents = json.load(json_file)

for agent in agents['data']:
    print(agent['agent.current_requests'])
'''


def merge_JsonFiles(filename):
    result = list()
    for f2 in filename:
        f1 = f"/tmp/sig_sci/{f2}"
        with open(f1, 'r') as infile:
            result.append(json.load(infile))

    with open('/tmp/sig_sci/merged_data.json', 'w') as output_file:
        json.dump(result, output_file)


if sigsci.authenticate():
    for tag in tags:
        sigsci.file = f"/tmp/sig_sci/{tag}_sigsci_logs.json"
        if os.path.isfile(sigsci.file):
            os.remove(sigsci.file)
        sigsci.get_list_events(tag)
        with open(sigsci.file) as json_file:
            logs = json.load(json_file)

files = os.listdir("/tmp/sig_sci/")
merge_JsonFiles(files)
