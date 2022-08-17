# importing the module
import json
from collections import namedtuple


def customDecoder(geek_dict):
    return namedtuple('X', geek_dict.keys())(*geek_dict.values())


geekJsonData = '{"name" : "sukumar", "id" : 1, "location" : "chittoor"}'

x = json.loads(geekJsonData, object_hook=customDecoder)

print(x)
print(x.name, x.id, x.location)
