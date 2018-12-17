import sys
sys.path.insert(0, 'src/')

from contextlib import contextmanager
from StringIO import StringIO

from irpef import main
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

class test_main_irpef(unittest.TestCase):

	def test_input_sequence(self):
	
		inputs = [27450, 'still_test', 'test']
		
		try:
			fake_input = inputs.pop
			original_raw_input = __builtins__.raw_input
			__builtins__.raw_input = lambda _: fake_input()
		
			with captured_output() as (out, err):
				main()
				output = out.getvalue().strip()
			
			self.assertAlmostEqual(float(output), 6811.50, delta=0.01)
		
		finally:
			__builtins__.raw_input = original_raw_input

	def test_irpef(self):
		
		try:
			original_raw_input = __builtins__.raw_input
			
			__builtins__.raw_input = lambda _: '65000'
			with captured_output() as (out, err):
				main()
				output = out.getvalue().strip()
			self.assertAlmostEqual(float(output), 21320, delta=0.01)
			
		finally:
			__builtins__.raw_input = original_raw_input

		
if __name__ == '__main__':	
	unittest.main()
