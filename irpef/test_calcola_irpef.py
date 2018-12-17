import sys
sys.path.insert(0, 'src/')

from irpef import calcola_irpef
import unittest

class test_calcola_irpef(unittest.TestCase):

	def test_calcolo(self):

		self.assertAlmostEqual(calcola_irpef(float(0)), 0.00, delta=0.01)
		self.assertAlmostEqual(calcola_irpef(float(15000)), 3450.00, delta=0.01)
		self.assertAlmostEqual(calcola_irpef(float(20000.50)), 4800.14, delta=0.01)
		self.assertAlmostEqual(calcola_irpef(float(75000)), 25420.00, delta=0.01)
		self.assertAlmostEqual(calcola_irpef(float(15000089.89)), 6443208.65, delta=0.01)


if __name__ == '__main__':
	unittest.main()
