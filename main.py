import json
import sys
import requests

def createIndexedDB(db):
	indexedDB = {}

	for student in db:
		indexedDB[student['matetu']] = student

	return indexedDB

def searchStudent(matricule, indexedDB):
	try:
		return indexedDB[matricule]['npetu']
	except KeyError:
		return None

if __name__ == "__main__":
	with open('config.json') as file:
		config = json.load(file)
	response = requests.get(config['db_url'])
	db = response.json()
	if len(sys.argv) < 2:
		print("Usage: main.py <matricule>")
		sys.exit()
	matricule = sys.argv[1]
	indexedDB = createIndexedDB(db)
	print(searchStudent(matricule, indexedDB))

