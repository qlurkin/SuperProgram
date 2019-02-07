import json
import sys

with open('db.json') as file:
	db = json.load(file)

if len(sys.argv) < 2:
	print("Usage: main.py <matricule>")
	sys.exit()

matricule = sys.argv[1]

indexedDB = {}

for student in db:
	indexedDB[student['matetu']] = student


print(indexedDB[matricule]['npetu'])

