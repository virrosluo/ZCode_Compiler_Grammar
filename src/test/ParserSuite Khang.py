import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_200(self):
		input = '''
## "ZQVg/ Ct1KrC~e9{
number pMVq[871.054e94,24,7e-73]
## 5G<>A|
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 200))

	def test_201(self):
		input = '''
func tUv8 (var jNq, string n4u[4.278,9.013E+45,6.472E-61])
	return

## quc9
func q8 ()	return
## n7|g9z#
## d{uoz_p4qP&H
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 201))

	def test_202(self):
		input = '''
number bu[338.083]
bool KmY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 202))

	def test_203(self):
		input = '''
number Ox[157,1,14.290] <- not [J3l("'"'"'"0:", HY6, h1V)[226.850e26, oK] == true] ## ??~<VA/>{<Xnrbb
var Lqm
var jxdW[66E+83,63.417] ## 9!d3)KBbg+P06
string XD[3.052E-87,63] <- true ## x}x2{KLB
'''
		expect = '''Error on line 3 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 203))

	def test_204(self):
		input = '''
func jC (var F5A[620,920], var Ch[5e10,6.133], string tcZy[4e60,862e87,19E-05])	return false

var JSv <- 4 ## Px6?f8
## p!`PXq<ng
bool Mii1 <- true ## |!27h;[x(<i3
## UyTYv_DiI"N
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 204))

	def test_205(self):
		input = '''
## X;^
string naZn[1.703e+31] ## jz?a
## C%],8o!]q>^FgxcU
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 205))

	def test_206(self):
		input = '''
number Pg5[5.720,41,974e-96] ## c|u0zsa
func fO (number oW, dynamic hcGk, var QB[2.268])	return
'''
		expect = '''Error on line 3 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 206))

	def test_207(self):
		input = '''
func rJcD (dynamic DR[8.785E+26,9.209,4])	return "{"
func v5 (dynamic iC, var D2[48.204E-11,782.971E42])
	begin
	end

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 207))

	def test_208(self):
		input = '''
## q-lFm7Q
number Rs[6E+95] <- true
func OOx (number QUA[7], number Bx)	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 208))

	def test_209(self):
		input = '''
string lR[8,8.838E68,63] ## ok
bool K9[305E81] ## eY1puy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 209))

	def test_210(self):
		input = '''
func ihZ ()	return true

func bmx (number Nd[8.197,29E+73,2.229E-62])
	return

## HV?O_tP^j1sSIg}gQ9wQ
dynamic gvi ## 4n jI1`Sy]q"a<b4gZm(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 210))

	def test_211(self):
		input = '''
func IsB8 (string tf0W[676.426E-18,76e-63,2E40], bool k2[48E+19])
	return
number IMB ## D>naJWB*Q]I
## +8vi?ftcqsa:St5O
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 211))

	def test_212(self):
		input = '''
## i_rf75{kSf-R
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 212))

	def test_213(self):
		input = '''
## jU]>j9~NI^`^u`$N>
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 213))

	def test_214(self):
		input = '''
func SNx (string x0[424.569e29])	return "'"3'"'"P"

## ]$<H!f+#_*JV^![x$
## T(<d3A
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 214))

	def test_215(self):
		input = '''
string HCV <- 9.869 ## &![%9 pec7$RLm
number zvm
string Ra <- 9e+32 ## :L(>8RP.DT/
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 215))

	def test_216(self):
		input = '''
## 7Hgo^ 
func Ru (var g2, string e8W[1E+48,98,12], dynamic KK)	begin
	end
## t-
number AwX[969E-05,85.324E-41] <- dhw ## YMFN2Tw#qyIxDkD,
dynamic VW
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 216))

	def test_217(self):
		input = '''
## oQ[W
## r,$
number PMuO <- BKt
dynamic vaN
bool kYm[8e+02] <- "G'"V" ## rivkBhQMli%.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 217))

	def test_218(self):
		input = '''
func JLf (string pPHW[4E93,912.439e88,114e+67], number Iso[313e-13,37,6], bool aZnr)	return
func EcF (bool ow3, string Rm6k)	return

dynamic PQ <- "'"`'""
number AKWU[16e+84,76.021e77,8]
var gPgf[801.844,1,985.800E-17] <- 3
'''
		expect = '''Error on line 7 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 218))

	def test_219(self):
		input = '''
number Ry[841.341e+14] ## `7JLUD
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 219))

	def test_220(self):
		input = '''
## Y1?l
func qz3 (number zN, string tn)	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 220))

	def test_221(self):
		input = '''
func GT1x (bool Sr, bool GV12[512E-04,40.321])	return

bool kp <- dt ## 0:{{%.)Eo7:OP
dynamic Jx ## g
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 221))

	def test_222(self):
		input = '''
func WaTM (number VBB[3.930,6.967e31,5.197e71], dynamic vGl[914,819.677], bool Zi)
	return "'"'""
## vvZ9T
func Z8 (string WbHL[29.018e-16,467.288E+80])
	return CgOp
number yC <- EINm
## v=
'''
		expect = '''Error on line 2 col 48: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 222))

	def test_223(self):
		input = '''
## ),kJPq|H
dynamic Jq <- WZvX ## S40;<k[8g`!lJ??=N
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 223))

	def test_224(self):
		input = '''
func aB (string Ze[90e-25])
	begin
		Ey <- dG8
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 224))

	def test_225(self):
		input = '''
string MC[9.709E+07,988.241E05,63] <- false
string ruD[72.801e91] <- 27.139E+48
func Vi (var rtd)	return "F'""
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 225))

	def test_226(self):
		input = '''
string fT8b[65] <- true ## D8]l3jv%nt
func F9E (bool Yx, number D8Q[4.653E-27], bool ovHe[58.639,34.734,227.909])	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 226))

	def test_227(self):
		input = '''
string aqF[32.508e+40,3e13]
bool jc[751E51,31] ## l^^V
number Mg[169,0e24,2.886E99] <- "'"{" ## ]?)zj5
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 227))

	def test_228(self):
		input = '''
func yPB2 (string tP)
	begin
		break
		## yWZM#{cn"oM:
		So84()
	end
var omCJ[3E-46,838]
func aiV (bool F3FB[115.724E-08])	return 53.978

bool Iuso[86.018e00,91.338] <- false
'''
		expect = '''Error on line 8 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 228))

	def test_229(self):
		input = '''
bool AbuQ <- "'"7'"" ## f
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 229))

	def test_230(self):
		input = '''
## 5N&?e %jzT^Frn;E5^
func Qd ()
	return
bool C7X[36.859E-22,99.802,59.857] ## 6B!M;#/qAcZ
func Gv ()
	begin
		return Mf
		## >r5 EaCp[{rM8DX5?goi
	end

func HFz (dynamic q4l, dynamic Fci5)
	return

'''
		expect = '''Error on line 12 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 230))

	def test_231(self):
		input = '''
## 8.A!_R0jU
## ]?gqB@FuovP,
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 231))

	def test_232(self):
		input = '''
func Lo (bool DH[38.522e17,912.240e-74], string NTxo[470E-76], dynamic n321[0.384,77E-53])	begin
		## p#JA@%%7
		## $t#H""FwHVsv Y8>Y~D
		awL("9B'"0'"", 9e-31)
	end

dynamic h8b <- true ## &}%^^HUzd_
## 2YcdU^`uf>C;X
func pTz (number Opx[7], dynamic mV, number nF)	begin
		## X)lf`[,l
		## J8/{m
	end
bool pX7[51.474,70.231] <- "'"d'"'"" ## R<k
'''
		expect = '''Error on line 2 col 63: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 232))

	def test_233(self):
		input = '''
## k4#j]2*
var XB <- 994.870
func Ls5E (bool Qb[0.652e19,3])
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 233))

	def test_234(self):
		input = '''
func h2 (number r5b[250.735E+54,90.044])
	begin
		continue
		begin
			## wYX|}lnKsie1L_J-GJh
		end
	end

number BJ[871.753]
func vi (dynamic ENI, var vj)
	begin
		## ,%*+P"*oAJ
		Q2(492.356)
	end
'''
		expect = '''Error on line 11 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 234))

	def test_235(self):
		input = '''
var OY3[829.027,22.595e82] <- TFZV
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 235))

	def test_236(self):
		input = '''
func XdGR (dynamic yb[0.911,58E-60,4.717e+47], dynamic ZB9, var WC_)	return 64
## R2%!(s|+7uo_
## D
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 236))

	def test_237(self):
		input = '''
## kB7Pvw*FYV
func Z2g8 ()
	return

## OcqN*i0T8nLSw
string NA[12.524,1E+26,219.099E24] <- 2e-64
## _6hbk
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 237))

	def test_238(self):
		input = '''
## 2IacN:N0V-SakX|"-+
var RD[36E09,641.662]
string Pc[1]
func TeP (dynamic F6aK, bool r3[0.418,94.565E+70,8], var NH6t[721.910,85,7])
	return Ul7

func el (number Kwf, bool H3u)
	begin
		break
		begin
		end
	end
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 238))

	def test_239(self):
		input = '''
## Y
bool ID ## .@
dynamic cF
string owg <- true
bool oYvb[59.996E40,1e52]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 239))

	def test_240(self):
		input = '''
## ;;8qSeR?u
func JrO (dynamic CCgt[14E87,8.046,272.425], var oU, dynamic SoA[26])
	return
var fD6[1.078,657e+37] ## :&F*f7aC0x~C]
func sAu (bool XO[219.681e-70], bool ZAvI)
	return "'"'"y2"
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 240))

	def test_241(self):
		input = '''
func O5 (var nVz, string l_K[7.346], string XSx)
	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 241))

	def test_242(self):
		input = '''
string fdX <- 944.056 ## N+M}pt?
## Qw<%0#u;3Yz])(M{6L.(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 242))

	def test_243(self):
		input = '''
func ylf (var Vk81, number C1kE[952.552])	begin
		for jtA until 64.863 by true
			break
	end
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 243))

	def test_244(self):
		input = '''
func liA (bool phy, string jhO[13e+13,3.339E11,72], string PYj[740e19,75e70])	return
func fDtA (bool qdPZ, number YKbA[8.759e-05,2E+17], var dr)	return
dynamic RGgG[3.556,319] <- "R|'"2"
number kuJ[8e+15] <- false ## sl$775gH_d7h]uul%B
'''
		expect = '''Error on line 3 col 52: var'''
		self.assertTrue(TestParser.test(input, expect, 244))

	def test_245(self):
		input = '''
bool GKw <- 167.956e29 ## OjL.[@)~Jd-9 .
bool Z7 <- M9A ## &k.
func tjP ()	begin
		## ]`#e%lq#a;-+CbCktUU
		## 5aCxr
		## 9c_j3/HX3>i*OJb{
	end
bool Tzu ## m7XTmV[Y[p*-:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 245))

	def test_246(self):
		input = '''
func ts (bool dP)
	return

## QCh
func oh ()
	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 246))

	def test_247(self):
		input = '''
bool iX
## M-(r"z>f}@Q/
## h D@p"9~xSCZ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 247))

	def test_248(self):
		input = '''
dynamic Wl7Y ## $
func adD (var WSl8, number uJ[6,2.271,688.585])	return

## (p~iTc Qs[]x6K
func H8PC (dynamic JT, number cE5C, string a4K[116.224,311.895,9])
	return 13
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 248))

	def test_249(self):
		input = '''
func MlWQ (number DRq[69,5.029,7.404E-63], string ZZ)
	return
## Xg7
func nL (var GTSI[612.819E+69,36.621])	return

## 4 lOwjCKX@Kcq"8#7s8Q
var be9v[8,605.831] ## tBP/>;u!5bG[r"CcH4
'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 249))

	def test_250(self):
		input = '''
dynamic bCi7[43E-84] <- true ## bJo$">9|!QM7
## y^mx9gvl&tzLMxQ
func iV (dynamic fJm[32])
	return
func hz ()	begin
	end

'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 250))

	def test_251(self):
		input = '''
func n0F (bool FO, dynamic OF[0,86.160])	return 10E-86

bool qe
func BW6a ()
	begin
		return true
	end
'''
		expect = '''Error on line 2 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 251))

	def test_252(self):
		input = '''
func FxE (var V9, dynamic od, dynamic xxkv)
	return true
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 252))

	def test_253(self):
		input = '''
dynamic GkN[1.535,8,4.509E+85] <- 19.687e-78 ## <W-|D
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 253))

	def test_254(self):
		input = '''
var LjCj ## N*N=n6/*>3^
number OYXG[2.456e+55,6,325E+14] <- 35 ## (Na[Q?<$5EN]J4gbj
func r0hY (number JT[63.455,4.209e+13,5.876], var WV5N[735,8.491e-50,261e94], string lw[409.032E+51,7.464,4.241E-29])	return
'''
		expect = '''Error on line 2 col 23: 
'''
		self.assertTrue(TestParser.test(input, expect, 254))

	def test_255(self):
		input = '''
func nQMq (var XS[2.545,595E+93,61], var Lb)	begin
	end
## :O-3XbETio{m
func VPCq (dynamic tfG)	return "'"'"'"s"
func yE ()	return
func X_A (bool VSg, number su3[233.215E66,9.001,5.427], var g3[36,183e52])	return

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 255))

	def test_256(self):
		input = '''
func h5q (number SI2z[4,8E-76,8.045E+02])
	begin
		##  xN[{ZWiM
		return w5
		return true
	end
bool pIK ## l
string nNy9 ## QOLg
string RGg[8.127E-33,3E+58] ## w2"#+SJTqX9Bm)"Iv
## C~LtL/+Lc S76>kY1`
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 256))

	def test_257(self):
		input = '''
## V]y>^p%B<
var wM ## pz]b 
## 5TfdgHU
'''
		expect = '''Error on line 3 col 15: 
'''
		self.assertTrue(TestParser.test(input, expect, 257))

	def test_258(self):
		input = '''
## |?ZmK |$Eyl[V|PcXj+z
func uA0Q (string idp5[66.315e10,2,6.473E-40])
	return
## ``qo?"ztb11I|.@s@(n
## `5Y(@@92GTOiop
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 258))

	def test_259(self):
		input = '''
func JamS (dynamic Gs, number aVJ2)	return
## <FldUO
## _KBe1*FyY
## t[^
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 259))

	def test_260(self):
		input = '''
func bl ()	begin
		## %*0Y|o,
		if 678.908E97 begin
			return D0
		end
		elif sp if 155.698 for p2 until hPy by Yt
			mdk("c'"k'"'"", Y7m, "=")
		elif U5 begin
		end
		elif 1 begin
			## i&?*s
			## fT^2N
		end
		elif "'"'"4J'"" break
		elif 999.715 number TPZC[56.801E77] <- F8I
		else if 23.275 continue
		elif true if 183E21 break
		elif 711e+73 continue
		elif true if "'"/" continue
		elif true number Q8V ## .-2yhT?ABke5
		elif "'"" string zD <- true ## *!MXP$P|d:3W[6Iza
		else Aohm <- "o"
		elif vs continue
		else if 566.402 return "'"'"U"
		elif false return 72.437
		elif false XQSR <- RM
		elif 605.633 for lq until 48E98 by TpAd
			begin
				## XXFlOIdWP
				## =
				## u
			end
		elif false return frBB
		elif fBbp number qtOU <- Va5S
		elif 204.134 dynamic DVD[66.413e-68,10.134E+85]
		elif false return
		elif "L'"'"" var lqi ##  @F=6yq~sBT
		elif "W_" continue
		else break
		elif 0.847 begin
			## }5G2}MR3D6Iko
		end
	end

## M[K=[o5K~g
## fn{/Mi"v>
'''
		expect = '''Error on line 4 col 5: 678.908E97'''
		self.assertTrue(TestParser.test(input, expect, 260))

	def test_261(self):
		input = '''
func fK (bool oyCK[4.172,39], var l5lF[2], dynamic Jufd)
	begin
		continue
		kAl3()
		## Z
	end
func RS ()	return

func vDB (dynamic eB[30e+27,97.468], dynamic n4N[7e+69,3.455], number GH)	return 990.618
func C1Gs (bool NHdB, var DYk[49E+98,4E-44])
	return 0.142E-25

var bx <- "e'"['""
'''
		expect = '''Error on line 2 col 30: var'''
		self.assertTrue(TestParser.test(input, expect, 261))

	def test_262(self):
		input = '''
func zTN5 (bool WHTu)	begin
		begin
			## rNI42X-|)Je7?&[7o/
			break
			for Vy1 until O9 by Au
				if 17.971E+10 ut(77e60, "D'"@")
				elif ItNz for kat until true by "'"G'"g'""
					for NZSe until 4.753 by true
						continue
				else cq <- gPKg
		end
		## gx40@!
	end
func cH (string gits[957], bool yQ, string uCu)
	return

func CVs (string k9IP, bool Up2)	begin
		## /tO+f-p~>,r)0
	end
'''
		expect = '''Error on line 7 col 7: 17.971E+10'''
		self.assertTrue(TestParser.test(input, expect, 262))

	def test_263(self):
		input = '''
number Lji[4.710,92.698e33] <- LQ
func oDA (bool VL5g, string v3pb[130.720E+67,20.550e+50])
	return false
func MSc (bool Fc7C[1.795E16], bool xUY, string ePI)
	begin
		if "'"|'"J" var LnFa[3,78.176E39] <- 16.551e-62 ## g$6YP$"nYdb}H{bz8
		elif true string uPJq[16,868e03] <- "'".'""
		elif false for CA until 8.871e+46 by false
			dynamic gb[7] ## Se5T:6I%%wAcsUqL&x
		else if "5R" rRe(69.342E-69, 9e-39)
		elif false continue
		elif fD begin
		end
		elif dKrt continue
		elif "Lj" if 5.240E+46 oXi("Q'"", false, "C'"'"'"'"")
		elif 390.552 if P6Q break
		elif EHSQ return 2E-18
		elif da string dX[107.659,1e-97] ## YR8swh0=6l"D#F,~
		elif "'"" bool rjdK[60,1.164,954] <- false ## 9c}@W:(l]an?
		elif false continue
		## c#!k
	end
func sP (bool ECCt)
	begin
		## :U
		## /
		if XdA var S2[77E-04]
		elif "'"'"o'"'"" nd(336, yP, false)
		elif Mbi number Mbl[797] <- false
		elif "'"'"W" if true jjPa[Qi, PFsZ] <- 2.761
		elif "'"'"a" for ff until ow by "'"'"V"
			begin
				## +f$El=Ojvj/
				YH <- "'"S"
				## xW&Jn`
			end
		elif 1 continue
		elif "o{'"'"'"" continue
		elif false begin
			continue
		end
	end
string w3Sg <- 9.850E+00
'''
		expect = '''Error on line 7 col 5: '"|'"J'''
		self.assertTrue(TestParser.test(input, expect, 263))

	def test_264(self):
		input = '''
## ,.m649
number Ol <- 7 ## di=|# @kBE-G]!m
func WUH ()
	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 264))

	def test_265(self):
		input = '''
## xlCdr|+@v0_y&T&O?>?
## p.j.S8!?3(=
func FTw (dynamic E_vD, bool YD4[96e+13,232,71.878], string hp)	begin
	end

## v.@d:^7RT[{Sb[m2
number ZJQ ## q-
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 265))

	def test_266(self):
		input = '''
## K,0Oc^
func RgU (dynamic hT, dynamic h8, number ZsB)	begin
	end
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 266))

	def test_267(self):
		input = '''
dynamic krd[39e+82] <- SK ## g>s8@_
## a#{8d9Bl/H|@b)N.abt
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 267))

	def test_268(self):
		input = '''
dynamic PFy <- ZbqU
func XjEG (number iJ4, dynamic Gi5[52,5.198], string pmSi[49.283])	begin
	end

bool Oh ## 0-=
## O>I|_{FD&1{`B[4
bool okr ## H *nZd> MR+wB
'''
		expect = '''Error on line 3 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 268))

	def test_269(self):
		input = '''
## x(
string cE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 269))

	def test_270(self):
		input = '''
dynamic Y11I <- 927.727
## Xy
## >I xT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 270))

	def test_271(self):
		input = '''
## (
## eO^mD3
func mFa (dynamic x5R[24.524])
	return
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 271))

	def test_272(self):
		input = '''
string UR <- 0e63
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 272))

	def test_273(self):
		input = '''
string jJBs[2] <- 376.637e+77 ## *wiiwZqy?{i$`btz
func k6 (dynamic sa, bool uSfZ)
	begin
		begin
		end
	end

string W5[102,51.101e-54]
func UzC (var I9UA[54.862])	return

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 273))

	def test_274(self):
		input = '''
string du <- 425.038e26
dynamic RuP0[16E63] <- 97.740e97
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 274))

	def test_275(self):
		input = '''
func HAQ8 (number OFco, dynamic tLhX, bool YL36[4,450,63])
	begin
		## =mz|k9>xLyA3G""
		for RIdu until J0c by 69E-32
			begin
			end
	end

string VoY[594,99E-78,3] <- true
'''
		expect = '''Error on line 2 col 24: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 275))

	def test_276(self):
		input = '''
var F7F[0.029]
## A?
var PpI <- q1O
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 276))

	def test_277(self):
		input = '''
number ZMso <- OzJk ## Dxc5GA
bool H9r
func wq3R (dynamic NmM[902], bool WPih[18.309E-99,50.798,111.213], bool gqJ)
	return dh
dynamic Xog[4E27] <- "'"" ## Ml6VaQ[J4tK zP<H?
string NRF[5.574] <- 6.800e71
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 277))

	def test_278(self):
		input = '''
number i0Ap <- "L'""
bool HLn <- 2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 278))

	def test_279(self):
		input = '''
var Zm9[4E+95] <- true
func kDx (dynamic mnr, number t6n[706E96,479e+04], var Uk9)	return

## %3oW
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 279))

	def test_280(self):
		input = '''
func mVO (var LN[7e-63,0E-77])
	return
## O/I
func Sdtj ()
	begin
		break
		var Rp <- rxtE
		## e!>-6Gb0
	end

## P8P
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 280))

	def test_281(self):
		input = '''
string qJ[0e-09,72,0.754] <- "'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 281))

	def test_282(self):
		input = '''
## 9*F(~$Nx:BsgSgjkf
func hcN (bool kK[706], var B19)	return
## 4f(sjco|)*|0
string Yr
'''
		expect = '''Error on line 3 col 24: var'''
		self.assertTrue(TestParser.test(input, expect, 282))

	def test_283(self):
		input = '''
func eIv1 (var R_)
	begin
		## ffDroE.hULo
	end

## ]n-0OV1qE*r(v1"k|S
number mai[19.570e-55] <- 199.475E+13
bool PB <- 7
## &
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 283))

	def test_284(self):
		input = '''
## m+TUi=q9 R=oG@
func g7 (var o56O)	begin
	end

func o2S1 (dynamic WE)
	return

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 284))

	def test_285(self):
		input = '''
func LTa ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 285))

	def test_286(self):
		input = '''
func q7J (string ED2)
	return
func v1jE (dynamic om, dynamic BhFX[597.942,64.022])	begin
	end
string c0Z <- 861.943
number Lxcd[9]
func XB7 (bool rw)	begin
		## YeWq2uZ
	end
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 286))

	def test_287(self):
		input = '''
func NqY (number A3fF[964.170e33,98.026,1], number DpM)	return
## 9ZFKAt)ae~@m-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 287))

	def test_288(self):
		input = '''
dynamic Wdx <- VO6 ## JDDoT^So: [St6t#U)9+
bool hq3p
number t2gw
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 288))

	def test_289(self):
		input = '''
func UgqP (dynamic Vg)	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 289))

	def test_290(self):
		input = '''
func hXa ()
	begin
		## F
		ESM <- false
	end

## IyNH":q
## 18czu6vh$0Fw4L^ULK
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 290))

	def test_291(self):
		input = '''
string tk[76,88.221,8e67] ## DOTS7l4@76
func nnn4 (var Pip7[44.582])	return false

func Ut (bool jj, var AqWZ[4])	return
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 291))

	def test_292(self):
		input = '''
## 6 
var x9[66E91,1.243e+72] ## s&^3DM2IAwE>
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 292))

	def test_293(self):
		input = '''
## 4 J=a({[Hw)C*/zK#[o
## /[a|d
dynamic fGnR[229,31.078E50] ## Z1qDJeK?1vSU,ZR^
number O54V[9.763e+79,3.604]
## F>tb$E6eKFy)
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 293))

	def test_294(self):
		input = '''
func xRen (string uk[0,8.849E97])	return

bool sPA <- Ecu
func qg (bool GQn, dynamic JE9[9,720.699e-26])
	return

number qP
## ]DXi&.XtWlZ
'''
		expect = '''Error on line 5 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 294))

	def test_295(self):
		input = '''
func jF (dynamic C9SA, var F7, bool LIyC[2e-01])	return "!m"

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 295))

	def test_296(self):
		input = '''
func vbEO (number xqKw[495.484], string UhN, bool ec8T[751E-38])
	begin
		if true continue
		elif rgU begin
		end
		elif "'"" Lt(412e+64)
		elif "'"'"'"'"" return
		elif "'"" if 81E+42 zO0 <- 28.821
		elif 7e-00 for LR until false by 2.428E51
			break
		elif false Ohi("z'"'"$", dq)["m", 2] <- "_"
		elif 0 if true continue
		elif cmAj for Kz until jVO by false
			number bD[760E+20,359.852] <- "'"'"*"
		elif false T49("Dc'"'"l")
		elif "d'"@'"'"" begin
			## P?[VyA9$|~?dY
		end
		elif 65 begin
		end
		elif true Rg(QZGM)
		elif kt xmsv(d5FK)
		else for hPEp until 895.820E75 by 5
			for psU9 until mk3 by false
				Le(9.759e-41)
		return ")'""
		## K12&hYq6>O=Im
	end

func UM (bool Tzvj, string za[1,302,31.777], string P2)	begin
		JN("-#", wE, false)[8.860e74, false, 3] <- false
	end
## +e8b>P"hrWdGP4u
## k
'''
		expect = '''Error on line 4 col 5: true'''
		self.assertTrue(TestParser.test(input, expect, 296))

	def test_297(self):
		input = '''
func gTU ()
	return "'"'""

## 6.muH<+db@;%!H+
## "Qk0q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 297))

	def test_298(self):
		input = '''
## @mw.A^;qn&
## KN7K*l`$nu5
func yD ()
	begin
		## >JOX0
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 298))

	def test_299(self):
		input = '''
var L4u[78]
## GTS0bR^o.~E
number kvz[5]
## rZU?`"do&b%Mi&W k(E
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 299))
