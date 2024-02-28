import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	def test_100(self):
		self.assertTrue(TestLexer.test('''## PFd.!N!QNeXl''', '''<EOF>''', 100))

	def test_101(self):
		self.assertTrue(TestLexer.test('''"[E
('"'""''', '''Unclosed String: [E''', 101))

	def test_102(self):
		self.assertTrue(TestLexer.test("K7HD", "K7HD,<EOF>", 102))

	def test_103(self):
		self.assertTrue(TestLexer.test("a$", "a,Error Token $", 103))

	def test_104(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 104))

	def test_105(self):
		self.assertTrue(TestLexer.test('''## Z/rF.w.k2@c*jY''', '''<EOF>''', 105))

	def test_106(self):
		self.assertTrue(TestLexer.test('''"t'","''', '''t'",,<EOF>''', 106))

	def test_107(self):
		self.assertTrue(TestLexer.test("282.035", "282.035,<EOF>", 107))

	def test_108(self):
		self.assertTrue(TestLexer.test("854.544e30", "854.544e30,<EOF>", 108))

	def test_109(self):
		self.assertTrue(TestLexer.test('''"\\y?<"''', '''Illegal Escape In String: \\y''', 109))

	def test_110(self):
		self.assertTrue(TestLexer.test("50.364E-05", "50.364E-05,<EOF>", 110))

	def test_111(self):
		self.assertTrue(TestLexer.test("DMV4QJ", "DMV4QJ,<EOF>", 111))

	def test_112(self):
		self.assertTrue(TestLexer.test("qE3V7F", "qE3V7F,<EOF>", 112))

	def test_113(self):
		self.assertTrue(TestLexer.test("92", "92,<EOF>", 113))

	def test_114(self):
		self.assertTrue(TestLexer.test("49.505", "49.505,<EOF>", 114))

	def test_115(self):
		self.assertTrue(TestLexer.test("xkB3dlQ", "xkB3dlQ,<EOF>", 115))

	def test_116(self):
		self.assertTrue(TestLexer.test('''## 3j>sAP-Tfhopy''', '''<EOF>''', 116))

	def test_117(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 117))

	def test_118(self):
		self.assertTrue(TestLexer.test('''##  Ez''', '''<EOF>''', 118))

	def test_119(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 119))

	def test_120(self):
		self.assertTrue(TestLexer.test("_YVWH6F6w", "_YVWH6F6w,<EOF>", 120))

	def test_121(self):
		self.assertTrue(TestLexer.test("m", "m,<EOF>", 121))

	def test_122(self):
		self.assertTrue(TestLexer.test("^Lp", "Error Token ^", 122))

	def test_123(self):
		self.assertTrue(TestLexer.test('''## /<n99`WBZV''', '''<EOF>''', 123))

	def test_124(self):
		self.assertTrue(TestLexer.test("tI", "tI,<EOF>", 124))

	def test_125(self):
		self.assertTrue(TestLexer.test("904", "904,<EOF>", 125))

	def test_126(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 126))

	def test_127(self):
		self.assertTrue(TestLexer.test("DuG", "DuG,<EOF>", 127))

	def test_128(self):
		self.assertTrue(TestLexer.test('''"'"KA$ ''', '''Unclosed String: '"KA$ ''', 128))

	def test_129(self):
		self.assertTrue(TestLexer.test("QPh", "QPh,<EOF>", 129))

	def test_130(self):
		self.assertTrue(TestLexer.test("lLn0y5Z", "lLn0y5Z,<EOF>", 130))

	def test_131(self):
		self.assertTrue(TestLexer.test('''## YJZtTL]D^D`dX[''', '''<EOF>''', 131))

	def test_132(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 132))

	def test_133(self):
		self.assertTrue(TestLexer.test('''": ''', '''Unclosed String: : ''', 133))

	def test_134(self):
		self.assertTrue(TestLexer.test("&mN_h#H9S", "Error Token &", 134))

	def test_135(self):
		self.assertTrue(TestLexer.test('''## b}w7i b~IWb^''', '''<EOF>''', 135))

	def test_136(self):
		self.assertTrue(TestLexer.test("@o2wYd", "Error Token @", 136))

	def test_137(self):
		self.assertTrue(TestLexer.test("r4AO", "r4AO,<EOF>", 137))

	def test_138(self):
		self.assertTrue(TestLexer.test('''## |m,@AP@1wOkMH=!!_5''', '''<EOF>''', 138))

	def test_139(self):
		self.assertTrue(TestLexer.test('''## hhz"OS!*]<<]."lTj& ''', '''<EOF>''', 139))

	def test_140(self):
		self.assertTrue(TestLexer.test("8.930", "8.930,<EOF>", 140))

	def test_141(self):
		self.assertTrue(TestLexer.test('''"'"K!'""''', '''\'"K!'",<EOF>''', 141))

	def test_142(self):
		self.assertTrue(TestLexer.test('''## ZF C5cnknmb*&"S''', '''<EOF>''', 142))

	def test_143(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 143))

	def test_144(self):
		self.assertTrue(TestLexer.test("264.466E42", "264.466E42,<EOF>", 144))

	def test_145(self):
		self.assertTrue(TestLexer.test("26dBcou7", "26,dBcou7,<EOF>", 145))

	def test_146(self):
		self.assertTrue(TestLexer.test("20E60", "20E60,<EOF>", 146))

	def test_147(self):
		self.assertTrue(TestLexer.test('''## tmT6;]2-VG0]>,|N''', '''<EOF>''', 147))

	def test_148(self):
		self.assertTrue(TestLexer.test("875.115", "875.115,<EOF>", 148))

	def test_149(self):
		self.assertTrue(TestLexer.test('''"
!"''', '''Unclosed String: ''', 149))

	def test_150(self):
		self.assertTrue(TestLexer.test("519", "519,<EOF>", 150))

	def test_151(self):
		self.assertTrue(TestLexer.test('''"(z"''', '''(z,<EOF>''', 151))

	def test_152(self):
		self.assertTrue(TestLexer.test("37.138e-07", "37.138e-07,<EOF>", 152))

	def test_153(self):
		self.assertTrue(TestLexer.test("@i", "Error Token @", 153))

	def test_154(self):
		self.assertTrue(TestLexer.test("^Ry9", "Error Token ^", 154))

	def test_155(self):
		self.assertTrue(TestLexer.test("9e03", "9e03,<EOF>", 155))

	def test_156(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 156))

	def test_157(self):
		self.assertTrue(TestLexer.test('''## LXScvTD},&z>X''', '''<EOF>''', 157))

	def test_158(self):
		self.assertTrue(TestLexer.test("wp51UC@$9", "wp51UC,Error Token @", 158))

	def test_159(self):
		self.assertTrue(TestLexer.test("300e-70", "300e-70,<EOF>", 159))

	def test_160(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 160))

	def test_161(self):
		self.assertTrue(TestLexer.test("iY@h", "iY,Error Token @", 161))

	def test_162(self):
		self.assertTrue(TestLexer.test('''"'"'"}'" ''', '''Unclosed String: '"'"}'" ''', 162))

	def test_163(self):
		self.assertTrue(TestLexer.test("229.962", "229.962,<EOF>", 163))

	def test_164(self):
		self.assertTrue(TestLexer.test('''## +v[RIrG[d''', '''<EOF>''', 164))

	def test_165(self):
		self.assertTrue(TestLexer.test("PtfJF0Ph", "PtfJF0Ph,<EOF>", 165))

	def test_166(self):
		self.assertTrue(TestLexer.test("ELp", "ELp,<EOF>", 166))

	def test_167(self):
		self.assertTrue(TestLexer.test("c$", "c,Error Token $", 167))

	def test_168(self):
		self.assertTrue(TestLexer.test("90.457e79", "90.457e79,<EOF>", 168))

	def test_169(self):
		self.assertTrue(TestLexer.test("8.976", "8.976,<EOF>", 169))

	def test_170(self):
		self.assertTrue(TestLexer.test("9.482", "9.482,<EOF>", 170))

	def test_171(self):
		self.assertTrue(TestLexer.test("184", "184,<EOF>", 171))

	def test_172(self):
		self.assertTrue(TestLexer.test('''## ^oBX#''', '''<EOF>''', 172))

	def test_173(self):
		self.assertTrue(TestLexer.test("Te$jZ", "Te,Error Token $", 173))

	def test_174(self):
		self.assertTrue(TestLexer.test('''## T#GxzBRqA[B4''', '''<EOF>''', 174))

	def test_175(self):
		self.assertTrue(TestLexer.test('''## (b''', '''<EOF>''', 175))

	def test_176(self):
		self.assertTrue(TestLexer.test('''"B'"P"''', '''B'"P,<EOF>''', 176))

	def test_177(self):
		self.assertTrue(TestLexer.test('''## GxD:OD@25$x5_j''', '''<EOF>''', 177))

	def test_178(self):
		self.assertTrue(TestLexer.test('''## 6e^HaQ3{|Ah5]kCE8''', '''<EOF>''', 178))

	def test_179(self):
		self.assertTrue(TestLexer.test("406", "406,<EOF>", 179))

	def test_180(self):
		self.assertTrue(TestLexer.test("133.215e+71", "133.215e+71,<EOF>", 180))

	def test_181(self):
		self.assertTrue(TestLexer.test("917.830", "917.830,<EOF>", 181))

	def test_182(self):
		self.assertTrue(TestLexer.test("20E46", "20E46,<EOF>", 182))

	def test_183(self):
		self.assertTrue(TestLexer.test("fzPAOZupZd", "fzPAOZupZd,<EOF>", 183))

	def test_184(self):
		self.assertTrue(TestLexer.test("8", "8,<EOF>", 184))

	def test_185(self):
		self.assertTrue(TestLexer.test("4", "4,<EOF>", 185))

	def test_186(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 186))

	def test_187(self):
		self.assertTrue(TestLexer.test('''## 7;1hQfZo;}[6/C?GJ$#b''', '''<EOF>''', 187))

	def test_188(self):
		self.assertTrue(TestLexer.test("164.220E+96", "164.220E+96,<EOF>", 188))

	def test_189(self):
		self.assertTrue(TestLexer.test("6E+96", "6E+96,<EOF>", 189))

	def test_190(self):
		self.assertTrue(TestLexer.test('''"h"''', '''h,<EOF>''', 190))

	def test_191(self):
		self.assertTrue(TestLexer.test('''## ngP''', '''<EOF>''', 191))

	def test_192(self):
		self.assertTrue(TestLexer.test("8.315e+67", "8.315e+67,<EOF>", 192))

	def test_193(self):
		self.assertTrue(TestLexer.test("5e41", "5e41,<EOF>", 193))

	def test_194(self):
		self.assertTrue(TestLexer.test("9.245E68", "9.245E68,<EOF>", 194))

	def test_195(self):
		self.assertTrue(TestLexer.test("463.730E94", "463.730E94,<EOF>", 195))

	def test_196(self):
		self.assertTrue(TestLexer.test('''## [5''', '''<EOF>''', 196))

	def test_197(self):
		self.assertTrue(TestLexer.test('''## J(k<.CJw ''', '''<EOF>''', 197))

	def test_198(self):
		self.assertTrue(TestLexer.test('''"\\v"''', '''Illegal Escape In String: \\v''', 198))

	def test_199(self):
		self.assertTrue(TestLexer.test('''## @,e{tPv27Y?UV~{=''', '''<EOF>''', 199))

	def test_200(self):
		self.assertTrue(TestLexer.test("78.926", "78.926,<EOF>", 200))

	def test_201(self):
		self.assertTrue(TestLexer.test('''## D^2]qGU&4T''', '''<EOF>''', 201))

	def test_202(self):
		self.assertTrue(TestLexer.test('''"k"''', '''k,<EOF>''', 202))

	def test_203(self):
		self.assertTrue(TestLexer.test('''## `)02P(E+{LYZ,>]iS''', '''<EOF>''', 203))

	def test_204(self):
		self.assertTrue(TestLexer.test('''## c8Q0YJ+CWOEYt}fD]L}''', '''<EOF>''', 204))

	def test_205(self):
		self.assertTrue(TestLexer.test('''## $]7vGb$7p pu]Wa''', '''<EOF>''', 205))

	def test_206(self):
		self.assertTrue(TestLexer.test('''## 9q"=MNth8!Qe&9''', '''<EOF>''', 206))

	def test_207(self):
		self.assertTrue(TestLexer.test("67", "67,<EOF>", 207))

	def test_208(self):
		self.assertTrue(TestLexer.test("qxsQco", "qxsQco,<EOF>", 208))

	def test_209(self):
		self.assertTrue(TestLexer.test("FQYMMTv", "FQYMMTv,<EOF>", 209))

	def test_210(self):
		self.assertTrue(TestLexer.test('''## :m:&8eN6/1;y''', '''<EOF>''', 210))

	def test_211(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 211))

	def test_212(self):
		self.assertTrue(TestLexer.test("HmSESw_I7z", "HmSESw_I7z,<EOF>", 212))

	def test_213(self):
		self.assertTrue(TestLexer.test("553.081E-36", "553.081E-36,<EOF>", 213))

	def test_214(self):
		self.assertTrue(TestLexer.test('''"\\ah'"b'"'""''', '''Illegal Escape In String: \\a''', 214))

	def test_215(self):
		self.assertTrue(TestLexer.test('''## 2-(#OM(L0|${/n ih,]>''', '''<EOF>''', 215))

	def test_216(self):
		self.assertTrue(TestLexer.test("98.213", "98.213,<EOF>", 216))

	def test_217(self):
		self.assertTrue(TestLexer.test("3.156e+48", "3.156e+48,<EOF>", 217))

	def test_218(self):
		self.assertTrue(TestLexer.test("414.641E22", "414.641E22,<EOF>", 218))

	def test_219(self):
		self.assertTrue(TestLexer.test("585.400e+60", "585.400e+60,<EOF>", 219))

	def test_220(self):
		self.assertTrue(TestLexer.test('''"W\\u'""''', '''Illegal Escape In String: W\\u''', 220))

	def test_221(self):
		self.assertTrue(TestLexer.test("90.486", "90.486,<EOF>", 221))

	def test_222(self):
		self.assertTrue(TestLexer.test('''## vgg-`K/NSyKO9G_f''', '''<EOF>''', 222))

	def test_223(self):
		self.assertTrue(TestLexer.test("3s", "3,s,<EOF>", 223))

	def test_224(self):
		self.assertTrue(TestLexer.test('''## f`#:zOE''', '''<EOF>''', 224))

	def test_225(self):
		self.assertTrue(TestLexer.test('''## >,x%lM@[(1jd`''', '''<EOF>''', 225))

	def test_226(self):
		self.assertTrue(TestLexer.test("pjOj$Cm1Er", "pjOj,Error Token $", 226))

	def test_227(self):
		self.assertTrue(TestLexer.test('''"X'"'"9 ''', '''Unclosed String: X'"'"9 ''', 227))

	def test_228(self):
		self.assertTrue(TestLexer.test("488.951", "488.951,<EOF>", 228))

	def test_229(self):
		self.assertTrue(TestLexer.test('''## x!=''', '''<EOF>''', 229))

	def test_230(self):
		self.assertTrue(TestLexer.test("7wmTkA1p", "7,wmTkA1p,<EOF>", 230))

	def test_231(self):
		self.assertTrue(TestLexer.test("#Jr2iyqeU", "Error Token #", 231))

	def test_232(self):
		self.assertTrue(TestLexer.test("54", "54,<EOF>", 232))

	def test_233(self):
		self.assertTrue(TestLexer.test("80", "80,<EOF>", 233))

	def test_234(self):
		self.assertTrue(TestLexer.test("90.666", "90.666,<EOF>", 234))

	def test_235(self):
		self.assertTrue(TestLexer.test("67", "67,<EOF>", 235))

	def test_236(self):
		self.assertTrue(TestLexer.test('''" '">"''', ''' '">,<EOF>''', 236))

	def test_237(self):
		self.assertTrue(TestLexer.test("WTs", "WTs,<EOF>", 237))

	def test_238(self):
		self.assertTrue(TestLexer.test("hkvzG", "hkvzG,<EOF>", 238))

	def test_239(self):
		self.assertTrue(TestLexer.test('''"'";
}"''', '''Unclosed String: '";''', 239))

	def test_240(self):
		self.assertTrue(TestLexer.test('''## iWFQ*ZSJ;u?-S''', '''<EOF>''', 240))

	def test_241(self):
		self.assertTrue(TestLexer.test("99", "99,<EOF>", 241))

	def test_242(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 242))

	def test_243(self):
		self.assertTrue(TestLexer.test("655.683", "655.683,<EOF>", 243))

	def test_244(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 244))

	def test_245(self):
		self.assertTrue(TestLexer.test('''## {%Q''', '''<EOF>''', 245))

	def test_246(self):
		self.assertTrue(TestLexer.test('''"'"'"Z'"\\jB"''', '''Illegal Escape In String: '"'"Z'"\\j''', 246))

	def test_247(self):
		self.assertTrue(TestLexer.test("9.074", "9.074,<EOF>", 247))

	def test_248(self):
		self.assertTrue(TestLexer.test('''";'"3'""''', ''';'"3'",<EOF>''', 248))

	def test_249(self):
		self.assertTrue(TestLexer.test("fU", "fU,<EOF>", 249))

	def test_250(self):
		self.assertTrue(TestLexer.test('''## #0~h/kkP +^PN''', '''<EOF>''', 250))

	def test_251(self):
		self.assertTrue(TestLexer.test('''## %e%|I[F@GEA$m''', '''<EOF>''', 251))

	def test_252(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 252))

	def test_253(self):
		self.assertTrue(TestLexer.test("I", "I,<EOF>", 253))

	def test_254(self):
		self.assertTrue(TestLexer.test('''## 7-]!~ObkO5_>+M{a/yJ''', '''<EOF>''', 254))

	def test_255(self):
		self.assertTrue(TestLexer.test('''## }-NFWMd}_ DcxtJy)f''', '''<EOF>''', 255))

	def test_256(self):
		self.assertTrue(TestLexer.test("78.778e+18", "78.778e+18,<EOF>", 256))

	def test_257(self):
		self.assertTrue(TestLexer.test("8DfiH", "8,DfiH,<EOF>", 257))

	def test_258(self):
		self.assertTrue(TestLexer.test("$_", "Error Token $", 258))

	def test_259(self):
		self.assertTrue(TestLexer.test("u$", "u,Error Token $", 259))

	def test_260(self):
		self.assertTrue(TestLexer.test("^", "Error Token ^", 260))

	def test_261(self):
		self.assertTrue(TestLexer.test('''"'"'"^m
'""''', '''Unclosed String: '"'"^m''', 261))

	def test_262(self):
		self.assertTrue(TestLexer.test('''"x#~'"
Y"''', '''Unclosed String: x#~'"''', 262))

	def test_263(self):
		self.assertTrue(TestLexer.test('''"* ''', '''Unclosed String: * ''', 263))

	def test_264(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 264))

	def test_265(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 265))

	def test_266(self):
		self.assertTrue(TestLexer.test("Rk$n8In", "Rk,Error Token $", 266))

	def test_267(self):
		self.assertTrue(TestLexer.test("KDz5", "KDz5,<EOF>", 267))

	def test_268(self):
		self.assertTrue(TestLexer.test("2OvLJ", "2,OvLJ,<EOF>", 268))

	def test_269(self):
		self.assertTrue(TestLexer.test('''## R(mb:C%4Po/UcLaqLn!''', '''<EOF>''', 269))

	def test_270(self):
		self.assertTrue(TestLexer.test("oSkz0ev", "oSkz0ev,<EOF>", 270))

	def test_271(self):
		self.assertTrue(TestLexer.test("NZD2C", "NZD2C,<EOF>", 271))

	def test_272(self):
		self.assertTrue(TestLexer.test('''"'"[ ''', '''Unclosed String: '"[ ''', 272))

	def test_273(self):
		self.assertTrue(TestLexer.test('''## ! PhPVjRWa/`{''', '''<EOF>''', 273))

	def test_274(self):
		self.assertTrue(TestLexer.test("6.160e29", "6.160e29,<EOF>", 274))

	def test_275(self):
		self.assertTrue(TestLexer.test("lonfuKpEsu", "lonfuKpEsu,<EOF>", 275))

	def test_276(self):
		self.assertTrue(TestLexer.test("4e86", "4e86,<EOF>", 276))

	def test_277(self):
		self.assertTrue(TestLexer.test('''## 1ZKkzPy^J''', '''<EOF>''', 277))

	def test_278(self):
		self.assertTrue(TestLexer.test("17", "17,<EOF>", 278))

	def test_279(self):
		self.assertTrue(TestLexer.test('''## ^:8bx").H@''', '''<EOF>''', 279))

	def test_280(self):
		self.assertTrue(TestLexer.test('''## aV5pg`CW_O#''', '''<EOF>''', 280))

	def test_281(self):
		self.assertTrue(TestLexer.test("pmsW38UwRI", "pmsW38UwRI,<EOF>", 281))

	def test_282(self):
		self.assertTrue(TestLexer.test('''## ;[Wf_;X-&jS!ra''', '''<EOF>''', 282))

	def test_283(self):
		self.assertTrue(TestLexer.test('''"'"'"!\\e	'""''', '''Illegal Escape In String: '"'"!\\e''', 283))

	def test_284(self):
		self.assertTrue(TestLexer.test('''## 7nuoh''', '''<EOF>''', 284))

	def test_285(self):
		self.assertTrue(TestLexer.test('''## 5ka=Ar''', '''<EOF>''', 285))

	def test_286(self):
		self.assertTrue(TestLexer.test("B", "B,<EOF>", 286))

	def test_287(self):
		self.assertTrue(TestLexer.test("6.966", "6.966,<EOF>", 287))

	def test_288(self):
		self.assertTrue(TestLexer.test("1d^wH3@Vp", "1,d,Error Token ^", 288))

	def test_289(self):
		self.assertTrue(TestLexer.test("8E+77", "8E+77,<EOF>", 289))

	def test_290(self):
		self.assertTrue(TestLexer.test('''"'"W'"'"'""''', '''\'"W'"'"'",<EOF>''', 290))

	def test_291(self):
		self.assertTrue(TestLexer.test('''"'"\\c'""''', '''Illegal Escape In String: '"\\c''', 291))

	def test_292(self):
		self.assertTrue(TestLexer.test("9.814", "9.814,<EOF>", 292))

	def test_293(self):
		self.assertTrue(TestLexer.test("641.055", "641.055,<EOF>", 293))

	def test_294(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 294))

	def test_295(self):
		self.assertTrue(TestLexer.test("CeBxlwI", "CeBxlwI,<EOF>", 295))

	def test_296(self):
		self.assertTrue(TestLexer.test("73.701", "73.701,<EOF>", 296))

	def test_297(self):
		self.assertTrue(TestLexer.test("5ogC", "5,ogC,<EOF>", 297))

	def test_298(self):
		self.assertTrue(TestLexer.test('''"W\\cq'"'"R"''', '''Illegal Escape In String: W\\c''', 298))

	def test_299(self):
		self.assertTrue(TestLexer.test('''"N'"\\my'"'""''', '''Illegal Escape In String: N'"\\m''', 299))

	def test_300(self):
		self.assertTrue(TestLexer.test('''## =+*''', '''<EOF>''', 300))

	def test_301(self):
		self.assertTrue(TestLexer.test('''"
w'""''', '''Unclosed String: ''', 301))

	def test_302(self):
		self.assertTrue(TestLexer.test("op", "op,<EOF>", 302))

	def test_303(self):
		self.assertTrue(TestLexer.test("dvtTGK", "dvtTGK,<EOF>", 303))

	def test_304(self):
		self.assertTrue(TestLexer.test("0.918", "0.918,<EOF>", 304))

	def test_305(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 305))

	def test_306(self):
		self.assertTrue(TestLexer.test("ovlhj", "ovlhj,<EOF>", 306))

	def test_307(self):
		self.assertTrue(TestLexer.test('''## 0Q,yK[s-E)C_,c+hq>HO''', '''<EOF>''', 307))

	def test_308(self):
		self.assertTrue(TestLexer.test("0.016", "0.016,<EOF>", 308))

	def test_309(self):
		self.assertTrue(TestLexer.test('''"'"<'""''', '''\'"<'",<EOF>''', 309))

	def test_310(self):
		self.assertTrue(TestLexer.test('''"'"w'"
'""''', '''Unclosed String: '"w'"''', 310))

	def test_311(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 311))

	def test_312(self):
		self.assertTrue(TestLexer.test('''## @j/%HF.9E''', '''<EOF>''', 312))

	def test_313(self):
		self.assertTrue(TestLexer.test("34.559E-64", "34.559E-64,<EOF>", 313))

	def test_314(self):
		self.assertTrue(TestLexer.test("990.836E-40", "990.836E-40,<EOF>", 314))

	def test_315(self):
		self.assertTrue(TestLexer.test("225E64", "225E64,<EOF>", 315))

	def test_316(self):
		self.assertTrue(TestLexer.test('''## ^''', '''<EOF>''', 316))

	def test_317(self):
		self.assertTrue(TestLexer.test("^p5AdKLrn", "Error Token ^", 317))

	def test_318(self):
		self.assertTrue(TestLexer.test("jd3W", "jd3W,<EOF>", 318))

	def test_319(self):
		self.assertTrue(TestLexer.test("32e-74", "32e-74,<EOF>", 319))

	def test_320(self):
		self.assertTrue(TestLexer.test("#H", "Error Token #", 320))

	def test_321(self):
		self.assertTrue(TestLexer.test('''## xR=<B?Q''', '''<EOF>''', 321))

	def test_322(self):
		self.assertTrue(TestLexer.test('''"\\xo'"L'","''', '''Illegal Escape In String: \\x''', 322))

	def test_323(self):
		self.assertTrue(TestLexer.test("8.423", "8.423,<EOF>", 323))

	def test_324(self):
		self.assertTrue(TestLexer.test('''## ;;^1keal?%U1C2''', '''<EOF>''', 324))

	def test_325(self):
		self.assertTrue(TestLexer.test('''"'"	V:S"''', '''\'"	V:S,<EOF>''', 325))

	def test_326(self):
		self.assertTrue(TestLexer.test('''## P&AlS?D''', '''<EOF>''', 326))

	def test_327(self):
		self.assertTrue(TestLexer.test('''"'"r#"''', '''\'"r#,<EOF>''', 327))

	def test_328(self):
		self.assertTrue(TestLexer.test("68.384", "68.384,<EOF>", 328))

	def test_329(self):
		self.assertTrue(TestLexer.test("649.512", "649.512,<EOF>", 329))

	def test_330(self):
		self.assertTrue(TestLexer.test('''## V|0n6~i#}@-y*Li,`X!''', '''<EOF>''', 330))

	def test_331(self):
		self.assertTrue(TestLexer.test("56e+83", "56e+83,<EOF>", 331))

	def test_332(self):
		self.assertTrue(TestLexer.test('''## LaGa38i6Je.<:(''', '''<EOF>''', 332))

	def test_333(self):
		self.assertTrue(TestLexer.test('''"z2\\kT9"''', '''Illegal Escape In String: z2\\k''', 333))

	def test_334(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 334))

	def test_335(self):
		self.assertTrue(TestLexer.test("wpX7rk", "wpX7rk,<EOF>", 335))

	def test_336(self):
		self.assertTrue(TestLexer.test('''## zaH<B&,FWt!3u7F[8''', '''<EOF>''', 336))

	def test_337(self):
		self.assertTrue(TestLexer.test("XUKlMJF9", "XUKlMJF9,<EOF>", 337))

	def test_338(self):
		self.assertTrue(TestLexer.test('''## a<>+K|7b''', '''<EOF>''', 338))

	def test_339(self):
		self.assertTrue(TestLexer.test('''## fzBgx+Ol0iCT?<djCwRo''', '''<EOF>''', 339))

	def test_340(self):
		self.assertTrue(TestLexer.test('''"\\y'"ip'"'""''', '''Illegal Escape In String: \\y''', 340))

	def test_341(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 341))

	def test_342(self):
		self.assertTrue(TestLexer.test("1E+55", "1E+55,<EOF>", 342))

	def test_343(self):
		self.assertTrue(TestLexer.test('''"@'"i'";"''', '''@'"i'";,<EOF>''', 343))

	def test_344(self):
		self.assertTrue(TestLexer.test('''## h7}ImGJNOv''', '''<EOF>''', 344))

	def test_345(self):
		self.assertTrue(TestLexer.test('''## #yW>0)''', '''<EOF>''', 345))

	def test_346(self):
		self.assertTrue(TestLexer.test("DS82", "DS82,<EOF>", 346))

	def test_347(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 347))

	def test_348(self):
		self.assertTrue(TestLexer.test('''## N {O.D90_''', '''<EOF>''', 348))

	def test_349(self):
		self.assertTrue(TestLexer.test("IEyYnQzU", "IEyYnQzU,<EOF>", 349))

	def test_350(self):
		self.assertTrue(TestLexer.test("407.001e+96", "407.001e+96,<EOF>", 350))

	def test_351(self):
		self.assertTrue(TestLexer.test("48", "48,<EOF>", 351))

	def test_352(self):
		self.assertTrue(TestLexer.test('''## _CEhZKuHhX:tL''', '''<EOF>''', 352))

	def test_353(self):
		self.assertTrue(TestLexer.test('''"'"'"?J'" ''', '''Unclosed String: '"'"?J'" ''', 353))

	def test_354(self):
		self.assertTrue(TestLexer.test('''## -)@^Jx3Y@CC<<x(''', '''<EOF>''', 354))

	def test_355(self):
		self.assertTrue(TestLexer.test("558", "558,<EOF>", 355))

	def test_356(self):
		self.assertTrue(TestLexer.test('''## l8jh2`Ct4!Ij5[-<i''', '''<EOF>''', 356))

	def test_357(self):
		self.assertTrue(TestLexer.test("Jp8d8FAu_8", "Jp8d8FAu_8,<EOF>", 357))

	def test_358(self):
		self.assertTrue(TestLexer.test('''")\\d '"'"'""''', '''Illegal Escape In String: )\\d''', 358))

	def test_359(self):
		self.assertTrue(TestLexer.test("0E48", "0E48,<EOF>", 359))

	def test_360(self):
		self.assertTrue(TestLexer.test('''## 6''', '''<EOF>''', 360))

	def test_361(self):
		self.assertTrue(TestLexer.test('''"'"'"S'"'""''', '''\'"'"S'"'",<EOF>''', 361))

	def test_362(self):
		self.assertTrue(TestLexer.test('''"	'" ''', '''Unclosed String: 	'" ''', 362))

	def test_363(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 363))

	def test_364(self):
		self.assertTrue(TestLexer.test("8.886", "8.886,<EOF>", 364))

	def test_365(self):
		self.assertTrue(TestLexer.test('''## 05Zz2.*D''', '''<EOF>''', 365))

	def test_366(self):
		self.assertTrue(TestLexer.test("$Ntk@bWYH7", "Error Token $", 366))

	def test_367(self):
		self.assertTrue(TestLexer.test("c2gokeoN", "c2gokeoN,<EOF>", 367))

	def test_368(self):
		self.assertTrue(TestLexer.test("65", "65,<EOF>", 368))

	def test_369(self):
		self.assertTrue(TestLexer.test('''"'"S"''', '''\'"S,<EOF>''', 369))

	def test_370(self):
		self.assertTrue(TestLexer.test('''## f&:A''', '''<EOF>''', 370))

	def test_371(self):
		self.assertTrue(TestLexer.test("3.819e+20", "3.819e+20,<EOF>", 371))

	def test_372(self):
		self.assertTrue(TestLexer.test("YzHBrC", "YzHBrC,<EOF>", 372))

	def test_373(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 373))

	def test_374(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 374))

	def test_375(self):
		self.assertTrue(TestLexer.test('''"'"'"&{"''', '''\'"'"&{,<EOF>''', 375))

	def test_376(self):
		self.assertTrue(TestLexer.test('''## 9q{jO2Qq_''', '''<EOF>''', 376))

	def test_377(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 377))

	def test_378(self):
		self.assertTrue(TestLexer.test('''## fQ:vOfPzlnUwU$!/''', '''<EOF>''', 378))

	def test_379(self):
		self.assertTrue(TestLexer.test('''"V ''', '''Unclosed String: V ''', 379))

	def test_380(self):
		self.assertTrue(TestLexer.test("159", "159,<EOF>", 380))

	def test_381(self):
		self.assertTrue(TestLexer.test("H0pu", "H0pu,<EOF>", 381))

	def test_382(self):
		self.assertTrue(TestLexer.test('''## |7.Qr}7S/T)sh''', '''<EOF>''', 382))

	def test_383(self):
		self.assertTrue(TestLexer.test("5e+51", "5e+51,<EOF>", 383))

	def test_384(self):
		self.assertTrue(TestLexer.test("x2@8zriK", "x2,Error Token @", 384))

	def test_385(self):
		self.assertTrue(TestLexer.test("ufi66bA", "ufi66bA,<EOF>", 385))

	def test_386(self):
		self.assertTrue(TestLexer.test('''## KwZ+cf-4 !@(f`?e0VL`''', '''<EOF>''', 386))

	def test_387(self):
		self.assertTrue(TestLexer.test("441E+36", "441E+36,<EOF>", 387))

	def test_388(self):
		self.assertTrue(TestLexer.test('''## lS9ABlv2H8''', '''<EOF>''', 388))

	def test_389(self):
		self.assertTrue(TestLexer.test("nvkb^1", "nvkb,Error Token ^", 389))

	def test_390(self):
		self.assertTrue(TestLexer.test('''"'";'"'"'""''', '''\'";'"'"'",<EOF>''', 390))

	def test_391(self):
		self.assertTrue(TestLexer.test("YuDK", "YuDK,<EOF>", 391))

	def test_392(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 392))

	def test_393(self):
		self.assertTrue(TestLexer.test("$i1q8v", "Error Token $", 393))

	def test_394(self):
		self.assertTrue(TestLexer.test('''"^'"'"'": ''', '''Unclosed String: ^'"'"'": ''', 394))

	def test_395(self):
		self.assertTrue(TestLexer.test('''"2- ''', '''Unclosed String: 2- ''', 395))

	def test_396(self):
		self.assertTrue(TestLexer.test('''## S!o:Dj#''', '''<EOF>''', 396))

	def test_397(self):
		self.assertTrue(TestLexer.test("ysg7w&l", "ysg7w,Error Token &", 397))

	def test_398(self):
		self.assertTrue(TestLexer.test("84e-09", "84e-09,<EOF>", 398))

	def test_399(self):
		self.assertTrue(TestLexer.test('''"
f'"'""''', '''Unclosed String: ''', 399))

	def test_400(self):
		self.assertTrue(TestLexer.test("dG_UioXs@Y", "dG_UioXs,Error Token @", 400))

	def test_401(self):
		self.assertTrue(TestLexer.test("4e", "4,e,<EOF>", 401))

	def test_402(self):
		self.assertTrue(TestLexer.test("iO4", "iO4,<EOF>", 402))

	def test_403(self):
		self.assertTrue(TestLexer.test('''## .@R#/{JJ9K6''', '''<EOF>''', 403))

	def test_404(self):
		self.assertTrue(TestLexer.test("r$qa2r", "r,Error Token $", 404))

	def test_405(self):
		self.assertTrue(TestLexer.test('''## 5F+[^.ZB_-|l(4w''', '''<EOF>''', 405))

	def test_406(self):
		self.assertTrue(TestLexer.test('''## oC,O?n''', '''<EOF>''', 406))

	def test_407(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 407))

	def test_408(self):
		self.assertTrue(TestLexer.test("ewY", "ewY,<EOF>", 408))

	def test_409(self):
		self.assertTrue(TestLexer.test("935e-26", "935e-26,<EOF>", 409))

	def test_410(self):
		self.assertTrue(TestLexer.test("795e55", "795e55,<EOF>", 410))

	def test_411(self):
		self.assertTrue(TestLexer.test("5.016e+38", "5.016e+38,<EOF>", 411))

	def test_412(self):
		self.assertTrue(TestLexer.test('''##  Gl,w|=xJ8L`djR;''', '''<EOF>''', 412))

	def test_413(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 413))

	def test_414(self):
		self.assertTrue(TestLexer.test("&DU$9w", "Error Token &", 414))

	def test_415(self):
		self.assertTrue(TestLexer.test("IB^2CuVlP", "IB,Error Token ^", 415))

	def test_416(self):
		self.assertTrue(TestLexer.test("764E+82", "764E+82,<EOF>", 416))

	def test_417(self):
		self.assertTrue(TestLexer.test('''## ,L9g+r-k<R''', '''<EOF>''', 417))

	def test_418(self):
		self.assertTrue(TestLexer.test('''## y2vGrVleow*''', '''<EOF>''', 418))

	def test_419(self):
		self.assertTrue(TestLexer.test('''## N:.rJ(Ua''', '''<EOF>''', 419))

	def test_420(self):
		self.assertTrue(TestLexer.test("8.711e-74", "8.711e-74,<EOF>", 420))

	def test_421(self):
		self.assertTrue(TestLexer.test("PUde", "PUde,<EOF>", 421))

	def test_422(self):
		self.assertTrue(TestLexer.test('''"Q'" ''', '''Unclosed String: Q'" ''', 422))

	def test_423(self):
		self.assertTrue(TestLexer.test("yr", "yr,<EOF>", 423))

	def test_424(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 424))

	def test_425(self):
		self.assertTrue(TestLexer.test("PjGcRXf", "PjGcRXf,<EOF>", 425))

	def test_426(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 426))

	def test_427(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 427))

	def test_428(self):
		self.assertTrue(TestLexer.test('''"'"L"''', '''\'"L,<EOF>''', 428))

	def test_429(self):
		self.assertTrue(TestLexer.test("2.763e-49", "2.763e-49,<EOF>", 429))

	def test_430(self):
		self.assertTrue(TestLexer.test('''"'"'"'"H"''', '''\'"'"'"H,<EOF>''', 430))

	def test_431(self):
		self.assertTrue(TestLexer.test('''"G\\v'""''', '''Illegal Escape In String: G\\v''', 431))

	def test_432(self):
		self.assertTrue(TestLexer.test("@", "Error Token @", 432))

	def test_433(self):
		self.assertTrue(TestLexer.test("976e69", "976e69,<EOF>", 433))

	def test_434(self):
		self.assertTrue(TestLexer.test('''## 9U:aR''', '''<EOF>''', 434))

	def test_435(self):
		self.assertTrue(TestLexer.test("82.690e-02", "82.690e-02,<EOF>", 435))

	def test_436(self):
		self.assertTrue(TestLexer.test('''"\\x'"eQ'""''', '''Illegal Escape In String: \\x''', 436))

	def test_437(self):
		self.assertTrue(TestLexer.test('''"P\\k'""''', '''Illegal Escape In String: P\\k''', 437))

	def test_438(self):
		self.assertTrue(TestLexer.test('''"_K\\o'""''', '''Illegal Escape In String: _K\\o''', 438))

	def test_439(self):
		self.assertTrue(TestLexer.test('''## )Bw$2e1FF.z>$Q}{7''', '''<EOF>''', 439))

	def test_440(self):
		self.assertTrue(TestLexer.test("7.793", "7.793,<EOF>", 440))

	def test_441(self):
		self.assertTrue(TestLexer.test('''## Yq=Dp1Dd>mP''', '''<EOF>''', 441))

	def test_442(self):
		self.assertTrue(TestLexer.test('''## gM3''', '''<EOF>''', 442))

	def test_443(self):
		self.assertTrue(TestLexer.test('''"'"
=r"''', '''Unclosed String: '"''', 443))

	def test_444(self):
		self.assertTrue(TestLexer.test('''## 0$qM-KwcO*Z1T%w6|UU?''', '''<EOF>''', 444))

	def test_445(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 445))

	def test_446(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 446))

	def test_447(self):
		self.assertTrue(TestLexer.test("756.622E01", "756.622E01,<EOF>", 447))

	def test_448(self):
		self.assertTrue(TestLexer.test('''## ?1YhUzQ''', '''<EOF>''', 448))

	def test_449(self):
		self.assertTrue(TestLexer.test('''"'"c\\q'""''', '''Illegal Escape In String: '"c\\q''', 449))

	def test_450(self):
		self.assertTrue(TestLexer.test('''"'"
'"S'","''', '''Unclosed String: '"''', 450))

	def test_451(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 451))

	def test_452(self):
		self.assertTrue(TestLexer.test('''## 5XM_hxiP80''', '''<EOF>''', 452))

	def test_453(self):
		self.assertTrue(TestLexer.test("139.496", "139.496,<EOF>", 453))

	def test_454(self):
		self.assertTrue(TestLexer.test("Xd3h1", "Xd3h1,<EOF>", 454))

	def test_455(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 455))

	def test_456(self):
		self.assertTrue(TestLexer.test("92.697", "92.697,<EOF>", 456))

	def test_457(self):
		self.assertTrue(TestLexer.test('''## [n^{~on~ 8~V/Yj''', '''<EOF>''', 457))

	def test_458(self):
		self.assertTrue(TestLexer.test('''"4B'"'""''', '''4B'"'",<EOF>''', 458))

	def test_459(self):
		self.assertTrue(TestLexer.test('''"\\s'"'"'"y-"''', '''Illegal Escape In String: \\s''', 459))

	def test_460(self):
		self.assertTrue(TestLexer.test("16e30", "16e30,<EOF>", 460))

	def test_461(self):
		self.assertTrue(TestLexer.test("914e-18", "914e-18,<EOF>", 461))

	def test_462(self):
		self.assertTrue(TestLexer.test('''## &9clMMrXLzFAZ?''', '''<EOF>''', 462))

	def test_463(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 463))

	def test_464(self):
		self.assertTrue(TestLexer.test('''## EfS!M$0"l''', '''<EOF>''', 464))

	def test_465(self):
		self.assertTrue(TestLexer.test("8.266", "8.266,<EOF>", 465))

	def test_466(self):
		self.assertTrue(TestLexer.test('''"a\\z>'"'"'""''', '''Illegal Escape In String: a\\z''', 466))

	def test_467(self):
		self.assertTrue(TestLexer.test("52.525e-92", "52.525e-92,<EOF>", 467))

	def test_468(self):
		self.assertTrue(TestLexer.test('''##  Q;wiRL^@0dVRm''', '''<EOF>''', 468))

	def test_469(self):
		self.assertTrue(TestLexer.test("374.614", "374.614,<EOF>", 469))

	def test_470(self):
		self.assertTrue(TestLexer.test("YYyTmh51d", "YYyTmh51d,<EOF>", 470))

	def test_471(self):
		self.assertTrue(TestLexer.test('''## 1B  $r;V''', '''<EOF>''', 471))

	def test_472(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 472))

	def test_473(self):
		self.assertTrue(TestLexer.test("W9hmE_RaV", "W9hmE_RaV,<EOF>", 473))

	def test_474(self):
		self.assertTrue(TestLexer.test('''"\\k'"'";'""''', '''Illegal Escape In String: \\k''', 474))

	def test_475(self):
		self.assertTrue(TestLexer.test("87.191e+54", "87.191e+54,<EOF>", 475))

	def test_476(self):
		self.assertTrue(TestLexer.test("40.755e-18", "40.755e-18,<EOF>", 476))

	def test_477(self):
		self.assertTrue(TestLexer.test("xGVZ1$r&hE", "xGVZ1,Error Token $", 477))

	def test_478(self):
		self.assertTrue(TestLexer.test('''"'"w\\z'"'""''', '''Illegal Escape In String: '"w\\z''', 478))

	def test_479(self):
		self.assertTrue(TestLexer.test('''"V!\\k'"X"''', '''Illegal Escape In String: V!\\k''', 479))

	def test_480(self):
		self.assertTrue(TestLexer.test("Qo", "Qo,<EOF>", 480))

	def test_481(self):
		self.assertTrue(TestLexer.test("6.459", "6.459,<EOF>", 481))

	def test_482(self):
		self.assertTrue(TestLexer.test('''## t3Ku8oO|W''', '''<EOF>''', 482))

	def test_483(self):
		self.assertTrue(TestLexer.test("3v_T6eqdl^", "3,v_T6eqdl,Error Token ^", 483))

	def test_484(self):
		self.assertTrue(TestLexer.test("yfdQCBzic0", "yfdQCBzic0,<EOF>", 484))

	def test_485(self):
		self.assertTrue(TestLexer.test("m", "m,<EOF>", 485))

	def test_486(self):
		self.assertTrue(TestLexer.test("WaStt", "WaStt,<EOF>", 486))

	def test_487(self):
		self.assertTrue(TestLexer.test("91.579", "91.579,<EOF>", 487))

	def test_488(self):
		self.assertTrue(TestLexer.test("111", "111,<EOF>", 488))

	def test_489(self):
		self.assertTrue(TestLexer.test('''## )K`Zzc{i@9SWvU0''', '''<EOF>''', 489))

	def test_490(self):
		self.assertTrue(TestLexer.test("246.381e+75", "246.381e+75,<EOF>", 490))

	def test_491(self):
		self.assertTrue(TestLexer.test('''"sF'""''', '''sF'",<EOF>''', 491))

	def test_492(self):
		self.assertTrue(TestLexer.test("410E19", "410E19,<EOF>", 492))

	def test_493(self):
		self.assertTrue(TestLexer.test('''"'"\\y'""''', '''Illegal Escape In String: '"\\y''', 493))

	def test_494(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 494))

	def test_495(self):
		self.assertTrue(TestLexer.test("6LzF", "6,LzF,<EOF>", 495))

	def test_496(self):
		self.assertTrue(TestLexer.test("4e00", "4e00,<EOF>", 496))

	def test_497(self):
		self.assertTrue(TestLexer.test('''"'"5'"C"''', '''\'"5'"C,<EOF>''', 497))

	def test_498(self):
		self.assertTrue(TestLexer.test("nR", "nR,<EOF>", 498))

	def test_499(self):
		self.assertTrue(TestLexer.test('''"j2$\\e_7"''', '''Illegal Escape In String: j2$\\e''', 499))

	def test_500(self):
		self.assertTrue(TestLexer.test("yi^L1RcXKu", "yi,Error Token ^", 500))

	def test_501(self):
		self.assertTrue(TestLexer.test('''## } )$$yAimO7eX!''', '''<EOF>''', 501))

	def test_502(self):
		self.assertTrue(TestLexer.test("6.347E-09", "6.347E-09,<EOF>", 502))

	def test_503(self):
		self.assertTrue(TestLexer.test("991.075", "991.075,<EOF>", 503))

	def test_504(self):
		self.assertTrue(TestLexer.test('''## OhsYS!o1|&''', '''<EOF>''', 504))

	def test_505(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 505))

	def test_506(self):
		self.assertTrue(TestLexer.test("83e-99", "83e-99,<EOF>", 506))

	def test_507(self):
		self.assertTrue(TestLexer.test("GDH", "GDH,<EOF>", 507))

	def test_508(self):
		self.assertTrue(TestLexer.test('''"I8'"'""''', '''I8'"'",<EOF>''', 508))

	def test_509(self):
		self.assertTrue(TestLexer.test("702.531e-27", "702.531e-27,<EOF>", 509))

	def test_510(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 510))

	def test_511(self):
		self.assertTrue(TestLexer.test('''## HAD?eMIY.''', '''<EOF>''', 511))

	def test_512(self):
		self.assertTrue(TestLexer.test('''## s[#=33ueY#MpQ{[f"XB]''', '''<EOF>''', 512))

	def test_513(self):
		self.assertTrue(TestLexer.test('''## &a9E"P,Q''', '''<EOF>''', 513))

	def test_514(self):
		self.assertTrue(TestLexer.test("863.206", "863.206,<EOF>", 514))

	def test_515(self):
		self.assertTrue(TestLexer.test('''## {9Lkc7;wS{}p?exin3''', '''<EOF>''', 515))

	def test_516(self):
		self.assertTrue(TestLexer.test('''"\\a'""''', '''Illegal Escape In String: \\a''', 516))

	def test_517(self):
		self.assertTrue(TestLexer.test('''"#H'" ''', '''Unclosed String: #H'" ''', 517))

	def test_518(self):
		self.assertTrue(TestLexer.test("cu5el", "cu5el,<EOF>", 518))

	def test_519(self):
		self.assertTrue(TestLexer.test("33E+79", "33E+79,<EOF>", 519))

	def test_520(self):
		self.assertTrue(TestLexer.test("403e+68", "403e+68,<EOF>", 520))

	def test_521(self):
		self.assertTrue(TestLexer.test("F8", "F8,<EOF>", 521))

	def test_522(self):
		self.assertTrue(TestLexer.test("kTC&ZgZE", "kTC,Error Token &", 522))

	def test_523(self):
		self.assertTrue(TestLexer.test("73OOdEXi", "73,OOdEXi,<EOF>", 523))

	def test_524(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 524))

	def test_525(self):
		self.assertTrue(TestLexer.test("4.183e+33", "4.183e+33,<EOF>", 525))

	def test_526(self):
		self.assertTrue(TestLexer.test('''"^'"'""''', '''^'"'",<EOF>''', 526))

	def test_527(self):
		self.assertTrue(TestLexer.test('''"qiI%"''', '''qiI%,<EOF>''', 527))

	def test_528(self):
		self.assertTrue(TestLexer.test("646.620e95", "646.620e95,<EOF>", 528))

	def test_529(self):
		self.assertTrue(TestLexer.test("ajLK", "ajLK,<EOF>", 529))

	def test_530(self):
		self.assertTrue(TestLexer.test('''## %L(m6=JLRAn;K''', '''<EOF>''', 530))

	def test_531(self):
		self.assertTrue(TestLexer.test("279.743e+35", "279.743e+35,<EOF>", 531))

	def test_532(self):
		self.assertTrue(TestLexer.test("96.433E-24", "96.433E-24,<EOF>", 532))

	def test_533(self):
		self.assertTrue(TestLexer.test("5Bn", "5,Bn,<EOF>", 533))

	def test_534(self):
		self.assertTrue(TestLexer.test("8qy", "8,qy,<EOF>", 534))

	def test_535(self):
		self.assertTrue(TestLexer.test("3.660", "3.660,<EOF>", 535))

	def test_536(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 536))

	def test_537(self):
		self.assertTrue(TestLexer.test("Lg&T9", "Lg,Error Token &", 537))

	def test_538(self):
		self.assertTrue(TestLexer.test("321E18", "321E18,<EOF>", 538))

	def test_539(self):
		self.assertTrue(TestLexer.test("#CxB", "Error Token #", 539))

	def test_540(self):
		self.assertTrue(TestLexer.test('''"B\\y]"''', '''Illegal Escape In String: B\\y''', 540))

	def test_541(self):
		self.assertTrue(TestLexer.test("949.734E+89", "949.734E+89,<EOF>", 541))

	def test_542(self):
		self.assertTrue(TestLexer.test("mek3JwcQ5k", "mek3JwcQ5k,<EOF>", 542))

	def test_543(self):
		self.assertTrue(TestLexer.test('''## vt''', '''<EOF>''', 543))

	def test_544(self):
		self.assertTrue(TestLexer.test("0e+03", "0e+03,<EOF>", 544))

	def test_545(self):
		self.assertTrue(TestLexer.test('''"	\\i="''', '''Illegal Escape In String: 	\\i''', 545))

	def test_546(self):
		self.assertTrue(TestLexer.test('''## >m_^Mf''', '''<EOF>''', 546))

	def test_547(self):
		self.assertTrue(TestLexer.test("I5", "I5,<EOF>", 547))

	def test_548(self):
		self.assertTrue(TestLexer.test('''## BsVS%1]''', '''<EOF>''', 548))

	def test_549(self):
		self.assertTrue(TestLexer.test("47.457e56", "47.457e56,<EOF>", 549))

	def test_550(self):
		self.assertTrue(TestLexer.test('''## <5ETk}3*NBHQRDY2j"vq''', '''<EOF>''', 550))

	def test_551(self):
		self.assertTrue(TestLexer.test('''"
`g'""''', '''Unclosed String: ''', 551))

	def test_552(self):
		self.assertTrue(TestLexer.test('''"'"'"g\\lD'""''', '''Illegal Escape In String: '"'"g\\l''', 552))

	def test_553(self):
		self.assertTrue(TestLexer.test('''"
'"'""''', '''Unclosed String: ''', 553))

	def test_554(self):
		self.assertTrue(TestLexer.test("_W2", "_W2,<EOF>", 554))

	def test_555(self):
		self.assertTrue(TestLexer.test("Kdgn", "Kdgn,<EOF>", 555))

	def test_556(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 556))

	def test_557(self):
		self.assertTrue(TestLexer.test("87.432", "87.432,<EOF>", 557))

	def test_558(self):
		self.assertTrue(TestLexer.test("nA", "nA,<EOF>", 558))

	def test_559(self):
		self.assertTrue(TestLexer.test("K", "K,<EOF>", 559))

	def test_560(self):
		self.assertTrue(TestLexer.test('''## s{^o(FM+Lz''', '''<EOF>''', 560))

	def test_561(self):
		self.assertTrue(TestLexer.test('''"`'""''', '''`'",<EOF>''', 561))

	def test_562(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 562))

	def test_563(self):
		self.assertTrue(TestLexer.test('''## zQ+U31C''', '''<EOF>''', 563))

	def test_564(self):
		self.assertTrue(TestLexer.test("43.839E+17", "43.839E+17,<EOF>", 564))

	def test_565(self):
		self.assertTrue(TestLexer.test('''## AFb|gaw''', '''<EOF>''', 565))

	def test_566(self):
		self.assertTrue(TestLexer.test("8fc1E0", "8,fc1E0,<EOF>", 566))

	def test_567(self):
		self.assertTrue(TestLexer.test('''"'" '"'"'""''', '''\'" '"'"'",<EOF>''', 567))

	def test_568(self):
		self.assertTrue(TestLexer.test("ve^a1s1D", "ve,Error Token ^", 568))

	def test_569(self):
		self.assertTrue(TestLexer.test("956", "956,<EOF>", 569))

	def test_570(self):
		self.assertTrue(TestLexer.test("936E+82", "936E+82,<EOF>", 570))

	def test_571(self):
		self.assertTrue(TestLexer.test('''"\\j@$"''', '''Illegal Escape In String: \\j''', 571))

	def test_572(self):
		self.assertTrue(TestLexer.test("IuO", "IuO,<EOF>", 572))

	def test_573(self):
		self.assertTrue(TestLexer.test('''## #`I''', '''<EOF>''', 573))

	def test_574(self):
		self.assertTrue(TestLexer.test('''"'"'"\\w<'"'""''', '''Illegal Escape In String: '"'"\\w''', 574))

	def test_575(self):
		self.assertTrue(TestLexer.test("1E33", "1E33,<EOF>", 575))

	def test_576(self):
		self.assertTrue(TestLexer.test("36E+06", "36E+06,<EOF>", 576))

	def test_577(self):
		self.assertTrue(TestLexer.test('''## qC+Rb3b.J{Zb*l9''', '''<EOF>''', 577))

	def test_578(self):
		self.assertTrue(TestLexer.test("76.023E78", "76.023E78,<EOF>", 578))

	def test_579(self):
		self.assertTrue(TestLexer.test('''"D'"'"'""''', '''D'"'"'",<EOF>''', 579))

	def test_580(self):
		self.assertTrue(TestLexer.test("9NEVw1", "9,NEVw1,<EOF>", 580))

	def test_581(self):
		self.assertTrue(TestLexer.test("4.548", "4.548,<EOF>", 581))

	def test_582(self):
		self.assertTrue(TestLexer.test("LjTnpV", "LjTnpV,<EOF>", 582))

	def test_583(self):
		self.assertTrue(TestLexer.test('''"\\i'"%'"o'""''', '''Illegal Escape In String: \\i''', 583))

	def test_584(self):
		self.assertTrue(TestLexer.test("3.330", "3.330,<EOF>", 584))

	def test_585(self):
		self.assertTrue(TestLexer.test('''## 2(2~3:0e iS6u:}91''', '''<EOF>''', 585))

	def test_586(self):
		self.assertTrue(TestLexer.test("g$k&QRy", "g,Error Token $", 586))

	def test_587(self):
		self.assertTrue(TestLexer.test("323", "323,<EOF>", 587))

	def test_588(self):
		self.assertTrue(TestLexer.test("44.654", "44.654,<EOF>", 588))

	def test_589(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 589))

	def test_590(self):
		self.assertTrue(TestLexer.test("KaqSk", "KaqSk,<EOF>", 590))

	def test_591(self):
		self.assertTrue(TestLexer.test('''## 1A&0(v0"V~:;I>''', '''<EOF>''', 591))

	def test_592(self):
		self.assertTrue(TestLexer.test('''## Ygk9''', '''<EOF>''', 592))

	def test_593(self):
		self.assertTrue(TestLexer.test('''## E_)*O{''', '''<EOF>''', 593))

	def test_594(self):
		self.assertTrue(TestLexer.test("h4d^W", "h4d,Error Token ^", 594))

	def test_595(self):
		self.assertTrue(TestLexer.test("NNiguu", "NNiguu,<EOF>", 595))

	def test_596(self):
		self.assertTrue(TestLexer.test("510", "510,<EOF>", 596))

	def test_597(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 597))

	def test_598(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 598))

	def test_599(self):
		self.assertTrue(TestLexer.test('''## IQ$$C''', '''<EOF>''', 599))

	def test_600(self):
		self.assertTrue(TestLexer.test('''## W''', '''<EOF>''', 600))

	def test_601(self):
		self.assertTrue(TestLexer.test("86", "86,<EOF>", 601))

	def test_602(self):
		self.assertTrue(TestLexer.test("v", "v,<EOF>", 602))

	def test_603(self):
		self.assertTrue(TestLexer.test("Q", "Q,<EOF>", 603))

	def test_604(self):
		self.assertTrue(TestLexer.test("20e-10", "20e-10,<EOF>", 604))

	def test_605(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 605))

	def test_606(self):
		self.assertTrue(TestLexer.test('''"'"\\o'""''', '''Illegal Escape In String: '"\\o''', 606))

	def test_607(self):
		self.assertTrue(TestLexer.test("881.360", "881.360,<EOF>", 607))

	def test_608(self):
		self.assertTrue(TestLexer.test("Te1bE", "Te1bE,<EOF>", 608))

	def test_609(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 609))

	def test_610(self):
		self.assertTrue(TestLexer.test('''"sbwJ"''', '''sbwJ,<EOF>''', 610))

	def test_611(self):
		self.assertTrue(TestLexer.test('''## +$G''', '''<EOF>''', 611))

	def test_612(self):
		self.assertTrue(TestLexer.test('''"84 ''', '''Unclosed String: 84 ''', 612))

	def test_613(self):
		self.assertTrue(TestLexer.test("rXW7w@O2BI", "rXW7w,Error Token @", 613))

	def test_614(self):
		self.assertTrue(TestLexer.test("W9P", "W9P,<EOF>", 614))

	def test_615(self):
		self.assertTrue(TestLexer.test("714.075e-74", "714.075e-74,<EOF>", 615))

	def test_616(self):
		self.assertTrue(TestLexer.test('''## Nv(sW#ZVZ''', '''<EOF>''', 616))

	def test_617(self):
		self.assertTrue(TestLexer.test('''## {[z$+ZIDQkJNC8pDiL.''', '''<EOF>''', 617))

	def test_618(self):
		self.assertTrue(TestLexer.test('''## M<d0$QKv''', '''<EOF>''', 618))

	def test_619(self):
		self.assertTrue(TestLexer.test("5R7i", "5,R7i,<EOF>", 619))

	def test_620(self):
		self.assertTrue(TestLexer.test("492", "492,<EOF>", 620))

	def test_621(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 621))

	def test_622(self):
		self.assertTrue(TestLexer.test("bX49^$2$#M", "bX49,Error Token ^", 622))

	def test_623(self):
		self.assertTrue(TestLexer.test("Vm", "Vm,<EOF>", 623))

	def test_624(self):
		self.assertTrue(TestLexer.test("1.696", "1.696,<EOF>", 624))

	def test_625(self):
		self.assertTrue(TestLexer.test('''## _U''', '''<EOF>''', 625))

	def test_626(self):
		self.assertTrue(TestLexer.test('''## iecS4d?''', '''<EOF>''', 626))

	def test_627(self):
		self.assertTrue(TestLexer.test("724E+97", "724E+97,<EOF>", 627))

	def test_628(self):
		self.assertTrue(TestLexer.test('''"'"'" ''', '''Unclosed String: '"'" ''', 628))

	def test_629(self):
		self.assertTrue(TestLexer.test('''## C>6''', '''<EOF>''', 629))

	def test_630(self):
		self.assertTrue(TestLexer.test('''## FmpwesF-c?"{r/=4,{br''', '''<EOF>''', 630))

	def test_631(self):
		self.assertTrue(TestLexer.test("V&8Io", "V,Error Token &", 631))

	def test_632(self):
		self.assertTrue(TestLexer.test('''## 6|u]''', '''<EOF>''', 632))

	def test_633(self):
		self.assertTrue(TestLexer.test('''## E)<N*}O/XJYbzcJ*+O}-''', '''<EOF>''', 633))

	def test_634(self):
		self.assertTrue(TestLexer.test("jNdC94mVE", "jNdC94mVE,<EOF>", 634))

	def test_635(self):
		self.assertTrue(TestLexer.test("CS", "CS,<EOF>", 635))

	def test_636(self):
		self.assertTrue(TestLexer.test("672.079e+26", "672.079e+26,<EOF>", 636))

	def test_637(self):
		self.assertTrue(TestLexer.test("HodmXVafY", "HodmXVafY,<EOF>", 637))

	def test_638(self):
		self.assertTrue(TestLexer.test("m3", "m3,<EOF>", 638))

	def test_639(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 639))

	def test_640(self):
		self.assertTrue(TestLexer.test("8.044e+52", "8.044e+52,<EOF>", 640))

	def test_641(self):
		self.assertTrue(TestLexer.test("8m#A9", "8,m,Error Token #", 641))

	def test_642(self):
		self.assertTrue(TestLexer.test('''"c'"
\\h'"'""''', '''Unclosed String: c'"''', 642))

	def test_643(self):
		self.assertTrue(TestLexer.test("qB", "qB,<EOF>", 643))

	def test_644(self):
		self.assertTrue(TestLexer.test('''"'"'"N ''', '''Unclosed String: '"'"N ''', 644))

	def test_645(self):
		self.assertTrue(TestLexer.test("1.949", "1.949,<EOF>", 645))

	def test_646(self):
		self.assertTrue(TestLexer.test('''"'"'"'""''', '''\'"'"'",<EOF>''', 646))

	def test_647(self):
		self.assertTrue(TestLexer.test("639e+69", "639e+69,<EOF>", 647))

	def test_648(self):
		self.assertTrue(TestLexer.test("1.648E77", "1.648E77,<EOF>", 648))

	def test_649(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 649))

	def test_650(self):
		self.assertTrue(TestLexer.test("B", "B,<EOF>", 650))

	def test_651(self):
		self.assertTrue(TestLexer.test("#3@d7ISqke", "Error Token #", 651))

	def test_652(self):
		self.assertTrue(TestLexer.test('''"\\ym"''', '''Illegal Escape In String: \\y''', 652))

	def test_653(self):
		self.assertTrue(TestLexer.test("889.579", "889.579,<EOF>", 653))

	def test_654(self):
		self.assertTrue(TestLexer.test('''"tL"''', '''tL,<EOF>''', 654))

	def test_655(self):
		self.assertTrue(TestLexer.test('''## zCr}p5kdh qC[>[V[''', '''<EOF>''', 655))

	def test_656(self):
		self.assertTrue(TestLexer.test('''## IM5Aaj2u|e1@[!''', '''<EOF>''', 656))

	def test_657(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 657))

	def test_658(self):
		self.assertTrue(TestLexer.test("DrSx5pJXM$", "DrSx5pJXM,Error Token $", 658))

	def test_659(self):
		self.assertTrue(TestLexer.test("&", "Error Token &", 659))

	def test_660(self):
		self.assertTrue(TestLexer.test('''## %;a^^A*=2LNan! ]z,bR''', '''<EOF>''', 660))

	def test_661(self):
		self.assertTrue(TestLexer.test("vu", "vu,<EOF>", 661))

	def test_662(self):
		self.assertTrue(TestLexer.test("329.401e71", "329.401e71,<EOF>", 662))

	def test_663(self):
		self.assertTrue(TestLexer.test("2_H7To", "2,_H7To,<EOF>", 663))

	def test_664(self):
		self.assertTrue(TestLexer.test('''## 4ns?jam~X''', '''<EOF>''', 664))

	def test_665(self):
		self.assertTrue(TestLexer.test("2e+46", "2e+46,<EOF>", 665))

	def test_666(self):
		self.assertTrue(TestLexer.test('''"Wb'"f'""''', '''Wb'"f'",<EOF>''', 666))

	def test_667(self):
		self.assertTrue(TestLexer.test('''"'"P\\m'"'""''', '''Illegal Escape In String: '"P\\m''', 667))

	def test_668(self):
		self.assertTrue(TestLexer.test("398", "398,<EOF>", 668))

	def test_669(self):
		self.assertTrue(TestLexer.test("QLF", "QLF,<EOF>", 669))

	def test_670(self):
		self.assertTrue(TestLexer.test("6NY8B&Ny^", "6,NY8B,Error Token &", 670))

	def test_671(self):
		self.assertTrue(TestLexer.test("9Lo6", "9,Lo6,<EOF>", 671))

	def test_672(self):
		self.assertTrue(TestLexer.test("79e90", "79e90,<EOF>", 672))

	def test_673(self):
		self.assertTrue(TestLexer.test("gRP$", "gRP,Error Token $", 673))

	def test_674(self):
		self.assertTrue(TestLexer.test('''## H!ZgGy+b{QghVb|,''', '''<EOF>''', 674))

	def test_675(self):
		self.assertTrue(TestLexer.test('''"\\aD|"''', '''Illegal Escape In String: \\a''', 675))

	def test_676(self):
		self.assertTrue(TestLexer.test('''"G'"t
'""''', '''Unclosed String: G'"t''', 676))

	def test_677(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 677))

	def test_678(self):
		self.assertTrue(TestLexer.test('''"c"''', '''c,<EOF>''', 678))

	def test_679(self):
		self.assertTrue(TestLexer.test('''"u"''', '''u,<EOF>''', 679))

	def test_680(self):
		self.assertTrue(TestLexer.test("uE", "uE,<EOF>", 680))

	def test_681(self):
		self.assertTrue(TestLexer.test('''## :3},''', '''<EOF>''', 681))

	def test_682(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 682))

	def test_683(self):
		self.assertTrue(TestLexer.test("86.705", "86.705,<EOF>", 683))

	def test_684(self):
		self.assertTrue(TestLexer.test('''## :pO/gZ"Sa-Y.d.DLp6+''', '''<EOF>''', 684))

	def test_685(self):
		self.assertTrue(TestLexer.test("Nn", "Nn,<EOF>", 685))

	def test_686(self):
		self.assertTrue(TestLexer.test('''"
U"''', '''Unclosed String: ''', 686))

	def test_687(self):
		self.assertTrue(TestLexer.test('''## ,s!v;?1Sb;/I|z6.~xd''', '''<EOF>''', 687))

	def test_688(self):
		self.assertTrue(TestLexer.test('''## fh4n-t-WiB^H"@=DNO''', '''<EOF>''', 688))

	def test_689(self):
		self.assertTrue(TestLexer.test("7.832E+70", "7.832E+70,<EOF>", 689))

	def test_690(self):
		self.assertTrue(TestLexer.test("31e75", "31e75,<EOF>", 690))

	def test_691(self):
		self.assertTrue(TestLexer.test('''## b9yv-<p''', '''<EOF>''', 691))

	def test_692(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 692))

	def test_693(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 693))

	def test_694(self):
		self.assertTrue(TestLexer.test("#H@g4_", "Error Token #", 694))

	def test_695(self):
		self.assertTrue(TestLexer.test("168.938", "168.938,<EOF>", 695))

	def test_696(self):
		self.assertTrue(TestLexer.test("3.949", "3.949,<EOF>", 696))

	def test_697(self):
		self.assertTrue(TestLexer.test('''"\\j'"@"''', '''Illegal Escape In String: \\j''', 697))

	def test_698(self):
		self.assertTrue(TestLexer.test("@80mwH", "Error Token @", 698))

	def test_699(self):
		self.assertTrue(TestLexer.test("PNjY88UQD", "PNjY88UQD,<EOF>", 699))

	def test_700(self):
		self.assertTrue(TestLexer.test('''## v;z''', '''<EOF>''', 700))

	def test_701(self):
		self.assertTrue(TestLexer.test("2.345", "2.345,<EOF>", 701))

	def test_702(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 702))

	def test_703(self):
		self.assertTrue(TestLexer.test("2kOL", "2,kOL,<EOF>", 703))

	def test_704(self):
		self.assertTrue(TestLexer.test("26.865", "26.865,<EOF>", 704))

	def test_705(self):
		self.assertTrue(TestLexer.test("pZaZ^&i", "pZaZ,Error Token ^", 705))

	def test_706(self):
		self.assertTrue(TestLexer.test("8.652E+38", "8.652E+38,<EOF>", 706))

	def test_707(self):
		self.assertTrue(TestLexer.test('''## XPIEBuw''', '''<EOF>''', 707))

	def test_708(self):
		self.assertTrue(TestLexer.test("5E+18", "5E+18,<EOF>", 708))

	def test_709(self):
		self.assertTrue(TestLexer.test('''"'""''', '''\'",<EOF>''', 709))

	def test_710(self):
		self.assertTrue(TestLexer.test('''## q-#r''', '''<EOF>''', 710))

	def test_711(self):
		self.assertTrue(TestLexer.test("fk8kJmx@", "fk8kJmx,Error Token @", 711))

	def test_712(self):
		self.assertTrue(TestLexer.test("24.759E-77", "24.759E-77,<EOF>", 712))

	def test_713(self):
		self.assertTrue(TestLexer.test('''## Lhx<P''', '''<EOF>''', 713))

	def test_714(self):
		self.assertTrue(TestLexer.test("bMC_pT", "bMC_pT,<EOF>", 714))

	def test_715(self):
		self.assertTrue(TestLexer.test('''"\\oS"''', '''Illegal Escape In String: \\o''', 715))

	def test_716(self):
		self.assertTrue(TestLexer.test('''"mI'" ''', '''Unclosed String: mI'" ''', 716))

	def test_717(self):
		self.assertTrue(TestLexer.test("&dn", "Error Token &", 717))

	def test_718(self):
		self.assertTrue(TestLexer.test("10.279", "10.279,<EOF>", 718))

	def test_719(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 719))

	def test_720(self):
		self.assertTrue(TestLexer.test('''"'"'"v"''', '''\'"'"v,<EOF>''', 720))

	def test_721(self):
		self.assertTrue(TestLexer.test("19E+60", "19E+60,<EOF>", 721))

	def test_722(self):
		self.assertTrue(TestLexer.test('''## KT:mHB''', '''<EOF>''', 722))

	def test_723(self):
		self.assertTrue(TestLexer.test('''## u5Aniu)DKCy5hp[8kOG''', '''<EOF>''', 723))

	def test_724(self):
		self.assertTrue(TestLexer.test("kue#$u4", "kue,Error Token #", 724))

	def test_725(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 725))

	def test_726(self):
		self.assertTrue(TestLexer.test("7W3", "7,W3,<EOF>", 726))

	def test_727(self):
		self.assertTrue(TestLexer.test("20E-62", "20E-62,<EOF>", 727))

	def test_728(self):
		self.assertTrue(TestLexer.test("QgntHWr", "QgntHWr,<EOF>", 728))

	def test_729(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'""''', '''\'"'"'"'",<EOF>''', 729))

	def test_730(self):
		self.assertTrue(TestLexer.test("Kfam^YpsQ9", "Kfam,Error Token ^", 730))

	def test_731(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 731))

	def test_732(self):
		self.assertTrue(TestLexer.test("6pI8$Mk88", "6,pI8,Error Token $", 732))

	def test_733(self):
		self.assertTrue(TestLexer.test("Ti", "Ti,<EOF>", 733))

	def test_734(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 734))

	def test_735(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 735))

	def test_736(self):
		self.assertTrue(TestLexer.test("gd#B&TK9", "gd,Error Token #", 736))

	def test_737(self):
		self.assertTrue(TestLexer.test("36e+78", "36e+78,<EOF>", 737))

	def test_738(self):
		self.assertTrue(TestLexer.test("7qJB", "7,qJB,<EOF>", 738))

	def test_739(self):
		self.assertTrue(TestLexer.test('''## J''', '''<EOF>''', 739))

	def test_740(self):
		self.assertTrue(TestLexer.test("08eCFonII", "08,eCFonII,<EOF>", 740))

	def test_741(self):
		self.assertTrue(TestLexer.test("6.119", "6.119,<EOF>", 741))

	def test_742(self):
		self.assertTrue(TestLexer.test('''## t"[md=-AYF-''', '''<EOF>''', 742))

	def test_743(self):
		self.assertTrue(TestLexer.test("hsM", "hsM,<EOF>", 743))

	def test_744(self):
		self.assertTrue(TestLexer.test('''"t.z ''', '''Unclosed String: t.z ''', 744))

	def test_745(self):
		self.assertTrue(TestLexer.test("4.518E-06", "4.518E-06,<EOF>", 745))

	def test_746(self):
		self.assertTrue(TestLexer.test('''## 5{`E/}''', '''<EOF>''', 746))

	def test_747(self):
		self.assertTrue(TestLexer.test('''"9'"\\q'""''', '''Illegal Escape In String: 9'"\\q''', 747))

	def test_748(self):
		self.assertTrue(TestLexer.test("j01", "j01,<EOF>", 748))

	def test_749(self):
		self.assertTrue(TestLexer.test('''## CJup]n Tx''', '''<EOF>''', 749))

	def test_750(self):
		self.assertTrue(TestLexer.test('''## 1+YU3{L)49bBPm[I''', '''<EOF>''', 750))

	def test_751(self):
		self.assertTrue(TestLexer.test("BXZnx0Re", "BXZnx0Re,<EOF>", 751))

	def test_752(self):
		self.assertTrue(TestLexer.test('''## uC/K;p{b''', '''<EOF>''', 752))

	def test_753(self):
		self.assertTrue(TestLexer.test("9.582E+74", "9.582E+74,<EOF>", 753))

	def test_754(self):
		self.assertTrue(TestLexer.test('''"\\p'""''', '''Illegal Escape In String: \\p''', 754))

	def test_755(self):
		self.assertTrue(TestLexer.test("RJ56y8", "RJ56y8,<EOF>", 755))

	def test_756(self):
		self.assertTrue(TestLexer.test('''## :!_$)CZhwD,21i0z''', '''<EOF>''', 756))

	def test_757(self):
		self.assertTrue(TestLexer.test('''## 4o2 HBPS|+''', '''<EOF>''', 757))

	def test_758(self):
		self.assertTrue(TestLexer.test("497.953E19", "497.953E19,<EOF>", 758))

	def test_759(self):
		self.assertTrue(TestLexer.test("450E33", "450E33,<EOF>", 759))

	def test_760(self):
		self.assertTrue(TestLexer.test("122.383e-86", "122.383e-86,<EOF>", 760))

	def test_761(self):
		self.assertTrue(TestLexer.test("49.566E63", "49.566E63,<EOF>", 761))

	def test_762(self):
		self.assertTrue(TestLexer.test("3.397", "3.397,<EOF>", 762))

	def test_763(self):
		self.assertTrue(TestLexer.test('''## GeVXCo[qOfY6''', '''<EOF>''', 763))

	def test_764(self):
		self.assertTrue(TestLexer.test('''">nV'"? ''', '''Unclosed String: >nV'"? ''', 764))

	def test_765(self):
		self.assertTrue(TestLexer.test('''"'"'"'"\\j'"'""''', '''Illegal Escape In String: '"'"'"\\j''', 765))

	def test_766(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 766))

	def test_767(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 767))

	def test_768(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 768))

	def test_769(self):
		self.assertTrue(TestLexer.test('''## i4D''', '''<EOF>''', 769))

	def test_770(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 770))

	def test_771(self):
		self.assertTrue(TestLexer.test('''## qUf&yW{1k3p9X;96,aHo''', '''<EOF>''', 771))

	def test_772(self):
		self.assertTrue(TestLexer.test('''"'"'"^'" ''', '''Unclosed String: '"'"^'" ''', 772))

	def test_773(self):
		self.assertTrue(TestLexer.test('''## :?:(BI!g<TOr|!1o''', '''<EOF>''', 773))

	def test_774(self):
		self.assertTrue(TestLexer.test('''## `=<b*j2N4$L"+NB`:R$''', '''<EOF>''', 774))

	def test_775(self):
		self.assertTrue(TestLexer.test('''## 9l)''', '''<EOF>''', 775))

	def test_776(self):
		self.assertTrue(TestLexer.test("mdFVgd9", "mdFVgd9,<EOF>", 776))

	def test_777(self):
		self.assertTrue(TestLexer.test("1W", "1,W,<EOF>", 777))

	def test_778(self):
		self.assertTrue(TestLexer.test("94", "94,<EOF>", 778))

	def test_779(self):
		self.assertTrue(TestLexer.test('''## (t&g!`768jlk''', '''<EOF>''', 779))

	def test_780(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 780))

	def test_781(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 781))

	def test_782(self):
		self.assertTrue(TestLexer.test("zkjI0etair", "zkjI0etair,<EOF>", 782))

	def test_783(self):
		self.assertTrue(TestLexer.test('''## o.jIf''', '''<EOF>''', 783))

	def test_784(self):
		self.assertTrue(TestLexer.test("OSikg$0bBV", "OSikg,Error Token $", 784))

	def test_785(self):
		self.assertTrue(TestLexer.test('''"b\\pB/'""''', '''Illegal Escape In String: b\\p''', 785))

	def test_786(self):
		self.assertTrue(TestLexer.test("43.675E+85", "43.675E+85,<EOF>", 786))

	def test_787(self):
		self.assertTrue(TestLexer.test('''## ,t(ND%0C7ubW [''', '''<EOF>''', 787))

	def test_788(self):
		self.assertTrue(TestLexer.test("gCS0h3n", "gCS0h3n,<EOF>", 788))

	def test_789(self):
		self.assertTrue(TestLexer.test("O@", "O,Error Token @", 789))

	def test_790(self):
		self.assertTrue(TestLexer.test('''## _*o=>h''', '''<EOF>''', 790))

	def test_791(self):
		self.assertTrue(TestLexer.test("d49vY3k0u", "d49vY3k0u,<EOF>", 791))

	def test_792(self):
		self.assertTrue(TestLexer.test('''## ++Gp8ZgjoCjOBe_''', '''<EOF>''', 792))

	def test_793(self):
		self.assertTrue(TestLexer.test('''"8sz"''', '''8sz,<EOF>''', 793))

	def test_794(self):
		self.assertTrue(TestLexer.test("61.693E-25", "61.693E-25,<EOF>", 794))

	def test_795(self):
		self.assertTrue(TestLexer.test('''"3'""''', '''3'",<EOF>''', 795))

	def test_796(self):
		self.assertTrue(TestLexer.test("86e64", "86e64,<EOF>", 796))

	def test_797(self):
		self.assertTrue(TestLexer.test("3k", "3,k,<EOF>", 797))

	def test_798(self):
		self.assertTrue(TestLexer.test("j", "j,<EOF>", 798))

	def test_799(self):
		self.assertTrue(TestLexer.test('''"\\a'""''', '''Illegal Escape In String: \\a''', 799))

	def test_800(self):
		self.assertTrue(TestLexer.test("@iWsoa52", "Error Token @", 800))

	def test_801(self):
		self.assertTrue(TestLexer.test("fQwbEgGy", "fQwbEgGy,<EOF>", 801))

	def test_802(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 802))

	def test_803(self):
		self.assertTrue(TestLexer.test("wxP4CGFJ", "wxP4CGFJ,<EOF>", 803))

	def test_804(self):
		self.assertTrue(TestLexer.test("77", "77,<EOF>", 804))

	def test_805(self):
		self.assertTrue(TestLexer.test('''"\\v'""''', '''Illegal Escape In String: \\v''', 805))

	def test_806(self):
		self.assertTrue(TestLexer.test('''## X[ED,zP2L''', '''<EOF>''', 806))

	def test_807(self):
		self.assertTrue(TestLexer.test('''"Ka"''', '''Ka,<EOF>''', 807))

	def test_808(self):
		self.assertTrue(TestLexer.test("70e-28", "70e-28,<EOF>", 808))

	def test_809(self):
		self.assertTrue(TestLexer.test("3", "3,<EOF>", 809))

	def test_810(self):
		self.assertTrue(TestLexer.test('''## g~O%Iy9G''', '''<EOF>''', 810))

	def test_811(self):
		self.assertTrue(TestLexer.test('''## MMFRr2 H>X''', '''<EOF>''', 811))

	def test_812(self):
		self.assertTrue(TestLexer.test('''## PpEKi:IrSg=a8g38V2''', '''<EOF>''', 812))

	def test_813(self):
		self.assertTrue(TestLexer.test("pcvy2l", "pcvy2l,<EOF>", 813))

	def test_814(self):
		self.assertTrue(TestLexer.test('''## I=Pdj''', '''<EOF>''', 814))

	def test_815(self):
		self.assertTrue(TestLexer.test("1.802", "1.802,<EOF>", 815))

	def test_816(self):
		self.assertTrue(TestLexer.test('''## ,5*Ao%stV!Y2''', '''<EOF>''', 816))

	def test_817(self):
		self.assertTrue(TestLexer.test("0EjcPC_Gys", "0,EjcPC_Gys,<EOF>", 817))

	def test_818(self):
		self.assertTrue(TestLexer.test("49.973e+54", "49.973e+54,<EOF>", 818))

	def test_819(self):
		self.assertTrue(TestLexer.test('''## 2Ra$XH''', '''<EOF>''', 819))

	def test_820(self):
		self.assertTrue(TestLexer.test('''"'"'"'"'" ''', '''Unclosed String: '"'"'"'" ''', 820))

	def test_821(self):
		self.assertTrue(TestLexer.test('''"'"8\\ct"''', '''Illegal Escape In String: '"8\\c''', 821))

	def test_822(self):
		self.assertTrue(TestLexer.test("8V_G", "8,V_G,<EOF>", 822))

	def test_823(self):
		self.assertTrue(TestLexer.test('''## H//jmj''', '''<EOF>''', 823))

	def test_824(self):
		self.assertTrue(TestLexer.test("27e+85", "27e+85,<EOF>", 824))

	def test_825(self):
		self.assertTrue(TestLexer.test('''## 7K%}Tl%{f''', '''<EOF>''', 825))

	def test_826(self):
		self.assertTrue(TestLexer.test('''## G]ZT wa.Ej''', '''<EOF>''', 826))

	def test_827(self):
		self.assertTrue(TestLexer.test("5.960", "5.960,<EOF>", 827))

	def test_828(self):
		self.assertTrue(TestLexer.test("7E+30", "7E+30,<EOF>", 828))

	def test_829(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 829))

	def test_830(self):
		self.assertTrue(TestLexer.test('''## >Nnn }`nh8s|QyYm[%''', '''<EOF>''', 830))

	def test_831(self):
		self.assertTrue(TestLexer.test("3e-43", "3e-43,<EOF>", 831))

	def test_832(self):
		self.assertTrue(TestLexer.test("0.547", "0.547,<EOF>", 832))

	def test_833(self):
		self.assertTrue(TestLexer.test("7E-95", "7E-95,<EOF>", 833))

	def test_834(self):
		self.assertTrue(TestLexer.test('''"
6'"X!"''', '''Unclosed String: ''', 834))

	def test_835(self):
		self.assertTrue(TestLexer.test('''## l#aNsWl![fFn%0h"''', '''<EOF>''', 835))

	def test_836(self):
		self.assertTrue(TestLexer.test("ZfL_pTxU@v", "ZfL_pTxU,Error Token @", 836))

	def test_837(self):
		self.assertTrue(TestLexer.test('''## `64f:9Tx[z27PHTQU)V''', '''<EOF>''', 837))

	def test_838(self):
		self.assertTrue(TestLexer.test("SVDJyqEF", "SVDJyqEF,<EOF>", 838))

	def test_839(self):
		self.assertTrue(TestLexer.test('''## R-{.f#$(Jd32;8"N''', '''<EOF>''', 839))

	def test_840(self):
		self.assertTrue(TestLexer.test("7.397", "7.397,<EOF>", 840))

	def test_841(self):
		self.assertTrue(TestLexer.test('''"W'"'" ''', '''Unclosed String: W'"'" ''', 841))

	def test_842(self):
		self.assertTrue(TestLexer.test("rZ$EH5Nnt", "rZ,Error Token $", 842))

	def test_843(self):
		self.assertTrue(TestLexer.test("53.116", "53.116,<EOF>", 843))

	def test_844(self):
		self.assertTrue(TestLexer.test("9", "9,<EOF>", 844))

	def test_845(self):
		self.assertTrue(TestLexer.test('''"WY?'" ''', '''Unclosed String: WY?'" ''', 845))

	def test_846(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 846))

	def test_847(self):
		self.assertTrue(TestLexer.test("iaM", "iaM,<EOF>", 847))

	def test_848(self):
		self.assertTrue(TestLexer.test("oC5djNzhSl", "oC5djNzhSl,<EOF>", 848))

	def test_849(self):
		self.assertTrue(TestLexer.test("5.969", "5.969,<EOF>", 849))

	def test_850(self):
		self.assertTrue(TestLexer.test("58.727", "58.727,<EOF>", 850))

	def test_851(self):
		self.assertTrue(TestLexer.test("909.262E-18", "909.262E-18,<EOF>", 851))

	def test_852(self):
		self.assertTrue(TestLexer.test("H", "H,<EOF>", 852))

	def test_853(self):
		self.assertTrue(TestLexer.test('''## rWX''', '''<EOF>''', 853))

	def test_854(self):
		self.assertTrue(TestLexer.test('''"'"'"'"q"''', '''\'"'"'"q,<EOF>''', 854))

	def test_855(self):
		self.assertTrue(TestLexer.test('''## y}8''', '''<EOF>''', 855))

	def test_856(self):
		self.assertTrue(TestLexer.test('''## :Qqa?#"7cn;xw''', '''<EOF>''', 856))

	def test_857(self):
		self.assertTrue(TestLexer.test("799.539", "799.539,<EOF>", 857))

	def test_858(self):
		self.assertTrue(TestLexer.test("0.907", "0.907,<EOF>", 858))

	def test_859(self):
		self.assertTrue(TestLexer.test("75e51", "75e51,<EOF>", 859))

	def test_860(self):
		self.assertTrue(TestLexer.test('''"'"'"m"''', '''\'"'"m,<EOF>''', 860))

	def test_861(self):
		self.assertTrue(TestLexer.test('''## vD1BhOL`Q-%fb''', '''<EOF>''', 861))

	def test_862(self):
		self.assertTrue(TestLexer.test("1Pdu5Jsw0", "1,Pdu5Jsw0,<EOF>", 862))

	def test_863(self):
		self.assertTrue(TestLexer.test("70.733e69", "70.733e69,<EOF>", 863))

	def test_864(self):
		self.assertTrue(TestLexer.test("QsK", "QsK,<EOF>", 864))

	def test_865(self):
		self.assertTrue(TestLexer.test("OG9@$", "OG9,Error Token @", 865))

	def test_866(self):
		self.assertTrue(TestLexer.test("L2oDJ", "L2oDJ,<EOF>", 866))

	def test_867(self):
		self.assertTrue(TestLexer.test("207.295", "207.295,<EOF>", 867))

	def test_868(self):
		self.assertTrue(TestLexer.test('''"\\k'"'""''', '''Illegal Escape In String: \\k''', 868))

	def test_869(self):
		self.assertTrue(TestLexer.test("9UkUl", "9,UkUl,<EOF>", 869))

	def test_870(self):
		self.assertTrue(TestLexer.test('''"'"6I"''', '''\'"6I,<EOF>''', 870))

	def test_871(self):
		self.assertTrue(TestLexer.test('''## Q''', '''<EOF>''', 871))

	def test_872(self):
		self.assertTrue(TestLexer.test('''"SP\\p'""''', '''Illegal Escape In String: SP\\p''', 872))

	def test_873(self):
		self.assertTrue(TestLexer.test("250e-34", "250e-34,<EOF>", 873))

	def test_874(self):
		self.assertTrue(TestLexer.test('''## ]~$)"ohtv;[:y''', '''<EOF>''', 874))

	def test_875(self):
		self.assertTrue(TestLexer.test('''## rdi{qOhmR[W@}_&''', '''<EOF>''', 875))

	def test_876(self):
		self.assertTrue(TestLexer.test('''"'"'"0~p"''', '''\'"'"0~p,<EOF>''', 876))

	def test_877(self):
		self.assertTrue(TestLexer.test("996.793", "996.793,<EOF>", 877))

	def test_878(self):
		self.assertTrue(TestLexer.test('''## j@WZ''', '''<EOF>''', 878))

	def test_879(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 879))

	def test_880(self):
		self.assertTrue(TestLexer.test('''## %;pm/5qeia7x_''', '''<EOF>''', 880))

	def test_881(self):
		self.assertTrue(TestLexer.test('''"'"B7VJ ''', '''Unclosed String: '"B7VJ ''', 881))

	def test_882(self):
		self.assertTrue(TestLexer.test("36.347", "36.347,<EOF>", 882))

	def test_883(self):
		self.assertTrue(TestLexer.test('''## N9WmpwjljEzLM#''', '''<EOF>''', 883))

	def test_884(self):
		self.assertTrue(TestLexer.test("rv$QO_", "rv,Error Token $", 884))

	def test_885(self):
		self.assertTrue(TestLexer.test("z70K8b", "z70K8b,<EOF>", 885))

	def test_886(self):
		self.assertTrue(TestLexer.test('''"'"'"5
'"O"''', '''Unclosed String: '"'"5''', 886))

	def test_887(self):
		self.assertTrue(TestLexer.test('''"J'"'" ''', '''Unclosed String: J'"'" ''', 887))

	def test_888(self):
		self.assertTrue(TestLexer.test('''"
'"'""''', '''Unclosed String: ''', 888))

	def test_889(self):
		self.assertTrue(TestLexer.test('''## 6"RaV~p8}msH8_BpaSgy''', '''<EOF>''', 889))

	def test_890(self):
		self.assertTrue(TestLexer.test('''"'"'"\\jh"''', '''Illegal Escape In String: '"'"\\j''', 890))

	def test_891(self):
		self.assertTrue(TestLexer.test("jLJ7U", "jLJ7U,<EOF>", 891))

	def test_892(self):
		self.assertTrue(TestLexer.test('''"+ ''', '''Unclosed String: + ''', 892))

	def test_893(self):
		self.assertTrue(TestLexer.test('''## plb+u#}T^3p|<`KU}=''', '''<EOF>''', 893))

	def test_894(self):
		self.assertTrue(TestLexer.test("1", "1,<EOF>", 894))

	def test_895(self):
		self.assertTrue(TestLexer.test("6.589", "6.589,<EOF>", 895))

	def test_896(self):
		self.assertTrue(TestLexer.test('''## a,#M.xX$H..^4|''', '''<EOF>''', 896))

	def test_897(self):
		self.assertTrue(TestLexer.test('''## k$&]`b~2[6SA?!''', '''<EOF>''', 897))

	def test_898(self):
		self.assertTrue(TestLexer.test("ooeb1g_w", "ooeb1g_w,<EOF>", 898))

	def test_899(self):
		self.assertTrue(TestLexer.test("886E+78", "886E+78,<EOF>", 899))

	def test_900(self):
		self.assertTrue(TestLexer.test('''## DJ''', '''<EOF>''', 900))

	def test_901(self):
		self.assertTrue(TestLexer.test("84.156", "84.156,<EOF>", 901))

	def test_902(self):
		self.assertTrue(TestLexer.test('''## 2q)?g@&''', '''<EOF>''', 902))

	def test_903(self):
		self.assertTrue(TestLexer.test("igtTr", "igtTr,<EOF>", 903))

	def test_904(self):
		self.assertTrue(TestLexer.test("56e+55", "56e+55,<EOF>", 904))

	def test_905(self):
		self.assertTrue(TestLexer.test("7.628", "7.628,<EOF>", 905))

	def test_906(self):
		self.assertTrue(TestLexer.test("nA_&jAZH", "nA_,Error Token &", 906))

	def test_907(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 907))

	def test_908(self):
		self.assertTrue(TestLexer.test("D", "D,<EOF>", 908))

	def test_909(self):
		self.assertTrue(TestLexer.test("7", "7,<EOF>", 909))

	def test_910(self):
		self.assertTrue(TestLexer.test("B1EoWD^$", "B1EoWD,Error Token ^", 910))

	def test_911(self):
		self.assertTrue(TestLexer.test('''"q"''', '''q,<EOF>''', 911))

	def test_912(self):
		self.assertTrue(TestLexer.test("CUIrcLFiGD", "CUIrcLFiGD,<EOF>", 912))

	def test_913(self):
		self.assertTrue(TestLexer.test("655e76", "655e76,<EOF>", 913))

	def test_914(self):
		self.assertTrue(TestLexer.test('''"\\g'""''', '''Illegal Escape In String: \\g''', 914))

	def test_915(self):
		self.assertTrue(TestLexer.test('''"
'""''', '''Unclosed String: ''', 915))

	def test_916(self):
		self.assertTrue(TestLexer.test('''## e)fE''', '''<EOF>''', 916))

	def test_917(self):
		self.assertTrue(TestLexer.test('''## Y7}]vN**84FM,<n t''', '''<EOF>''', 917))

	def test_918(self):
		self.assertTrue(TestLexer.test("3.717", "3.717,<EOF>", 918))

	def test_919(self):
		self.assertTrue(TestLexer.test('''## UgH-mRVg>=j<@Bg''', '''<EOF>''', 919))

	def test_920(self):
		self.assertTrue(TestLexer.test("N", "N,<EOF>", 920))

	def test_921(self):
		self.assertTrue(TestLexer.test('''## 7>KD''', '''<EOF>''', 921))

	def test_922(self):
		self.assertTrue(TestLexer.test('''"'" ''', '''Unclosed String: '" ''', 922))

	def test_923(self):
		self.assertTrue(TestLexer.test('''"'"\\w'"K'""''', '''Illegal Escape In String: '"\\w''', 923))

	def test_924(self):
		self.assertTrue(TestLexer.test('''## [7dc''', '''<EOF>''', 924))

	def test_925(self):
		self.assertTrue(TestLexer.test('''"W"''', '''W,<EOF>''', 925))

	def test_926(self):
		self.assertTrue(TestLexer.test('''## "''', '''<EOF>''', 926))

	def test_927(self):
		self.assertTrue(TestLexer.test("0e+20", "0e+20,<EOF>", 927))

	def test_928(self):
		self.assertTrue(TestLexer.test('''"u
x'"'""''', '''Unclosed String: u''', 928))

	def test_929(self):
		self.assertTrue(TestLexer.test("&SAF#RE&R", "Error Token &", 929))

	def test_930(self):
		self.assertTrue(TestLexer.test("&&yd0", "Error Token &", 930))

	def test_931(self):
		self.assertTrue(TestLexer.test('''"'"\\o'"'""''', '''Illegal Escape In String: '"\\o''', 931))

	def test_932(self):
		self.assertTrue(TestLexer.test("tsf#aZctwX", "tsf,Error Token #", 932))

	def test_933(self):
		self.assertTrue(TestLexer.test("290.357", "290.357,<EOF>", 933))

	def test_934(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 934))

	def test_935(self):
		self.assertTrue(TestLexer.test('''""''', ''',<EOF>''', 935))

	def test_936(self):
		self.assertTrue(TestLexer.test("#$yrhk", "Error Token #", 936))

	def test_937(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 937))

	def test_938(self):
		self.assertTrue(TestLexer.test('''## lyLIK0<0 N''', '''<EOF>''', 938))

	def test_939(self):
		self.assertTrue(TestLexer.test("342.734e-88", "342.734e-88,<EOF>", 939))

	def test_940(self):
		self.assertTrue(TestLexer.test("P9k", "P9k,<EOF>", 940))

	def test_941(self):
		self.assertTrue(TestLexer.test('''"1-"''', '''1-,<EOF>''', 941))

	def test_942(self):
		self.assertTrue(TestLexer.test("wUqS", "wUqS,<EOF>", 942))

	def test_943(self):
		self.assertTrue(TestLexer.test("91.135", "91.135,<EOF>", 943))

	def test_944(self):
		self.assertTrue(TestLexer.test('''"
B'"'""''', '''Unclosed String: ''', 944))

	def test_945(self):
		self.assertTrue(TestLexer.test('''## Q&:k|''', '''<EOF>''', 945))

	def test_946(self):
		self.assertTrue(TestLexer.test("6", "6,<EOF>", 946))

	def test_947(self):
		self.assertTrue(TestLexer.test("#s0Ic", "Error Token #", 947))

	def test_948(self):
		self.assertTrue(TestLexer.test('''## 6`<I)o''', '''<EOF>''', 948))

	def test_949(self):
		self.assertTrue(TestLexer.test("$BxRO4dzop", "Error Token $", 949))

	def test_950(self):
		self.assertTrue(TestLexer.test("184.103", "184.103,<EOF>", 950))

	def test_951(self):
		self.assertTrue(TestLexer.test('''## *]+v(DX.W_4_''', '''<EOF>''', 951))

	def test_952(self):
		self.assertTrue(TestLexer.test("85.508", "85.508,<EOF>", 952))

	def test_953(self):
		self.assertTrue(TestLexer.test("75", "75,<EOF>", 953))

	def test_954(self):
		self.assertTrue(TestLexer.test("2.033E+43", "2.033E+43,<EOF>", 954))

	def test_955(self):
		self.assertTrue(TestLexer.test("5.668", "5.668,<EOF>", 955))

	def test_956(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 956))

	def test_957(self):
		self.assertTrue(TestLexer.test('''## Ob>0%:Su`''', '''<EOF>''', 957))

	def test_958(self):
		self.assertTrue(TestLexer.test("36", "36,<EOF>", 958))

	def test_959(self):
		self.assertTrue(TestLexer.test("c", "c,<EOF>", 959))

	def test_960(self):
		self.assertTrue(TestLexer.test("5", "5,<EOF>", 960))

	def test_961(self):
		self.assertTrue(TestLexer.test("827.571", "827.571,<EOF>", 961))

	def test_962(self):
		self.assertTrue(TestLexer.test("A7", "A7,<EOF>", 962))

	def test_963(self):
		self.assertTrue(TestLexer.test('''"'"'""''', '''\'"'",<EOF>''', 963))

	def test_964(self):
		self.assertTrue(TestLexer.test('''## &kCL;''', '''<EOF>''', 964))

	def test_965(self):
		self.assertTrue(TestLexer.test('''"
5"''', '''Unclosed String: ''', 965))

	def test_966(self):
		self.assertTrue(TestLexer.test('''"/zS\\e'""''', '''Illegal Escape In String: /zS\\e''', 966))

	def test_967(self):
		self.assertTrue(TestLexer.test("^CDlFFA^_U", "Error Token ^", 967))

	def test_968(self):
		self.assertTrue(TestLexer.test('''## UowTS&i33lwk@l|W''', '''<EOF>''', 968))

	def test_969(self):
		self.assertTrue(TestLexer.test('''":a"''', ''':a,<EOF>''', 969))

	def test_970(self):
		self.assertTrue(TestLexer.test("t7ei", "t7ei,<EOF>", 970))

	def test_971(self):
		self.assertTrue(TestLexer.test("918.711e89", "918.711e89,<EOF>", 971))

	def test_972(self):
		self.assertTrue(TestLexer.test('''## C&5.*:~Vy~|m*''', '''<EOF>''', 972))

	def test_973(self):
		self.assertTrue(TestLexer.test("L", "L,<EOF>", 973))

	def test_974(self):
		self.assertTrue(TestLexer.test('''## +*1spt1.J19|<S2s''', '''<EOF>''', 974))

	def test_975(self):
		self.assertTrue(TestLexer.test('''"\\xj"''', '''Illegal Escape In String: \\x''', 975))

	def test_976(self):
		self.assertTrue(TestLexer.test('''## lGXO''', '''<EOF>''', 976))

	def test_977(self):
		self.assertTrue(TestLexer.test('''"'"\\jN"''', '''Illegal Escape In String: '"\\j''', 977))

	def test_978(self):
		self.assertTrue(TestLexer.test("5l09W9u^T", "5,l09W9u,Error Token ^", 978))

	def test_979(self):
		self.assertTrue(TestLexer.test('''"'"+ ''', '''Unclosed String: '"+ ''', 979))

	def test_980(self):
		self.assertTrue(TestLexer.test("q", "q,<EOF>", 980))

	def test_981(self):
		self.assertTrue(TestLexer.test('''"\\c'"'""''', '''Illegal Escape In String: \\c''', 981))

	def test_982(self):
		self.assertTrue(TestLexer.test('''## ;Q_>X''', '''<EOF>''', 982))

	def test_983(self):
		self.assertTrue(TestLexer.test("W2LeJ", "W2LeJ,<EOF>", 983))

	def test_984(self):
		self.assertTrue(TestLexer.test("inAPYb&nX", "inAPYb,Error Token &", 984))

	def test_985(self):
		self.assertTrue(TestLexer.test('''"a'" ''', '''Unclosed String: a'" ''', 985))

	def test_986(self):
		self.assertTrue(TestLexer.test("w", "w,<EOF>", 986))

	def test_987(self):
		self.assertTrue(TestLexer.test("2", "2,<EOF>", 987))

	def test_988(self):
		self.assertTrue(TestLexer.test('''"'"
'""''', '''Unclosed String: '"''', 988))

	def test_989(self):
		self.assertTrue(TestLexer.test("16", "16,<EOF>", 989))

	def test_990(self):
		self.assertTrue(TestLexer.test("4.385E55", "4.385E55,<EOF>", 990))

	def test_991(self):
		self.assertTrue(TestLexer.test("9.176E-32", "9.176E-32,<EOF>", 991))

	def test_992(self):
		self.assertTrue(TestLexer.test('''## `8FPFT#mP-B''', '''<EOF>''', 992))

	def test_993(self):
		self.assertTrue(TestLexer.test('''"\\a'"I["''', '''Illegal Escape In String: \\a''', 993))

	def test_994(self):
		self.assertTrue(TestLexer.test("0", "0,<EOF>", 994))

	def test_995(self):
		self.assertTrue(TestLexer.test('''"sA-K"''', '''sA-K,<EOF>''', 995))

	def test_996(self):
		self.assertTrue(TestLexer.test("20", "20,<EOF>", 996))

	def test_997(self):
		self.assertTrue(TestLexer.test("421e28", "421e28,<EOF>", 997))

	def test_998(self):
		self.assertTrue(TestLexer.test('''"\\d'""''', '''Illegal Escape In String: \\d''', 998))

	def test_999(self):
		self.assertTrue(TestLexer.test("3e63", "3e63,<EOF>", 999))
