import sys
sys.path.insert(0, 'src/')

from contextlib import contextmanager
from StringIO import StringIO

from pasqua import main
import unittest

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class test_main_easter(unittest.TestCase):

	def test_year_sequence(self):
	
		inputs = ['2000', 'test', '1582']
		
		try:
			fake_input = inputs.pop
			original_raw_input = __builtins__.raw_input
			__builtins__.raw_input = lambda _: fake_input()
		
			with captured_output() as (out, err):
				main()
				output = out.getvalue().strip()
			
			self.assertEqual(output, '23 April 2000')
		
		finally:
			__builtins__.raw_input = original_raw_input

	def test_easter(self):
		
		try:
			original_raw_input = __builtins__.raw_input
			
			__builtins__.raw_input = lambda _: '2018'
			with captured_output() as (out, err):
				main()
				output = out.getvalue().strip()
			self.assertEqual(output, '01 April 2018')
			
			__builtins__.raw_input = lambda _: '1980'
			with captured_output() as (out, err):
				main()
				output = out.getvalue().strip()
			self.assertEqual(output, '06 April 1980')			
		
		finally:
			__builtins__.raw_input = original_raw_input

		
if __name__ == '__main__':	
	unittest.main()
