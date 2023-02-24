import json

files = open("/tmp/sig_sci/logs.json")
json_file = json.load(files)

print(type(json_file))
val1 = (json_file[1])
print(type(val1))
print(val1.keys())
del val1['totalCount']
print(val1.keys())
val_in = val1['data']

