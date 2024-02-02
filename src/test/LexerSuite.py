import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test1_comment(self):
		self.assertTrue(TestLexer.test('''## jakshgjkashgjkasd \n## asjkdghajksdhgkajsdg \ndgjksdajglkadsjg ## asjdghjkasdhgjka\n## sajgdhkjasdhgjasd''','''
,
,dgjksdajglkadsjg,
,<EOF>''',1))
		
	def test2_comment(self):
		input = 'a ## Comment. \rb'
		expected = 'a,\n,b,<EOF>' 
		self.assertTrue(TestLexer.test(input, expected, 2))

	def test3_comment(self):
		input = 'a ## Comment. \r\nb'
		expected = 'a,\n,b,<EOF>'
		self.assertTrue(TestLexer.test(input, expected, 3))