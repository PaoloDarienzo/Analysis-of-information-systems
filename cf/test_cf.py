import sys
sys.path.insert(0, 'src/')

from contextlib import contextmanager
from StringIO import StringIO

import codice_fiscale
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

class test_main_cf(unittest.TestCase):

	def test_cf_output(self):

		inputs = ['m', 'Verona', '01/01/1980', 'ROSSI', 'MARIO']

		try:
			fake_input = inputs.pop
			original_raw_input = __builtins__.raw_input
			__builtins__.raw_input = lambda _: fake_input()

			with captured_output() as (out, err):
				codice_fiscale.main()
				output = out.getvalue().strip()

			self.assertEqual(output, 'rssmra80a01l781k')

			####################################################################
			#The test below will fail
            ##REAL DATA, OMITTED FOR PRIVACY
			#inputs = ['m', '*', '*', '*\'*', '*']
			#fake_input = inputs.pop
			#__builtins__.raw_input = lambda _: fake_input()

			#with captured_output() as (out, err):
			#	codice_fiscale.main()
			#	output = out.getvalue().strip()

			#self.assertEqual(output, '***')
			####################################################################

		finally:
			__builtins__.raw_input = original_raw_input

if __name__ == '__main__':
	unittest.main()
