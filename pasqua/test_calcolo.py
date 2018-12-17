import sys
sys.path.insert(0, 'src/')

from pasqua import calcolo_pasqua
import unittest

class test_easter_algorithm(unittest.TestCase):

	#if d+e<10, then easter is in March
	def test_easter_in_march(self):
		self.assertEqual(calcolo_pasqua(2002).strftime("%Y-%m-%d"), '2002-03-31')
		self.assertEqual(calcolo_pasqua(2008).strftime("%Y-%m-%d"), '2008-03-23')

	#if d+e>=10, then easter is in April
	def test_easter_in_april(self):
		self.assertEqual(calcolo_pasqua(2000).strftime("%Y-%m-%d"), '2000-04-23')
		self.assertEqual(calcolo_pasqua(2001).strftime("%Y-%m-%d"), '2001-04-15')

	#if result is is April 26th or April 25th (and d=28, e=6, a>10), then result should be result-7
	def test_easter_exception(self):
		self.assertEqual(calcolo_pasqua(1978).strftime("%Y-%m-%d"), '1978-03-19')
		self.assertEqual(calcolo_pasqua(1989).strftime("%Y-%m-%d"), '1989-03-19')

if __name__ == '__main__':	
	unittest.main()
