"""
Generar JSON para ejercicio de años bisiestos
"""

def es_bisiesto(anio):
    "Determinar si un año dado es bisiesto."
    if anio % 400 == 0 or anio % 4 == 0 and anio % 100 != 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto


import json

FILENAME = ".github/classroom/autograding.json"

cases = [
    ("no_bisiesto", 2021),
    ("bisiesto_no_secular", 2020),
    ("bisiesto_secular", 2000),
    ("secular_no_bisiesto", 2100)
    ]

output = {}
tests = []

for tag, case in cases:
    inp = f"{case}"
    if es_bisiesto(case):
        outp = "sí"
    else:
        outp = "no"
    name = tag
    entry = {
        "name": name,
        "setup": "",
        "run": "LANG=en_US.utf8 timeout 3m python3 main.py",
        "input": inp,
        "output": outp,
        "comparison": "included",
        "timeout": 1,
        "points": 1
        }
    tests.append(entry)
tests = {"tests": tests}

with open(FILENAME, "w") as f:
    json.dump(tests, f, indent=2)
