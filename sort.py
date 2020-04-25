from openpyxl import *
import json

data = {}
data['Kingdom'] = []
data['Park'] = []
data['Persona'] = []

wb = load_workbook('LetsPlay.xlsx')

for row in wb['Kingdom'].values: 
    data['Kingdom']+= row

for row in wb['Park'].values:
    data['Park']+= row

for row in wb['Persona'].values:
    data['Persona'] += row

for row in wb['Persona2'].values:
    data['Persona']+= row

for row in wb['Persona3'].values:
    data['Persona']+= row

for row in wb['Persona4'].values:
    data['Persona']+= row

for row in wb['Persona5'].values:
    data['Persona']+= row

for row in wb['Persona6'].values:
    data['Persona']+= row

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4, sort_keys=True)