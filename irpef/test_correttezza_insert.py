import sys
sys.path.insert(0, 'src/')

from irpef import reddito_corretto
import unittest

class test_main_irpef(unittest.TestCase):
	
	def test_reddito_insert(self):
						
		self.assertEqual(reddito_corretto('value'), False)
		self.assertEqual(reddito_corretto(25000), True)
		self.assertEqual(reddito_corretto('25000'), True)
		self.assertEqual(reddito_corretto(25000.9871), True)
		self.assertEqual(reddito_corretto('25000.9871'), True)
		self.assertEqual(reddito_corretto(-100), False)

if __name__ == '__main__':	
	unittest.main()
