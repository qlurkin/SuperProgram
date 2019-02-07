import unittest
import main

class Test(unittest.TestCase):
	def setUp(self):
		self.indexedDB = {
			"11111": {"npetu": "Lurkin"}
		}

	def test_search(self):
		self.assertEqual(main.searchStudent("11111", self.indexedDB), "Lurkin")

	def test_not_found(self):
		self.assertEqual(main.searchStudent("11112", self.indexedDB), None)

unittest.main()
