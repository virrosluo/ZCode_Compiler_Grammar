import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_600(self):
		input = '''
func zvz ()
return "'"'"'""
var E2
func Ow (number nj[65,484.398,0], number t2T[5,4.602], string DlM)
begin
	## Ok/MVZydJT1QZnKsLj^
	## )`+b?/tNH$
	## gydY46Y"P
end
func R1v6 (var A4a[5.355,0.199])
return 9.105
func Ztn ()
return

'''
		expect = '''Error on line 4 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 600))