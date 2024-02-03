import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_100(self):
		self.assertTrue(TestLexer.test('''## Ul]mO*''', '''<EOF>''', 100))

	def test_101(self):
		self.assertTrue(TestLexer.test('''## p8Q}l BL#d1HQFM''', '''<EOF>''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("28.371E+65", "28.371E+65,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test('''"'"\\va'"='""''', '''Illegal Escape In String: '"\\v''', 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("18e59", "18e59,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''## A:&Nz)D;=(NCBqv{?:''', '''<EOF>''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test("40", "40,<EOF>", 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("mkHQKK8", "mkHQKK8,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("cz$_k", "cz,Error Token $", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"9'"\\x2'""''', '''Illegal Escape In String: 9'"\\x''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("1.625E-49", "1.625E-49,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test('''"{'"Q3 ''', '''Unclosed String: {'"Q3 ''', 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 113))

	def test_114(self):
		self.assertTrue(TestLexer.test('''"{'"'"\\h'""''', '''Illegal Escape In String: {'"'"\\h''', 114))

	def test_115(self):
		self.assertTrue(TestLexer.test('''":'"'"d8"''', ''':'"'"d8,<EOF>''', 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''## Uak''', '''<EOF>''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test("20.456", "20.456,<EOF>", 117))

	def test_118(self):
		self.assertTrue(TestLexer.test("Och03Ay", "Och03Ay,<EOF>", 118))

	def test_119(self):
		self.assertTrue(TestLexer.test("qPLRn_gJC", "qPLRn_gJC,<EOF>", 119))

	def test_120(self):
		self.assertTrue(TestLexer.test('''## "ON3RWpk0#Eu''', '''<EOF>''', 120))

	def test_121(self):
		self.assertTrue(TestLexer.test("j", "j,<EOF>", 121))

	def test_122(self):
		self.assertTrue(TestLexer.test('''"h ''', '''Unclosed String: h ''', 122))

	def test_123(self):
		self.assertTrue(TestLexer.test('''## ""g}ceuz8t`''', '''<EOF>''', 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''## <pnx.O!=[a/IlW''', '''<EOF>''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("YF#hP#s", "YF,Error Token #", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test('''"'"
'"/"''', '''Unclosed String: '"''', 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("Qel$g81&", "Qel,Error Token $", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test("qdM1T7@l$", "qdM1T7,Error Token @", 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("oEW", "oEW,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("563.377", "563.377,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## Kn:1-''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test("0.864e-64", "0.864e-64,<EOF>", 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''"+'"\\ep'"Y"''', '''Illegal Escape In String: +'"\\e''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''" '"'"n9"''', ''' '"'"n9,<EOF>''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''"B'"'"52"''', '''B'"'"52,<EOF>''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("7PrZ&@j", "7,PrZ,Error Token &", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("36.831E-61", "36.831E-61,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''## [''', '''<EOF>''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''"p'"'"FL"''', '''p'"'"FL,<EOF>''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("7Rn", "7,Rn,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("39.210", "39.210,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test("52E+63", "52E+63,<EOF>", 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''"Y'""''', '''Y'",<EOF>''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("328.049", "328.049,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("409", "409,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test("X@kWUPmzO", "X,Error Token @", 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("12", "12,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''## 3>gH''', '''<EOF>''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("XrFaBHj0B", "XrFaBHj0B,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("880.652e40", "880.652e40,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''## ?8-G4m''', '''<EOF>''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("^hQ9", "Error Token ^", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("3.409", "3.409,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''"'"'" As ''', '''Unclosed String: '"'" As ''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''"? ''', '''Unclosed String: ? ''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''## Q%$<1g.lRtdf2''', '''<EOF>''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test('''## ~|V5=|b"c1A~k~''', '''<EOF>''', 158))

	def test_159(self):
		self.assertTrue(TestLexer.test('''"I\\gF."''', '''Illegal Escape In String: I\\g''', 159))

	def test_160(self):
		self.assertTrue(TestLexer.test("49.981", "49.981,<EOF>", 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("8.712e-09", "8.712e-09,<EOF>", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("8E+08", "8E+08,<EOF>", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("326.020e+24", "326.020e+24,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''## &)=<FlT8H''', '''<EOF>''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("42.284e05", "42.284e05,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("bHGP", "bHGP,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("##egLrv", "<EOF>", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("987.142", "987.142,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test('''"^'""''', '''^'",<EOF>''', 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''"'"P'"\\w'""''', '''Illegal Escape In String: '"P'"\\w''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''## r|`#!1an*vYft&z#)n<''', '''<EOF>''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''"L\\o~'""''', '''Illegal Escape In String: L\\o''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("24kt", "24,kt,<EOF>", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test("3.373E68", "3.373E68,<EOF>", 174))

	def test_175(self):
		self.assertTrue(TestLexer.test("986", "986,<EOF>", 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("310", "310,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("48", "48,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("vyl5N", "vyl5N,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test('''"r'"'"'" ''', '''Unclosed String: r'"'"'" ''', 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("6.135", "6.135,<EOF>", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("20E54", "20E54,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"'"\\w'""''', '''Illegal Escape In String: '"\\w''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''## aC''', '''<EOF>''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("29.858", "29.858,<EOF>", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test('''"'"  ''', '''Unclosed String: '"  ''', 185))

	def test_186(self):
		self.assertTrue(TestLexer.test("&", "Error Token &", 186))

	def test_187(self):
		self.assertTrue(TestLexer.test("8.002E+99", "8.002E+99,<EOF>", 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("cxH", "cxH,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test('''"\\a'""''', '''Illegal Escape In String: \\a''', 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''## 2_(n6-S''', '''<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("193.580", "193.580,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''"]'"'"'"2 ''', '''Unclosed String: ]'"'"'"2 ''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''## D*rKuyX4d][+w''', '''<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("299e61", "299e61,<EOF>", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("565", "565,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test('''"'"
U"''', '''Unclosed String: '"''', 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("^U96beH&^", "Error Token ^", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''## lTUdzM)@(0_?2~''', '''<EOF>''', 199))
