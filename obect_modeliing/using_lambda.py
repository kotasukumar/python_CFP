import json
from collections import namedtuple

data = '{"name" : "sukumar", "id" : 1, "location" : "chittoor"}'
print(data)

x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

print(x)
print(x.name, x.id, x.location)
