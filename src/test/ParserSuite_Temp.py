import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_6(self):
		input = '''
func SqV ()
	begin
		begin
			number a <- foo(a)[1]
		end
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 6))

	def test_5(self):
			input = """
func foo(number a, string b, bool c) 
	return (toString(a) ... toString(c)) ... b


	
func main()


	return 0


begin


	number a <- 10



	string b <- \"a string\"
	bool c <- true


end
					"""
			expect = """Error on line 13 col 0: begin"""
			self.assertTrue(TestParser.test(input,expect,5))

	def test_7(self):
			input = """
		var VoTien
"""
			expect = """Error on line 2 col 12: \n"""
			self.assertTrue(TestParser.test(input,expect,7))