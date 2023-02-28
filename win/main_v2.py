from SigSciApiPy.SigSci import *
import os.path
import json
import time
from random import random
import re
# setup sigsci api module
sigsci = SigSciAPI()

# required variables
sigsci.email = "moiz.lakdawala@workjam.com"
sigsci.corp = "workjam"
sigsci.site = "gcp-prod"
sigsci.api_token = "fa003294-5c0d-48ac-be69-67fe01e2b55a"
tags = ['SQLI']
sigsci.from_time = "-3d"

if sigsci.authenticate():
    for tag in tags:
        handcrrafted_logs=[]
        main_logs={}
        sigsci.file = f"C:\\Users\\Moiz\\logs\\{tag}.json"
        if os.path.isfile(sigsci.file):
            os.remove(sigsci.file)
        test = sigsci.get_list_events(tag)
        data = test['data']
        for z in range(len(data)):
                extracted_data = data[z]
                print(extracted_data.keys())