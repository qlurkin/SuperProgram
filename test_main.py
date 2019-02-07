import unittest
import main

class Test(unittest.TestCase):
	def test_search(self):
		indexedDB = {
			"11111": {"npetu": "Lurkin"}
		}

		self.assertEqual(main.searchStudent("11111", indexedDB), "Lurkin")

	def test_not_found(self):
		indexedDB = {
			"11111": {"npetu": "Lurkin"}
		}

		self.assertEqual(main.searchStudent("11112", indexedDB), None)

unittest.main()
