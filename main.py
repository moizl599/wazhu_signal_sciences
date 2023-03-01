from SigSciApiPy.SigSci import *
import os.path
import json
from random import random
# setup sigsci api module
sigsci = SigSciAPI()

# required variables
sigsci.email = "moiz.lakdawala@workjam.com"
sigsci.corp = "workjam"
sigsci.site = "gcp-prod"
sigsci.api_token = "fa003294-5c0d-48ac-be69-67fe01e2b55a"
tags = ['SQLI']
sigsci.from_time = "-7d"
if sigsci.authenticate():
    for tag in tags:
        signal_science_logs = {'WAF_timestamp':'',
                               'WAF_source':'',
                               'WAF_Remote_country':'',
                               'WAF_action':'',
                               'WAF_reason':'',
                               }
        sigsci.file = f"C:\\Users\\Moiz\\logs\\{tag}.json"
        lopgfile= f"C:\\Users\\Moiz\\logs\\{tag}_logs.log"
        if os.path.isfile(sigsci.file):
            os.remove(sigsci.file)
        if os.path.isfile(lopgfile):
            os.remove(lopgfile)
        with open(lopgfile, 'x') as logs_file:
            test = sigsci.get_list_events(tag)
            data = test['data']
            for z in range(len(data)):
                    extracted_data = data[z]
                    res = {key: extracted_data[key] for key in extracted_data.keys()
        & {'timestamp','source','remoteCountryCode','action','reasons'}}
                    signal_science_logs = {'WAF_timestamp':res['timestamp'],
                               'WAF_source':res['source'],
                               'WAF_Remote_country':res['remoteCountryCode'],
                               'WAF_action':res['action'],
                               'WAF_reason':res['reasons'],
                               }
                    with open(f"C:\\Users\\Moiz\\logs\\{tag}_logs.log", 'a') as f:
                         json.dump(signal_science_logs,f)
                         f.write('\n')

             
       
