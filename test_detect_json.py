import json

# read json
with open("test.json", "r") as f:
    data = json.load(f)

print(len(data.get("items")))
