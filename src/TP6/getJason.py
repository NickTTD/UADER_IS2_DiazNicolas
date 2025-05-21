# Código original decompilado con pylingual, lo edité en getJasonEdit.py
import json
import sys

jsonfile = sys.argv[1]
jsonkey = "token1"
with open(jsonfile, "r") as myfile:
    data = myfile.read()
obj = json.loads(data)
print(str(obj[jsonkey]))
