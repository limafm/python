import json

json_file = "example.json"

with open(json_file) as json_data_file:
  data = json.load(json_data_file)

print (json.dumps(data))