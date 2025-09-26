import json
file = open("students.json", "r")
data = json.load(file)

name_lookup = {v["PathName"]: v for v in data.values()}

