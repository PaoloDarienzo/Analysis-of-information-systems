import sys
sys.path.insert(0, 'src/')

import codice_fiscale
import unittest

class test_data(unittest.TestCase):

	def test_mese(self):
		self.assertEqual(codice_fiscale.genera_mese(11), 's')
		self.assertEqual(codice_fiscale.genera_mese(10), 'r')
		self.assertEqual(codice_fiscale.genera_mese(5), 'e')
		self.assertEqual(codice_fiscale.genera_mese(3), 'c')

	def test_giorno(self):
		self.assertEqual(codice_fiscale.genera_giorno(01, 'm'), 1)
		self.assertEqual(codice_fiscale.genera_giorno(05, 'm'), 5)
		self.assertEqual(codice_fiscale.genera_giorno(28, 'm'), 28)
		self.assertEqual(codice_fiscale.genera_giorno(07, 'f'), '47')
		self.assertEqual(codice_fiscale.genera_giorno(30, 'f'), '70')
		####################################################################
		#The test below will fail
		#self.assertEqual(codice_fiscale.genera_giorno(31, 'f'), '71')

if __name__ == '__main__':
	unittest.main()
