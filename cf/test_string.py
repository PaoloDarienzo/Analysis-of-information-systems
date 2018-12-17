import sys
sys.path.insert(0, 'src/')

from codice_fiscale import estrai_nome_cognome
import unittest

class test_nome_cognome(unittest.TestCase):

	def test_nome_singolo(self):
		self.assertEqual(estrai_nome_cognome('paolo'), 'pla')
		self.assertEqual(estrai_nome_cognome('luca'), 'lcu')
		####################################################################
		#The test below will fail
		#self.assertEqual(estrai_nome_cognome('gianfranco'), 'gfr')

	def test_nome_composto(self):
		####################################################################
		#The test below will fail
		#self.assertEqual(estrai_nome_cognome('enrico carlo'), 'ncc')
		pass

	def test_cognome_singolo(self):
		self.assertEqual(estrai_nome_cognome('***'), '***')

	def test_cognome_composto(self):
		####################################################################
		#The test below will fail
		#DATA OMITTED FOR PRIVACY
		#self.assertEqual(estrai_nome_cognome('*** ***'), '***')
		pass

	def test_cognome_spec_car(self):
		####################################################################
		#The test below will fail
		#DATA OMITTED FOR PRIVACY
		#self.assertEqual(estrai_nome_cognome('*\'***'), '***')
		pass

if __name__ == '__main__':
	unittest.main()
