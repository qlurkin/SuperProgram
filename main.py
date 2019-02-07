import json
import sys
import requests

with open('config.json') as file:
	config = json.load(file)

response = requests.get(config['db_url'])
print(response.status_code)
db = response.json()

if len(sys.argv) < 2:
	print("Usage: main.py <matricule>")
	sys.exit()

matricule = sys.argv[1]

def createIndexedDB(db):
	indexedDB = {}

	for student in db:
		indexedDB[student['matetu']] = student

	return indexedDB

indexedDB = createIndexedDB(db)

def searchStudent(matricule, indexedDB):
	return indexedDB[matricule]['npetu']


print(searchStudent(matricule, indexedDB))

