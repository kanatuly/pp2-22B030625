import json
from tabulate import tabulate

f = open("sample-data.json", "r")
data = json.load(f)
output_data = []
headers = ['dn', 'descr', 'speed', 'mtu']

for item in data["imdata"]:
    output_data.append([item["l1PhysIf"]["attributes"][header] for header in headers])


print(tabulate(output_data, headers=["DN", "Description", "Speed", "MTU"]))
