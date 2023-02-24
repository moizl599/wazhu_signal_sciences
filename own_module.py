import requests
import json

# Initial setup

endpoint = 'https://dashboard.signalsciences.net/api/v0'

email = 'moiz.lakdawala@workjam.com'
token = 'ec4e281d-32b3-4177-9c84-73777c7ceab9'

# Fetch list of corps

headers = {
    'Content-type': 'application/json',
    'x-api-user': email,
    'x-api-token': token
}
actions = ['info', 'flagged']
tags = ['SQLI', 'XSS', 'TRAVERSAL', 'BACKDOOR', 'LOG4J-JNDI', 'AWS-SSRF']
logs = {}
blocked_ips = []
days = 7
for action in actions:
    if action == 'info':
        for tag in tags:
            corps = requests.get(
                endpoint + f'/corps/workjam/sites/gcp-prod/events?&pretty=True&tag={tag}&from=-{days}d',
                headers=headers)
            query_results = json.loads(corps.text)
            data = query_results['data']
            for z in range(len(data)):
                extracted_data = data[z]
                if extracted_data["source"]:
                    logs.update(extracted_data)

                    all_logs = json.dumps(logs)
                    with open("sample.json", "a") as outfile:
                        outfile.write(all_logs)
