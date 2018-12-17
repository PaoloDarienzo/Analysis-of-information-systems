import sys
sys.path.insert(0, 'src/')

from pasqua import is_year_correct
import unittest

class test_main_easter(unittest.TestCase):
	
	def test_year_inserted(self):
						
		self.assertEqual(is_year_correct('value'), False)
		self.assertEqual(is_year_correct(1980), True)
		self.assertEqual(is_year_correct('1980'), True)
		self.assertEqual(is_year_correct(2018), True)
		self.assertEqual(is_year_correct(1582), False)
		self.assertEqual(is_year_correct(2500), False)

if __name__ == '__main__':	
	unittest.main()
