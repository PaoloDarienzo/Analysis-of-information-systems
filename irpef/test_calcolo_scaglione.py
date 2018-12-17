import sys
sys.path.insert(0, 'src/')

from irpef import calcolo_scaglione
import unittest

class test_calcolo_scaglione(unittest.TestCase):

	def test_scaglione(self):
		self.assertEqual(calcolo_scaglione(float(0)), [15000, 23])
		self.assertEqual(calcolo_scaglione(float(25000.86)), [15000, 27])
		self.assertEqual(calcolo_scaglione(float(75000)), [55000, 41])
		self.assertEqual(calcolo_scaglione(float(76000.01)), [75000, 43])


if __name__ == '__main__':
	unittest.main()
