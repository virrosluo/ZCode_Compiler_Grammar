import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_100(self):
		self.assertTrue(TestLexer.test('''## 2Ak*I8.(r!trF];N''', '''<EOF>''', 100))

	def test_101(self):
		self.assertTrue(TestLexer.test('''## E%%''', '''<EOF>''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test('''"u@'"\\zP"''', '''Illegal Escape In String: u@'"\\z''', 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("n7Xd&V", "n7Xd,Error Token &", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test("76E+19", "76E+19,<EOF>", 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''"nn'" ''', '''Unclosed String: nn'" ''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test("I5", "I5,<EOF>", 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("4kRQmUMCo3", "4,kRQmUMCo3,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test('''## /*}y*.pI6RrB^`vd&C&&''', '''<EOF>''', 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"\\d'""''', '''Illegal Escape In String: \\d''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("h", "h,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("86Gjal9p", "86,Gjal9p,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test('''## JW6/l7|$''', '''<EOF>''', 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("6.960", "6.960,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test('''## x,Oc:|X7WeY.5#U''', '''<EOF>''', 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''## +nM0L}H)9nCshQDO<h''', '''<EOF>''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test("Jn4d", "Jn4d,<EOF>", 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''## >''', '''<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test("70.059E+27", "70.059E+27,<EOF>", 120))

	def test_121(self):
		self.assertTrue(TestLexer.test('''"'"'"\\s?'""''', '''Illegal Escape In String: '"'"\\s''', 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("89e+43", "89e+43,<EOF>", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test('''"\\p'""''', '''Illegal Escape In String: \\p''', 123))

	def test_124(self):
		self.assertTrue(TestLexer.test('''## nHdDeU4wJcY5S;UU5!!''', '''<EOF>''', 124))

	def test_125(self):
		self.assertTrue(TestLexer.test('''"\\g&'"g{"''', '''Illegal Escape In String: \\g''', 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("38E98", "38E98,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("774.124", "774.124,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("0.412e-54", "0.412e-54,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("mYee&", "mYee,Error Token &", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## [^;j9Py:?:ao<uF7qSG#''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''## @DWOJaLr:7''', '''<EOF>''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''## 0L#/J6}sUlP;|Aom''', '''<EOF>''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test('''"b'""''', '''b'",<EOF>''', 134))

	def test_135(self):
		self.assertTrue(TestLexer.test("49", "49,<EOF>", 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("n", "n,<EOF>", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("RiKvc", "RiKvc,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test("j", "j,<EOF>", 138))

	def test_139(self):
		self.assertTrue(TestLexer.test("xk$L7", "xk,Error Token $", 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("77", "77,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test("61", "61,<EOF>", 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## =''', '''<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test("9.818", "9.818,<EOF>", 143))

	def test_144(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("ehLL", "ehLL,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("30e57", "30e57,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test('''## 5''', '''<EOF>''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test('''"m'"'"
'"'""''', '''Unclosed String: m'"'"''', 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''## qb)}L>P2ay:''', '''<EOF>''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test('''## 6}G]#-,4Xn"s#D}''', '''<EOF>''', 150))

	def test_151(self):
		self.assertTrue(TestLexer.test("776.488", "776.488,<EOF>", 151))

	def test_152(self):
		self.assertTrue(TestLexer.test('''## JQEm]`6-"[BfS`''', '''<EOF>''', 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("771.693", "771.693,<EOF>", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("1e84", "1e84,<EOF>", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test('''"xa'""''', '''xa'",<EOF>''', 155))

	def test_156(self):
		self.assertTrue(TestLexer.test('''"7'"'" ''', '''Unclosed String: 7'"'" ''', 156))

	def test_157(self):
		self.assertTrue(TestLexer.test("V16oal", "V16oal,<EOF>", 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("4.099e76", "4.099e76,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''## h["Oe)''', '''<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test('''## T*Ph$4bS7{s!>hSUy!''', '''<EOF>''', 161))

	def test_162(self):
		self.assertTrue(TestLexer.test("678.283e-36", "678.283e-36,<EOF>", 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("P", "P,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''## Y<:",%[lmH!usZSFEk*n''', '''<EOF>''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test('''"	\\p'"'""''', '''Illegal Escape In String: 	\\p''', 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("35e89", "35e89,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test('''"&bo> ''', '''Unclosed String: &bo> ''', 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("704.337e+31", "704.337e+31,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("s", "s,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test('''## o]w+WgP:qU''', '''<EOF>''', 170))

	def test_171(self):
		self.assertTrue(TestLexer.test('''"
#"''', '''Unclosed String: ''', 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''"\\l'""''', '''Illegal Escape In String: \\l''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test("602", "602,<EOF>", 176))

	def test_177(self):
		self.assertTrue(TestLexer.test("md93", "md93,<EOF>", 177))

	def test_178(self):
		self.assertTrue(TestLexer.test("Ew2A9ukdil", "Ew2A9ukdil,<EOF>", 178))

	def test_179(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 179))

	def test_180(self):
		self.assertTrue(TestLexer.test('''"[[4
'""''', '''Unclosed String: [[4''', 180))

	def test_181(self):
		self.assertTrue(TestLexer.test('''"\\k-"''', '''Illegal Escape In String: \\k''', 181))

	def test_182(self):
		self.assertTrue(TestLexer.test('''"r'"&w"''', '''Unclosed String: r'"&''', 182))

	def test_183(self):
		self.assertTrue(TestLexer.test('''"'"
^	("''', '''Unclosed String: ''', 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("5.327", "5.327,<EOF>", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("53e62", "53e62,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''## +.TNc{$>(*?_&FaQ"Rdf''', '''<EOF>''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## uzW^~*e1U''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("@1ms@", "Error Token @", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''## .?s=gvT4)Z2eVZyy!{''', '''<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test("9LaK_F", "9,LaK_F,<EOF>", 191))

	def test_192(self):
		self.assertTrue(TestLexer.test('''"\\c@"''', '''Illegal Escape In String: \\c''', 192))

	def test_193(self):
		self.assertTrue(TestLexer.test('''## Na''', '''<EOF>''', 193))

	def test_194(self):
		self.assertTrue(TestLexer.test('''"e"''', '''e,<EOF>''', 194))

	def test_195(self):
		self.assertTrue(TestLexer.test('''## _o-REZ;0TwmS6jTsS.+`''', '''<EOF>''', 195))

	def test_196(self):
		self.assertTrue(TestLexer.test("9.016E+15", "9.016E+15,<EOF>", 196))

	def test_197(self):
		self.assertTrue(TestLexer.test("1.922e03", "1.922e03,<EOF>", 197))

	def test_198(self):
		self.assertTrue(TestLexer.test("VCf", "VCf,<EOF>", 198))

	def test_199(self):
		self.assertTrue(TestLexer.test("0.956", "0.956,<EOF>", 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("aO9", "aO9,<EOF>", 200))

	def test_201(self):
		self.assertTrue(TestLexer.test('''"&R-F"''', '''&R-F,<EOF>''', 201))

	def test_202(self):
		self.assertTrue(TestLexer.test("yGW", "yGW,<EOF>", 202))

	def test_203(self):
		self.assertTrue(TestLexer.test("UaU$uB", "UaU,Error Token $", 203))

	def test_204(self):
		self.assertTrue(TestLexer.test("6.683e+31", "6.683e+31,<EOF>", 204))

	def test_205(self):
		self.assertTrue(TestLexer.test("31", "31,<EOF>", 205))

	def test_206(self):
		self.assertTrue(TestLexer.test('''## HY''', '''<EOF>''', 206))

	def test_207(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 207))

	def test_208(self):
		self.assertTrue(TestLexer.test("L8nrNxgO", "L8nrNxgO,<EOF>", 208))

	def test_209(self):
		self.assertTrue(TestLexer.test("48E+10", "48E+10,<EOF>", 209))

	def test_210(self):
		self.assertTrue(TestLexer.test('''## Q:"jwv''', '''<EOF>''', 210))

	def test_211(self):
		self.assertTrue(TestLexer.test('''## "%a-kU`!PYx!#''', '''<EOF>''', 211))

	def test_212(self):
		self.assertTrue(TestLexer.test("51.511", "51.511,<EOF>", 212))

	def test_213(self):
		self.assertTrue(TestLexer.test('''## *b%1''', '''<EOF>''', 213))

	def test_214(self):
		self.assertTrue(TestLexer.test('''"%\\o'"sq'""''', '''Illegal Escape In String: %\\o''', 214))

	def test_215(self):
		self.assertTrue(TestLexer.test("nIgF", "nIgF,<EOF>", 215))

	def test_216(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 216))

	def test_217(self):
		self.assertTrue(TestLexer.test("3E+83", "3E+83,<EOF>", 217))

	def test_218(self):
		self.assertTrue(TestLexer.test("WhRe", "WhRe,<EOF>", 218))

	def test_219(self):
		self.assertTrue(TestLexer.test("49KM@vot9d", "49,KM,Error Token @", 219))

	def test_220(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 220))

	def test_221(self):
		self.assertTrue(TestLexer.test('''## w:S''', '''<EOF>''', 221))

	def test_222(self):
		self.assertTrue(TestLexer.test('''"'"'"i'""''', '''\'"'"i'",<EOF>''', 222))

	def test_223(self):
		self.assertTrue(TestLexer.test('''## NMH0YX;1^YDh?.(^YQ''', '''<EOF>''', 223))

	def test_224(self):
		self.assertTrue(TestLexer.test("Ti", "Ti,<EOF>", 224))

	def test_225(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'"v"''', '''\'"'"'"'"v,<EOF>''', 225))

	def test_226(self):
		self.assertTrue(TestLexer.test('''## H11w''', '''<EOF>''', 226))

	def test_227(self):
		self.assertTrue(TestLexer.test('''"'
'""''', '''Illegal Escape In String: '''', 227))

	def test_228(self):
		self.assertTrue(TestLexer.test('''## MD+iY/oJ@T!|r~`''', '''<EOF>''', 228))

	def test_229(self):
		self.assertTrue(TestLexer.test("299.427", "299.427,<EOF>", 229))

	def test_230(self):
		self.assertTrue(TestLexer.test('''## ?p5ukz|-^jR"")yK''', '''<EOF>''', 230))

	def test_231(self):
		self.assertTrue(TestLexer.test('''## 4&.t=$''', '''<EOF>''', 231))

	def test_232(self):
		self.assertTrue(TestLexer.test("94", "94,<EOF>", 232))

	def test_233(self):
		self.assertTrue(TestLexer.test('''"\\h'""''', '''Illegal Escape In String: \\h''', 233))

	def test_234(self):
		self.assertTrue(TestLexer.test("X", "X,<EOF>", 234))

	def test_235(self):
		self.assertTrue(TestLexer.test("Zc4652$", "Zc4652,Error Token $", 235))

	def test_236(self):
		self.assertTrue(TestLexer.test("7E+59", "7E+59,<EOF>", 236))

	def test_237(self):
		self.assertTrue(TestLexer.test("765.709", "765.709,<EOF>", 237))

	def test_238(self):
		self.assertTrue(TestLexer.test('''## cXt2` P7pwLVCUR!W''', '''<EOF>''', 238))

	def test_239(self):
		self.assertTrue(TestLexer.test('''## -[H,ckH-Fq>vy''', '''<EOF>''', 239))

	def test_240(self):
		self.assertTrue(TestLexer.test("2E+64", "2E+64,<EOF>", 240))

	def test_241(self):
		self.assertTrue(TestLexer.test('''"'"*'""''', '''\'"*'",<EOF>''', 241))

	def test_242(self):
		self.assertTrue(TestLexer.test("G@Z^kZYGU", "G,Error Token @", 242))

	def test_243(self):
		self.assertTrue(TestLexer.test("qR", "qR,<EOF>", 243))

	def test_244(self):
		self.assertTrue(TestLexer.test('''## W''', '''<EOF>''', 244))

	def test_245(self):
		self.assertTrue(TestLexer.test('''## ]] xNj87G&Hn''', '''<EOF>''', 245))

	def test_246(self):
		self.assertTrue(TestLexer.test("518", "518,<EOF>", 246))

	def test_247(self):
		self.assertTrue(TestLexer.test('''## :Ak1%<18+''', '''<EOF>''', 247))

	def test_248(self):
		self.assertTrue(TestLexer.test('''"M{
'"F"''', '''Unclosed String: M{''', 248))

	def test_249(self):
		self.assertTrue(TestLexer.test('''"Z\\z'""''', '''Illegal Escape In String: Z\\z''', 249))

	def test_250(self):
		self.assertTrue(TestLexer.test('''## a''', '''<EOF>''', 250))

	def test_251(self):
		self.assertTrue(TestLexer.test('''";#R\\j?"''', '''Illegal Escape In String: ;#R\\j''', 251))

	def test_252(self):
		self.assertTrue(TestLexer.test('''"\\kD"''', '''Illegal Escape In String: \\k''', 252))

	def test_253(self):
		self.assertTrue(TestLexer.test("3.006", "3.006,<EOF>", 253))

	def test_254(self):
		self.assertTrue(TestLexer.test('''## %s`9u:(8@;!O3e$J,J''', '''<EOF>''', 254))

	def test_255(self):
		self.assertTrue(TestLexer.test('''## hh58TuT=C6bl''', '''<EOF>''', 255))

	def test_256(self):
		self.assertTrue(TestLexer.test('''"/\\w*V"''', '''Illegal Escape In String: /\\w''', 256))

	def test_257(self):
		self.assertTrue(TestLexer.test('''"R'"'"'""''', '''R'"'"'",<EOF>''', 257))

	def test_258(self):
		self.assertTrue(TestLexer.test("xyOAXE", "xyOAXE,<EOF>", 258))

	def test_259(self):
		self.assertTrue(TestLexer.test("80.094e+79", "80.094e+79,<EOF>", 259))

	def test_260(self):
		self.assertTrue(TestLexer.test("3e+92", "3e+92,<EOF>", 260))

	def test_261(self):
		self.assertTrue(TestLexer.test('''## J[-T+<A8r>e''', '''<EOF>''', 261))

	def test_262(self):
		self.assertTrue(TestLexer.test('''## ;''', '''<EOF>''', 262))

	def test_263(self):
		self.assertTrue(TestLexer.test("2.065", "2.065,<EOF>", 263))

	def test_264(self):
		self.assertTrue(TestLexer.test("308E87", "308E87,<EOF>", 264))

	def test_265(self):
		self.assertTrue(TestLexer.test("646.728E-37", "646.728E-37,<EOF>", 265))

	def test_266(self):
		self.assertTrue(TestLexer.test('''"'"!["''', '''\'"![,<EOF>''', 266))

	def test_267(self):
		self.assertTrue(TestLexer.test("92.903E+70", "92.903E+70,<EOF>", 267))

	def test_268(self):
		self.assertTrue(TestLexer.test("zLjm", "zLjm,<EOF>", 268))

	def test_269(self):
		self.assertTrue(TestLexer.test("P", "P,<EOF>", 269))

	def test_270(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 270))

	def test_271(self):
		self.assertTrue(TestLexer.test('''"UE'"!'""''', '''UE'"!'",<EOF>''', 271))

	def test_272(self):
		self.assertTrue(TestLexer.test('''"\\yF'""''', '''Illegal Escape In String: \\y''', 272))

	def test_273(self):
		self.assertTrue(TestLexer.test("9.270e-49", "9.270e-49,<EOF>", 273))

	def test_274(self):
		self.assertTrue(TestLexer.test("pJGmS3Pq", "pJGmS3Pq,<EOF>", 274))

	def test_275(self):
		self.assertTrue(TestLexer.test("u&ix_", "u,Error Token &", 275))

	def test_276(self):
		self.assertTrue(TestLexer.test('''"\\cF"''', '''Illegal Escape In String: \\c''', 276))

	def test_277(self):
		self.assertTrue(TestLexer.test("300.515E71", "300.515E71,<EOF>", 277))

	def test_278(self):
		self.assertTrue(TestLexer.test('''"'"/
'"'"3"''', '''Unclosed String: '"/''', 278))

	def test_279(self):
		self.assertTrue(TestLexer.test('''". ''', '''Unclosed String: . ''', 279))

	def test_280(self):
		self.assertTrue(TestLexer.test("60E67", "60E67,<EOF>", 280))

	def test_281(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 281))

	def test_282(self):
		self.assertTrue(TestLexer.test("809e+30", "809e+30,<EOF>", 282))

	def test_283(self):
		self.assertTrue(TestLexer.test("239", "239,<EOF>", 283))

	def test_284(self):
		self.assertTrue(TestLexer.test("K0XeKL0", "K0XeKL0,<EOF>", 284))

	def test_285(self):
		self.assertTrue(TestLexer.test('''## [q)JCT"s''', '''<EOF>''', 285))

	def test_286(self):
		self.assertTrue(TestLexer.test('''"\\c'"~"''', '''Illegal Escape In String: \\c''', 286))

	def test_287(self):
		self.assertTrue(TestLexer.test('''## );;o$''', '''<EOF>''', 287))

	def test_288(self):
		self.assertTrue(TestLexer.test("QRS", "QRS,<EOF>", 288))

	def test_289(self):
		self.assertTrue(TestLexer.test("2.376E+58", "2.376E+58,<EOF>", 289))

	def test_290(self):
		self.assertTrue(TestLexer.test('''"o'";O'""''', '''o'";O'",<EOF>''', 290))

	def test_291(self):
		self.assertTrue(TestLexer.test('''"'"
t'"'""''', '''Unclosed String: '"''', 291))

	def test_292(self):
		self.assertTrue(TestLexer.test('''## zp$[`[Bv3Ex(xYp''', '''<EOF>''', 292))

	def test_293(self):
		self.assertTrue(TestLexer.test('''"Q"''', '''Q,<EOF>''', 293))

	def test_294(self):
		self.assertTrue(TestLexer.test('''"x&"''', '''x&,<EOF>''', 294))

	def test_295(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 295))

	def test_296(self):
		self.assertTrue(TestLexer.test('''## ?Ylw824X[NVQbz}qd)!-''', '''<EOF>''', 296))

	def test_297(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'" ''', '''Unclosed String: '"'"'"'" ''', 297))

	def test_298(self):
		self.assertTrue(TestLexer.test("IY", "IY,<EOF>", 298))

	def test_299(self):
		self.assertTrue(TestLexer.test("6E60", "6E60,<EOF>", 299))

	def test_300(self):
		self.assertTrue(TestLexer.test('''"'"\\pO"''', '''Illegal Escape In String: '"\\p''', 300))

	def test_301(self):
		self.assertTrue(TestLexer.test("j75GmWHZN", "j75GmWHZN,<EOF>", 301))

	def test_302(self):
		self.assertTrue(TestLexer.test('''"d"''', '''d,<EOF>''', 302))

	def test_303(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 303))

	def test_304(self):
		self.assertTrue(TestLexer.test('''## Y$]s=Z5}Jb-i9''', '''<EOF>''', 304))

	def test_305(self):
		self.assertTrue(TestLexer.test('''"@'"^
'"@"''', '''Unclosed String: @'"^''', 305))

	def test_306(self):
		self.assertTrue(TestLexer.test('''"!'"'"\\st"''', '''Illegal Escape In String: !'"'"\\s''', 306))

	def test_307(self):
		self.assertTrue(TestLexer.test('''"'"\\q'"}"''', '''Illegal Escape In String: '"\\q''', 307))

	def test_308(self):
		self.assertTrue(TestLexer.test('''## J[]=[`ZiuDEhSeZEV[_R''', '''<EOF>''', 308))

	def test_309(self):
		self.assertTrue(TestLexer.test("mtuj4g", "mtuj4g,<EOF>", 309))

	def test_310(self):
		self.assertTrue(TestLexer.test("2#V$4wgiP@", "2,Error Token #", 310))

	def test_311(self):
		self.assertTrue(TestLexer.test("i", "i,<EOF>", 311))

	def test_312(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 312))

	def test_313(self):
		self.assertTrue(TestLexer.test("q06e@CEn7E", "q06e,Error Token @", 313))

	def test_314(self):
		self.assertTrue(TestLexer.test("J7BTMk2Cb", "J7BTMk2Cb,<EOF>", 314))

	def test_315(self):
		self.assertTrue(TestLexer.test('''## kjMa j}`2eX;t''', '''<EOF>''', 315))

	def test_316(self):
		self.assertTrue(TestLexer.test("8puqVS", "8,puqVS,<EOF>", 316))

	def test_317(self):
		self.assertTrue(TestLexer.test('''## Gilp|o},*b]GbN''', '''<EOF>''', 317))

	def test_318(self):
		self.assertTrue(TestLexer.test('''"'"
'"'""''', '''Unclosed String: '"''', 318))

	def test_319(self):
		self.assertTrue(TestLexer.test('''## Z7&~<pW9G4Mz*)''', '''<EOF>''', 319))

	def test_320(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 320))

	def test_321(self):
		self.assertTrue(TestLexer.test("16.658E+76", "16.658E+76,<EOF>", 321))

	def test_322(self):
		self.assertTrue(TestLexer.test("193", "193,<EOF>", 322))

	def test_323(self):
		self.assertTrue(TestLexer.test("7.152e01", "7.152e01,<EOF>", 323))

	def test_324(self):
		self.assertTrue(TestLexer.test("5.162", "5.162,<EOF>", 324))

	def test_325(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 325))

	def test_326(self):
		self.assertTrue(TestLexer.test('''"
S7i"''', '''Unclosed String: ''', 326))

	def test_327(self):
		self.assertTrue(TestLexer.test("15.532", "15.532,<EOF>", 327))

	def test_328(self):
		self.assertTrue(TestLexer.test("85e-22", "85e-22,<EOF>", 328))

	def test_329(self):
		self.assertTrue(TestLexer.test('''"
1"''', '''Unclosed String: ''', 329))

	def test_330(self):
		self.assertTrue(TestLexer.test("cj35z", "cj35z,<EOF>", 330))

	def test_331(self):
		self.assertTrue(TestLexer.test("38", "38,<EOF>", 331))

	def test_332(self):
		self.assertTrue(TestLexer.test('''"- "''', '''- ,<EOF>''', 332))

	def test_333(self):
		self.assertTrue(TestLexer.test('''"'"'"]\\x'""''', '''Illegal Escape In String: '"'"]\\x''', 333))

	def test_334(self):
		self.assertTrue(TestLexer.test("311e+07", "311e+07,<EOF>", 334))

	def test_335(self):
		self.assertTrue(TestLexer.test("96e-75", "96e-75,<EOF>", 335))

	def test_336(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 336))

	def test_337(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 337))

	def test_338(self):
		self.assertTrue(TestLexer.test('''## =,Ky3ITFVL 1v''', '''<EOF>''', 338))

	def test_339(self):
		self.assertTrue(TestLexer.test('''## a''', '''<EOF>''', 339))

	def test_340(self):
		self.assertTrue(TestLexer.test("jJf", "jJf,<EOF>", 340))

	def test_341(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 341))

	def test_342(self):
		self.assertTrue(TestLexer.test("58.713e-17", "58.713e-17,<EOF>", 342))

	def test_343(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 343))

	def test_344(self):
		self.assertTrue(TestLexer.test('''## W@Bw8''', '''<EOF>''', 344))

	def test_345(self):
		self.assertTrue(TestLexer.test("bazJ0", "bazJ0,<EOF>", 345))

	def test_346(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 346))

	def test_347(self):
		self.assertTrue(TestLexer.test('''## 0u,''', '''<EOF>''', 347))

	def test_348(self):
		self.assertTrue(TestLexer.test('''## `@z[R_QKK5PK4]''', '''<EOF>''', 348))

	def test_349(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 349))

	def test_350(self):
		self.assertTrue(TestLexer.test('''## mA''', '''<EOF>''', 350))

	def test_351(self):
		self.assertTrue(TestLexer.test("XfUsC&W", "XfUsC,Error Token &", 351))

	def test_352(self):
		self.assertTrue(TestLexer.test('''"
'"'""''', '''Unclosed String: ''', 352))

	def test_353(self):
		self.assertTrue(TestLexer.test("RDf", "RDf,<EOF>", 353))

	def test_354(self):
		self.assertTrue(TestLexer.test('''"nr/'""''', '''Unclosed String: ''', 354))

	def test_355(self):
		self.assertTrue(TestLexer.test('''## B]U/+%Cx''', '''<EOF>''', 355))

	def test_356(self):
		self.assertTrue(TestLexer.test("wQXQDi4k", "wQXQDi4k,<EOF>", 356))

	def test_357(self):
		self.assertTrue(TestLexer.test('''## ~r^j6''', '''<EOF>''', 357))

	def test_358(self):
		self.assertTrue(TestLexer.test("G", "G,<EOF>", 358))

	def test_359(self):
		self.assertTrue(TestLexer.test('''"f'"'"'"w ''', '''Unclosed String: f'"'"'"w ''', 359))

	def test_360(self):
		self.assertTrue(TestLexer.test("21.106", "21.106,<EOF>", 360))

	def test_361(self):
		self.assertTrue(TestLexer.test('''## v^3MikL?dRUHRgZg#]mO''', '''<EOF>''', 361))

	def test_362(self):
		self.assertTrue(TestLexer.test('''## d0#:Pi#c{}L1c[IV~&kG''', '''<EOF>''', 362))

	def test_363(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 363))

	def test_364(self):
		self.assertTrue(TestLexer.test("Hf_", "Hf_,<EOF>", 364))

	def test_365(self):
		self.assertTrue(TestLexer.test("WKx684E&0", "WKx684E,Error Token &", 365))

	def test_366(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 366))

	def test_367(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 367))

	def test_368(self):
		self.assertTrue(TestLexer.test("174", "174,<EOF>", 368))

	def test_369(self):
		self.assertTrue(TestLexer.test("YskyX", "YskyX,<EOF>", 369))

	def test_370(self):
		self.assertTrue(TestLexer.test('''"'">9[4"''', '''\'">9[4,<EOF>''', 370))

	def test_371(self):
		self.assertTrue(TestLexer.test("385", "385,<EOF>", 371))

	def test_372(self):
		self.assertTrue(TestLexer.test("84.876e98", "84.876e98,<EOF>", 372))

	def test_373(self):
		self.assertTrue(TestLexer.test('''## W''', '''<EOF>''', 373))

	def test_374(self):
		self.assertTrue(TestLexer.test("EKJOCZuH", "EKJOCZuH,<EOF>", 374))

	def test_375(self):
		self.assertTrue(TestLexer.test("BpVz01ma", "BpVz01ma,<EOF>", 375))

	def test_376(self):
		self.assertTrue(TestLexer.test("WD5", "WD5,<EOF>", 376))

	def test_377(self):
		self.assertTrue(TestLexer.test("577E92", "577E92,<EOF>", 377))

	def test_378(self):
		self.assertTrue(TestLexer.test('''## K5&W7yAV2/i3zMdU4N''', '''<EOF>''', 378))

	def test_379(self):
		self.assertTrue(TestLexer.test('''## -''', '''<EOF>''', 379))

	def test_380(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 380))

	def test_381(self):
		self.assertTrue(TestLexer.test('''## `%a}1"*?CO|''', '''<EOF>''', 381))

	def test_382(self):
		self.assertTrue(TestLexer.test('''## dcj9r''', '''<EOF>''', 382))

	def test_383(self):
		self.assertTrue(TestLexer.test('''"'"'"s"''', '''\'"'"s,<EOF>''', 383))

	def test_384(self):
		self.assertTrue(TestLexer.test("658", "658,<EOF>", 384))

	def test_385(self):
		self.assertTrue(TestLexer.test('''"~ "''', '''~ ,<EOF>''', 385))

	def test_386(self):
		self.assertTrue(TestLexer.test('''"
Pkg'"'""''', '''Unclosed String: ''', 386))

	def test_387(self):
		self.assertTrue(TestLexer.test("5$n1$HJd", "5,Error Token $", 387))

	def test_388(self):
		self.assertTrue(TestLexer.test('''## ?i,hyCC[zMjn:9K''', '''<EOF>''', 388))

	def test_389(self):
		self.assertTrue(TestLexer.test('''## 4kS!nG:Fz^!*''', '''<EOF>''', 389))

	def test_390(self):
		self.assertTrue(TestLexer.test("Qr6zdRSuK", "Qr6zdRSuK,<EOF>", 390))

	def test_391(self):
		self.assertTrue(TestLexer.test("7.570e21", "7.570e21,<EOF>", 391))

	def test_392(self):
		self.assertTrue(TestLexer.test("9e+98", "9e+98,<EOF>", 392))

	def test_393(self):
		self.assertTrue(TestLexer.test('''## w[.Cu^kSS%`<>=Y.U''', '''<EOF>''', 393))

	def test_394(self):
		self.assertTrue(TestLexer.test("45.340", "45.340,<EOF>", 394))

	def test_395(self):
		self.assertTrue(TestLexer.test('''## %w#''', '''<EOF>''', 395))

	def test_396(self):
		self.assertTrue(TestLexer.test("22", "22,<EOF>", 396))

	def test_397(self):
		self.assertTrue(TestLexer.test('''## P|7:[t%!vYt}9m/BzQ''', '''<EOF>''', 397))

	def test_398(self):
		self.assertTrue(TestLexer.test("gWCKDaZ", "gWCKDaZ,<EOF>", 398))

	def test_399(self):
		self.assertTrue(TestLexer.test("lo^qa", "lo,Error Token ^", 399))

	def test_400(self):
		self.assertTrue(TestLexer.test('''## T''', '''<EOF>''', 400))

	def test_401(self):
		self.assertTrue(TestLexer.test("70.044", "70.044,<EOF>", 401))

	def test_402(self):
		self.assertTrue(TestLexer.test("qKAl8D", "qKAl8D,<EOF>", 402))

	def test_403(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 403))

	def test_404(self):
		self.assertTrue(TestLexer.test('''## @k]q^v[=fQ''', '''<EOF>''', 404))

	def test_405(self):
		self.assertTrue(TestLexer.test("76.511", "76.511,<EOF>", 405))

	def test_406(self):
		self.assertTrue(TestLexer.test('''## [TFXD''', '''<EOF>''', 406))

	def test_407(self):
		self.assertTrue(TestLexer.test("dEW", "dEW,<EOF>", 407))

	def test_408(self):
		self.assertTrue(TestLexer.test("77", "77,<EOF>", 408))

	def test_409(self):
		self.assertTrue(TestLexer.test("532.569e-86", "532.569e-86,<EOF>", 409))

	def test_410(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 410))

	def test_411(self):
		self.assertTrue(TestLexer.test("39.927", "39.927,<EOF>", 411))

	def test_412(self):
		self.assertTrue(TestLexer.test("416e-67", "416e-67,<EOF>", 412))

	def test_413(self):
		self.assertTrue(TestLexer.test('''"D{'"'"'" ''', '''Unclosed String: D{'"'"'" ''', 413))

	def test_414(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 414))

	def test_415(self):
		self.assertTrue(TestLexer.test("x@Iaut2z6Y", "x,Error Token @", 415))

	def test_416(self):
		self.assertTrue(TestLexer.test('''## >U(FaRO5C''', '''<EOF>''', 416))

	def test_417(self):
		self.assertTrue(TestLexer.test('''## Dg`gd@dH$q?F1>2]_@''', '''<EOF>''', 417))

	def test_418(self):
		self.assertTrue(TestLexer.test('''"
'"'"'"'""''', '''Unclosed String: ''', 418))

	def test_419(self):
		self.assertTrue(TestLexer.test('''## l1tLe(a-tQ$x(E?@8''', '''<EOF>''', 419))

	def test_420(self):
		self.assertTrue(TestLexer.test("2e+66", "2e+66,<EOF>", 420))

	def test_421(self):
		self.assertTrue(TestLexer.test('''## J(^ u9&wMZ:7f''', '''<EOF>''', 421))

	def test_422(self):
		self.assertTrue(TestLexer.test('''## cH/N0K+fuH5wMPA@;CP''', '''<EOF>''', 422))

	def test_423(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 423))

	def test_424(self):
		self.assertTrue(TestLexer.test("12.116", "12.116,<EOF>", 424))

	def test_425(self):
		self.assertTrue(TestLexer.test("517", "517,<EOF>", 425))

	def test_426(self):
		self.assertTrue(TestLexer.test('''## f6N;NcYd$''', '''<EOF>''', 426))

	def test_427(self):
		self.assertTrue(TestLexer.test("g@ZjD@#", "g,Error Token @", 427))

	def test_428(self):
		self.assertTrue(TestLexer.test("NYw@KPKVS", "NYw,Error Token @", 428))

	def test_429(self):
		self.assertTrue(TestLexer.test("5E+84", "5E+84,<EOF>", 429))

	def test_430(self):
		self.assertTrue(TestLexer.test("qwAAF&XH", "qwAAF,Error Token &", 430))

	def test_431(self):
		self.assertTrue(TestLexer.test("20.302", "20.302,<EOF>", 431))

	def test_432(self):
		self.assertTrue(TestLexer.test('''"
'"2"''', '''Unclosed String: ''', 432))

	def test_433(self):
		self.assertTrue(TestLexer.test('''## k@jA''', '''<EOF>''', 433))

	def test_434(self):
		self.assertTrue(TestLexer.test("jUD", "jUD,<EOF>", 434))

	def test_435(self):
		self.assertTrue(TestLexer.test('''## cXw2%CW<h^BrCb&''', '''<EOF>''', 435))

	def test_436(self):
		self.assertTrue(TestLexer.test('''## ic;nzcXfXwN3w_F><&W%''', '''<EOF>''', 436))

	def test_437(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 437))

	def test_438(self):
		self.assertTrue(TestLexer.test("170.548", "170.548,<EOF>", 438))

	def test_439(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 439))

	def test_440(self):
		self.assertTrue(TestLexer.test('''"*\\j'"''', '''Illegal Escape In String: *\\j''', 440))

	def test_441(self):
		self.assertTrue(TestLexer.test('''## mQqH;epZZw]^u''', '''<EOF>''', 441))

	def test_442(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 442))

	def test_443(self):
		self.assertTrue(TestLexer.test('''## t&iz''', '''<EOF>''', 443))

	def test_444(self):
		self.assertTrue(TestLexer.test("11e+59", "11e+59,<EOF>", 444))

	def test_445(self):
		self.assertTrue(TestLexer.test("84.716", "84.716,<EOF>", 445))

	def test_446(self):
		self.assertTrue(TestLexer.test('''## g!Z,sk''', '''<EOF>''', 446))

	def test_447(self):
		self.assertTrue(TestLexer.test('''## i)sOH7''', '''<EOF>''', 447))

	def test_448(self):
		self.assertTrue(TestLexer.test('''"0W$'""''', '''0W$'",<EOF>''', 448))

	def test_449(self):
		self.assertTrue(TestLexer.test("1E-39", "1E-39,<EOF>", 449))

	def test_450(self):
		self.assertTrue(TestLexer.test("9.471e-74", "9.471e-74,<EOF>", 450))

	def test_451(self):
		self.assertTrue(TestLexer.test("V_ytC^c", "V_ytC,Error Token ^", 451))

	def test_452(self):
		self.assertTrue(TestLexer.test("2E-54", "2E-54,<EOF>", 452))

	def test_453(self):
		self.assertTrue(TestLexer.test("Lb3Que", "Lb3Que,<EOF>", 453))

	def test_454(self):
		self.assertTrue(TestLexer.test("3.531E56", "3.531E56,<EOF>", 454))

	def test_455(self):
		self.assertTrue(TestLexer.test("imC@Ocs", "imC,Error Token @", 455))

	def test_456(self):
		self.assertTrue(TestLexer.test('''"X\\p'""''', '''Illegal Escape In String: X\\p''', 456))

	def test_457(self):
		self.assertTrue(TestLexer.test("10e+49", "10e+49,<EOF>", 457))

	def test_458(self):
		self.assertTrue(TestLexer.test('''## 0zJuP3:G"xR?pzw[5,O''', '''<EOF>''', 458))

	def test_459(self):
		self.assertTrue(TestLexer.test('''"<\\qzz'""''', '''Illegal Escape In String: <\\q''', 459))

	def test_460(self):
		self.assertTrue(TestLexer.test("532.381", "532.381,<EOF>", 460))

	def test_461(self):
		self.assertTrue(TestLexer.test("5W", "5,W,<EOF>", 461))

	def test_462(self):
		self.assertTrue(TestLexer.test("407", "407,<EOF>", 462))

	def test_463(self):
		self.assertTrue(TestLexer.test("36", "36,<EOF>", 463))

	def test_464(self):
		self.assertTrue(TestLexer.test("Bu57JeH", "Bu57JeH,<EOF>", 464))

	def test_465(self):
		self.assertTrue(TestLexer.test('''"'"\\e'"aI"''', '''Illegal Escape In String: '"\\e''', 465))

	def test_466(self):
		self.assertTrue(TestLexer.test("141.283E+87", "141.283E+87,<EOF>", 466))

	def test_467(self):
		self.assertTrue(TestLexer.test("821.069", "821.069,<EOF>", 467))

	def test_468(self):
		self.assertTrue(TestLexer.test('''## @Q/Z]''', '''<EOF>''', 468))

	def test_469(self):
		self.assertTrue(TestLexer.test("731.131", "731.131,<EOF>", 469))

	def test_470(self):
		self.assertTrue(TestLexer.test("597", "597,<EOF>", 470))

	def test_471(self):
		self.assertTrue(TestLexer.test('''"'"A\\v'"'"w"''', '''Illegal Escape In String: '"A\\v''', 471))

	def test_472(self):
		self.assertTrue(TestLexer.test('''## _R:rTx0GVx96?''', '''<EOF>''', 472))

	def test_473(self):
		self.assertTrue(TestLexer.test('''## ?_",-q8pp6''', '''<EOF>''', 473))

	def test_474(self):
		self.assertTrue(TestLexer.test("7.541", "7.541,<EOF>", 474))

	def test_475(self):
		self.assertTrue(TestLexer.test('''## 1a7$gPHX;''', '''<EOF>''', 475))

	def test_476(self):
		self.assertTrue(TestLexer.test('''## `.<!Ibwd}!OsKb2c.@d''', '''<EOF>''', 476))

	def test_477(self):
		self.assertTrue(TestLexer.test('''"3\\u'"'"i"''', '''Illegal Escape In String: 3\\u''', 477))

	def test_478(self):
		self.assertTrue(TestLexer.test('''## W}y''', '''<EOF>''', 478))

	def test_479(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 479))

	def test_480(self):
		self.assertTrue(TestLexer.test('''## Jsg%E''', '''<EOF>''', 480))

	def test_481(self):
		self.assertTrue(TestLexer.test('''"'"'"i\\a'""''', '''Illegal Escape In String: '"'"i\\a''', 481))

	def test_482(self):
		self.assertTrue(TestLexer.test("AUezTF9G", "AUezTF9G,<EOF>", 482))

	def test_483(self):
		self.assertTrue(TestLexer.test("606.784", "606.784,<EOF>", 483))

	def test_484(self):
		self.assertTrue(TestLexer.test("oNoj^VhJQW", "oNoj,Error Token ^", 484))

	def test_485(self):
		self.assertTrue(TestLexer.test('''## F1J>9]lk`WB_}D''', '''<EOF>''', 485))

	def test_486(self):
		self.assertTrue(TestLexer.test('''"\\w8)"''', '''Illegal Escape In String: \\w''', 486))

	def test_487(self):
		self.assertTrue(TestLexer.test("LCDdQUrR", "LCDdQUrR,<EOF>", 487))

	def test_488(self):
		self.assertTrue(TestLexer.test("7G&iOko", "7,G,Error Token &", 488))

	def test_489(self):
		self.assertTrue(TestLexer.test('''## lsgBN/xh=Er>''', '''<EOF>''', 489))

	def test_490(self):
		self.assertTrue(TestLexer.test("qpoy6mIh9", "qpoy6mIh9,<EOF>", 490))

	def test_491(self):
		self.assertTrue(TestLexer.test("757", "757,<EOF>", 491))

	def test_492(self):
		self.assertTrue(TestLexer.test('''"'"\\e'"'"'""''', '''Illegal Escape In String: '"\\e''', 492))

	def test_493(self):
		self.assertTrue(TestLexer.test('''## (]TQ3l ;-Ev}a(,M''', '''<EOF>''', 493))

	def test_494(self):
		self.assertTrue(TestLexer.test('''"\\a'""''', '''Illegal Escape In String: \\a''', 494))

	def test_495(self):
		self.assertTrue(TestLexer.test('''"'"\\pH"''', '''Illegal Escape In String: '"\\p''', 495))

	def test_496(self):
		self.assertTrue(TestLexer.test('''"c'"'"'" ''', '''Unclosed String: c'"'"'" ''', 496))

	def test_497(self):
		self.assertTrue(TestLexer.test("70", "70,<EOF>", 497))

	def test_498(self):
		self.assertTrue(TestLexer.test("207e-90", "207e-90,<EOF>", 498))

	def test_499(self):
		self.assertTrue(TestLexer.test("8e-17", "8e-17,<EOF>", 499))

	def test_500(self):
		self.assertTrue(TestLexer.test("8.140E77", "8.140E77,<EOF>", 500))

	def test_501(self):
		self.assertTrue(TestLexer.test("&", "Error Token &", 501))

	def test_502(self):
		self.assertTrue(TestLexer.test("92e-29", "92e-29,<EOF>", 502))

	def test_503(self):
		self.assertTrue(TestLexer.test('''"U'"('"'""''', '''U'"('"'",<EOF>''', 503))

	def test_504(self):
		self.assertTrue(TestLexer.test('''"c
'"'"-'""''', '''Unclosed String: c''', 504))

	def test_505(self):
		self.assertTrue(TestLexer.test('''## ZKSCR#b<fx|q+QNRuRy:''', '''<EOF>''', 505))

	def test_506(self):
		self.assertTrue(TestLexer.test("3Kr4Z", "3,Kr4Z,<EOF>", 506))

	def test_507(self):
		self.assertTrue(TestLexer.test("j2", "j2,<EOF>", 507))

	def test_508(self):
		self.assertTrue(TestLexer.test("bw", "bw,<EOF>", 508))

	def test_509(self):
		self.assertTrue(TestLexer.test("63e23", "63e23,<EOF>", 509))

	def test_510(self):
		self.assertTrue(TestLexer.test('''## 5u[x>''', '''<EOF>''', 510))

	def test_511(self):
		self.assertTrue(TestLexer.test("mp", "mp,<EOF>", 511))

	def test_512(self):
		self.assertTrue(TestLexer.test('''## N~cc1ef{WR^z85>y>z''', '''<EOF>''', 512))

	def test_513(self):
		self.assertTrue(TestLexer.test('''"\\e'""''', '''Illegal Escape In String: \\e''', 513))

	def test_514(self):
		self.assertTrue(TestLexer.test("7.274E+51", "7.274E+51,<EOF>", 514))

	def test_515(self):
		self.assertTrue(TestLexer.test('''## "aAM''', '''<EOF>''', 515))

	def test_516(self):
		self.assertTrue(TestLexer.test("0.173", "0.173,<EOF>", 516))

	def test_517(self):
		self.assertTrue(TestLexer.test('''"\\xw"''', '''Illegal Escape In String: \\x''', 517))

	def test_518(self):
		self.assertTrue(TestLexer.test('''"N&Z ''', '''Unclosed String: N&Z ''', 518))

	def test_519(self):
		self.assertTrue(TestLexer.test("96.641e+10", "96.641e+10,<EOF>", 519))

	def test_520(self):
		self.assertTrue(TestLexer.test('''## ON|?frC6cYs~c47''', '''<EOF>''', 520))

	def test_521(self):
		self.assertTrue(TestLexer.test('''## KqFQV.`r7>U''', '''<EOF>''', 521))

	def test_522(self):
		self.assertTrue(TestLexer.test('''"'"Z'"\\v'""''', '''Illegal Escape In String: '"Z'"\\v''', 522))

	def test_523(self):
		self.assertTrue(TestLexer.test("e", "e,<EOF>", 523))

	def test_524(self):
		self.assertTrue(TestLexer.test("x_n^KeK", "x_n,Error Token ^", 524))

	def test_525(self):
		self.assertTrue(TestLexer.test("8.761", "8.761,<EOF>", 525))

	def test_526(self):
		self.assertTrue(TestLexer.test("LJjxX91tSf", "LJjxX91tSf,<EOF>", 526))

	def test_527(self):
		self.assertTrue(TestLexer.test('''"2'"U>: ''', '''Unclosed String: 2'"U>: ''', 527))

	def test_528(self):
		self.assertTrue(TestLexer.test('''"g(D
'""''', '''Unclosed String: g(D''', 528))

	def test_529(self):
		self.assertTrue(TestLexer.test("7e48", "7e48,<EOF>", 529))

	def test_530(self):
		self.assertTrue(TestLexer.test('''## =&''', '''<EOF>''', 530))

	def test_531(self):
		self.assertTrue(TestLexer.test('''"
.?E'""''', '''Unclosed String: ''', 531))

	def test_532(self):
		self.assertTrue(TestLexer.test("8.412e-43", "8.412e-43,<EOF>", 532))

	def test_533(self):
		self.assertTrue(TestLexer.test("4.884E-22", "4.884E-22,<EOF>", 533))

	def test_534(self):
		self.assertTrue(TestLexer.test('''## rrD24E^NqM1H''', '''<EOF>''', 534))

	def test_535(self):
		self.assertTrue(TestLexer.test('''## F_!mX}1%~>VL$|W ''', '''<EOF>''', 535))

	def test_536(self):
		self.assertTrue(TestLexer.test("$RNu9yama", "Error Token $", 536))

	def test_537(self):
		self.assertTrue(TestLexer.test('''## /W"y?S_>~l"50orpuW''', '''<EOF>''', 537))

	def test_538(self):
		self.assertTrue(TestLexer.test("414", "414,<EOF>", 538))

	def test_539(self):
		self.assertTrue(TestLexer.test('''## "zLdx`ag"Fcb 8%j+''', '''<EOF>''', 539))

	def test_540(self):
		self.assertTrue(TestLexer.test("l2C@LE&0VX", "l2C,Error Token @", 540))

	def test_541(self):
		self.assertTrue(TestLexer.test("606", "606,<EOF>", 541))

	def test_542(self):
		self.assertTrue(TestLexer.test('''## C s.^]^|gZ[)]/ q<xW+''', '''<EOF>''', 542))

	def test_543(self):
		self.assertTrue(TestLexer.test("Nod", "Nod,<EOF>", 543))

	def test_544(self):
		self.assertTrue(TestLexer.test("50", "50,<EOF>", 544))

	def test_545(self):
		self.assertTrue(TestLexer.test("XEONsjX", "XEONsjX,<EOF>", 545))

	def test_546(self):
		self.assertTrue(TestLexer.test("1.753", "1.753,<EOF>", 546))

	def test_547(self):
		self.assertTrue(TestLexer.test('''"u-"''', '''u-,<EOF>''', 547))

	def test_548(self):
		self.assertTrue(TestLexer.test('''"\\m/"''', '''Illegal Escape In String: \\m''', 548))

	def test_549(self):
		self.assertTrue(TestLexer.test('''"P\\qQ"''', '''Illegal Escape In String: P\\q''', 549))

	def test_550(self):
		self.assertTrue(TestLexer.test('''## U1u>etk%pwr4''', '''<EOF>''', 550))

	def test_551(self):
		self.assertTrue(TestLexer.test("c&", "c,Error Token &", 551))

	def test_552(self):
		self.assertTrue(TestLexer.test("EcpvHX5BX", "EcpvHX5BX,<EOF>", 552))

	def test_553(self):
		self.assertTrue(TestLexer.test('''## $"`(?''', '''<EOF>''', 553))

	def test_554(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 554))

	def test_555(self):
		self.assertTrue(TestLexer.test('''"s'"'"'" ''', '''Unclosed String: s'"'"'" ''', 555))

	def test_556(self):
		self.assertTrue(TestLexer.test("78", "78,<EOF>", 556))

	def test_557(self):
		self.assertTrue(TestLexer.test('''## sS;''', '''<EOF>''', 557))

	def test_558(self):
		self.assertTrue(TestLexer.test("GcrSkgAs", "GcrSkgAs,<EOF>", 558))

	def test_559(self):
		self.assertTrue(TestLexer.test('''"'"'"\\m'"TO"''', '''Illegal Escape In String: '"'"\\m''', 559))

	def test_560(self):
		self.assertTrue(TestLexer.test('''## $cxyu|@(n''', '''<EOF>''', 560))

	def test_561(self):
		self.assertTrue(TestLexer.test('''"\\g'""''', '''Illegal Escape In String: \\g''', 561))

	def test_562(self):
		self.assertTrue(TestLexer.test('''"'"\\xq"''', '''Illegal Escape In String: '"\\x''', 562))

	def test_563(self):
		self.assertTrue(TestLexer.test("f$MA", "f,Error Token $", 563))

	def test_564(self):
		self.assertTrue(TestLexer.test('''"\\i'"Nx'","''', '''Illegal Escape In String: \\i''', 564))

	def test_565(self):
		self.assertTrue(TestLexer.test('''"'"\\m'""''', '''Illegal Escape In String: '"\\m''', 565))

	def test_566(self):
		self.assertTrue(TestLexer.test('''"'"e ''', '''Unclosed String: '"e ''', 566))

	def test_567(self):
		self.assertTrue(TestLexer.test('''##  gP3''', '''<EOF>''', 567))

	def test_568(self):
		self.assertTrue(TestLexer.test("7E-11", "7E-11,<EOF>", 568))

	def test_569(self):
		self.assertTrue(TestLexer.test("8aM@donKH", "8,aM,Error Token @", 569))

	def test_570(self):
		self.assertTrue(TestLexer.test("412E07", "412E07,<EOF>", 570))

	def test_571(self):
		self.assertTrue(TestLexer.test("14", "14,<EOF>", 571))

	def test_572(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 572))

	def test_573(self):
		self.assertTrue(TestLexer.test("idQUT4veh8", "idQUT4veh8,<EOF>", 573))

	def test_574(self):
		self.assertTrue(TestLexer.test("8.017E-44", "8.017E-44,<EOF>", 574))

	def test_575(self):
		self.assertTrue(TestLexer.test("0.764E-18", "0.764E-18,<EOF>", 575))

	def test_576(self):
		self.assertTrue(TestLexer.test('''## 7_nm`Bf]{''', '''<EOF>''', 576))

	def test_577(self):
		self.assertTrue(TestLexer.test('''"
<{"''', '''Unclosed String: ''', 577))

	def test_578(self):
		self.assertTrue(TestLexer.test('''## F&xaa''', '''<EOF>''', 578))

	def test_579(self):
		self.assertTrue(TestLexer.test("4e60", "4e60,<EOF>", 579))

	def test_580(self):
		self.assertTrue(TestLexer.test("27.339E+77", "27.339E+77,<EOF>", 580))

	def test_581(self):
		self.assertTrue(TestLexer.test('''## .:''', '''<EOF>''', 581))

	def test_582(self):
		self.assertTrue(TestLexer.test('''"'"'"j'""''', '''\'"'"j'",<EOF>''', 582))

	def test_583(self):
		self.assertTrue(TestLexer.test('''"y"''', '''y,<EOF>''', 583))

	def test_584(self):
		self.assertTrue(TestLexer.test("32.314e+75", "32.314e+75,<EOF>", 584))

	def test_585(self):
		self.assertTrue(TestLexer.test("4Zz86", "4,Zz86,<EOF>", 585))

	def test_586(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 586))

	def test_587(self):
		self.assertTrue(TestLexer.test("891", "891,<EOF>", 587))

	def test_588(self):
		self.assertTrue(TestLexer.test("Cn", "Cn,<EOF>", 588))

	def test_589(self):
		self.assertTrue(TestLexer.test('''"\\u'"'""''', '''Illegal Escape In String: \\u''', 589))

	def test_590(self):
		self.assertTrue(TestLexer.test('''## Y8BXxs''', '''<EOF>''', 590))

	def test_591(self):
		self.assertTrue(TestLexer.test('''"'"bc\\l-'""''', '''Illegal Escape In String: '"bc\\l''', 591))

	def test_592(self):
		self.assertTrue(TestLexer.test("@ywjPW", "Error Token @", 592))

	def test_593(self):
		self.assertTrue(TestLexer.test('''"o"''', '''o,<EOF>''', 593))

	def test_594(self):
		self.assertTrue(TestLexer.test("dQecfh8zAQ", "dQecfh8zAQ,<EOF>", 594))

	def test_595(self):
		self.assertTrue(TestLexer.test('''"-V"''', '''-V,<EOF>''', 595))

	def test_596(self):
		self.assertTrue(TestLexer.test('''## 4 hbH_fiK''', '''<EOF>''', 596))

	def test_597(self):
		self.assertTrue(TestLexer.test('''"!'" ''', '''Unclosed String: !'" ''', 597))

	def test_598(self):
		self.assertTrue(TestLexer.test("67.905", "67.905,<EOF>", 598))

	def test_599(self):
		self.assertTrue(TestLexer.test("oMe", "oMe,<EOF>", 599))
