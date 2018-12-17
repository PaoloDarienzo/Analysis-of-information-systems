import sys
sys.path.insert(0, 'src/')

import codice_fiscale
import unittest

class test_codici(unittest.TestCase):

	def test_codice_comune(self):
		self.assertEqual(codice_fiscale.codice_comune('verona'), 'l781')
		self.assertEqual(codice_fiscale.codice_comune('udine'), 'l483')
		self.assertEqual(codice_fiscale.codice_comune('legnago'), 'e512')
		####################################################################
		#The test below will fail and result in an error
		#self.assertEqual(codice_fiscale.genera_giorno('aversa'), 'a512')

	def test_codice_controllo(self):
		#*** fiscal code; omitted for privacy
		#* code; omitted for privacy
		self.assertEqual(codice_fiscale.genera_codice_controllo('***'), '*')
		self.assertEqual(codice_fiscale.genera_codice_controllo('***'), '*')

if __name__ == '__main__':
	unittest.main()
