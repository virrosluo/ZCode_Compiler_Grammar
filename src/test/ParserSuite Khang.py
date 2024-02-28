import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_1000(self):
		input = '''
## #=xO1$ [Bf_!i[=9w2U
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1000))

	def test_1001(self):
		input = '''
## [VI-Evvh;[`8R)w^
## Y/)$4Kp?odx7S4YRw
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1001))

	def test_1002(self):
		input = '''
## @*C#} a.[)L-Ghe
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1002))

	def test_1003(self):
		input = '''
## ,u|MeQ_
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1003))

	def test_1004(self):
		input = '''
## "#$S+SS~kt
func Qe (dynamic xaPJ)
	return [Uyqm[21.664E-05, true, lZ]]
## E
func Knqf (string Jz1E[91.295,9], dynamic hWM[69.930e+00,4], string iHt9[8.505,982])	return "'"A"

## FG{(|,c#Hmj][r
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1004))

	def test_1005(self):
		input = '''
var pVYA[8,230.975e+11]
string SX <- true ## >Z&j>2.-|t~
dynamic alU[81.487,85e+53,8]
bool gkj <- ei
## `+(BHpV )ch$}Th6UC
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1005))

	def test_1006(self):
		input = '''
dynamic g1
## xHx|U(j,E0
var miI
string vlOk <- fO ##  ULl:U&BYoE|
## nx^%JzrJBAogmL
'''
		expect = '''Error on line 4 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 1006))

	def test_1007(self):
		input = '''
## ?}42>CG#jRSk-~(tr n~
## fsss
## yb"-&za0xJ6*
func GAL (var Iw7)
	return
## rIhP-F]);bNH)]jm
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1007))

	def test_1008(self):
		input = '''
dynamic ukt[59.394] <- true ## p 
## p+O84V"S}yJm:6bh%
func Yq ()	begin
		## !Ha#QAq+cPDK/uG
		## 2[##Pc<>Pj9@@
		## PE?iRIRzD8#J!*Qd`
	end

func c16 (string u0d)
	begin
		## ,^sEb"5wv~AO#
		n3d(Lpe, "8")
	end
func pY9 (var JUmj, dynamic cv)	return
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1008))

	def test_1009(self):
		input = '''
func psID ()
	return
dynamic k8pH[127,5.146E+05,0e-85] <- 0E34 ## eALuI}
## gaFUx
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1009))

	def test_1010(self):
		input = '''
## K,k~
bool fM6J
func ft (string P5gE[755.196,935E+49,6.507e04])
	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1010))

	def test_1011(self):
		input = '''
number j8[3.398] ## ,Ow(s,:Dk:nhMq1(
func Qk6 ()
	return
func n4et (dynamic wDO)	begin
		De <- "a'"i"
	end
## 4043VY/
func Jy6U (string kcox[0.623e-03,479])	return

'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1011))

	def test_1012(self):
		input = '''
func VAm (number TT[232E+93], var ru[6.890,481E+70,149])	begin
	end
func WzuF (var uuZS[9,2E+70,758.214], var zIoH, var qt5)	begin
	end

## DH@
func Ma (bool iJJ)
	begin
		## QzK?P%ir$-u
		begin
			return
			if bcI break
			elif 0e-66 number ST <- Vwq
			elif true for JUhh until "Me'"" by hrsM
				break
			else dynamic Ba0Z <- Kt ## Y+&.TKZk28a/1XzHe
		end
		PEl[838, 19] <- "B'"'""
	end

'''
		expect = '''Error on line 2 col 30: var'''
		self.assertTrue(TestParser.test(input, expect, 1012))

	def test_1013(self):
		input = '''
## z~A##lxWQQ
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1013))

	def test_1014(self):
		input = '''
## >-T?Na%&1F.opNYd*
number Vpy
func KL1s (var oOD[478e-74], var vt6N, dynamic lPDS[60,18,0.311E+33])	begin
		if false continue
		elif "'"'"" continue
		elif 7 FQ()["t='"'""] <- ma
		elif 448e+68 Xq(61, uuZG)
		elif 962e+12 break
		elif AWcP if 613.791E+36 begin
		end
		else dynamic STC ## 2)zTL?617Lao:s#B
		bool eXgm[10.540E14] ## OyteH7H6mf1
		awV3 <- "'"'"'""
	end

## E
## DFp{[e*/Ln0>1tdJ
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1014))

	def test_1015(self):
		input = '''
func ggrq (string zfL, dynamic O_Z)
	begin
		## $Mg5<XI*NEPVakV
		ce <- 771
	end

number Onn
## :vZ2|U9RIz?PuFrcfD,
dynamic zc72 ## -;g}.^EFI>LU/w#
'''
		expect = '''Error on line 2 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1015))

	def test_1016(self):
		input = '''
## AUH-MICy~6!M]yp
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1016))

	def test_1017(self):
		input = '''
func R5 (dynamic qRz, var hNrk)
	return true

dynamic FXE[216e38] ## i8BUq#U4q7L]hN
func r_u (bool d74S[58E-71,9.779,1E-23], number Pzoo[5.167E-60,938E85,35e-36], bool Tt5S[391E52,5e79,675e75])	return "'"'"'"5"
## .
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1017))

	def test_1018(self):
		input = '''
dynamic w3v[487,5] ## `|(|
## F?OSP7<4"Fj]9t~knc
func Ocg (string H62H[375.338E+39], var b74D[93E33,4])
	return

## S,(9.(
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1018))

	def test_1019(self):
		input = '''
func vTQ (var gI[7E02], string fap)	begin
	end
func qDU (number sf, string h0[77,46.557E+68])
	return buW

func sLg ()	return

func woBr (number hS4)	return
number ACD[8.931e+37,5.772] <- true ## Dn
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1019))

	def test_1020(self):
		input = '''
func KUli ()
	return

number jF ## ZcfXpvRAV]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1020))

	def test_1021(self):
		input = '''
string aq[406,464] ##  A0s{^
dynamic aM2u[71.121e84] <- "'"'"'"'"N" ## 5Vk)!f
number n7 ## "F$i|]*="]
func J6S (var P8)
	return

'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1021))

	def test_1022(self):
		input = '''
## 6I-VYZy_S
func ct6e ()
	return "v'"'"'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1022))

	def test_1023(self):
		input = '''
func Zak ()	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1023))

	def test_1024(self):
		input = '''
## <kW>Wt5jc[brH)5X97C
bool K1lL <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1024))

	def test_1025(self):
		input = '''
func zE (number p5[34])
	begin
		## An[{Q1t)>^2CD/Kd!
		break
		## #R3Ht]S6h TB
	end

string Ho <- false
## 59<Ku"[";h/}"mj6j],
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1025))

	def test_1026(self):
		input = '''
func gqA (string rf, string aK, var RB[10.898,409,0e87])	begin
		## GP+ d?0jA!h~
	end
var ZRG[3.733e-50,0e-41,919E-03] ## ,;7lSkgl)H ^
func heaJ ()
	begin
		## nQ~415ki J"H0gCp
	end
var iU <- false ## 2J0zpiUfu)kxR5
## LqPTzP72?GAl{ 
'''
		expect = '''Error on line 2 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 1026))

	def test_1027(self):
		input = '''
## EA
func gS2 (bool AQ[7E-72,473])
	return
func AxFf ()	return

## :s{)fHR
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1027))

	def test_1028(self):
		input = '''
func TiI (bool Lx, var a7[9.788e+05,7.333E05])
	begin
		## Z6tEe2(-
		## XWnliW,5}L#TMJ
	end
'''
		expect = '''Error on line 2 col 19: var'''
		self.assertTrue(TestParser.test(input, expect, 1028))

	def test_1029(self):
		input = '''
## ""NxHbG
## D-R/FX2M<#{
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1029))

	def test_1030(self):
		input = '''
string Ojs[438.380e+50,1,383E-60] ## DE-:K)`e@5/c*zIl
bool psli[911.498] <- "J'"" ## #
func BT (bool IlXt, dynamic ddVb, number Exj[89])
	return "'"'""
'''
		expect = '''Error on line 4 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1030))

	def test_1031(self):
		input = '''
func Eo (string YGpR[8e+46,9,2], dynamic CXb[74.998E72])
	begin
		## xZA+!C.=
	end

dynamic jvGR[35.688,73,0.173e-21] ## qM]5
func Cb (var Mm)	return

dynamic RK5z[40] ## M^WtQ
## M#-C7]uj&feK 
'''
		expect = '''Error on line 2 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1031))

	def test_1032(self):
		input = '''
## `T5k{1WsmL^`@@-(?}X
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1032))

	def test_1033(self):
		input = '''
## QM7X3Os*p}G/Avb
dynamic rJE8 ## dzM5a"Co{cJ-*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1033))

	def test_1034(self):
		input = '''
func nd (string fP[3])
	begin
		begin
			## =@Bm;8*^_=#:
			scE1 <- false
		end
		## 3gzt(&@3)r$r$V
	end

func bat (number ymJ2)	begin
		## Om0~pM01
	end
number tt[1.867E-83,938.602]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1034))

	def test_1035(self):
		input = '''
func TK (string ad[20E+86,6.755E42], bool AqeF[3.107E-74,3.330,88], dynamic DXn)
	begin
		R3F(qXcn, omU)
		DhJC <- ZVmi
		## L]zrP
	end
bool KD <- true ## )>wRlgV
## a5veZ5TKuLQ@ t7PmfJ
'''
		expect = '''Error on line 2 col 68: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1035))

	def test_1036(self):
		input = '''
var fwe[5.749e+30,8.972,5] <- false ## emKpX
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1036))

	def test_1037(self):
		input = '''
number vGM[180e03,2]
number GcW <- 190e-10
## }sQlD`>V?oa)_D"@]*g
## +%}oBoF
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1037))

	def test_1038(self):
		input = '''
## Uw?,z6`,F"&F
## aVD
func sIX (string lpA, bool Tc[54.009], bool UM2X[408.513E52,2.804e+57])	begin
	end

bool CA <- false
## Sj[a_-^qDJ/_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1038))

	def test_1039(self):
		input = '''
func k1 (string G5jd)
	begin
		break
	end

number J7Y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1039))

	def test_1040(self):
		input = '''
## o3C2
var u7[9.226,6.161E16] ## DU(I_EU
dynamic dQZM ## M)4
## ~{:y
string AhJv <- "'"D'"j"
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1040))

	def test_1041(self):
		input = '''
bool Suym[217.500,248,8.883E-63] <- 10e31
dynamic m8hg <- 3.086e+41
## ^1}l:h8X5HLL@^n
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1041))

	def test_1042(self):
		input = '''
## Pp<m6y
## PP*3
func icQ (number CZFj[6.535,5.658E09,7E10], string jm_, number E0q)	return
bool IkZ5 <- 893e01
func talJ (var Oi8[2e-13,40.614,682.973E-89])	return
'''
		expect = '''Error on line 6 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1042))

	def test_1043(self):
		input = '''
func KNNb (number f5ZO[69E+93,0.325])	return 13

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1043))

	def test_1044(self):
		input = '''
number eL ## v233_KW !(
number gtR[8,32,64.772E-90] ## yL(l[4>6B[r }:TSP
## X!,s9xl,Ld#78@ Ct)B;
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1044))

	def test_1045(self):
		input = '''
## 8FJ
func FVu (number XzL)
	return false
func XB (bool OoC[732.842e+98,644.327])
	return "'"'"R'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1045))

	def test_1046(self):
		input = '''
func ri0 (dynamic hBDx)
	return

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1046))

	def test_1047(self):
		input = '''
## tI#]GrSUdsY[k>UTSa
number yz[11,9.689E+41,626] <- "h'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1047))

	def test_1048(self):
		input = '''
string Krj[95.205e64,2.377,4e+50] <- 4 ## ~m2)
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1048))

	def test_1049(self):
		input = '''
func aO3D (dynamic k8, dynamic u6p5)	begin
		for hi until e5 by "'"h"
			return false
	end
string qwk[186.294,976.991,1.556]
func SaDF ()	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1049))

	def test_1050(self):
		input = '''
##  cscHc 0}#Q69!u^43mZ
var OIs6[8.811E93,818e92] <- 34.226 ## P.R3Rt5R3)XDurq,Lf
number Mth[949.119e+26,478.783,7.874] <- vN
bool lA_A ## #sZ{UAkq~u3J7*PPAN
dynamic a5j9[83.443E+39,680,37.436e92]
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1050))

	def test_1051(self):
		input = '''
number sYLn[6]
var aNPt[4] <- true ## fw
number n0 ## cLtPA
dynamic y04[808,87.342] <- TC
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1051))

	def test_1052(self):
		input = '''
## *)GQ;
bool z6U
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1052))

	def test_1053(self):
		input = '''
## 7#!;W
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1053))

	def test_1054(self):
		input = '''
string YD[32.631,0.150E37,1] <- 2.213E41
number Dp[17E+87]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1054))

	def test_1055(self):
		input = '''
func QTq (number vt0[7.955,140E-65], var Sh)	return Wq_l

func uv (bool MEJ[85,430.072e45])
	begin
		## 8V5T7Z]
	end
## bPXx!
string PvRC[29.493E+26,7e+65,489.429e+35] <- "q'"'"'"'"" ## 9BYD$fKY:?#=+
func UQ (bool EhxL[342.508,64.111e+64])
	return "'"'"l3'""

'''
		expect = '''Error on line 2 col 37: var'''
		self.assertTrue(TestParser.test(input, expect, 1055))

	def test_1056(self):
		input = '''
var Ak6[502e28,5E+93,965.759e47] <- sd ## {#TJ!
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1056))

	def test_1057(self):
		input = '''
## moLC6
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1057))

	def test_1058(self):
		input = '''
## RVbF^
func UP ()
	begin
	end

string bMn[2e+48,0E+34] <- 40 ## -ai[T0;x>$XK~ Q@
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1058))

	def test_1059(self):
		input = '''
## 9[&EHiwa4hR{o&w*U
func vR (bool fl[0.498E05,75e-18])
	return OA
## UH6yAKDI^FQg.@Kt3=nJ
string hcWp[377E-11] <- B1B ## g|/F5e[=Im+^M_Eg&a_
func GB (var slcI[651E+97,9E29], dynamic jGO)
	return true
'''
		expect = '''Error on line 7 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1059))

	def test_1060(self):
		input = '''
dynamic b8E <- "=[" ## m*ciron]Tv~6+D6bP
## _QA
var Sf9[3,537.331] <- S5T ## A:"SWQ>{czv^ONSS-
func iBWR (var Xoyq, var wEp, bool Gv[57E+05,78.703,233])
	return

## lxhbW
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1060))

	def test_1061(self):
		input = '''
## #oW6
## =u%C.01N)7y3lEp{^rB
## ?
func imQk ()	begin
		return
		## im1=5)P7
	end
func Nm (var bqZO, dynamic dwE[6,97.258,5E92])	begin
	end
'''
		expect = '''Error on line 9 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1061))

	def test_1062(self):
		input = '''
func tss (var lT, bool ya[2])	begin
		k0B <- 314
		## (KpZgnnS;56bpiXlrs+"
	end

## ~0FXCI9.bc50#b8
var zRVz[32.062E+12,80,147E-95] ## 8p]
string D8[5.676,2,45] <- "'"x'"'""
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1062))

	def test_1063(self):
		input = '''
number zK7 <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1063))

	def test_1064(self):
		input = '''
func B2Ew (string U9nn[3E-39,6.933], bool dYP[6,8.546])
	begin
		return true
	end
bool be[34,13.043]
func Jy9a (bool DTP, number Wk)
	begin
		if false break
		elif xj9P bool B2I <- qVcD ## _Wg I
		elif 4 h0W()
		elif "'"fNU2" break
		elif Uu return "'"Y"
		elif 33.009E+98 bool c1 <- "#'"" ## 69lNitl~{+O>Qe2WZm0/
		else zFfG(114.675E+50, true)
		dt26()
		var HmlQ[145,659.775e89,600.384]
	end

'''
		expect = '''Error on line 9 col 5: false'''
		self.assertTrue(TestParser.test(input, expect, 1064))

	def test_1065(self):
		input = '''
## q4qSqI=L5_?;
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1065))

	def test_1066(self):
		input = '''
## 4Q<s/AXhN))Uug*&>
## JNT|a|+1pVG]vRs
func a9a (string WJGk)	return
number wS <- 8.792E-83
func Oqv ()	begin
		## ]8
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1066))

	def test_1067(self):
		input = '''
bool zhH
## ~.gB)
func WAB ()	begin
		for WSSQ until uf8 by "k'""
			for QB7 until "i" by "v9'" ""
				for iO until "}'"" by 2.372
					continue
	end
## !b1)o[c+t..F|Ws i
'''
		expect = ''''''
		self.assertTrue(TestParser.test(input, expect, 1067))

	def test_1068(self):
		input = '''
func J_ (bool sx, var eJQ[6E+56,94e+14], string Z5[792.817,649e+23,83.932])	begin
		## 8+>l.
		return
		## 1o)
	end
func liYn (string EvV[57.003,9.327,5], dynamic lHBG)
	begin
		## l#jYn#Z%^[N
		if "l'"'"" break
		elif "$'"'"Y'"" break
		else begin
		end
	end
bool YTVt <- zE
'''
		expect = '''Error on line 2 col 18: var'''
		self.assertTrue(TestParser.test(input, expect, 1068))

	def test_1069(self):
		input = '''
## 6>
bool vB0 <- Ak_V ## M/@_Y
## ji(w|SO/hNE.~f
number sOu9 <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1069))

	def test_1070(self):
		input = '''
func SAz (number apnZ)	return

number IBT[82e17] <- "'"" ## Szynsj/
func MF (var LIc, string S0O[570.367e+92,692E-27,2.580], bool lz)
	return

## tW
'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1070))

	def test_1071(self):
		input = '''
func qzH (string tpU[4])	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1071))

	def test_1072(self):
		input = '''
dynamic Ge1X[73.208e-00] ## {Y
## 0&3Y>5^Yk
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1072))

	def test_1073(self):
		input = '''
func MYLQ (number PzM[960.925E+49,128.097])	begin
	end

## `.UA6XfkPEUK7">+qkj
func Iaf (dynamic LLgI)	return "'""
func B2K2 ()	begin
		## )Ms~^:s;]TlaI~g
		## #2.)
		for lrT until 50.828 by 2.569E-61
			bool y6[22E-69,609E42,2.497e49] <- Q4Vc
	end
'''
		expect = '''Error on line 6 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1073))

	def test_1074(self):
		input = '''
string gx[9,686E+13] <- true ## b*&S[[V"Y^t!`mg=~Ou]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1074))

	def test_1075(self):
		input = '''
func Ftk (string rptH[9e+93,3e93,0.855], dynamic T6[533.391])
	begin
	end
## 1XA9;ZVP5JB%[k&+,oK
string Xqj3[4e-29,173e+45,43]
'''
		expect = '''Error on line 2 col 41: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1075))

	def test_1076(self):
		input = '''
bool inJ5 <- 3 ## zm5
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1076))

	def test_1077(self):
		input = '''
bool zy <- 54.681E50
bool whms[5e36,60.092e-18,4.766e18] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1077))

	def test_1078(self):
		input = '''
## u>yp^)cO3oMwzCxu
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1078))

	def test_1079(self):
		input = '''
string vZ <- 924.352
bool P5zZ <- 7 ## YHPo?]w[kR-#?00
func mOj_ (string LHB[2.934E-40,768.889E+01], dynamic F1V[9.085e-53,999E-23,27])
	begin
		Io65 <- gak
		##  IGD:no#zz
	end

var Uc[95] <- "'"'"'"'"'""
func kJ (string zyU4[947.967,92E91], dynamic pI, number Pm)
	return

'''
		expect = '''Error on line 4 col 46: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1079))

	def test_1080(self):
		input = '''
number Atf[65e+17,3] ## GD!
string EfK[44E-19,3,34] ## <e?ZzYmcdK?9uC]hLB"
func iwv (number Sux[987e80], string KaSK)
	return true
## 7G
number dXEz[0e37] ## na<UTn
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1080))

	def test_1081(self):
		input = '''
var LZAa <- false
func MO (bool WXM5[425.539,42.988], bool gX4w[59.462e86,38,64e-13], string z7e[55,4.367,6E59])
	begin
		## =]^F^LGc0~F
		if false for MP until sV by A7un
			Qa <- true
		elif false break
	end

## nz6i`?YejIg?J
'''
		expect = '''Error on line 6 col 5: false'''
		self.assertTrue(TestParser.test(input, expect, 1081))

	def test_1082(self):
		input = '''
func PLuF (dynamic ZWeO, number GT)
	return
number Rih1[65] <- false ## :i~
var o19 <- zupn
string cK <- Km
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1082))

	def test_1083(self):
		input = '''
dynamic BvH[834E+72] ## G|r@OOTI4}8
number Cr[7,911.350E93,9.458e48]
func cseH ()	begin
		## Qd.QO!dD?FH-}=9]tb@4
		## [
		## E]=Q@W{
	end

func NO_A (var Rc[4])	return

'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1083))

	def test_1084(self):
		input = '''
## RB=(=*ds@{i
func RooU ()
	return
var e_Dh <- true
## 7qD;W$^<k}qa
func AA (var ucf, var WtB)
	return "]'"'"e"

'''
		expect = '''Error on line 7 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1084))

	def test_1085(self):
		input = '''
## #RP.=[9Df
string AgO <- LARS ## }K[@-
## G&4Y}nb:SAOJ"0y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1085))

	def test_1086(self):
		input = '''
bool gUh3[0E-04,81,468] <- "'"'"C8"
## yh~u`0!rpDeTtqi6S*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1086))

	def test_1087(self):
		input = '''
dynamic oKY5[1.829e+13,988,5E+96]
var c2 <- 2.637e+91
func Zp (dynamic WyCI, bool XLR[1E+97,722.233], dynamic jAR)
	begin
		## dK|k-b
	end

func G6 (var ryO[5.481e-81])	begin
	end

number us8B <- "'"i" ## ZC$5
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1087))

	def test_1088(self):
		input = '''
dynamic japN <- no3 ## _Ec>/ykK2
dynamic sY[66,391,7]
## {DT_;;@v}{ZG!{7=bXS
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1088))

	def test_1089(self):
		input = '''
## &ehqJ
## n6G3(9+
func pH (var Lwoc, dynamic KT[543], string K7z)
	begin
		begin
			continue
		end
		## pI 2$uWy
		if 867.213e02 number vk
		elif d_ break
		elif PH uv(dUqg, 444.804, 24.194E+22)
	end

func B1 (dynamic oP[50.575,16])
	return

'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1089))

	def test_1090(self):
		input = '''
##  bxF%W
bool tU[9.013,931.868e-18,8.447] <- "'"gj0" ## k{A2<A r#S2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1090))

	def test_1091(self):
		input = '''
number Hv[949.664e-33]
## bo
## ^tm1}8
func hw (dynamic tA[9E92,8,16], string jx[5,8,291.444E+04])	begin
	end

## ko|""}{;UVhIBJ
'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1091))

	def test_1092(self):
		input = '''
dynamic Lr[6.290E+01,6E+69,8] <- u1 ## -18a@
string MYNX[561E64]
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1092))

	def test_1093(self):
		input = '''
## ,?"Gob[#]
dynamic M5
var i9 <- "'"'"" ## ^FOCZ(c|i+w6sfm@
var t7[2.429,71.980] <- g2 ## JT>1><oFFjV(8EuA,
bool SSr ## &`1v*P!JN>RoP$
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1093))

	def test_1094(self):
		input = '''
## D
func BVpG (bool jR[92.718,7.447,5E72], var ucC[66e07,5.965,47])	return 76.063
## a6ulV
func II ()
	begin
	end

'''
		expect = '''Error on line 3 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 1094))

	def test_1095(self):
		input = '''
dynamic JQ <- "Y"
func Ij ()	begin
		## nfm8w]Ff|8+{ql-
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1095))

	def test_1096(self):
		input = '''
## ^^.68W1UCJ]b&]WMI
func fI (number Wtml, string Ols[8], string z7[6.082])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1096))

	def test_1097(self):
		input = '''
func Za4 (bool q1yI, var VzO[25e+98,3])
	return

'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1097))

	def test_1098(self):
		input = '''
dynamic H3F ## Qx`Mr:QiEEd"fKKsBt
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1098))

	def test_1099(self):
		input = '''
func Ec (number TQPE, dynamic Hk[560.279,487E03])	begin
		begin
		end
		## F^g84Y
		## u+c6TbLDJ.qEh~[4o
	end

'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1099))

	def test_1100(self):
		input = '''
bool dZ[27]
number qZ6[25.577e+52,33.906]
number Jg
## 0vq
func Nx7 (number H7[287.713e+73,44.372e-32,553e+28])
	return false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1100))

	def test_1101(self):
		input = '''
func nOob (number yUDI, string mse[683.572,7.117e64,990.306e-23], bool F2K)
	begin
		return
	end
## E_*Oyy[,
func gDm ()	begin
		for C_ until "'"'"'"" by false
			return
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1101))

	def test_1102(self):
		input = '''
func YIAJ (string Cofq[60,4e-43,38.476e+14], bool jj89)
	return 2.860

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1102))

	def test_1103(self):
		input = '''
## 9xdm+jFm6`kD[j5bg
func uo ()	begin
	end

func FyU ()	begin
		for mPEl until true by "'"'"zw'""
			return lQpC
		## l3upc,%
		## *<=!dDVExOg!I
	end
func gz0P (var eR[308.554e09], dynamic ZfM)
	return

## S@.O*sM2mx|}_
'''
		expect = '''Error on line 12 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1103))

	def test_1104(self):
		input = '''
func tvIw (string kelO[63.941], string p_xL)	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1104))

	def test_1105(self):
		input = '''
bool Ov3S <- yev
dynamic vL[7] <- "'"N'"" ## U(&CR
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1105))

	def test_1106(self):
		input = '''
bool Tfsm <- 324.983e+65 ## 68r"<r`R
number WtiF
string R7o
func WW (dynamic K3GD, string kS9T[982.513e14,71,3.865E81], var Xh[943.171e-04,989.838e+77])
	begin
		## Lmy%7*0mx76dBtKb|;bC
		ro["o'"'""] <- 4.641
	end
func gN (var kQ, string yL[0,81E11,0.368E+73])	begin
		## 71gX%r6w3kchSC
		## 0sTl:*{z,
		for UxX9 until "'"H'"" by "'"'"a'""
			return
	end

'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1106))

	def test_1107(self):
		input = '''
## *v(O#ES)%J}3cfp=
## KIfKN$>^WVl1
## cs4
bool SH <- 47.952
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1107))

	def test_1108(self):
		input = '''
func glBE (number MaS, string agh[48.990E84,91.079e+50])
	begin
		continue
	end
func Cn8w (bool ifi[57,39])
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1108))

	def test_1109(self):
		input = '''
string Bf <- mObP
func vkZ (bool qD[19.074,99,403.033], bool Vux, bool HRIg)	return

bool Fa5[39E+23,19e+29,480e-08] <- Eci
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1109))

	def test_1110(self):
		input = '''
number BOZ[367e-04,94e+23] ## nTg0K`Z~x
string TLs
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1110))

	def test_1111(self):
		input = '''
func jwOM (var BEHr[3E+89,351.832,61e80], dynamic ee[3.718e+68], var mv[2,51.383])
	begin
		break
	end

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1111))

	def test_1112(self):
		input = '''
dynamic Pre[966.017E08,6.696]
func c4o8 (string nVGY)	begin
		## Q`o2Me
		for suM until true by true
			yccc <- "'"f@'"$"
	end

string bRI0
dynamic zmRx[0.403e+92,530] <- AI
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1112))

	def test_1113(self):
		input = '''
## =@>iY^_W:iE&
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1113))

	def test_1114(self):
		input = '''
var AHA <- true ## l1|Iu>H6H:V6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1114))

	def test_1115(self):
		input = '''
var LMg <- K5
## YoH)so#
## BUkOiV#ef
## .RlWyD`GZ0dlzB J 
## :
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1115))

	def test_1116(self):
		input = '''
func CrNJ (string Kxl2, string sZ7[267.939], var FCxj)
	return "~'"'""
func j13 ()
	return

func hA (bool qPFg)	return "`e-'"J"
'''
		expect = '''Error on line 2 col 45: var'''
		self.assertTrue(TestParser.test(input, expect, 1116))

	def test_1117(self):
		input = '''
bool wgC ## |j#+vXFLF:Z
## X>YB#I)#7ORvrh|&
var Slo[745.491] <- eSK ## 4xwEW*SXMO|VcK
string ajQ[622,3.749E+41,8.195e+96]
func YtBI ()	return
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1117))

	def test_1118(self):
		input = '''
## =T
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1118))

	def test_1119(self):
		input = '''
func Wx ()	return hp8
## kHl+&i+q%?4v)"!OdOr.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1119))

	def test_1120(self):
		input = '''
func N0k (var AvXL, string iaJ)	begin
		return "'"Y"
		for k2og until 2.816 by 3.211
			begin
				## FO2`y4pp2z$3)q
				continue
				## *C?QYpen}j
			end
	end
bool W_ <- 0
func QJap ()	return 356e84

## }*}jp$rqt_T5C
func XO7l (number UrDv[42.173e+80])	return

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1120))

	def test_1121(self):
		input = '''
func fxS (string Ksk0[72e-90,928.907e-63,4e21])
	return 68

func TN (bool r93W, string uKw[3E-81], number Jr[4E-01,175E85,6e55])	return

## j(;)>] 76MA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1121))

	def test_1122(self):
		input = '''
dynamic S3Fx
func Jdp (dynamic uNUo[6e14,802.035E-18,569E43], string HLSL[700E+22,4], bool cx1M)
	return 80e+69
func zfW (var Aoj[442], bool p5Kq)	return
## WMo35`?&8.|{$e 
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1122))

	def test_1123(self):
		input = '''
number TXsF ## :Ri?.UXvC9X
## jUZ9X}zp<"DlI2M;`
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1123))

	def test_1124(self):
		input = '''
## vJrgUF nIQ-
bool kK <- "'"'"" ## U<(90F8<<<< )S%bUd_g
## ul9V4An_qy|r}H
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1124))

	def test_1125(self):
		input = '''
func jr6 ()	begin
	end
## N
## .^(t(G4IK>s
string itZ9 <- Ge ## H{Vb!"#JvH?z}YrItO$
func NLWw (var QSXG, bool q4L[456E-58])
	begin
		## LZ7yM zYk
	end
'''
		expect = '''Error on line 7 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1125))

	def test_1126(self):
		input = '''
number Nqd ## Dt!u[
## O
func zW (bool WNhO)	return Ihv
func Wh_ ()	begin
		string RGko[1e+48] <- "7`"
		## {0|rOgi,8RUwIbJA2P
		vUTr <- true
	end

## 5b!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1126))

	def test_1127(self):
		input = '''
## [rbTV@>5J>Cb*
## :)YoGwGygU6P+hD0
func Sq ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1127))

	def test_1128(self):
		input = '''
func p86t (dynamic mCk)	return 87
func E7sJ (dynamic ukC, dynamic Q7zw, dynamic O9)	return
## A8ugT
func RO (bool ReC[23.984E+66,13.676,175])
	begin
		for IrB6 until 57.389 by lW
			begin
				return
				## 3Z<xM{uTM(JIS]y5
			end
		return true
	end
## ^#D;R=JwdT)tU
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1128))

	def test_1129(self):
		input = '''
func Jr ()
	return
number qU6[62e94,672,2.064e-51] ## OEyUbDB^i+^7]iR%9|W
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1129))

	def test_1130(self):
		input = '''
number wn4 <- "n" ## j3"E$ V^TV4E2:Gb"qc
number PG[1.595e-40,99] <- "'"'"7"
string vMQE[342,9.489] ## GFhw1`
## !5^>IlU#80"AQ
func dGcX (dynamic Ob[546.804,284e43])
	begin
	end
'''
		expect = '''Error on line 6 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1130))

	def test_1131(self):
		input = '''
number kf[9.558E90,5] <- false ## sm~
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1131))

	def test_1132(self):
		input = '''
string ap
## k;&)Hfcm)t
bool qBW ## Cq^ ,f72g!v:LG,6n[
func MLC7 (var hzQ[70])
	begin
	end
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1132))

	def test_1133(self):
		input = '''
bool lQd <- 22.186 ## K^Mg=^
var Jh[5.386,166e08,5] <- true ## z]k)7{x-/(v3VZg
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1133))

	def test_1134(self):
		input = '''
## C-sU2VNwk92p05@@4o
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1134))

	def test_1135(self):
		input = '''
bool WO[4,34E86] <- false ## g84u2Iv/C_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1135))

	def test_1136(self):
		input = '''
## ?PK
string UWTx
string vQg[1e+68,59E+87,62e+07]
## @DE8j/p=H]
## 9Y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1136))

	def test_1137(self):
		input = '''
## z?:4
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1137))

	def test_1138(self):
		input = '''
dynamic bpRO[173.422e03,2.052,45.088] <- ":"
bool oUBm
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1138))

	def test_1139(self):
		input = '''
## Gq62x:iAce>7.J0
func nW6k (string S_z[1.790,12], number L9y7[4.307E59,8.503], string RU[126.172])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1139))

	def test_1140(self):
		input = '''
## VgY:dbG.|YWo FJp
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1140))

	def test_1141(self):
		input = '''
number bWZ3[9.113,34,938.440E16] <- false ## w($5}Q"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1141))

	def test_1142(self):
		input = '''
func n7 (bool ZNTp)
	begin
		## V6{L#kMJ<(m0
		## -4
	end

bool qBYz <- wp ## J)}9i}l>q8~6~qsJob|
## c
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1142))

	def test_1143(self):
		input = '''
## cmZo$?
## CJ
func BmKS (bool WUj3)
	return "G'"'"'""

dynamic xiR ## ost3,STOLL,.v&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1143))

	def test_1144(self):
		input = '''
func wDhf (string p2y)	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1144))

	def test_1145(self):
		input = '''
bool b9y <- "'"~^" ## joxFlCf97[B"W~5P
number B8C <- pV
string Xycn ## H`B=zCAbv
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1145))

	def test_1146(self):
		input = '''
bool loz ## B.AS],p"nnVCj_,En
dynamic DY <- YY
func Y9ad (bool H2)
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1146))

	def test_1147(self):
		input = '''
func uee (bool gR[98.934], var HP[8e11], dynamic SI)
	begin
		if Uwu break
		elif false for WH1 until false by TF
			LPSe()
		elif true for edgO until x4 by "n:"
			return
		elif "['"6" begin
			## e}H
			return
		end
	end

string H3gF[341.997e+19] <- "'"" ## omI
'''
		expect = '''Error on line 2 col 27: var'''
		self.assertTrue(TestParser.test(input, expect, 1147))

	def test_1148(self):
		input = '''
dynamic Qdi[390.412,6.203e+06] <- "%'"'"N"
## >jbb2_#a^Y
## MhGT^8sMdfiiIM2
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1148))

	def test_1149(self):
		input = '''
var LO[654E-14] <- false
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1149))

	def test_1150(self):
		input = '''
## .7g@a(rjIaU+
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1150))

	def test_1151(self):
		input = '''
## 1b]3I/gEZ6 (
## gs4ChtuaB|=Gr6Q|]k
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1151))

	def test_1152(self):
		input = '''
## *vkNgtbf*0cOQ
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1152))

	def test_1153(self):
		input = '''
## OP+ooQ2[r]^</nZl26N)
func d4 (dynamic m0C, number SJi, dynamic Xac[116])
	return

## 8 t
func Ev46 ()
	return QO
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1153))

	def test_1154(self):
		input = '''
var Yh[1.055,42E62,3] <- false
func tb ()	return
string v1
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1154))

	def test_1155(self):
		input = '''
func r4sU ()
	return

func UNW (bool ZUNZ)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1155))

	def test_1156(self):
		input = '''
func LZZ (number vgUn[11,3.569E-90], string oenw[4.054,87,3.001], dynamic RCC)	return "'"?#z'""
dynamic B6
'''
		expect = '''Error on line 2 col 66: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1156))

	def test_1157(self):
		input = '''
dynamic v_[2,47.979e-63] <- 2.372
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1157))

	def test_1158(self):
		input = '''
## ?;{J|7%
## Zl;[80mV_Y?w7Wrf6$N&
func XR0u (bool OZ, var ieN[6.284,719])
	begin
		## |`I
	end

number Gxj <- false ## 4$mr1V>
'''
		expect = '''Error on line 4 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1158))

	def test_1159(self):
		input = '''
string yOZ[157.505e37,8,4e+17] ## uA(zjT yO^X!5)!
string kB84[8.258,30.771,5] <- false ## f_@|UHP>mn`S
number hC30 <- 4e-99
number PNP <- J5n ## nSe]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1159))

	def test_1160(self):
		input = '''
## A.C?u|T+7r/Nm
func lD (bool mzI, number UjZN[62.011,723E-66])
	begin
		return iEtz
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1160))

	def test_1161(self):
		input = '''
## R7A&Mq3V/)+!BS/I2O
string ha[6.951,5] <- 93E+64
func cCH (string DcR[72.904e+11], var Bgh, dynamic xB)	return 6.329E00
func D5Ix (bool OP)
	return false

func JZW6 ()
	begin
	end

'''
		expect = '''Error on line 4 col 34: var'''
		self.assertTrue(TestParser.test(input, expect, 1161))

	def test_1162(self):
		input = '''
string chYS <- false ## p,7
dynamic gZ[161.240,246] <- tgzW
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1162))

	def test_1163(self):
		input = '''
number MX6 <- mrU
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1163))

	def test_1164(self):
		input = '''
## zQo2
func ZSlz (dynamic Egg, dynamic vz[8e-44,1], var iMZU[82e-13,345])
	begin
		return "'"'"'"~"
		RL()
	end
dynamic zBVm[8.789,6.597e73]
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1164))

	def test_1165(self):
		input = '''
var tHBv[520.707,14.489e79] <- LRa
## F8Po&uU|1i("
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1165))

	def test_1166(self):
		input = '''
string py[81.325] <- 4.502e38
func YB ()	return ":?5'""
number yC ## t.at6k/#QRovE +
bool pgf <- 23E+97 ## 6
## K:NG_Wc%N!/:j,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1166))

	def test_1167(self):
		input = '''
number hi7Z[3,2.437E-57]
## |56xlAREv2_%G
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1167))

	def test_1168(self):
		input = '''
func xJW6 (bool QKN, number c_[3.903])
	return true

## YX6j,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1168))

	def test_1169(self):
		input = '''
## bTLQL
func z1g (number uX[6.306E59,20.525e+62], dynamic PSd)	return
'''
		expect = '''Error on line 3 col 42: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1169))

	def test_1170(self):
		input = '''
func vbC (number pIho[194E-56])	return r3WO
## -4x:fTwB6UCL4`k
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1170))

	def test_1171(self):
		input = '''
func hNdf ()
	return 564e-29
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1171))

	def test_1172(self):
		input = '''
func dL (var mv, var F5i, var Ldp[3E49,774.941e+80,5e+30])
	begin
		## )?/E
		bool rw <- 219 ## FLHK8LT
		break
	end
## Iy8TP>5+afMV/UD!XJn"
number cNFM <- "'"h/'""
func NoF (number lwxV, string hY[48.791e96], string ug[318.162,27.206E+77,6e-92])	return

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1172))

	def test_1173(self):
		input = '''
## *QdTNqijQ1`o-3.;q2V
number khSJ[1.397E+71,0.952,16.593]
## aK([b#}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1173))

	def test_1174(self):
		input = '''
var FKcp
dynamic ET ## *z{Tz$^aoON9="55,^:
func TFAl (number xN[84E-75,6,93e14], bool xKLR[8.491e-17,9e-45])
	return true

'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 1174))

	def test_1175(self):
		input = '''
dynamic t19[414.015e+46,172E56,4.766e66] <- fnS ## mcE|A=
## !8BZ4
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1175))

	def test_1176(self):
		input = '''
func q6 (dynamic wH[32])
	return 3

var aQ5 ## )p sdQVKb [(HrNmNz6
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1176))

	def test_1177(self):
		input = '''
## DN(S-
func XcVg ()	begin
		## ={yH.}Z`@H
		## xF;Z
		## ;bkedMFSi0Jc
	end

## jx l),IT#FC /`^h>13"
## XIn~?^8FtEY{ ?)
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1177))

	def test_1178(self):
		input = '''
bool yu0[4e-72] ## ^Jrjf]Ply2r-Xtl#O
func gNJ (bool akrf, bool J9K[4.242,36.015e05,5.953e41])	return ueC
## $
func IwxK ()	begin
	end
bool EHTI <- 46.627
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1178))

	def test_1179(self):
		input = '''
## B*!k>&N$i(
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1179))

	def test_1180(self):
		input = '''
## qRZ*j3z<Huu544 
## p}[D!lt9E=
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1180))

	def test_1181(self):
		input = '''
## T@.6E
func sg1s ()
	begin
		continue
	end
func pg ()
	return TCR

func lW2 (var MTYD, number IZ8I[648], dynamic fuYm[13,8.194E+27,49e80])
	begin
	end
'''
		expect = '''Error on line 10 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1181))

	def test_1182(self):
		input = '''
## %lfEP=,
## bU3$E:{v"!Je
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1182))

	def test_1183(self):
		input = '''
## +:]cY pz#vK@&0v<
func qwm (string lfM[396.296e+06,365e+43], number MK_)
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1183))

	def test_1184(self):
		input = '''
func ioRH (bool gZM)
	begin
		## 2Z>51
		## .CRT_$b5AqTqEKoR
	end

var MVLk[1e-38,9.312] ##  CLwdEIC]u|
## nx?7v^ziVt7:W4m}-4
func qBBS ()	begin
		## I$tShn64wCOSOmgWT
		return "'"'"t'"'""
	end

func Ioc (bool tYF[71E80,183.003E+03], string WWc4[231.852,442])	return Cn

'''
		expect = '''Error on line 8 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1184))

	def test_1185(self):
		input = '''
func k_og (dynamic ej6H[8.356e-14,98E-43], dynamic Phk, number i_x[80,749.821])
	begin
		## 0uPYsox,g"=Bu&}16~X
		## Mk5a"z
	end
var eLdh[62E-76,8.499E+02,6.640] ## ,=8x_$O>{>"+ Nmv}*
func BwY ()	return
## Vr
var FSu6 <- "'"4l"
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1185))

	def test_1186(self):
		input = '''
## F
func IXA ()	begin
		## $vD)&m=g;z|W
		break
	end

dynamic Bi <- false
func XV8a ()	return
number n_A8[0] ## cWvn
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1186))

	def test_1187(self):
		input = '''
dynamic f7fM[9.938E+53] <- itK
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1187))

	def test_1188(self):
		input = '''
## D@!+-
func n2TV ()	begin
		## Z*16:E21V
		## A>TFgPYN0`-,?
	end

## ^F0>lmS#]VGk@
string qnp ## j3}[>C&
bool GDQ <- dZEE
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1188))

	def test_1189(self):
		input = '''
## XC>~YbA5&]9xKxqsE`r5
## 9<YA{r
func Go (var LdYp, number ylu, bool TA[125.164])
	return "`'"L"
func G76 (bool jqvX, number k1l9)	return

## G5@EQ) [
'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1189))

	def test_1190(self):
		input = '''
bool bOD[0.126,95,93.265E-14] <- "^" ## ||rU*P^l5Z)41MGjpT&
func mnS (dynamic RvUe, dynamic BIm[71.553E27,69])	return

## /?@NgE |@B+
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1190))

	def test_1191(self):
		input = '''
## S:?I`O J2Dz"iBw
number oGC <- "'""
## ivD"K>^2Z|Pu/`
bool ci[985,76E+13] <- 7e92 ## B$%;O3zVRY#r=@|+M
## 7(KdvVq,56M7~Wg^U
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1191))

	def test_1192(self):
		input = '''
func V9I (number BqnF[87.829], bool cJN[1.550E13,95.626E+39,7E+78])	return
func a_Q (bool Zz4)	return "s'"'"(*"

## qBn8
## v6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1192))

	def test_1193(self):
		input = '''
## UT$dfh)NC
## Z2
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1193))

	def test_1194(self):
		input = '''
## Tba}@H:;!e+97|$*
func s22s ()
	begin
		## Gp8N2W=R@e{x@b)ORqS0
		for Qqk until "'"" by 175.719E52
			break
		begin
			## %3FP
			## ke4C}
		end
	end

func IWL (bool GEdY)	begin
		## qBv*H>N"O04ZUqh|5
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1194))

	def test_1195(self):
		input = '''
bool mf
## >z)3{Et~
number YjLr <- "'"Tq" ## 1x2TO@
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1195))

	def test_1196(self):
		input = '''
func sP (string ip[437], var dJ[81.235E+97,431e62,341.517])
	return 51.080
'''
		expect = '''Error on line 2 col 25: var'''
		self.assertTrue(TestParser.test(input, expect, 1196))

	def test_1197(self):
		input = '''
string qx <- 112 ## 5|LOA0!
bool lHPi <- "w#'"'"&" ## HXwT
## v]c-4[<xqT0DX
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1197))

	def test_1198(self):
		input = '''
number Cp6v <- "'"'"'"" ## 1.>G;yw
string SH3R <- sWd
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1198))

	def test_1199(self):
		input = '''
func k0 (var Fn[8], number IKx2)
	return 9.028
dynamic poY[450,69.221e-22,9]
func On (number K7l[2.342,88.671], var A5vv[78,2E17,181.110E51], bool ju)	return 0e-18

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1199))

	def test_1200(self):
		input = '''
dynamic qZc
## UOO}EM=
bool c3lU[7E83,0.306,1.115E-03] ## i 2]^Sp,@=tpJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1200))

	def test_1201(self):
		input = '''
func vL (dynamic OGS[1.044e-16,82E57])
	return
func EuQ (var SOor)
	return Jn

bool Kkm[2e86,489.690]
bool zZ1
func D75t (string LU)
	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1201))

	def test_1202(self):
		input = '''
## TQpb{F*!}n]]hV
## zR
func xa (number vHZ[978], var Am[821e75,361.612,423.722])
	begin
		break
		## Og=]HD4{:rQ-yJTS
	end

func Ro ()
	begin
	end

## 4F5-0;dvsNP
'''
		expect = '''Error on line 4 col 26: var'''
		self.assertTrue(TestParser.test(input, expect, 1202))

	def test_1203(self):
		input = '''
func ll (dynamic pu[3.952e-50], var VCb, bool jAgZ)	return true

bool t0q8 ## tRFEX
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1203))

	def test_1204(self):
		input = '''
string uat
## rn
## |w>j?Khbz
## A$|So{coO(yT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1204))

	def test_1205(self):
		input = '''
number FD <- "'""
## 2U.S8l:W<)3
number RoXh <- false ## k6e}$Y}]`,&}
## 0eM
## 10TFl)]g^>2dg
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1205))

	def test_1206(self):
		input = '''
## jd.R1oO35
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1206))

	def test_1207(self):
		input = '''
func dpaQ (bool vUr[8,8.493e28,9e+95], dynamic pf, number HVBD[424E+03,29.338])	begin
		break
	end
## e
func jEn (bool FWs)	return "'"'"'"'"'""
## hu
func sAoD ()
	return WnnS
'''
		expect = '''Error on line 2 col 39: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1207))

	def test_1208(self):
		input = '''
func Xp2 (dynamic hX, dynamic ma[0.193e91])
	begin
		## Ct{.Pti4Wu)3T0F
	end

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1208))

	def test_1209(self):
		input = '''
## =$tb+Y3:LWb9mB+ky?#
bool kUk
## aKk7
## U
## q1~/0ZqJxQ{D=+f2Sz
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1209))

	def test_1210(self):
		input = '''
func ovHN ()	begin
		break
		return Xk71
	end

func OX2h (number W7, var LH[0,15])	return iBV0
string JG[6.230,485,32]
## Lwr$
## -z;]-
'''
		expect = '''Error on line 7 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 1210))

	def test_1211(self):
		input = '''
string nV[169,25E+74] <- true ## e;
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1211))

	def test_1212(self):
		input = '''
number PJR[89.352e+18,374E51,452] <- Cr ## 5YST8I
bool Uw[3.055,49E23,4.601] <- "'"F'""
func FxTg ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1212))

	def test_1213(self):
		input = '''
bool Ks
number aR_L[210.448E-65,924e80]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1213))

	def test_1214(self):
		input = '''
func eB (number VB7[43e+26])
	return "Tb'"(H"

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1214))

	def test_1215(self):
		input = '''
string Az6a[4.194,10.881] <- yygn ## w9z@60`
## ]tYvMo5OdSN5:#q
## 5eDp=0mw09b_@*5}8ws
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1215))

	def test_1216(self):
		input = '''
dynamic tmS ## g5P{X0g,MO
## Y5L%<?ZwwANRs**OQ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1216))

	def test_1217(self):
		input = '''
func yYC (bool GTS, var GpKK[1E-85])
	return dm
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1217))

	def test_1218(self):
		input = '''
dynamic DX2i <- 262E-71
dynamic wzJ[706] <- A9q
## 2tY eAF-U`.HOAc
bool X3T[580.217] <- false
## @=O{?@:?
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1218))

	def test_1219(self):
		input = '''
## ]tA %kIt7BCe0"iUb
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1219))

	def test_1220(self):
		input = '''
## aC|v0jPejj7
dynamic Xr3q[2.806,319E+80,9.879e67] ## }%i{
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1220))

	def test_1221(self):
		input = '''
## _TM))
number YQ ## ;g/
bool oiox[1,64] <- "V/l'"'"" ## 0YZRNO7t
func T2 ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1221))

	def test_1222(self):
		input = '''
## BoF@>q|X3
func s3 (number R6k[5,48,6.150])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1222))

	def test_1223(self):
		input = '''
func ZX (bool ysE[85,470.504e+68], bool jRz[309E52,31e-91])
	begin
		## !T*}%MSDX&K
	end

bool ryg <- 819 ## /5mV4cJYh
bool Jl[23.842,389.722e-49] ## )&AuH
func av (number ZUY8)
	return PHnU
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1223))

	def test_1224(self):
		input = '''
func tKI (var Rs[60.214E-46,21.735E75], number PjRP[13e60,61e-00,936E-83])	return 0.210e75

string PFx[6e-82] ## BJ(MP`7Ek
func Pa ()
	begin
		## e
	end

func lQH (dynamic YNF)	return S_5
string P5[998,353]
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1224))

	def test_1225(self):
		input = '''
func VM (var L8jw[464e-58,19.106e+55], var ooH[26], var l3B8[9.268E+99,848E+64,242.317])
	return

dynamic I5O[60.412e-44,48.715]
func Rs ()
	return

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1225))

	def test_1226(self):
		input = '''
## >Cnx[#g]4,
dynamic Gg2b[4.788] <- "'"ah"
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1226))

	def test_1227(self):
		input = '''
string EKz[9.996,3] <- UiI
## %8]"Ec_
## z)z&cPh*4x.
func Bb7R ()	return
string ZY[8.017e+44] ## gG11)
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1227))

	def test_1228(self):
		input = '''
func OEI (dynamic x2z4, dynamic UYl)
	begin
		continue
		## Q=Ie/LMc-k"e>&6_I
	end

func uR (bool D2HR, var A7)	return
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1228))

	def test_1229(self):
		input = '''
func t7G6 (string gr, string sEF, string Wesa[6,6.697e+80])	begin
		continue
	end

## eMK=LMp>0y#)
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1229))

	def test_1230(self):
		input = '''
## mh}VX.cz>_!hfT
## bli
func Im (var lT, string eRjO[6.877e+31], bool r77)
	begin
		## t"8<<P0Ub
		## -3];,VT-w!
		## <RfaW/RJl ULc},
	end

'''
		expect = '''Error on line 4 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1230))

	def test_1231(self):
		input = '''
bool hle[9E+40,17.730,5E31] <- Sr23
var yaR ## HjM.Y[N"YA2t78pm
dynamic JYYF[1,4e59,4.074E+94] <- bTO ## kqZs@z#?h
func kwp (number kTa[72.032], number Mbl[4,39.627], dynamic n3sP[75.708])	return VJC0

## <y[K+5?&4(MuNsd)
'''
		expect = '''Error on line 3 col 27: 
'''
		self.assertTrue(TestParser.test(input, expect, 1231))

	def test_1232(self):
		input = '''
string gSa <- "'"'"!" ## xqjypkWHE9
func i4n (var lj[9.369], dynamic nxu[8.883])	begin
		## i4].[cBr6Ea !^0%r. r
	end
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1232))

	def test_1233(self):
		input = '''
var em[0.896e+17,357] <- 2.699e+89 ## |j{H-*ha *!Jm
func PG ()
	begin
		## <BgZecz
		## a_QWg
		## SP]18Q1FgL1/
	end
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1233))

	def test_1234(self):
		input = '''
string F2Og <- 1 ## QrV,7t&LBxMOKvSh9kHt
## E;5edZ+/a=5|/Ht*
func JB (number WW[9.105,661.890e-95], var JGG5)
	return N1

## _=-&zbfF,$j3jVx@U
## GwdjTmLbh
'''
		expect = '''Error on line 4 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 1234))

	def test_1235(self):
		input = '''
func iC (number Xyrp)	return
string twe[782E+70,13.080] <- "H'"" ## ?
string Nkk6[256,32,277.412]
func yyl (dynamic x6, string tm)	begin
	end
'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1235))

	def test_1236(self):
		input = '''
## aL<gr
## }/_0H1-w?|^:XG*
func jBZm ()	return "'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1236))

	def test_1237(self):
		input = '''
func EBt (string Koc[41.914,1e+13], number uc7y)
	return

func ZLR (number so[0e-57], string gk, string u9V)
	return pFGf

dynamic Wh1[72e+06,382] <- true ## %9 hy!UQS^u)
## h+7B-2BAua)B
'''
		expect = '''Error on line 8 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1237))

	def test_1238(self):
		input = '''
## 8I{Q2(U}ZT2@ve_
func VKT (bool Lb, dynamic DC_0[4])	return

number BD[2] <- Mx1 ## OB
## +rW@PV.yFb=$RCU
'''
		expect = '''Error on line 3 col 19: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1238))

	def test_1239(self):
		input = '''
## :bQ_N?QO_zH#OYt aN
## KpyS1
dynamic gD4X[97E+95,275,736.594e+85] <- true ## B"{|d7b
## Xu
var ac[1.580,6.820E-09,12E+77] <- 110
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1239))

	def test_1240(self):
		input = '''
## RT]2~m!{
func xz ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1240))

	def test_1241(self):
		input = '''
string yZhG ## ygKRKq&?
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1241))

	def test_1242(self):
		input = '''
string ihZh <- 10E96 ## qq8w)
number MG <- true ## 66U(HAp((~W|[*95%
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1242))

	def test_1243(self):
		input = '''
## eX6t<W%E3
func YN (string wJ, var cij, string Bt[83e12])
	return 0E+06
## k6bnnvLq-Tz4RR:JX
bool pljp[46.618E89] <- false ## =jm7[aBT1d24wq,
'''
		expect = '''Error on line 3 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1243))

	def test_1244(self):
		input = '''
number Uf[527] <- 47
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1244))

	def test_1245(self):
		input = '''
## Q}k~_[oxGZ9kGuC{&`j
number UUf[3E69,692e-14] ## #x)(|x ht;E/:8
func za (bool aRD)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1245))

	def test_1246(self):
		input = '''
number CpJ <- false ## N^66Dnz:%:<^f]F
func X2 ()	return "'"'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1246))

	def test_1247(self):
		input = '''
## vcL!x)}he
number oi[450.262,2.345E-19] <- 739.592e61
string LKk[244.255E98]
number P1uh
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1247))

	def test_1248(self):
		input = '''
## UR_;WpYtJK[)G
## LPkw*Wr&vY
string VkCd[6e-74,877e+80] <- "C'""
func fw ()
	return "'"a'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1248))

	def test_1249(self):
		input = '''
func U5rA ()	return 51

## hB<_|pP9X-|9~ET$
## g#4VsHeK@0
func iFD (bool jc, number Ir6T)	return

var g4A ## kA
'''
		expect = '''Error on line 8 col 13: 
'''
		self.assertTrue(TestParser.test(input, expect, 1249))

	def test_1250(self):
		input = '''
func f7w (dynamic UDla[78.303e-46,38.624,86.443])
	return 3.600

dynamic SrA3 ## {=oYso;GqI@QY|-
## i(,9s?ama?rEqucbl,_[
dynamic X5 <- "J?a" ## 3CJAk8[Aj6ZR4U
bool Dvun <- 5
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1250))

	def test_1251(self):
		input = '''
## w
func Zo_7 ()	begin
		## ~9-lvkA?cd&k)kg
		for YKB until 4 by pes0
			cH["*joZ", "(", 481e40] <- WW
	end

number R8u4
## C8M+x
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1251))

	def test_1252(self):
		input = '''
func eZ1 (dynamic qqPu)
	begin
		## "EM3ykA)N1d?
	end

func J4R (bool gW, var pYSW)	begin
	end

## 35U;(V%n1w_9
func Ai ()	begin
		return
		## L9Z=x@wEHSv>{
		## 1us[1NOggK2gh+
	end
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1252))

	def test_1253(self):
		input = '''
func ofGl (string f_, string GvVQ)	return 8.861E+95
func wj (number zqQ2[2,280e-58])	begin
		w9W(48e-25, "l'"'",")
		## %1ot#Fo^MiL{
	end
func Crxj ()
	return "i"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1253))

	def test_1254(self):
		input = '''
## 2E 0:tVbz3yv-U+eoF
func wSZ (number qT, number ro)	begin
	end

## GmxIsJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1254))

	def test_1255(self):
		input = '''
number Hw8o <- ")"
## a?367A
bool p2z <- "b{_'"" ## 93
dynamic cpj
func P4p (dynamic OP1S[2.252E-06,10e08,9])
	begin
		uB <- 3.933e22
	end

'''
		expect = '''Error on line 6 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1255))

	def test_1256(self):
		input = '''
## %YI`@gE_J4
## +MVk"<#^S
## a!~3
string nmq[39,133E-32] ## :BAwr;tcSN-[%uVE,
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1256))

	def test_1257(self):
		input = '''
## O,_/S8IPaf
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1257))

	def test_1258(self):
		input = '''
func TZmx (dynamic CM[7,8], dynamic QywZ[4,4,99])	return fXXS
## P1ONvn7dOc_w
dynamic pU5C
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1258))

	def test_1259(self):
		input = '''
func I2 ()	return false
## ll,N&BG n{
number Ki <- "'"Lq'">"
func zdU_ (number eXM[835,4])	begin
		if ee for Iv until "'"}^'"(" by Si
			break
		elif MIAX return "'""
		elif 795.148 if "-_b" if "'"R" continue
		elif bx var H1D[86] <- "'"" ## p0Kn~;$E"J(CgjM?A
		elif "'"" thlb("1'"6h", "'"")
		elif "Ir#k" begin
			## 4xH^w=~Z({Q
			## _#8UG&7]!;_;
		end
		elif true Awb <- 2E-85
		else return
		else break
		begin
		end
	end
'''
		expect = '''Error on line 6 col 5: ee'''
		self.assertTrue(TestParser.test(input, expect, 1259))

	def test_1260(self):
		input = '''
bool ML <- "h7a" ## 2U
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1260))

	def test_1261(self):
		input = '''
dynamic pZVw <- true
number TjWV <- YMU
func ioY (dynamic Xq, string Nitp)
	begin
		begin
		end
		d8p(false)
		## i
	end

'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1261))

	def test_1262(self):
		input = '''
func eOAK ()
	begin
		number DW5n[7] <- L0
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1262))

	def test_1263(self):
		input = '''
number Xe[33.993E-04] <- "P'""
func cBUh (dynamic Wa[746E22,997e+59], dynamic Wyqz[247E13])
	return kd

var sM[10,4.010E+85] <- CnrM ## c=R,
func YQ ()	return MO
number uS8X <- "[k'"B"
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1263))

	def test_1264(self):
		input = '''
## K
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1264))

	def test_1265(self):
		input = '''
bool X6Y <- Np ## tX%@Z
## _sFH/Yi/s-%#+z!L" ?
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1265))

	def test_1266(self):
		input = '''
## pUQI8cuXiN<b0g{?.{
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1266))

	def test_1267(self):
		input = '''
dynamic JxF[5.623,692,6E37] ## x$;?GK
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1267))

	def test_1268(self):
		input = '''
func tyV (dynamic H7o, string Bfmg[2.291,527.272E94,0])	return gdrU

## [!5W[9_foowW6wD.z
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1268))

	def test_1269(self):
		input = '''
## $Pm#~xG.-L
func TjuC (dynamic s_, var s7D8[72.395e+45,8e-44])
	return
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1269))

	def test_1270(self):
		input = '''
## K,f/1|jF
func etao ()
	return 95.397

func TQ (string NYA)	return true
func HccV (number H7Na, number pi3, bool UG)
	begin
		## SEtO3Z`
		## %n]7tpg#Q
	end
## *hCu?g5*B
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1270))

	def test_1271(self):
		input = '''
bool yL ## }#vcT[9RZ =Ch0AspOl
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1271))

	def test_1272(self):
		input = '''
func eS (number Pcag[347e-37], dynamic tx2, string mPo[67,2.590E-08])	return

'''
		expect = '''Error on line 2 col 31: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1272))

	def test_1273(self):
		input = '''
func Z6 (dynamic VFDw, dynamic KXsH[755e-88,8])
	return false

number Fo_b[2.996,4.027E48] <- seWx
var UAI
func Yi (bool FA, bool bdv[3.910,5e35], var q0[0.932e+45,308.611e+99])	return IQ
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1273))

	def test_1274(self):
		input = '''
## :bNKw
## ,/.yQE!239N__<
string lXE <- ou6z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1274))

	def test_1275(self):
		input = '''
## .
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1275))

	def test_1276(self):
		input = '''
var rq[62,16e+84]
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1276))

	def test_1277(self):
		input = '''
var Nh[5E34,1.023e+18,3.316e28] <- false ## ynl85G8M3MP8|74
## Yf%e:o~+V3IpDN|^^
func Hh (bool ZcIA[27])	begin
	end
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1277))

	def test_1278(self):
		input = '''
## KFSh6q_C-cETMX)XP
dynamic Tt[502,4,47.392] ## 3&d
'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1278))

	def test_1279(self):
		input = '''
number EcE <- 66
var fhST[333.307,629.513,43] ## E;e-(
## kvr|:
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1279))

	def test_1280(self):
		input = '''
func U4S ()
	return
func Qgzh (bool LR[3.208E-98,54.669e+83], bool vwQC, dynamic KHV)
	begin
		## F[Tj.j@jMSLUY
		##  [ru#
		jF["'"vu'""] <- 92.850
	end
## on9>7+k]L$
'''
		expect = '''Error on line 4 col 53: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1280))

	def test_1281(self):
		input = '''
func lMQa ()	return CNk
number r62l[67E-28,0e-95,26e-19]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1281))

	def test_1282(self):
		input = '''
func s4 (var kaN, dynamic o8N)	return
## na]-$Blgd"G[l
bool IL[30.719e10]
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1282))

	def test_1283(self):
		input = '''
func q5 (var pSW)
	begin
		number RE[59e-08] <- true
		## lBM-4tUTl}27tH7w`Z
		if 6.671 return
		else if 436 for wG until 27e-26 by qYYx
			break
		elif 0.946e-93 if 689.991E+24 UF(K3, Wn)
		elif "'"" if 546.876E+13 for enC7 until N2r7 by 1E54
			return 777
		elif vze return
		elif Qt if "W'"'"3'"" break
		elif dADa oSF1(false, 1.411e+63)
		else var CIO[0,49,9E92] <- prY ## fA(_"
		elif "'"" for VFxb until OU4r by 5.370E-65
			break
		elif false return
		elif "RS'"'"" for MW until ",,_" by false
			if aj return "'"'"N"
			elif "'"'"" begin
				continue
			end
			elif false begin
				## rh2EwXlLM;4
			end
			elif 770.720 continue
			elif 73.774e+89 sC(95)[0.560, "8'""] <- c5h
			elif ".'"'"[" break
			else if "'"'"5" continue
			elif dT5 n3(6e-48, "'"$q'"'"")[A6gQ] <- 87.197
			elif 7.991 number vYO0
			elif zrj continue
			elif 73.921 CUb("`}#U,")[71.464e95, 4e+56, true] <- oTSy
		else xMn(Vd, ";'"")
		else break
		elif "'"'"" vHqh()
		elif "}Pv3'"" return
		elif BC return Jr
	end
func NQj (number Hb[928,925.925], number QB)	return "'"'"'"'""
## U_lC3{<m0|Ibx
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1283))

	def test_1284(self):
		input = '''
var ENW_ <- true
## "(*GGUD_%rq
## je!Y9%:oR<>q
## .qV>wX p)"=FVf^Q:F~O
func NU (number Hei[3], number IT1)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1284))

	def test_1285(self):
		input = '''
dynamic UE[9e+77,8.402,7] ## NX
var Dc
func Te (var R_)	return "/5**K"

## jB5:G
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1285))

	def test_1286(self):
		input = '''
## TQIr
## aG
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1286))

	def test_1287(self):
		input = '''
## )r]Gy@,Bd$>A
func Hf (dynamic nCnV)
	return

'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1287))

	def test_1288(self):
		input = '''
var n9_Q[4.024e34] ## +I$a*hnW0=?1o[{g?U
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1288))

	def test_1289(self):
		input = '''
var t3[692.984] <- 333e63 ## IXw
## %pn$~NBO0#ou
func Lu ()
	return
func Q592 (dynamic Bd, dynamic R3Yz, bool P9[2E52,5,5])	begin
		if 0e+15 lO3(false, "!'"'"")
		OE7(xx)["H", 963.234E+31, " '""] <- 77.608
	end

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1289))

	def test_1290(self):
		input = '''
## {GsCZyg
dynamic WeI
func aOCg (bool OG4, var dk0N[20.805,382.990], dynamic PVA[633e-56])	begin
		## y
		## )bm85lN49Um)v?gy]T
	end

'''
		expect = '''Error on line 4 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1290))

	def test_1291(self):
		input = '''
## FpQ#{.BM(.AU(gV)Y%
string PQq ## k
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1291))

	def test_1292(self):
		input = '''
func Xnw (var bi[791.884,529], number to2p[1.129E-28,65.074E18], number f293[671.999e+62,0.822E-38,9.372E90])	return LT
var HC[8E-71,805] <- "'"" ## RoR?bI[6bB8XATsduL]S
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1292))

	def test_1293(self):
		input = '''
## 3iQ"})m*$5a6/wM*f7]v
func NruK ()	begin
		## ]i:Ev*
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1293))

	def test_1294(self):
		input = '''
## =FtDgtV$Wm
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1294))

	def test_1295(self):
		input = '''
func yg (string o8, var TYQ[833.982,921.743,67.667], number EW1)
	return 0.090

func Vn (string g2, number xcmb, bool ReW5[8E-94])	begin
		## 4Q
	end

'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1295))

	def test_1296(self):
		input = '''
## :paD`po
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1296))

	def test_1297(self):
		input = '''
func nF (dynamic hF[18.162], number woTT[6.781E-98,4.913E31,897.777], string Mh[73e+71])	begin
		## %[kYEU}KT^Q"6W#q
		begin
		end
		for oW until "(D'"'"" by "'"'"$,"
			if false return TgH
			elif "'"$'"v" dynamic Yt[1E+50] <- "'"'""
			elif "'"25%#" if 6E29 E39("'"'"'"'"")[8.173E-52, oar, 0.276E54] <- "aC'"'""
			elif "wn'">" if 2.893 break
			elif "'"7'"4" for Eye until 630.267E+89 by 47.821
				break
			elif hd uiSF <- ri
			elif 10e-23 return true
			else break
			elif "'"'"'"" sSE <- "+2'"'"'""
			elif 99.025 for hB until nyK by qO9
				KB <- "'"|"
			elif true for Ah1h until lb by uH08
				break
			elif 625.508 return
			elif "'")nx'"" if false if Jy1p continue
			elif Hx var sc88[96] <- 5E+93
			elif 57.911 r40b(pbvN, 7e-34, "'">'"")[true, Qk] <- false
			else Y6oR()
			elif true return
			elif "'"'"__" begin
				begin
				end
				## amxs#1
			end
			elif JX jta("'"'"B9'"")
			else break
			else bBqg[CX9] <- wf
	end

var PL6R <- Rm ## +_IP{rJ
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1297))

	def test_1298(self):
		input = '''
## ]|
## ;^C3]4yj{!:%oaio
func hji (string wch[381e-22,53])
	return

string uV0Y[7.324E67,69,0.404] <- S_N
func eTJe (string alSK, number dl_)
	return 5.232

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1298))

	def test_1299(self):
		input = '''
func xI (dynamic L8x, bool Gx, var c9f[0.804e07,1.023])	begin
		## 6 9_={
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1299))

	def test_1300(self):
		input = '''
number qVj[49.495e+27] <- "'"" ## 6LGH"K+n+fhT)a
## `E"<O&K1iMaevnJtJ(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1300))

	def test_1301(self):
		input = '''
dynamic JdO[37.642,1e+29] ## d?
func n6 ()
	return false
number h_N[87.380,5,30.968E02] <- Ah ## qdyNA]4Sn!Jcr${X
## UK
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1301))

	def test_1302(self):
		input = '''
## DqP5!Fc,uv/In7Kz/
number rf6[4.443] ## r
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1302))

	def test_1303(self):
		input = '''
string CR0 <- false
## ]
func vZl (var iy, var SBc[1E+47], number xd)	return oJmW
func rJXJ (string tiAW[0.565e05], var o0[79.930e76,10,35E39])	return np
func RovI (bool OY, bool d05, number nr[37.571,174])	return
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1303))

	def test_1304(self):
		input = '''
var fA9a[0.578,26.179,965.297] <- 778.040
number H4
number GT
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1304))

	def test_1305(self):
		input = '''
func geCj (dynamic wf[4,5])	begin
		string Z_
		xok(868.020e-41, "'"")
	end

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1305))

	def test_1306(self):
		input = '''
## :
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1306))

	def test_1307(self):
		input = '''
number tzqw[10.763,88] <- false ## NN|*A
bool Y3 <- 307.943
func NLib (number KNYP[7,52.746,248.725e01], dynamic CtTu[2.907,97.244], var ZxA[135E77])
	return
func KCy ()	return

'''
		expect = '''Error on line 4 col 45: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1307))

	def test_1308(self):
		input = '''
bool xdKi[47,5e+95]
func t3mc (var KNIK[3e15,7.020], number EM)
	return jbN

var gU ## vt.k
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1308))

	def test_1309(self):
		input = '''
func Itn (number Aw7)	begin
		UF[615.323e10] <- qsRq
	end
func PNd (bool DVzh, var V8qI, var JHM[14.242e-21,4E-36,219.474E+45])
	begin
		break
	end

string avZg
'''
		expect = '''Error on line 5 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1309))

	def test_1310(self):
		input = '''
string hUyX <- "'"7!" ## Y?`S>V
## mC=Ylh>q
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1310))

	def test_1311(self):
		input = '''
func rr (var C_ku, bool W0G[58.777,306.841])	return
## H}s@i]9}+
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1311))

	def test_1312(self):
		input = '''
## I$e:*k
number eUhR[9.901,5.763]
dynamic evpv <- QX ## ?~%}Mv|R]Tnw)m
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1312))

	def test_1313(self):
		input = '''
var A3
func HP0 ()
	begin
		## aL
	end

'''
		expect = '''Error on line 2 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 1313))

	def test_1314(self):
		input = '''
## H2N0l:I"fJCRlm!7a4
## o9Z fdY8vSl
func uSN ()	return UQ

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1314))

	def test_1315(self):
		input = '''
bool tPow[2e68,6e02,5e+56] ## GkgOa/y8Lq,D&+oh~
bool ow[9e-16] <- true ## :2iI
## `%V*|)j7
bool IN ## #)QR
## qlMN`UJa0;
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1315))

	def test_1316(self):
		input = '''
##  
func lun (dynamic vl6Z[92.849], bool LODl)	return "Iu"

string yXnO <- PxP0
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1316))

	def test_1317(self):
		input = '''
number v02U[990.406] <- "'"W'"'"" ## 2$bLykNV^
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1317))

	def test_1318(self):
		input = '''
func zKHl ()	return 4.945E35
func vy5N (string nC[32.921E+83,82.120,727.389])	begin
	end
## )6%ZM|%~/
bool MLb8 <- zaW2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1318))

	def test_1319(self):
		input = '''
func cZi_ (dynamic NR[95.261])	return

'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1319))

	def test_1320(self):
		input = '''
func M1 (var o7u, dynamic Orw[648E29,4,702], dynamic YN[53,8e+75])	return
func gUh (dynamic k4[457.380e49,7], var wMYh[3E+37,348e33])	begin
	end
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1320))

	def test_1321(self):
		input = '''
func Sx (number A9X)
	return true
dynamic MY ## (:9H$o,Nuu`l
func zaOC (var xL16, bool A2[671.370,126E58], bool C4r)
	return 1.418
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1321))

	def test_1322(self):
		input = '''
## G!D_cuCS
func du73 (string dIPU)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1322))

	def test_1323(self):
		input = '''
bool A0sY
## Ej6(Yne
## Eb7Sf`9v-u7z>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1323))

	def test_1324(self):
		input = '''
## tr]Q^!=Fj(S$0q*s$X
string jdhV[7.060E16,9.879]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1324))

	def test_1325(self):
		input = '''
dynamic WlZB <- "8P"
func mWD (var Pv9_[82.178])
	begin
		if "c'"VV" break
		elif cdVz break
		elif true K2RU(false)[tt, 57] <- "'"'""
		elif "y'"'"" if true for nXu until "'"" by 9.996E82
			continue
		elif "Sh'"" continue
		elif "L" if 4e48 string Ihu
		elif false E6S(IC78, 2e-03)[false] <- "'"'"'""
		elif 59E71 if "s'"" hU7("'"'"", QD)
		elif "'"'"'"" bMX8 <- false
		elif 808e65 break
		elif Ot for K6Oc until "'"Z'"." by "'"'"'"L'""
			continue
		elif 67 for QU until 486 by "'""
			begin
			end
		elif 61.023e+46 continue
		elif true if false for tR until false by true
			break
		elif "'"'"" continue
		elif "'"" se <- "X'"Q"
		elif true dynamic Zlp[57]
		elif LccU if 7.550 break
		elif izDE continue
		elif 577 begin
			## +y2$+n6~6Y
			for Wi until 2.300 by "FP'""
				for OC until 46.331E77 by uA4
					return
			break
		end
		elif Naqu return 7.554E20
		elif 0.816E+17 begin
			## m-LE8=<5ZMzn3
			break
		end
		else aubH(false, "'"z'"")
		else if false begin
		end
		elif QBbJ bool IWBb <- "'"" ## WBPQ/{{6z(u5nHJ?m3
		elif 8E-15 for KPd until 4.896E+21 by 535e-61
			begin
				## jQ22KC|F#
				## @Q!W@5z~T_FKn
				dc(399.297e10, z3Ta)
			end
		elif 15E+40 number rr
		elif 9 JdF(Peyo, 94.092e71)
		elif 286E-87 continue
		else break
		elif "'"'"'"" string kSk_ <- true ## ROY;o<A>6Gr$:s
		elif S3 return
		elif SeCN qT(9E97, false, "'"r")
		else HU("(9rI", 302e-93, 21E55)
		else dynamic cPn <- true ## C
		## rI(Cr.,Y|,zR"KE
	end
bool C9S <- 405.991e+82
func LM (string Dx[899.637e-20], string mps[0.425,811e-16], number jY[983,7.647,936E-40])
	begin
		return FyeB
		for Ckbj until "Y'"" by 7E61
			return nUT
		## 4
	end

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1325))

	def test_1326(self):
		input = '''
bool dyG[165.914e+78]
## =VZH)URz;*m") C_wf:
dynamic AOpn ## q_
## ?(l_jKA<_9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1326))

	def test_1327(self):
		input = '''
var daS[929] ## /3UJW&c..$)?_JT|Yx
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1327))

	def test_1328(self):
		input = '''
dynamic W30 <- "'""
func EU ()
	begin
		## !Hk|8pr0]-M-sW}frS
	end
func aeA (number qY, bool NZ)	return "'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1328))

	def test_1329(self):
		input = '''
string XP8[19.525]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1329))

	def test_1330(self):
		input = '''
func GLG (bool fl, number d4_L[95])
	return
func QUeb (string cjr, dynamic ZpeZ)	return QA
func Ed (var o4, dynamic fk[895])
	return
'''
		expect = '''Error on line 4 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1330))

	def test_1331(self):
		input = '''
## ug"CSNo%DB>F&yg>Ug
dynamic f0a[31.465e87,61e37,514e+64] ## 55gd(Q
dynamic npr <- 489
bool m8f <- Kw
number EFU <- 72.969
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1331))

	def test_1332(self):
		input = '''
dynamic i2fB <- "'""
## MxIN`Z(&:9JdH?@/{Q
string sFp <- true ## 2z]"VO
func gM (number kHhs[943.548e+43])	return Z0
## DptL+UC_Nj1?/N:r
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1332))

	def test_1333(self):
		input = '''
## T~}i-LJ;y|w
number qzqk[564.318e-38,99] <- Z8G0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1333))

	def test_1334(self):
		input = '''
string OlEu
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1334))

	def test_1335(self):
		input = '''
func SqQ (number Gn, number cr, dynamic h7z[4.165,70E-82,307E+46])
	begin
		## nr6}~dVzsy%I^x_
	end

## HdA-Oj~2i+B|C~zmO|hA
## +S@ (.b:8bc)mr`*:N=
'''
		expect = '''Error on line 2 col 32: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1335))

	def test_1336(self):
		input = '''
func O5t (number s63, dynamic lEA, var BT)
	return true
## PJ]CwOSw2me)]ZmJ
'''
		expect = '''Error on line 2 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1336))

	def test_1337(self):
		input = '''
dynamic H9tm[195.443E57] <- 73e81
## /
## FG9:8|bC.FPDYb=
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1337))

	def test_1338(self):
		input = '''
## rrRBgs!=
number oYH <- 49 ## (3^$FTp(`;vDH^rq
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1338))

	def test_1339(self):
		input = '''
func VA7 ()	return iN0
func xZFq ()
	begin
		## $4Xwg,op7sk^;PKaDQ
		## 6aXsrhyqT{H]Y
		## ;#<AtR4Gg3`
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1339))

	def test_1340(self):
		input = '''
## 2q
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1340))

	def test_1341(self):
		input = '''
## se+4ZE^4#s
func Mga (string vPpE, bool GcpD)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1341))

	def test_1342(self):
		input = '''
number LXS <- "'"p"
func mS (var ESz1[874E45], bool mr, bool hDtY[76.245e64,48e-53,353e+98])
	begin
		ioXk <- false
	end

func hcD ()	return 48

'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1342))

	def test_1343(self):
		input = '''
## [qiog98p"|eq()P
func Ou9 (string WtKH[34.426E+89], dynamic F9J, string iry[84.272,74.099])
	return l0
func BJ (dynamic sS8, bool Lcb[38E+15,634E33,2], var Bt0[56])
	return
## [WiMx[sGG4%OSJ
'''
		expect = '''Error on line 3 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1343))

	def test_1344(self):
		input = '''
func daym (var MHoB)	begin
	end
## ,}WHnHpNA?,,
func TykG (dynamic EF, var Ceye[6.363e-71,36.514,998.568])
	begin
		## oRbi"y2
		## S{V;m
	end
## ND t?uBy,z
## 3V
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1344))

	def test_1345(self):
		input = '''
func WNQ (var EQ)	return 6e-66
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1345))

	def test_1346(self):
		input = '''
string LQ[8E-63,0,429.187E+04] <- iXe
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1346))

	def test_1347(self):
		input = '''
func An ()
	return 5.912E-28

dynamic iez[79.266e73] <- "N'""
func Sp (var Zbu[83.213e+33])	begin
		## oi)nG=<R<O;VH8
		continue
		continue
	end
'''
		expect = '''Error on line 5 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1347))

	def test_1348(self):
		input = '''
number xDU0[137E-75,6,18.629e+48] <- bP
number N5 <- "'"WN^h"
func Ls (dynamic DE)	return 9.461

## ``(jMk og"TFz1$wV#;
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1348))

	def test_1349(self):
		input = '''
## m^Pb}(=V#:,Jqg:zrn~]
## 0Oa%(~)TP}*bbGF
bool p1S ## )}#zJ7*
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1349))

	def test_1350(self):
		input = '''
func R3b (string S30x[1,6.928E+83], number lD[363.190])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1350))

	def test_1351(self):
		input = '''
func M3l ()	return "2'"S22"

dynamic ANz[912.042e-65] <- "'"("
func K_oE ()
	begin
		bool RnY[563E-78,547.205] ## x4cR3! g!_-dB
	end

func u8wo (var RUa, dynamic kYHK, var XP[1.237])
	return false
## ]By6e? S6W
'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1351))

	def test_1352(self):
		input = '''
## L!nt"[
func GY (number RHt, var Bl0c[2.160E23,69.136], string Hix)
	begin
		## QLj_:bq3v?b:u1
	end

bool Y6MN[26,734e57] ## 7d~9l9V5#lIt
## {Uz3v 1I*,+y/<I.y1D
func ral ()	return

'''
		expect = '''Error on line 3 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1352))

	def test_1353(self):
		input = '''
func Ul5 (dynamic Zlgv[4.833], dynamic eCD[99.994e-13,810.483], dynamic Wd[91.459E+99,988e37])	return false

## sqP^xr<Qa`PF?`
## Mji
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1353))

	def test_1354(self):
		input = '''
## *Gr]6
number pFm ## YaLRLv=]KbNp+07jcAA{
func tpHR (bool vq[20e89], number YO)	begin
		## h
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1354))

	def test_1355(self):
		input = '''
## VY[
func Ionm (bool We3, string OGwI[82.256e27,7.520,583e-52])	return 5.613
func OI9 ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1355))

	def test_1356(self):
		input = '''
func saQ3 ()	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1356))

	def test_1357(self):
		input = '''
## qjT>]D&A}ee
func Nb7k (bool HGpC[761.183E-47,800.469,9.384E+30])
	return "'"'"'"'""

string Whmp[4,756.161E+02,654E+50] <- uzW ## %9F"@-C.<Nx
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1357))

	def test_1358(self):
		input = '''
var rmwZ[29,17.863E+32] <- 87.848E13
## Fh
func Zp ()	begin
		## 4$]a)-m2@O8&
	end
## mz%7+5OG.fR#J
var eIfq
'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1358))

	def test_1359(self):
		input = '''
## A}Lss[51P@
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1359))

	def test_1360(self):
		input = '''
## twnpX?
func sUZJ (bool MOg, dynamic O6)
	return

string n5O[453.711E74,9E-06,10.491] <- 18.064 ## ^L[3lp;l2
func yg5 ()	return
number cC[6.405,634.054e+95,8] <- r5B
'''
		expect = '''Error on line 3 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1360))

	def test_1361(self):
		input = '''
string hi[3e-58,7.951,69E-29]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1361))

	def test_1362(self):
		input = '''
## Zf551T9CV.E(:nzo
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1362))

	def test_1363(self):
		input = '''
func LH (dynamic ee5r[850,2], number GZ[900])
	begin
		## r
		break
	end
func HA (var AE)
	begin
		## 7sdrMP!;8Bc
		## M~18T*g;q"2bLYcn=
	end
func BMi (number Rzz[29.793], dynamic gfR[271,904.632,40.523E+52])
	return 39.114
string IblW <- "f"
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1363))

	def test_1364(self):
		input = '''
func qL (bool sZVf[9,9.960e+87], bool ZT1[6.455,3e-93,947.518E+35], bool m1[6.795e+65,108,8e+59])
	return fnA

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1364))

	def test_1365(self):
		input = '''
## ,&t^!sH9Z<6n
bool j4Mn[61e+35] <- zzkf ## >">Bs2^9!_dQs/Pb^6Zs
## b9*S918rR$<8CH:
func YjP (bool wO[59e+09], string tk)
	return

string OB[681E-24,458,670.589] <- 851 ## |USqz.3/kgg`/:^lI<X#
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1365))

	def test_1366(self):
		input = '''
func FrvL (dynamic cLh3)	return true
var xS4 <- eCGA
## +}q<h4+vF!R%HDuk[+c_
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1366))

	def test_1367(self):
		input = '''
dynamic pQ9[0E+34,5E+61] ## nI$_+1R&B
func AR5 (var gIzK[40.936e-91,320.223E-33,90.632], dynamic g0pQ, var Ac[1.235,9.047,512.946])
	return 108.025
string Cv
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1367))

	def test_1368(self):
		input = '''
## *
var uvq[988.585,855.101E40] ## $eo0kS~)tj0=}}x
func Ni (bool iKeg[1.721,6,8.809], dynamic hc[84,0.282,3.479E-44])	return ruo
func ZGgO ()	begin
	end
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1368))

	def test_1369(self):
		input = '''
func QrN3 (bool Qo4, number Vjp[61e-29])
	return "'"F|"

func d_GB (dynamic syq)
	return

func H2L (bool Rf2[636.257,462], var XK[281.969,5.788e-64], var qKO[8.837e21,50])	return
func iula ()	return true

'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1369))

	def test_1370(self):
		input = '''
func kJq (dynamic D4[5,47,97E31])	return
var Ip ## ;(f.!
func kt ()
	begin
		return
		q_("I'"")
		## />Q3E
	end

dynamic xe[144]
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1370))

	def test_1371(self):
		input = '''
## [k_OA9eZ4uQ.e
number hK4z[3,3] <- Rex
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1371))

	def test_1372(self):
		input = '''
bool Ixzp[5.385,5E-34] <- false ## H)F-mzp*)8oK2MEBs,M
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1372))

	def test_1373(self):
		input = '''
number JmeO[9.187e+19] <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1373))

	def test_1374(self):
		input = '''
func XzWc (dynamic tSwu[99.241,55E54,41.444], string KA)
	begin
		## pGuAS67=
		vM <- "0'"'""
		## t,BSnE+
	end
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1374))

	def test_1375(self):
		input = '''
string Hkt
## 5hhdCH,Y|g,5jA
func Lrh (bool s3, number aUA)	begin
		## g$Jb;0aO~2MJh.<V{@)w
		break
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1375))

	def test_1376(self):
		input = '''
number pV[4,30.043,6e05] <- 347 ## /&c$AYV4-n^
number io <- iYAn
dynamic RHtD[866.190,70E73,220E20] ## (i6,iPcFwmt
## }
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1376))

	def test_1377(self):
		input = '''
number OTB <- B8L5 ## JGnsYH&4!5C(R]@[
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1377))

	def test_1378(self):
		input = '''
## >XEwY|dp6|
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1378))

	def test_1379(self):
		input = '''
func hKF ()	begin
		## SGP:}V%{c2a5EZo@a
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1379))

	def test_1380(self):
		input = '''
## xMIB-q`,hTsKs
func s6 ()	return
## Vp7jDN4y500OX9
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1380))

	def test_1381(self):
		input = '''
func KcPY (string yMC, string WE[57,293.877,490], var lZf[33,0.662])	begin
		begin
			##  rhE3gi,[`"HDOS)ah
			## kCV
			## qfUj5Q*
		end
		## Q9.f70`~z
		break
	end
func bK2Y (bool Ao[905e-85,6.510], bool yoJN[823E76])	return "'""
## 2N/qc$X,poyYgd_|
func z2jo (string SIp)
	begin
		if "'"" continue
		elif DeQ1 for U2V9 until MEy by 23E76
			begin
				## &Vas`f>)>`#e|h
				return "q'"y"
			end
		elif 186 return uvPg
		elif "%" var A0H[51e+72,48.549,17e-10] <- V0y3
		elif true for yEt until kixr by eF
			lIV("}H?H")
		else if 86 Fz()
		else return tFR
		## gD>11A&91RzfH
	end
'''
		expect = '''Error on line 2 col 50: var'''
		self.assertTrue(TestParser.test(input, expect, 1381))

	def test_1382(self):
		input = '''
dynamic FrRn[8.327e-25,978.667e58] ## &b5fv,%%CGhU
func LX2X (bool akbn[7], var Eep[82.183e-76,5.278E30,486.782E+46], string B3Xu)
	begin
		return
	end
bool H1j[817.522,4.606] <- 833.997 ## 3bQxG}(~cBum:IC
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1382))

	def test_1383(self):
		input = '''
func A2pZ (dynamic loyZ[829.271E-54,97e-79,380E67], var MiS[22E10], string xN8F[8])
	return false
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1383))

	def test_1384(self):
		input = '''
## 2
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1384))

	def test_1385(self):
		input = '''
func hxiV (var Mq, var Pv)	begin
		## j+VwNeB,6!iK7hB5
		## GbhV
		return CbI
	end

func HVJ (dynamic y9e[288])
	begin
	end

## y
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1385))

	def test_1386(self):
		input = '''
number Ww[673.587,115.348] ## i*-APMCV:!0
func Tx (string VUlU, number Lu2F[58,8.487,789.986E79])
	return

## Th1Q((E~y!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1386))

	def test_1387(self):
		input = '''
func Ba (bool HY, dynamic rY[9], dynamic yk)	begin
		## aD/*qB#d0
		dynamic xy[8e24,97e44,83.076] <- false ## j*Y1"k6[
		## 8`2o5Y*(N:1>b&.$t=
	end

bool rD[705.202e-38]
var CY[443.115,60.350E+21] ## ]R$^bvZI!k>QfNy`v
string xv[93e-72] <- jMPg ## TrSWoL$0xf[]=fVW
'''
		expect = '''Error on line 2 col 18: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1387))

	def test_1388(self):
		input = '''
func eSe (bool Tuc, dynamic Xagc)
	begin
		## p%
	end
var QM[9.799e22] <- 55.377 ## ;)x0:+&0WcA
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1388))

	def test_1389(self):
		input = '''
func wb ()	begin
		if 58 begin
			## 6]GEyk/c,?hVU8Is
			## &BF*J}e3<sI]xAC_p
		end
		elif "'"]" for gwH until true by "'"'"'"'""
			bool uE8[64] ## tg]ule1,::^
		elif "'"'"6'"" if "'"'"'"m" rGx()
		elif "'"'"~" break
		else Yu(UGt, false)[S6z, bo2Q, false] <- 1.523
	end

## RZTn?J]GJ]V%
## Qon"5*j{NMf
func F74u ()
	return "7"
'''
		expect = '''Error on line 3 col 5: 58'''
		self.assertTrue(TestParser.test(input, expect, 1389))

	def test_1390(self):
		input = '''
func QF0j (var N_g0, dynamic hYm)	return e4jC
dynamic sZq
func Wbdi (dynamic Rq[948e-29], var pD9[2e-97,542E-18,820.444], number Wnry)	begin
		## UMg
		dynamic zYV <- IK ## 1^pXg8tn]N(
		if 26 begin
		end
		else if st continue
		elif false return
		elif 6.588E95 break
		elif QZ return
		else var Xoj <- false ## Bse_*eG~!
	end
## dA?,ke>P`?qBHrcBgRZb
func z5kp (bool TE)	return 85

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1390))

	def test_1391(self):
		input = '''
## "0c[
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1391))

	def test_1392(self):
		input = '''
func XbT ()
	return

string Be[34,702e86] <- oXr
var Itr_[437E+90,754.933E09] ## 5Ve
## zk+}Hwg-/
var ifV <- "!"
'''
		expect = '''Error on line 6 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1392))

	def test_1393(self):
		input = '''
## YI
func l3 (string Dw[5.043,4])
	begin
		if 7 continue
		elif false NNt()
		## @, 4qM.oQv
		## w-iFb5@<};G6
	end
## =IAeIr
func JL (dynamic XA[8E-62,57.450,6.238E-17], dynamic kTQ9)
	return
'''
		expect = '''Error on line 5 col 5: 7'''
		self.assertTrue(TestParser.test(input, expect, 1393))

	def test_1394(self):
		input = '''
func fEyU (bool vyqJ)
	return
func Dtm (string ku[28e-23,97,27E+43], dynamic ajx[176.448E08,49.087E96], number i9w[485,80.059E+03])
	return
## L$3VKhG.kP;NHYqP
## !$iZzNQ3R?o{E(HS
'''
		expect = '''Error on line 4 col 39: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1394))

	def test_1395(self):
		input = '''
dynamic Wc6 ##  :3:,X<sXYi
func kF3 (dynamic RC[402.011e+61,32.280,994.564], bool a0[463.104E+35,9E27,84.766], string iFZh)
	return
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1395))

	def test_1396(self):
		input = '''
bool tg ## fF?E1>>s
func lRG (string LPs[635,1e-80,26e21])	return true

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1396))

	def test_1397(self):
		input = '''
func z2Od (var KQkX, dynamic aJ[50.322,8.492], var ebUF[313.503E-29])	begin
		string ua ## _wDU Dj+*~;UH
		## )@y)
		return
	end

string mA3[99.332e-31,5.697e+66]
number CTEf[197e34] <- iKoc ## *tf:,d2n-7[M4Wm![v
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1397))

	def test_1398(self):
		input = '''
func MCH (number tP[925,99E51,5.983E48])
	return true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1398))

	def test_1399(self):
		input = '''
func hi5o (bool vfhL)
	return "u{'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1399))

	def test_1400(self):
		input = '''
## fm&D<iOR7lk`909F VjZ
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1400))

	def test_1401(self):
		input = '''
## nYV}#sVJP^
func WYN ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1401))

	def test_1402(self):
		input = '''
number aa
## t^
dynamic yMYH[57e+41] <- 2.496
## n
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1402))

	def test_1403(self):
		input = '''
string Sn <- 746E-38
dynamic xQf ## :7DuizJ:H^]B@q/C9n
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1403))

	def test_1404(self):
		input = '''
string JnD4[8.817,170.147,310.881e-99] ## $$k~60;{kUY
bool aTU[2E+55,7e15,11.836e+80] ## J!2
func FK (bool TV0I, dynamic h78k, string z58_[869E59,97.930e-02,510.128])
	begin
	end

'''
		expect = '''Error on line 4 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1404))

	def test_1405(self):
		input = '''
func xasH (bool rki[6,691,40.708E+87])	return true

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1405))

	def test_1406(self):
		input = '''
func jFr (number qZPx[0,608E79,56.515], bool bg_[538e+34,0.797e+78], number z2[59.390E10])	return

## l#X{u-5qKEZu A
func ZI5 (number Zva)	return
string MAz[1.072e+70,4.051] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1406))

	def test_1407(self):
		input = '''
func PI7R ()	return 32

string s6 <- false
bool ur[57e+83,3,99e-17] ## _CROh*>Ts%`4?Y
func M3r (string jtg)
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1407))

	def test_1408(self):
		input = '''
func QErG ()
	return
dynamic EZ <- "'"" ## :+lNYh8&d
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1408))

	def test_1409(self):
		input = '''
func gHn (dynamic Re9[653.811e-13,947])
	return
func H8 (dynamic M5[81.755e05], number bxX_[44E+90,6.693E23,47e+31], var NIpQ)	return YkY

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1409))

	def test_1410(self):
		input = '''
## ~%k
func h29N ()	begin
		if aQ continue
		elif 9 for vTfw until 768.266e77 by true
			for Er until iPQ by "E'"3'"'""
				if "'"'"'"" for NWI until true by false
					if 649.753e09 begin
						for eIIh until true by gJP
							iN2F[false, "-.'"'"", ")'"'"'""] <- 79.711E15
						for QeRk until 419 by 887
							begin
								continue
								## t
							end
						## hB>Dw!YPf#0U4
					end
					elif Dt return
					elif "m'"" uRQ5[33.629, "c'"S'"", true] <- pzV
					elif "C" if 6 if "'"" continue
					elif false BM <- lkQ
					elif 983.750E09 begin
						## /@&>24sJG7-@|e_
						## x[#doV"r&2bt
						## A#Cn6E},JR
					end
					elif false CkAU("'"'"}'"'"", false)
					else break
					elif true continue
					else Wg("'"o(Z", MXA3, "Y")
				elif 203.584E-15 break
				elif rs break
				elif R8b uZo()
				elif true for zq2 until true by "'"'"'"'"N"
					vB3(false, "'"Y", zVn)
		else if false for sidb until "m'"nF'"" by Rl
			continue
		elif false sm3 <- "'"'""
		elif 5 return
		elif "'"'"'"'"" for W07 until false by 79
			oq(kzep, vy)[48.956e45] <- jCjJ
		elif sP1D begin
			break
			for uGT until XGM by "'"'"+E"
				for sstC until false by 68.594E32
					begin
						return
						## 3P;o5
					end
		end
		else begin
			K09["'"", 2.608E+43, 43E13] <- true
			Cdr(true, "DZi")
			## 8?|M*4IB?}aHF|BO
		end
		## _M29-"
	end
## {
func r8d4 ()
	return
'''
		expect = '''Error on line 4 col 5: aQ'''
		self.assertTrue(TestParser.test(input, expect, 1410))

	def test_1411(self):
		input = '''
bool xpT[6.921] <- false ## ;V
var aV <- 639.179E92 ## (vE#A"77RKa6
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1411))

	def test_1412(self):
		input = '''
## i1G3:
number m66L <- 1e94 ## A6tbM?"HAgFk8+8k^
dynamic Fn7[9.352,429.624,88E54] <- false
## y"~}_e
## "wa"ySfZ&OK54n%UPmYs
'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1412))

	def test_1413(self):
		input = '''
func dy5F (var mX, dynamic CGF)	return El

func zA ()	return 3
var NDlK[432e-17,7.917] <- 7.472E-54
func EGb (var s6n[6.908E+98,662.491])
	begin
		return "4'""
		begin
			## FOFTF+
			## (aX/|w5
			break
		end
		## F.
	end
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1413))

	def test_1414(self):
		input = '''
func kLy (number GmHs[5.607,503,244.164], number dv[54E-24,3,9.913E00], string RLSP[2E-42,9E+13])	return "0'",u'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1414))

	def test_1415(self):
		input = '''
string WTUZ[27.910,6.938] ## +VABo=e%y=E8*R+cm
number ynY <- "%O'""
## ^0pQX~Q
## >
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1415))

	def test_1416(self):
		input = '''
func D_iO (var obft[81,1.842,990.236E+78])
	return
bool kmt[2] <- Usgu ## }`g
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1416))

	def test_1417(self):
		input = '''
func NxK (string SJup)	begin
		## [-n2;ha7
		continue
	end
## r$]pCU%_n+
## {KMf[P?WV_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1417))

	def test_1418(self):
		input = '''
func sER (dynamic hZ[35e96,3,319e58], string YQey)
	return "h'"'""

## 2c48T~Kk!xg?N9WR5/U
func Gbj (var ouYL[68.831e95])	return 16
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1418))

	def test_1419(self):
		input = '''
func nAgY (dynamic lmem, bool vsb[48.862E-74,93])	begin
		## ksK><jR;mGL?8*7T:V62
	end

bool tnPZ[568e94,22.670,79.165] <- "'"d|D'"" ## &N=!0l=@cI[q
number wgJS[8e42,615.576] <- cOP ## 3Jqfe*lXlr[r
var VIs[3.455e+46] <- false ## NA%
number m1[0,8,874] ## 9i&:;
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1419))

	def test_1420(self):
		input = '''
func oV ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1420))

	def test_1421(self):
		input = '''
string mgwV
string G32[9.554e20,223e-29,3.585] ## 0^4(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1421))

	def test_1422(self):
		input = '''
## mdLj~Z3My[&u
dynamic lm[36.872e-48] ## -3/
## "g~Dv~m}_R
func Hz (dynamic QUi)
	begin
		continue
	end

'''
		expect = '''Error on line 3 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1422))

	def test_1423(self):
		input = '''
func Zf03 ()	return "["

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1423))

	def test_1424(self):
		input = '''
func WIW (string OUCs[1], number PKb[53,81,2], var OVCW[0,28.265E-78,4.452])	return "'"km~"
## H)<qQx
## {zt.Y3
'''
		expect = '''Error on line 2 col 47: var'''
		self.assertTrue(TestParser.test(input, expect, 1424))

	def test_1425(self):
		input = '''
string buXU[62,799.533,7E-58] <- true
dynamic L1Fw[45e73]
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1425))

	def test_1426(self):
		input = '''
func w_w (bool qV)
	begin
		## $}In.L)|V5VPbR
		Di(13.043E-61)
		if "a'"'"&'"" bool Ev[49E03,8.714,6e+87] ## 9h(8Z$yScHy{"I{8TB>
	end
bool FfVs[3.298E06] ## 7
## *=[?%SLdg-
func Ax9 (number HCH, var RY[126,7.432E+93], dynamic Hpui)
	begin
		## fkl,`{tL=
		string A4 <- Wdm9
		## "5TEgu/q5k@8:&
	end

'''
		expect = '''Error on line 6 col 5: a'"'"&'"'''
		self.assertTrue(TestParser.test(input, expect, 1426))

	def test_1427(self):
		input = '''
number gVc
func KG ()	return "9A"

## WemTcAa)iH
func M3_Q (string W8)
	return
number IRB ## ;0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1427))

	def test_1428(self):
		input = '''
number mk[10.951]
func KKS (var qcC[43.145e-05,27.945], number WUX)
	begin
		## RMUzy3`zGU3}aP%vv;32
	end
## t#
## GxV4pR>RD7~vhg*
## c"7sKb>-w
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1428))

	def test_1429(self):
		input = '''
## hapCs
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1429))

	def test_1430(self):
		input = '''
func uCZq ()
	begin
		break
	end

func Zp ()	return false

func ik (number RLmr[947,86E+97])	begin
		## |N
		begin
			## (T=Fn$l/<nS$"][sby
			tGPO(false)
			begin
				return "('""
				dynamic fg[50.702]
				c2Tp(TA)
			end
		end
		## W-J<}XZ7oo?aZ@twP
	end
var xo[44e-09] <- 0
## )am@`[dT,>/k^~TliA
'''
		expect = '''Error on line 16 col 14: ['''
		self.assertTrue(TestParser.test(input, expect, 1430))

	def test_1431(self):
		input = '''
## ss<J~,aiJS fvlPzIJ
number f82
## ,<2
func EhPo (dynamic Ww[8])	begin
		## y-}a
		eH[186.675, 1.327E+37] <- eBC
	end

'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1431))

	def test_1432(self):
		input = '''
var jyJr ## lQ:,;}
number ATT[5.355,9e24] ## hX
var zK[11e48,23]
'''
		expect = '''Error on line 2 col 18: 
'''
		self.assertTrue(TestParser.test(input, expect, 1432))

	def test_1433(self):
		input = '''
string EB <- 77 ## l]t?Vn]1tUpH6:50Q)B
bool VoZ ## JUdL=u6GN,pfTE?
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1433))

	def test_1434(self):
		input = '''
bool i2[16e-01,41] <- "'"'"S" ## z
number Mnq <- true
func PvpM (bool eq1[1], string eI)
	begin
		string Er0e[86.083,1.208] ## 1m})FXv8;7f
		continue
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1434))

	def test_1435(self):
		input = '''
func MOQ2 ()	return

func Lm (number ri)
	return

func v9l ()
	return

func k8Ub (var us, number l8)	return T9Qt
## VjX}Qf:_g$V*
'''
		expect = '''Error on line 10 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1435))

	def test_1436(self):
		input = '''
## bNtfmC@/)lc
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1436))

	def test_1437(self):
		input = '''
## IWss{C^,
## 5eZQ~#w|z~I
func ba (number Qm)	return

## U|52~6Pf
## %"N!>us%p}K
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1437))

	def test_1438(self):
		input = '''
var FyO <- false
## Yb |x2SqXvN!j[TJ4
## :/wc`SLnyol
## AX%}Wk6V_kFSewF|=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1438))

	def test_1439(self):
		input = '''
func Xva1 ()	begin
		## &-[s(Zu@>WQV
	end
func tb (bool Wm, dynamic nyRh[57E+94,7e18], bool Cr[856.171e-28,6,84e27])
	return 319e-98

func cSmd (number xQ, number AH_)	return
func GdjZ (var K5[999], bool rn)
	return
## yJ
'''
		expect = '''Error on line 5 col 18: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1439))

	def test_1440(self):
		input = '''
dynamic udNG[9.857] <- GKMT ## rLXn9}eNb9t>>
var NvDV[7e+10,31.998E41] <- ":0'"r" ## |{@BM(
string O4e[1.556]
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1440))

	def test_1441(self):
		input = '''
func k7 (dynamic EQ, bool g3zc[861], string Eh[54E+31,561,6.170E39])	begin
		return cAO
		Fa(false, true)
		continue
	end

func BgKU ()
	return Mre3
## dl17IK9x
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1441))

	def test_1442(self):
		input = '''
bool LT
## 6%7,W^s;5kIq0([_hn
## +cD:h1{7a~ar]P
string EQ[83E+88,0e+77,9E54]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1442))

	def test_1443(self):
		input = '''
bool XQTs[92.333,927] ## @&pg[OD
func Dkud (number yE[25.719])
	begin
		var ZGD[782.734]
	end

var eLzv <- "'"'"D(j"
## UG &j.3
'''
		expect = '''Error on line 5 col 9: ['''
		self.assertTrue(TestParser.test(input, expect, 1443))

	def test_1444(self):
		input = '''
func SeF (string Ad, string TxF, bool ciu[2,107e51])	return
dynamic OX <- true ## j36RPGUzo
## S?j;^bqIs[<rq_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1444))

	def test_1445(self):
		input = '''
dynamic Zly ## VX=?ZuHIU1h/WZg_S>8Z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1445))

	def test_1446(self):
		input = '''
func kN (string QY)	return
bool eIUS[64,7E-57] <- false ## oP1wQ$if2[O)@G*7@-
bool Kf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1446))

	def test_1447(self):
		input = '''
func sjZ ()
	return
number J5 ## PThHU18!&s|kzV=]=u
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1447))

	def test_1448(self):
		input = '''
number Hi[103.947,4] <- true ## ~v#LJ~D.q<{U Rw0x
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1448))

	def test_1449(self):
		input = '''
func g8Q (bool Iw, number M8oE)
	return
## N2lm.#_7gB$5J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1449))

	def test_1450(self):
		input = '''
string J0z ## 6-3|6(9+:
## >^IJ]37FnqN%}2$",#-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1450))

	def test_1451(self):
		input = '''
## _8}I:3~HFP%
## }|J D4N}7}&
var Eo <- swGL ## )C]:D,~+FZ,8mI1
func gv ()
	return 23E49

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1451))

	def test_1452(self):
		input = '''
string UAwH[323]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1452))

	def test_1453(self):
		input = '''
## sK 
## T-[O{
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1453))

	def test_1454(self):
		input = '''
number pNm <- true
string EkK <- 81 ## e;]I86CQDd<4itbx
func iVTN (var Vj8[83.681], bool fv_)
	return

number Ymo[8,12.566E-77] <- false ## ]iV
## "jj>O&xv_FY)"hpMsH
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1454))

	def test_1455(self):
		input = '''
var upw <- true ## ;jY!3$zG00XK6o"m5
func i3 (bool LU[225.473], var Fk)	begin
		return 45.873
		if true begin
			continue
			## K#D2aY$}&>G|VN}F`VeF
			## JrzW5Jw
		end
		elif 4.166 if QZDY if "'"+'"" k_3 <- false
		elif 90 string dE ## v%N=GKc~3
		elif 969.838e25 for LGI5 until tD7 by false
			bool hM[0.987e-45,93.205,41] ## m4lE
		elif 3 begin
		end
		elif "u'"['"'"" QjA(true)[891.101] <- "@'"'""
		elif true string pU ## ~TDeB0qNYGir9c5#p"Z
		else var yb <- BYsI
		elif CPs for IzoV until false by false
			if false return
			elif Hkx Ofx("E")
			elif true begin
				number T9k[4] <- true
				begin
					begin
						## Z
					end
				end
			end
			else UI()
		elif true if 3e+41 for KpA until ke3p by 60
			break
		elif 74.783e40 break
		elif "'"'"+'"" UEp(true, false, hG)["'""] <- qLxm
		elif true for jjG until Zi by 6.856e18
			hY(jEGq, Xw, 5E-18)[mPY, "yL'"", nXAc] <- true
		elif 42E-19 Zm(false, true)
		elif "_el'"" if false dynamic wJsO ## qJ83t<|M=&UP1cu
		elif dC begin
		end
		elif 6.234 for Ug until 2 by "2EB'""
			K0X()
		elif 37.666E-51 if 218e31 continue
		else Mv(88.315)
		else break
		else jyDK()[17e99, true, 973.401] <- Phd
		elif PrM O4rw <- "'"'"[h"
		else var rafL[3] <- 84.265E+80
		## ,WIf
	end

'''
		expect = '''Error on line 3 col 27: var'''
		self.assertTrue(TestParser.test(input, expect, 1455))

	def test_1456(self):
		input = '''
var WX[9e+80,60e+52] <- true
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1456))

	def test_1457(self):
		input = '''
string scg
var s5Mi ## :;8JI~{
var NjrO[80.907,57,7] <- Tyra ## L(#X32|
## 6YG_*s,bL
'''
		expect = '''Error on line 3 col 19: 
'''
		self.assertTrue(TestParser.test(input, expect, 1457))

	def test_1458(self):
		input = '''
##  ?~BS{?OT*oPoS"
func URXd (string hb, number wg1h[44,12e+23])	return "8G'"'"P"

## PD~:5t<@Nrg}
number vzx[7.461] ## 6UnaT)5?M.75R
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1458))

	def test_1459(self):
		input = '''
func tO83 ()
	return 78E+82

##  mqO=e8IO(m<ld7W
dynamic LjHx ## we1Lhp-W;nbM@i<=
func q5b (bool w7s[4e64,6])
	return
## P<w3;ly"{Owy 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1459))

	def test_1460(self):
		input = '''
## [48Lg?
## *f1{vL/j ,rZvm/3w
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1460))

	def test_1461(self):
		input = '''
func so (var vt[5.812,500e+25], dynamic pO[51], number UKU[64.306])
	return
func Qr ()
	return 6e95
var yN[138,8] <- 171
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1461))

	def test_1462(self):
		input = '''
number Av ## $5m6
bool F4Q <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1462))

	def test_1463(self):
		input = '''
bool tvd[471.010e-07] <- 6E+73
string d1 ## Mb6wy:
dynamic Hj6m[38E57] <- Ia
## C!pW+_RB
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1463))

	def test_1464(self):
		input = '''
func HV (var R3t, bool fdlt)	begin
		continue
	end
string SrvZ[699,207.954e54] <- "g'"$'"}" ## BzO#i
func gj ()	begin
		Ja(false, "'"'"&Q")
		number w5RG[79.754,412E51,1E+62]
		## % SiJ+xX8
	end
number L7[891,79] <- oEy2 ## -@z>URW+CiNgM`o.
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1464))

	def test_1465(self):
		input = '''
func oCGz (var hQ[39e29,7E-29], dynamic JSz, bool x7R9[4e+78,714,31])
	return

func eR (string f7sg[8.908,69.072], var zgRh, bool Kn[493,607E-25,0])
	return

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1465))

	def test_1466(self):
		input = '''
## >
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1466))

	def test_1467(self):
		input = '''
func YK4 (dynamic ogsV, string GC)	return "'"pT'"'""
number WS[780E-36,5.081] <- 284E+82
func LP6H (bool rXPk, string F8JY[855.798E-19,369.306], dynamic Vy[7,402,9.808])	return
func AW (dynamic R7ti, var A5_f)	begin
	end

'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1467))

	def test_1468(self):
		input = '''
var Sp[95E+56,8.619e+44] <- 24.921 ## %:vqsd(saZ]=]CI&o/
func QX2m (bool qz[77.448E-65,3E76,4.770], number nqCU[3,2.070,594.865])
	return
## 5uk<_imr6?c-S
bool sU ## >PT 7ChTR>$(t`>_u%
func EY_d (var CWGW[3.661E26,0E57], bool jX0z, bool Ro7c)	begin
		continue
	end

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1468))

	def test_1469(self):
		input = '''
func I2G (bool Rj4, dynamic GW[996,4.029])
	return

func On ()	return

string kZN[0.318] ## N+K~:%&,zapqC~Q`VwP
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1469))

	def test_1470(self):
		input = '''
## ^5J8Q
func GT ()	begin
		## 57
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1470))

	def test_1471(self):
		input = '''
## *~
## [pU
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1471))

	def test_1472(self):
		input = '''
string hd <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1472))

	def test_1473(self):
		input = '''
## 7b1:}
func wF2 (bool xb, bool aq)
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1473))

	def test_1474(self):
		input = '''
func VTC ()
	return ipKY
func l9Nl ()
	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1474))

	def test_1475(self):
		input = '''
func eb (number xFcr[29,368,941.921e67], var MyGk)	begin
	end

'''
		expect = '''Error on line 2 col 41: var'''
		self.assertTrue(TestParser.test(input, expect, 1475))

	def test_1476(self):
		input = '''
var RE[48.350e-20]
func FHg (dynamic Xu2C, bool Dz6p)
	return true
func L5 (string Flj, bool Dj4[2,3.844], number Lg[69E80])
	return

## oOotc6"Z
func OdU ()
	return "'""

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1476))

	def test_1477(self):
		input = '''
## 3<
## eqB7
dynamic e2 <- "[jCn"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1477))

	def test_1478(self):
		input = '''
## +3"oNzwc-.`
number RcG[49.376,0.384e+74,1.285] ## $sO-vRZD nxfM<b
number g4 ## ~E:@G5PcnrO<qoW
func xAft (string PeG, bool RO)	return QVVy
bool ZT[47.176e95,53E-30] <- 6.165 ## t^TJCE7S:<Yur
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1478))

	def test_1479(self):
		input = '''
## VHke:SdSaNCCttP"9O+T
## <3u#
dynamic xI0T <- "qm"
## [igqm.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1479))

	def test_1480(self):
		input = '''
## UsFB{SB[*)5F;d
var iQAE[2.189E+92,44E72] ## bPFdV)Y
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1480))

	def test_1481(self):
		input = '''
## nZ/3jXvZ{W 1Gw#%
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1481))

	def test_1482(self):
		input = '''
func cHw (string IK, string TF9D[0E27,247.050], string as[957.478,3.471E11,0.833])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1482))

	def test_1483(self):
		input = '''
## /vRVwe]
## <
dynamic yTN[612e-48,6]
func emL (dynamic Wb0t[8e55], bool tp2, bool vVIm)	return

var UE ## I(i#v*j
'''
		expect = '''Error on line 4 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1483))

	def test_1484(self):
		input = '''
## v_|(a*q$CwWWRqC9aa>%
func qa (bool cE6)
	return
## p%w7Wsk6g
func gHF (string bj, var EG9U[49.953,35,87.871])	begin
		## 3HeN{c7%]
	end

func uw0h (dynamic LbS)	return
'''
		expect = '''Error on line 6 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1484))

	def test_1485(self):
		input = '''
number seM <- "'"U" ## i;sS0I<@.#8FqguYPPvf
## BJ&hK!j
number jwH3 <- true ## k"jgjQ;bN 
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1485))

	def test_1486(self):
		input = '''
string zBSo <- Dy5X
func tqr ()
	begin
	end
## Pytkb,+?qf3E8J1
## ahX3CpO
## /Oy1Zb)R
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1486))

	def test_1487(self):
		input = '''
string KqX[9,6.426] ## C{ ^d
string h6bV ## FSc_gp
func jpSS (string oxI, var h0e[2.714e+74,731.247,16.162], string qmU[49e90,280e+74,3.879])	return

string EAd ## 4e2Lz%
'''
		expect = '''Error on line 4 col 23: var'''
		self.assertTrue(TestParser.test(input, expect, 1487))

	def test_1488(self):
		input = '''
## 3
func aavc (bool ojY[5.623,46e32], dynamic zVQ, dynamic jGxT)	return
'''
		expect = '''Error on line 3 col 34: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1488))

	def test_1489(self):
		input = '''
number wJ[934E04,138,80e+59] ## e I#BZT]XWE(zM~*_{x
func pA_t (string Zbra, var Qc)
	return
'''
		expect = '''Error on line 3 col 24: var'''
		self.assertTrue(TestParser.test(input, expect, 1489))

	def test_1490(self):
		input = '''
func ZNb (bool Mf8, var dl7, bool TEt[781.714E+36])
	return

## U
number Md[1.780,579.473] ## 3ez`;bLo~
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1490))

	def test_1491(self):
		input = '''
string GMNw ## hGX(].(R;7
func BF5 (bool Ig_, var noXU, dynamic LBAh)	begin
		return
		break
	end
'''
		expect = '''Error on line 3 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1491))

	def test_1492(self):
		input = '''
func hYe6 (string VcXn, bool Xa[16e-11])
	return false

## w|9mC!mm5z=Bm
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1492))

	def test_1493(self):
		input = '''
## a3>51}(!Bm($;Ab
## CiV|f7E<*
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1493))

	def test_1494(self):
		input = '''
dynamic i5[9,0E-10,956.392E+84] <- qWI ## "I ,{USaTTM>k
func t4hV (var fzzZ[5.561e80], dynamic PZ[42,631.538E24,0.574E-42])	return o9F8

'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1494))

	def test_1495(self):
		input = '''
## m
var Rph[2.736E08]
## y
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1495))

	def test_1496(self):
		input = '''
var eui[2e-90,1] ## `O=(9WmR
var C3 <- false ## On-/WGb:
## 13n3AX2B"YS#Vlx
## V>hvLt<Xh@e3x49=<A
## iPMih8-fsU~dLd&
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1496))

	def test_1497(self):
		input = '''
bool zlx[302.382,57E69,0]
func vw (number lcN, var ENw[5,60.254E-72,995])	return

func CJG ()	return

## iS3`)~wX(iqhO-e.;<
## e`Xq)]
'''
		expect = '''Error on line 3 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1497))

	def test_1498(self):
		input = '''
number ZGG7[90.728E+57,955,280] <- cs9B ## m<maZCVuJ
var koVx
func sV (string fA[5.674E-47,395,175E16])
	return
func mLI (var p_ZG, number Efw[81,8], dynamic Q7p)	begin
		begin
			## `[pJ7R)30xx0-
			continue
			bool BZ[203.865,1E-64,66.575e-48] <- true ## 7!pM9JA
		end
	end

'''
		expect = '''Error on line 3 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 1498))

	def test_1499(self):
		input = '''
func D2 (bool atdU[2.608,10.033,9.167E+21], bool smr[930.822E29,95,123E74])	begin
		return true
		for xx until 2 by 152e-14
			if 7.901e06 return
			elif "'" T'"" for uqGF until jD by true
				break
			elif G6Q break
		bool aa
	end

func jFoq (var WK[3,33.740], number jRM, bool nYv)	begin
	end

## aX 5$~:!e
func n13J (number K5[4,4.420E-28,475E+85], number Zlk[896.549E-48], var bf[21,7.415e94])
	begin
		## #MNL *}Q+)5FWND2V,UO
		## eSH8@B{l{>c{
		## 2DX[9Q|o@$q79MUU
	end
## I7=9}jIS_as#
'''
		expect = '''Error on line 5 col 6: 7.901e06'''
		self.assertTrue(TestParser.test(input, expect, 1499))

	def test_1500(self):
		input = '''
## O%Knj j
func fgm (dynamic k6)	return 256.247

func Axl (number SX)	return

## l[>CX>
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1500))

	def test_1501(self):
		input = '''
func UUO1 (string te[93.414,168.391e76,89], var be[6.021,91E+41])	return 12

func gQ (number v0Vc, dynamic CpH, dynamic bLZ)
	return

## RMnR1qV8@a >EM:4k
dynamic LfU <- C7
'''
		expect = '''Error on line 2 col 44: var'''
		self.assertTrue(TestParser.test(input, expect, 1501))

	def test_1502(self):
		input = '''
func aIo (number jY, number Qeh)
	begin
		Y6mL(8.537, KBH)
	end

## l7PUwwI 6"
func tD ()	begin
		## ,:
		bool DZWk[625.540e-01,2.309] <- MqS
		continue
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1502))

	def test_1503(self):
		input = '''
func MBs (dynamic d6H, bool gRcd)	return
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1503))

	def test_1504(self):
		input = '''
number WGt[90.433e+20,5.035e+20,362.293E-91] <- iUK_
## cfNS>G%$>o
## J0.xp
func Vaa ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1504))

	def test_1505(self):
		input = '''
dynamic cO[75E87,34] <- false
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1505))

	def test_1506(self):
		input = '''
func iec (string dl7H[185E64,89.259])
	return true

## O&)AJ@A]3Cq]/;1`9nU!
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1506))

	def test_1507(self):
		input = '''
func K4UA (number jQT, bool CZjV[1.162,7])
	begin
	end
func mpC5 (dynamic SNH[51.019e12,0.139E+27,9], number Tg, dynamic ArPY)
	begin
		break
		number bN3 <- UgU ## ?xmW0G6
	end

func umbs (var bEzY, number Ut)
	return

var PM2c[3e-16,79.801e-05] <- 36
bool xupl[0E50,9E+51]
'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1507))

	def test_1508(self):
		input = '''
func ZJ (bool BTW, bool nd[98.211e18], string vpq[121.038,1.371])
	begin
		begin
			break
		end
		if oZ4 bool bGJ[9.375E06,16.335E-22,627e70]
		elif 8e66 dynamic b9l <- "'"1'"'"'""
		elif true Yn(0.170, true, "'"")
		elif true bool v6j8 <- 85 ## 2
		elif 25.927E+83 continue
		elif 0.919e+08 string CT[6E+33]
		else return
	end

'''
		expect = '''Error on line 7 col 5: oZ4'''
		self.assertTrue(TestParser.test(input, expect, 1508))

	def test_1509(self):
		input = '''
## QhK,,"
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1509))

	def test_1510(self):
		input = '''
## 2N+q(m4/5Bfu
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1510))

	def test_1511(self):
		input = '''
## -33;l
## :(vG8D9m-6iOBBO<
func f1N ()
	return "'"'"o'"'""

dynamic Pwc <- 992
func rStL ()	return "'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1511))

	def test_1512(self):
		input = '''
func sUK (string U8[2,177.446], var Rk, string tO[8.674e-86,36e-51])
	return

'''
		expect = '''Error on line 2 col 32: var'''
		self.assertTrue(TestParser.test(input, expect, 1512))

	def test_1513(self):
		input = '''
## =Br,YN"tz5f;UQk5u
## "VI7sP]4K7t{+kjMJ
## sW2 wX
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1513))

	def test_1514(self):
		input = '''
## @e6dO6*<(;%le
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1514))

	def test_1515(self):
		input = '''
## vj,s9k9@Ic@_
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1515))

	def test_1516(self):
		input = '''
## ?&wOn]kDQ!@
func Hk (bool AXK[249.455,4.893,17.506], dynamic YSU[527e+54,50,408])	return false

'''
		expect = '''Error on line 3 col 41: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1516))

	def test_1517(self):
		input = '''
number wHf[387.822E+70] <- "b'"'"" ## /}[q3gOT,-3gPP
func Ydt (string ae[26.634E64,7])
	begin
		## z[s5%:gA{
		bool bqFt <- pChl ## $M8g`Lzj
	end

func jPZf ()	begin
		## R6rm$/PE]6:x;?_!02
		## G}-%l@G2^Z5a
	end
## c9 2Wpf
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1517))

	def test_1518(self):
		input = '''
bool qM[40.978E+09]
string TD[34e+21,8.375E05,38.244e61] <- "1'"HZ" ## L@s8pcU,
func eD (number wNXV, var iXj2[566.109e-56])	begin
		for C7O until 1.331 by "Q|"
			break
		return
	end
'''
		expect = '''Error on line 4 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 1518))

	def test_1519(self):
		input = '''
dynamic zU[21.294E-57,0E26] <- dcsz ## 5q7uNDA@7>N 7|
number le1[51.158e90]
## C=eh
dynamic ErKO <- Jac ## hX`!8e
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1519))

	def test_1520(self):
		input = '''
number gmt[738.282,202,3.535e-00] <- 8.603E-04 ## L{_E9
string Qa[768E-95,75.761,836]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1520))

	def test_1521(self):
		input = '''
func p4 (dynamic ZX[60.298e-04,97.047e40,48E+48])
	begin
	end

func M4N (bool i8yl, number oP, dynamic WH)	return
## k}K5U6H+5FQAwy:r
func Gs_y (string iGvR)	return zvD
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1521))

	def test_1522(self):
		input = '''
dynamic ag[324.993]
func t_ (string t3wc[3.210E-70,9E-29])
	return R4WC

## |"d^`~ecpF
func Uyj (dynamic TATk, var n4)
	begin
	end

'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1522))

	def test_1523(self):
		input = '''
## 1#7QPaWLdwv -]]I(
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1523))

	def test_1524(self):
		input = '''
## 2:
dynamic ta_ <- zS
func pMI4 (string s8p[6,9.097])	begin
		begin
		end
		## /qL<JnJUw+xKZEX%ncY"
	end

func Qfe (bool Aogh[938,26.922])	return "8m'"Z"

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1524))

	def test_1525(self):
		input = '''
func Xk (var ox[84.876E-51], dynamic lSo, dynamic Fl[156.604,16e+45,273])	begin
		return
	end

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1525))

	def test_1526(self):
		input = '''
bool BgX8[18] <- GX
number Rf
## b.:l,QZ*bTr-YE_<>%6j
func Bes1 ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1526))

	def test_1527(self):
		input = '''
bool dPO <- 4.661 ## $J%901
bool Iqq2 <- "'"" ## 98CSJ63EOAkE2V
bool KigO[743.517] ## hrybA%Sr^/n$Yhu{EdN
dynamic MB[0,13E33,5.345E-27] <- 7 ## T_;cdxUGRMR(d_;^
'''
		expect = '''Error on line 5 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1527))

	def test_1528(self):
		input = '''
## t2_YtL%c+
## )q,dL_n7_D^>@*
## `6J^q$vVJ
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1528))

	def test_1529(self):
		input = '''
func j3 (string xL[763.221e+78,119E-45,28E-06], var w29)	return "'""
'''
		expect = '''Error on line 2 col 48: var'''
		self.assertTrue(TestParser.test(input, expect, 1529))

	def test_1530(self):
		input = '''
## kr
var rviQ[2,0] <- 501.311e-21
func Lmva ()	return
## /|)]@LijW
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1530))

	def test_1531(self):
		input = '''
func Gu ()
	begin
		## 2^jPv`YoxIgz-!g1Jp
		## :.
	end

func As (string xw2[315e-14,639E+34,20.950], var f0S6[520,86], number I2Z[313.207,1.267,164.112])
	return

'''
		expect = '''Error on line 8 col 45: var'''
		self.assertTrue(TestParser.test(input, expect, 1531))

	def test_1532(self):
		input = '''
func jQ ()
	return f27K

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1532))

	def test_1533(self):
		input = '''
func Xw ()	begin
	end

func J4M (number KuoQ, bool xOC[14,733.738,3.290e35])
	return Cg
## KBO!lR"0W>3iA %Us4
## "1<.:
dynamic Wuk7
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1533))

	def test_1534(self):
		input = '''
string wYcR[484,39.327,507.455] <- 13.583 ## ;SQ>.
func VVZO (string rPh, dynamic J3jP, number mIu)	return true

func VBM (var B0R)
	return "h'"L'"'""
## vG/_S#EY
func yy65 (string kvMT[2.383,37.940,516E56], dynamic y2tU[695.880e+99,14.395E+99])
	begin
		## R#/pw2gd8J8G4PT
	end

'''
		expect = '''Error on line 3 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1534))

	def test_1535(self):
		input = '''
func uK ()
	return 8.526E18
## SuE7FGI/Xfq
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1535))

	def test_1536(self):
		input = '''
number cKk9 ## UqA)D}4S
bool vPi <- false
func B96 (string V8Jl)	return

func cC (string xqI, bool ox)	begin
		## /Rq]~Cq1O7
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1536))

	def test_1537(self):
		input = '''
dynamic qKH
func CSl (dynamic uOy, string HvPI, var lndV[799.007])	begin
		SfGQ(Wx1l)
		Nb2n("P'"'"'"", 343.307e+20, "5b'">")
	end

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1537))

	def test_1538(self):
		input = '''
## hXa)/
## D%&c9
func tn7 (bool uP5, var Tpzc)	return
'''
		expect = '''Error on line 4 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1538))

	def test_1539(self):
		input = '''
number bh <- false ## tDh0M^Cp),ruL,RTiM)
number C71
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1539))

	def test_1540(self):
		input = '''
## QI~Z[R<^|bH&!zC=
string QY <- 5.797 ## gf)ejC8yt^GyfOM@?
## j{FiRH=UK#Ta.P6g.
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1540))

	def test_1541(self):
		input = '''
func Zqm (bool RE[86.937])	begin
		## A~qHPW
	end
func QUq4 (string Q36G)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1541))

	def test_1542(self):
		input = '''
dynamic ws6 <- 76.981e-59 ## b,Xf5$cuGS]v0
func qt ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1542))

	def test_1543(self):
		input = '''
##  ,$j;1/Z,
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1543))

	def test_1544(self):
		input = '''
## W$K!b9}/t=_Y<n
## yz|/D&0B}IC5
bool bABB[549.769E99]
func bws (var e3AH)
	begin
		## &m
		## ;
	end
number DXc[6] <- 5.051e-15 ## FR
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1544))

	def test_1545(self):
		input = '''
func DoNN (bool or[49.527E-30])
	return
var k_7f[519.367e+34,898.421e39,408.041e23] ## .:M5tY20v>n
var v2X5 ## rk,^|uEY/RsT*B`
## _;.1}OT
'''
		expect = '''Error on line 2 col 16: or'''
		self.assertTrue(TestParser.test(input, expect, 1545))

	def test_1546(self):
		input = '''
func S_a (var dMGj, bool mXI[4e76,937.955], bool CiA)
	return

func cZId ()	return 424E-98
## &PQMX2[eK2P]7_2
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1546))

	def test_1547(self):
		input = '''
## EFkB,|b)V3$Y^z&:
func XC (dynamic tt[3.045,1.470,933.636], dynamic cC, number y4JA)	return

func yIR (dynamic R_[6.116e-14])	return "'""
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1547))

	def test_1548(self):
		input = '''
bool wGQi[405.751e-41,13.865,233] <- D02 ## *^x<o
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1548))

	def test_1549(self):
		input = '''
## lkJO2&JY}5KybO2
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1549))

	def test_1550(self):
		input = '''
func aqG_ (var dSe[115,18.208], bool K2x, bool wn[8.448E+40])
	return
## {~^Beq.q7(=E0UE
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1550))

	def test_1551(self):
		input = '''
## ]O{WD!)^s
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1551))

	def test_1552(self):
		input = '''
dynamic cei
## b/|o7
func M0XV (dynamic QN[306e+52])	begin
		## s9_#qvc6Z31c%VN"p.~^
		## @t2k7U/aY/lZ:zd0
		for wTZ until "'"}$X" by 717.694e-69
			bool w_
	end
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1552))

	def test_1553(self):
		input = '''
## O
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1553))

	def test_1554(self):
		input = '''
bool UDES
## q
## bCPj4)pn;w(uz|_
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1554))

	def test_1555(self):
		input = '''
func T5N ()
	return "'"a""
dynamic JI[4.467] <- "'"'"'"'""
var JHt[495] ## (NzY25jf~;quKSsq rN]
dynamic WmBM[278.951e84] <- UgD
'''
		expect = ''''''
		self.assertTrue(TestParser.test(input, expect, 1555))

	def test_1556(self):
		input = '''
## G`crb^86q&82jMc.+YR
## 0L-b2fmC:,LMA/Txv
## k{}?Y
## &cHC.Or$*
number rT <- AOHM ## NfY5sGC
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1556))

	def test_1557(self):
		input = '''
## }Ej#"PHJiE
dynamic gVaF[7E+39] <- Fx
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1557))

	def test_1558(self):
		input = '''
func Y5EN (var hIz[13.893E+95,0E-73], bool I0[704.164,5e81,7], dynamic smT)	return 958

bool jvE5[3,275.855e04] <- nvI ## j5eK,4?&34d+Zb[6
dynamic Gz6h
bool S5n <- 75.804
func Rc ()
	begin
		number ps[8.115,9.997E+88,71]
		## -6_XPR.@[P{CJE/?WtM
		continue
	end

'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1558))

	def test_1559(self):
		input = '''
func sE (string Vrbb[2e44,957,563.856], var s_9[6.199,435])	return "+8"

func lc0W (string Ybl[11E51,852.393], var UCQ_)
	begin
		## *9d~X[GV!sy2cY+gC%>y
		## O_4
		## [a.f$3mRy/k
	end
func eC ()
	return
## Fu&)5(Vp
number FtW
'''
		expect = '''Error on line 2 col 40: var'''
		self.assertTrue(TestParser.test(input, expect, 1559))

	def test_1560(self):
		input = '''
## eN|QJ*]i2*
number ogC[78.363e-13,4E+50,1.548E62]
## {T6BQK?e[&
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1560))

	def test_1561(self):
		input = '''
var ehx9 <- "'"" ## v[l)bdT
## 5kaajB6g^U-;%
## +P!ju-g1B-d]Wf~Bw
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1561))

	def test_1562(self):
		input = '''
## g
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1562))

	def test_1563(self):
		input = '''
number cI[81e46] ## X;Ih?>rz=iNT
func wrsx ()	begin
		if "'"r" return
		elif true tvhc <- "'"D"
		elif YKz fC()["'"'"", false] <- false
		elif "'"'"'"" for e1K until "J'"E" by "d'"Xp9"
			number VwQd
		else return
		break
		qj(" '"'"", 85)
	end
number gjT <- true
'''
		expect = '''Error on line 4 col 5: '"r'''
		self.assertTrue(TestParser.test(input, expect, 1563))

	def test_1564(self):
		input = '''
func JUPU (dynamic gw[540.040,302e04])	begin
		break
		## "BqZmX&t_CU^8|
	end

bool Xg1
string Bhy
func CX ()	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1564))

	def test_1565(self):
		input = '''
bool BZHy[727.424e09] <- false ## .CC;[x#$SqHTq
func VcMf (dynamic Moma[560e+64,705.357], dynamic Jx[2.610e-17,73,6])	return 6E+96

number xig[28.548,50.172,733]
bool lE <- "I_"
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1565))

	def test_1566(self):
		input = '''
## {u_4`p!z4F
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1566))

	def test_1567(self):
		input = '''
func ZiU (var HSX, var Cdz[89])
	return qT

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1567))

	def test_1568(self):
		input = '''
## lB>Yx
## -`.#
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1568))

	def test_1569(self):
		input = '''
func XgN (dynamic SWzC, string mn[22E+08,3.222,3.950E-66], var Dx[4.384])
	begin
		number tS <- false
		return 1.186E-35
		## A=g
	end
var IRq[14,13.934] <- false ## 0CXqA
'''
		expect = '''Error on line 2 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1569))

	def test_1570(self):
		input = '''
string LIpS[85e80] ## iGQ+
## ?1ry{:{TKUlow
var bpj[124.303E+24,48.146E99,6e90] ## Sks$
dynamic DV <- vrID
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1570))

	def test_1571(self):
		input = '''
## beOE@Uf
## [iv]m~.-8nD:Jt4!)HOT
func rwfv (string jL9, number Ihy[1.465,4e+58])	return
func mD88 ()	return false

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1571))

	def test_1572(self):
		input = '''
func DTr (bool o2[9], var NP35, number qt1b[56e-28,205.083e94])
	begin
		for zE2 until cyjL by 9.543e-43
			continue
	end

bool ulO[2.657E+53,546,8e06] <- w8t
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 1572))

	def test_1573(self):
		input = '''
## f-Vx%
string KRs[5e-47,606.573E-39]
func FF (bool MBi4)
	return
## Jum>2+L9wR;0%{/R#
## u%$b1G3uy<&:Z
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1573))

	def test_1574(self):
		input = '''
var Ct[44,88.357] ## w-x"wMi;?
## RW%M.B
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1574))

	def test_1575(self):
		input = '''
var lU[73e35,24.204E-53,88.531] ## s;,<P.|BC[G.N 4
## Rf#h2?!#iu:?k<z,q]^
var yTT <- "'"'""
func jn6 (dynamic JDb_[451.212e-56], string xFS, dynamic BJ4)
	return "'"ec'""

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1575))

	def test_1576(self):
		input = '''
string FL[7e+22,22,74]
number M4
func FEOo ()	return true
## wibkyx{s!42*u#l4(~1
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1576))

	def test_1577(self):
		input = '''
func Oij1 (var Tb[5.242,432e-66,613.416E10])
	return 169E+03
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1577))

	def test_1578(self):
		input = '''
var zz7 ## 8/nCu] Sv5k+hHphs
func jYWy (var ZP[30.135e+25])
	return false
dynamic Tf_[8.087] ## X,^J&VQf 0a$6yv
func yNm ()
	begin
		number LNYQ
		## .%z|EN}Xj4cW
		## 8VHJeIq=I31x
	end

## b_xtKj)O1TMeYwJ=/^
'''
		expect = '''Error on line 2 col 28: 
'''
		self.assertTrue(TestParser.test(input, expect, 1578))

	def test_1579(self):
		input = '''
string yn[15,22.016] <- 1e53 ## (w^JV`|""@&2u
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1579))

	def test_1580(self):
		input = '''
string tN0r <- 660 ## 8,?
## y
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1580))

	def test_1581(self):
		input = '''
func yvK ()	return 568.774e60

string I7P[0,292] ## }
func ZW6 (number NJd)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1581))

	def test_1582(self):
		input = '''
## WsEh(CeJ"6,8J
dynamic k_w ## FC2!JsYpR*4f
func aA0 (var ofE, var q_[802,393])
	return 0
## u0 "`{{n {3`o
var Jhcx[50.010e+72,734] <- 8.557 ## _IA?#-
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1582))

	def test_1583(self):
		input = '''
func XO27 (number U9XJ, var A1, dynamic Rh[543E38])
	return
## mx^
func a8G (var K6, bool NR, string Fp[125.505E+99,68.287])
	return
number jXg <- 40.849 ## W
'''
		expect = '''Error on line 2 col 24: var'''
		self.assertTrue(TestParser.test(input, expect, 1583))

	def test_1584(self):
		input = '''
string vqU1
## #q1pRIuX
var kKgZ <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1584))

	def test_1585(self):
		input = '''
bool hn[6.052E-49,5,37e04] ## .2
## {0wRtPf$,Hec
number P77
bool FF <- true ## 7B:
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1585))

	def test_1586(self):
		input = '''
string vc <- false
func fhvh ()	return
number IOy <- true ## r;2_EBe.Pe)S.Rz`%u
bool i3 <- Xq5
func VA ()
	return "'"7E>"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1586))

	def test_1587(self):
		input = '''
dynamic wbU7[483,74]
number YtFw[1,848.706,910.481E-20] ## ))$TBZpV7sJ8
func vHJP (number aQ[53E+31,92.109], string fd3N)	return true
number Dmr <- 91E-72 ## ;}ph
number ejHY[60,7e-75] <- false ## !8k1a`U^~WDFC1xW:_
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1587))

	def test_1588(self):
		input = '''
func Hg (string un[219e+85,736], dynamic BG_0, number DjkT)
	return "A'"RN>"

'''
		expect = '''Error on line 2 col 33: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1588))

	def test_1589(self):
		input = '''
func vhig ()	begin
		## YITce/
		## xqad/+V_xK7#YTj9/`#
		for uz until "m " by true
			break
	end
## Su{V3$Uz#%rAj2fJw
## ^>
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1589))

	def test_1590(self):
		input = '''
bool uGis
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1590))

	def test_1591(self):
		input = '''
func vsAR (string SKk, dynamic y3[98E-36,1.868e+06,49], dynamic SuT[184.505E+96,973.897e+22])
	return

## ?
## r
dynamic deb
'''
		expect = '''Error on line 2 col 23: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1591))

	def test_1592(self):
		input = '''
## <
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1592))

	def test_1593(self):
		input = '''
var mmZ ## L&<!ErS5cD7)xRl
## X1&}T=leGGVF+ahO
'''
		expect = '''Error on line 2 col 26: 
'''
		self.assertTrue(TestParser.test(input, expect, 1593))

	def test_1594(self):
		input = '''
func T8Gx ()
	return YA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1594))

	def test_1595(self):
		input = '''
func k9x (bool TcP[153.342e65,13E+09], var ppJq, var z9[2E-90])
	begin
		iV_()["'"J'"4'"", false] <- 575.152e+76
	end

## :=2Vy~D"EF>v]:Vv
number QAXr[6,9.924]
## IC0z{1DPm].(Yz]Q~
'''
		expect = '''Error on line 2 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 1595))

	def test_1596(self):
		input = '''
## X1[k1c}JSsJ{7
## m3Ep]]+!seY
bool qROe[921e+89] <- "+" ## b~;>uwyKsv5 Q}
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1596))

	def test_1597(self):
		input = '''
func AHcI ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1597))

	def test_1598(self):
		input = '''
## )aRS</w~tieW_pA=
var JAb[7.876] ## {zZ(]
func Pq (bool iy1[591.426,9.335,83.956E-01])
	return kHc

func WH ()	return "O"

'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1598))

	def test_1599(self):
		input = '''
func jYiZ (bool LTW[53], number ON)
	return "S>'"Rn"

## z2rW>K;P*v!o0-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1599))

	def test_1600(self):
		input = '''
## gB
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1600))

	def test_1601(self):
		input = '''
number jaHP[290.754E+90,296.883,8.415e45] <- true
## @y|/V[ig
func PJlI (number Zt, bool mI)
	begin
		KZq2(fKnG, Zj_S)
		## 0ih7=
		## 3t(3BNGf19q,RDGyH.S
	end
func bV8 ()	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1601))

	def test_1602(self):
		input = '''
func lOX (var CWL[9,993e+47,699E93])
	return
bool MeSQ[9E+44,231.802] <- "'"U'"H'""
## 2t:DI#iLpl3H$
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1602))

	def test_1603(self):
		input = '''
dynamic f_Fu[0.472]
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1603))

	def test_1604(self):
		input = '''
## l|o~,.Gf,WQ,.0iglX.D
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1604))

	def test_1605(self):
		input = '''
dynamic sM9[30e-79] <- true ## 8o Y_68=3ixjv7
string IUAo[4E-89,58]
func Xi (var o5RY[68])	return

## ftR_
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1605))

	def test_1606(self):
		input = '''
func AG (var Rl, bool nnd1[87.956])
	return

## 64)|
bool Nc0r[2.983e89,3.751e-01]
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1606))

	def test_1607(self):
		input = '''
## ^DT|%9w`<K
## -vQ
string Z38e
## 3Z}`rZYY-
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1607))

	def test_1608(self):
		input = '''
func Lr (dynamic dvAA[1,115.263], var J6XW)
	return
var OG
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1608))

	def test_1609(self):
		input = '''
func KMXX ()
	return

## |+L?zB|
func HTz8 (string UM, string tN, number lw[904.251E56,44])
	return 43.295
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1609))

	def test_1610(self):
		input = '''
var Oc <- "WML"
func ssu2 (var E1g)
	return
## P3;4 0`hI+
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1610))

	def test_1611(self):
		input = '''
number lvg
func OWm ()	return vXq3
## CS;jo}Nq.<:g%A3
func Mh (var Jk[73,99,48.135E+74])	return k0S

string uJv[6.787E60,26.505e58] <- "d" ## ({Xd_BQ
'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1611))

	def test_1612(self):
		input = '''
bool Mq ## M2A7a^R~]2MOt
## z;zD6/cvhj,p D~t
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1612))

	def test_1613(self):
		input = '''
func UR ()
	return 15E+20

## QE9;:^
dynamic uTYb <- SX
string csvl[5.939E+80,481.397] ## (D]aa]g$W
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1613))

	def test_1614(self):
		input = '''
var sK0[8.212E-34,63.582,2.690E-99] <- fipp ## 2gx $!c{XPq`]Q3M; 
number z_[61]
func kR7 (bool rYo, dynamic eN)
	return

## [
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1614))

	def test_1615(self):
		input = '''
func v_yr (var a8)	begin
		continue
		for xeFn until "q'"" by 344.261
			for CfTe until false by true
				for H2P until MV by false
					V0tr[false, ZDEd] <- "['"="
		## z+-oV],(K+1<
	end
## x>B~"#y>?TY(JE@
bool Piz[984.547e+89,789.383] <- false ## 1n$V:
string WLE[91,26.586E-86] ## OOuOUL
var z21[62.282]
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1615))

	def test_1616(self):
		input = '''
func IB (dynamic Xs, bool GK)	begin
		## H@zlX
	end

func qV7e ()
	begin
		## Qjd=F
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1616))

	def test_1617(self):
		input = '''
bool mAwX[771E+02,4.066] ## &,;0rr01X
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1617))

	def test_1618(self):
		input = '''
## EF/tU$?aO}q;
func ajUr (bool p3Dq[976e-24,14,6e-77])
	return q8s7

dynamic EjrS <- 62.566E-80
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1618))

	def test_1619(self):
		input = '''
string Q5
bool HvQ2[15e47,7.814,5.539E+07]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1619))

	def test_1620(self):
		input = '''
## 8@<t]PC%Ceec)N:
## N
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1620))

	def test_1621(self):
		input = '''
## f<?L=P
## %O6-H*>3Mzv{jVnZs*
func Hlcd (number ud)
	begin
	end

func dH ()
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1621))

	def test_1622(self):
		input = '''
func q8 (string tw, bool GYqK[3.270E+52,277.103e+70,94.583e+27])
	begin
	end

func pd ()	return
func L0dG (dynamic Dh8q[18e+21])
	return
bool eb <- VIKh ## QZw~r[pXCZ.
'''
		expect = '''Error on line 7 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1622))

	def test_1623(self):
		input = '''
bool Xz[5.475,973.996,3.971e+36]
func fOR (dynamic Ek7u, bool ao)	return true
dynamic Wg
bool Tno ## XLR#
number ApVv ## 2DN"8{OhAkQ%7&4Y
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1623))

	def test_1624(self):
		input = '''
func OUQ7 (dynamic oA[90.098,534.892e-37,75.342], var OTE[73,13,5], var dDR3[13.230E83,75E-85])	return 86.751E+77
func jk (number jQ, number bV9s)	return
func iD ()
	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1624))

	def test_1625(self):
		input = '''
var tbT ## >*eyd`iJ[!u
string O_ <- true
## 35^Ot9}~5cL|@[G
## !7U=>9NPW.=I1
## UPrTo;}e{{T},t;e/^G|
'''
		expect = '''Error on line 2 col 22: 
'''
		self.assertTrue(TestParser.test(input, expect, 1625))

	def test_1626(self):
		input = '''
func wI (number Up, var d_Yl[24e28,27.451,7E58])
	return true
number ckd5 <- false ## 9U(vS3#l#*$
func q9xw (var wZzu)
	return

##  a9|1>z[.|b
func gal (var gu[620E-04,86.184E-53])	return sP
'''
		expect = '''Error on line 2 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1626))

	def test_1627(self):
		input = '''
var IL2 <- 7
## n?/=hx;<$?R+/)2]!ew$
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1627))

	def test_1628(self):
		input = '''
number MdGz
bool p9b6[445E20,540.092e+68]
var mh15 <- 539 ## ,/g09/c
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1628))

	def test_1629(self):
		input = '''
func hM ()	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1629))

	def test_1630(self):
		input = '''
func pqeh (dynamic fv[2E-47])	begin
		continue
		## ZbW{M#fv-7tR[yF}
		bool vJbZ ## cLO`[G,pb dns
	end
func MW ()	return
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1630))

	def test_1631(self):
		input = '''
## e-uRJ#DE
func QmH ()	begin
		## AO` 6;o
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1631))

	def test_1632(self):
		input = '''
## #/n
var AdA <- "'"G"
## S}JYae
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1632))

	def test_1633(self):
		input = '''
## PZA;<<QC>{ZGRt/
var UnuS[838.647,748.465E-56] <- Amk
string gSN ## g<_#bIo@9zb
func hY0 ()
	return 403.635
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1633))

	def test_1634(self):
		input = '''
## gF[`D3-
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1634))

	def test_1635(self):
		input = '''
## ]AN[b:tJ 7;C-}1[y
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1635))

	def test_1636(self):
		input = '''
dynamic Z_v[5.398,13,29.790] <- "q'"r"
## u?{#:2`8K
bool ph_i[788] <- 50
func qh7R (string vUV[751,5e-51], var szOM, string Zd[780.519,6e66,646.760])
	return

## 11`&<lR?I,kcZaR6P41D
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1636))

	def test_1637(self):
		input = '''
## H1>^yX.&B&r;
## t_xQKVN??c#).Zp1B
func fWS1 (var Vh, dynamic vqi[99.812E-41])	return

number ZX ## >xr,Ruk
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1637))

	def test_1638(self):
		input = '''
number FRU <- 307
dynamic qbX[2,99.175,26.115]
bool qq1 <- "'"N'"'"F" ## McxF%-K*b4?|qT
var fP <- true ## O7uc~r6>
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1638))

	def test_1639(self):
		input = '''
## %Nin4pwWdz$_QIZ.
bool opA7 <- false ## `>VlA=
func ysS ()	return og

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1639))

	def test_1640(self):
		input = '''
func QTe (bool d0AY[390,6.871,24e-78], var v79)	return
var eM2G[99] ## v@
'''
		expect = '''Error on line 2 col 39: var'''
		self.assertTrue(TestParser.test(input, expect, 1640))

	def test_1641(self):
		input = '''
bool rVxr[53E-45,0,900] <- "'"l'"4"
func vyV (dynamic x6h)	return 865

string Cp2 ## V>aBaD
func kJA8 (bool Z1Wh)	begin
		begin
			if 8 if IHSv pEi[BZHx, false, efc] <- 55E+43
			elif "HF'"'"" for CbCD until ns by 6.709
				dynamic k3u[49e+28]
			elif false continue
			elif true dynamic Vze
			elif 94.493E16 return 5E-45
			elif false continue
			elif 54.055e+21 break
			elif 24.042e+43 if 4 break
			elif "'"" dynamic o1l ## za
			elif bA5w for RbDs until true by 186e+13
				for Jq20 until false by 58E-89
					ubHa <- "Y-"
			elif Jkcg for bDL until 48.362 by false
				return true
			elif true if true break
			elif dQsV begin
				if HE9 var W9i ## PjFLmJ*
				elif false begin
					for CJ_ until 492 by false
						if "'"M'"" return zEpV
						elif "1'"t=?" return
						elif 7E08 Ff <- "}"
						elif "MT'"" EZQC("'"")[59.871e+14] <- "'"bj"
						else if ";'"VD" for PSm until 7E-51 by true
							bool qlm[31.869e27]
						elif true jmNr(false, "a,'"", "'"9+")
						elif gj KYac[iFT] <- true
						elif "]'"" begin
						end
						elif cj Vk("'"*")["'"c/"] <- CgN
				end
				elif "'".Z'"" for VV until true by false
					var Cc <- "'"1'"'"'""
				elif ZgLT continue
				elif "'"'"" begin
					sh0[QT, "'"H", lNJl] <- false
					## atE`IVL(zm#&x@/IwB-!
					return
				end
				elif 73e+75 break
				else for xzA until false by "'"z'"'""
					begin
						continue
						GP("'"3Z", 95.211E+93, mQU)
					end
				## JGWtCQo^_Y>-P
				## &6
			end
			else if true xhZ()[a3X] <- SP
			elif 799E-29 var kRcW ## ;>V#PFFic2cjyBI"M4
			elif 9 PZV()[false] <- "~"
			elif 472E24 return
		end
		begin
			## dM
		end
	end

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1641))

	def test_1642(self):
		input = '''
dynamic QO[9E+16,4E+48] <- nU
func cMbh ()
	return gso
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1642))

	def test_1643(self):
		input = '''
## MqILEWen
## #WEU16ykUi
func UbfD (dynamic GE, string G0f)	return xS3Q

func lajY (dynamic Wa4L)	return
'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1643))

	def test_1644(self):
		input = '''
## [SqT"g
string Dz <- 22.497 ## <D!!SySq*N
func jNiS (dynamic Jvtd, dynamic UttT[157e+84,62.933E93,64.857])	return "'""

'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1644))

	def test_1645(self):
		input = '''
var nHk <- false
bool dfp[5e04,8.925] <- 14E+85
## =LCl0clBs?CwX1,vZ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1645))

	def test_1646(self):
		input = '''
##  9iL;4VtN7h^b
string eQC[7.766,5.576]
func v4c (dynamic qQF)
	return

## )fe6]?X/|B6`-am
'''
		expect = '''Error on line 4 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1646))

	def test_1647(self):
		input = '''
bool WX
number a3fQ ## *
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1647))

	def test_1648(self):
		input = '''
bool g0mG ## MSn^{<=
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1648))

	def test_1649(self):
		input = '''
## hA;d]=K^BpV%x~
dynamic rTDS <- false ## [+7%P(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1649))

	def test_1650(self):
		input = '''
## -WE$f
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1650))

	def test_1651(self):
		input = '''
var sg0t[36E+69,888] ## e&A6o1ln~Vd_vWu3
number Az2F[2.479,7.113e+06] <- "3'"'"T'""
func Mf2n ()	return

'''
		expect = '''Error on line 2 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1651))

	def test_1652(self):
		input = '''
## 1G`=K+yWW;m;Yo
## Ql&R{bV8"QjYjtV
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1652))

	def test_1653(self):
		input = '''
dynamic Az ## SXqLh$>I
func mH (string koX[79.470,54E-28])	return
var OTNt[46.525e-92,82,5e-10] ## Fms|0%
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1653))

	def test_1654(self):
		input = '''
## x&ow)
## ;@2}CFrPU
## 8
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1654))

	def test_1655(self):
		input = '''
## ,f/Nir
func lL (number R_hj)
	return
bool mR3[66.219E+24,803e-72] <- true ## s{kg=Ik!N
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1655))

	def test_1656(self):
		input = '''
func UD (string IBW, var x7, dynamic hDG)	return
func Lf (dynamic GA_)	return "k"

bool Kr5u[6e-52,2E02,917] <- "'"P'"'"" ## R`f2:|2>8R86 ?Oza^}9
func TJ1b (number kt0I, var ue)
	return
'''
		expect = '''Error on line 2 col 21: var'''
		self.assertTrue(TestParser.test(input, expect, 1656))

	def test_1657(self):
		input = '''
func oMyN (var s865[2.040e+24], number kiO7)	return 3.224

func xFf (bool Fcr[59.751E+09,2.890E-07,5.778e-88])	return false

## ]3NAw-n&zN8D03
## 5FJlDMPH-f[s
func p3mY (string LM[84.456], var GWNC, dynamic m8U)	return
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1657))

	def test_1658(self):
		input = '''
## rne_-5EVn
var Yr <- 43.299E+57
func yU (dynamic BXbx[8.171e+85,789.547e-10,764.086], string ue0b, string wFZr)	return

'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1658))

	def test_1659(self):
		input = '''
## |Eik}l?!J|p
var vJwA[62.748e-53,254e32] ## cjuqRh+;0 Z
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1659))

	def test_1660(self):
		input = '''
## *3r-TLv}&scIP5Zu-dYy
func XbpC (dynamic g_ht[5])
	return oQNt

string ZkQh ## "!vrZ
## )H#Gc+k^~`}dJ&
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1660))

	def test_1661(self):
		input = '''
## y)e0ZSjjB4rpK&8.~
## !4aC){
number knl
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1661))

	def test_1662(self):
		input = '''
func YwM (var UwYP, dynamic V4l[4.421E+60], dynamic qe[2.357,39.076])
	begin
		break
		break
		## b+#C-vF<
	end
## J+f!c|wl(9LKO[
## #DJtN6q)R+Kc:-@iZ9
func oML (var X1XD[91.837E35,9E-32,977e-48])
	return 7e+00

## }.6*PR*LGGsV
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1662))

	def test_1663(self):
		input = '''
func fQc ()
	return
## j@THOL~F,43Iqdqnee
func bvz (var fSyY)	begin
		for LUb until 281E-90 by true
			break
	end

string BI ## `1}N6RYQH
'''
		expect = '''Error on line 5 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1663))

	def test_1664(self):
		input = '''
number K9So[65E-43,1e+70,6e-39]
func pqL (bool Uz[835,18,5], number rB, number Qet)	begin
		## |HcGZ}N fB_a;6=4
	end

## OLQ$|ZZt]1tP59
## $t.w^t?w!q&
## y&f4(jrMxy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1664))

	def test_1665(self):
		input = '''
func SNl (var z2BI[5.247E90], number xGOp[99,8], dynamic SjR[74.408E+72,557E-06,59.317])	begin
		## ypSlH
		## i #6s?0
	end

func vOzM (dynamic KH5G)
	begin
		if false dynamic sa
		else begin
		end
		for dp until "'"x3'"'"" by "'"/"
			for SxU0 until 11.196 by "'"p'""
				nu <- 5.501
		## ~<8n@tr :k!j#7rp/t
	end

'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1665))

	def test_1666(self):
		input = '''
func KDLq ()
	return

func kqM (bool Wy7H, dynamic Gx)	begin
		WBy7 <- mvE
		dynamic Gma9 <- "'"'"'";'""
	end

string wa <- true
dynamic rBn[3.266E-78,17e74,11] <- false
'''
		expect = '''Error on line 5 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1666))

	def test_1667(self):
		input = '''
## XI0=7mBO*7O22&;
func Aw (string CWt[76.173e-84,0.941E-81,8e67], dynamic aQ[3,0e-09])
	begin
		## !?c/%7CE
		## ZQ7"+^u+v*~0.
		bttr()
	end
func V5S (number z5AI, bool gEl, var oJK)
	return "'"u'""

func VTL (dynamic U2t[2], bool ARdD)
	return
string aRix <- Ldrw
'''
		expect = '''Error on line 3 col 48: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1667))

	def test_1668(self):
		input = '''
func SDTv (string BlNQ)	begin
		continue
	end
var Js4[6.571e-90,696E94,4e-53] <- lFQo ## D
func JM (dynamic KBt_, bool r6[77.086E-86,22,5.660e+63], number T7w)
	begin
		return
		## i#b)8*?"<TX[>JJq
		continue
	end
## )4;`Tf4<0
'''
		expect = '''Error on line 5 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1668))

	def test_1669(self):
		input = '''
bool XpI
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1669))

	def test_1670(self):
		input = '''
bool l3x[388.188E98] ## $#NbYP{-hl||CF(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1670))

	def test_1671(self):
		input = '''
func R4 (number SEmq, var jN, var wC[70.270,4,33])
	return "$9'":'""

number km <- TH7w ## 0uk]Z|E>Q1(:/&oRO#>
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 1671))

	def test_1672(self):
		input = '''
number g2BW ## .k)pRU3.<Jce
## t./XyfN
## p
func iOo (bool R2E[820.772,4.702], number Un, dynamic VR)
	return

## d@^Mct
'''
		expect = '''Error on line 5 col 46: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1672))

	def test_1673(self):
		input = '''
func Duku (string yjHU)
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1673))

	def test_1674(self):
		input = '''
dynamic C6x[448.414E-36] <- q9E
var m9Kh ## _&*XrZ)js;hP5G2
func FA35 (bool HaW0, string K5[2e+95,9,341.465])	return NPk

## ^a%W|
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1674))

	def test_1675(self):
		input = '''
func m1 (bool gOe)	return
func NN ()	return
func EYR (var Nmwu, dynamic ZclN, number QlK)	begin
		## 3b8)rb969S3QimZ4f
	end

## 7z`XB3d[S4~qo
var wId[635.751] <- ")?b"
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1675))

	def test_1676(self):
		input = '''
## *}|[}
var wxe[4E+44] ## <[=/T`
dynamic M4DA[166.043] ## at7bR(^]p2sUP4
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1676))

	def test_1677(self):
		input = '''
bool B8tz[652.626,78e-74] <- "'"'""
string uVD[8e-10]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1677))

	def test_1678(self):
		input = '''
## W/-q ,?
func j1b (var qiwp[950.738E-89,8,96], string OE)
	return

func J3RZ ()	begin
		return 4E+06
		KqaC <- 55.230
		break
	end
func atH (string LQ3, var zL[11.002e-87,17E+29], dynamic qOkT[86])
	begin
		begin
			## d6uF)X F
		end
		for heey until 5.030 by 84e47
			for e4 until false by bKjN
				bool ti <- 31.359 ## FHnl-o760J2Z
	end
number EKio ## D"PV|GL!exkU47%S[_l
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1678))

	def test_1679(self):
		input = '''
bool WA
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1679))

	def test_1680(self):
		input = '''
func UP (dynamic XE3O, bool nZ[70,272e-58])	return false

## [.Rq7l#i
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1680))

	def test_1681(self):
		input = '''
## xXPfUX%6l
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1681))

	def test_1682(self):
		input = '''
func qfC (var qev, bool u6Q, string Xc[732.341])
	begin
		## Iq"^
	end
dynamic iU <- "'"'""
string lCv6 <- 76.768E55 ## ;P&P}T
## :#ht^=8b*4<dmh
## W%6M
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1682))

	def test_1683(self):
		input = '''
func sf (var cz, dynamic bl)
	begin
		## ]Oc29;<I9-
		continue
		## vo(r:,+2sHD
	end

dynamic Blr[881,2e-79,653] <- "=,"
func S6A9 ()
	begin
	end
## [+GF6Z5f<Om(
var Uzp[96E-41,634e+93,964] ## [sMs`x~4h8tC}x.
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1683))

	def test_1684(self):
		input = '''
bool Cc6 ## ?|sLD)77f@p]az{<"
func QGz (var lo0B, var nW, bool d_d[181.070E-19,273.205,895.735])	begin
	end
func ueZw ()	return 48.568e59

'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1684))

	def test_1685(self):
		input = '''
dynamic Vr3 <- "'"'"^'""
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1685))

	def test_1686(self):
		input = '''
## "6ND:
number gxKs <- true
string b9Hs[54.941] <- false ## szlIL33QT#?hEE3BA
## x;SV,SYuR/zU:(*q
func vor (var q9R[2,869E25,545.598])
	return "'""

'''
		expect = '''Error on line 6 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1686))

	def test_1687(self):
		input = '''
bool SP_ ## lv17$]Ky;=>7A[:
## n#U8Iw]Q9@ZI&2_R]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1687))

	def test_1688(self):
		input = '''
## d;A;d
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1688))

	def test_1689(self):
		input = '''
## GH;GpG=.t%iw4w]6F:)
string vdD
bool Xht ## / #hHTes
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1689))

	def test_1690(self):
		input = '''
func XH (var o3Y[9], var KY[667.016E-07,554.302])
	return

func z2Nt (string PrBS[686.375e14,4], string q44, bool KUG)
	begin
		## EB(#i-=Om}VH
		begin
			## !>p;$Q
			for UYmp until NM0n by "'"='"'""
				begin
				end
		end
	end

string I6[2E+42,757E-44] <- 6.374 ## }B@`9Si3L1BU0NF
func lKD ()
	return true
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1690))

	def test_1691(self):
		input = '''
var l3a[832] <- Jp ## cbehg_&9Y[7iRU!z/
func BFng (number M0c[113E64], number txa7)
	begin
		## _q
	end

'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1691))

	def test_1692(self):
		input = '''
## 9Jwp[C,p7oNnt%Mac
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1692))

	def test_1693(self):
		input = '''
## B6p+eai9lA}w}f(5t
var lSAr[68.280,256] <- 6
## <5Ytmv
## h1kl3U,m
'''
		expect = '''Error on line 3 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1693))

	def test_1694(self):
		input = '''
func fWZf ()
	return 14.382
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1694))

	def test_1695(self):
		input = '''
number n51[159.098,412E+30,537e-68] <- 5E78
func ZMA (string cX, bool pc)
	begin
		## sly
		## 5Ppat2]Y*mUb|sFCrj=
	end

func Eo (var Y_, dynamic xLI[40.919e-52], dynamic FHY)	return false

func xrJ (string Ub, var b0[18.286], string uogX[217.243E+55])
	begin
		for UOl until "K'"K" by 53
			continue
		JQ["'"", "'""] <- "'"^"
	end
## 7`U;@qQ
'''
		expect = '''Error on line 9 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1695))

	def test_1696(self):
		input = '''
var PX[7.647E72] <- ykWJ ## ^3z*vF+l
'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1696))

	def test_1697(self):
		input = '''
string vF[8e+37,163.964]
## xP^L;:$8|&P*H]AVcBq>
func rK ()
	begin
		unV <- false
		## p
		## e]qv#>9}
	end

func GBK (bool zf[1,2.011e+11,90E38], var Qu[7.563], string dA[0.190,90.372E+64,3.056e+97])	return "'"'""
func eF (bool Dy[30E-05,1], string T8xs, string QnJ[30e81,49.731,0.227])	begin
	end
'''
		expect = '''Error on line 11 col 38: var'''
		self.assertTrue(TestParser.test(input, expect, 1697))

	def test_1698(self):
		input = '''
dynamic Sq <- true
func abGo (var aUBe)	return

'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1698))

	def test_1699(self):
		input = '''
number pm[4e72,930.752E14,62.714] ## =orVuch6U#G#!@c=>!?
bool ns
## Bf.7|t*as?Z[ODwU(j
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1699))

	def test_1700(self):
		input = '''
func bapN (number IO0B, bool Z82)	return 94.985e59

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1700))

	def test_1701(self):
		input = '''
func Gzwr (string RDL2, dynamic eVC[973,10.286,0], var z6)
	return DNYt
func EKV (string hC1v, dynamic UhRE[98,37])	return true

## rc/apN 
'''
		expect = '''Error on line 2 col 24: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1701))

	def test_1702(self):
		input = '''
func a8W (bool Y4K, dynamic imhD)
	return 507e+82

## DRj
var dpi8[4.325E90,76.825] <- "J'"'""
## 2v>tA"-;m%w{T3(
## n_ItHyC.;^^QmJ
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1702))

	def test_1703(self):
		input = '''
## 6!LT:+,lj@WcKWW
## Z"wE!`R[/f9xNUx!
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1703))

	def test_1704(self):
		input = '''
func C9 (string phi[3.089e+82,558e21], dynamic yes[73.273e-99,95,20.460e-04])	begin
		## +/(zZC)zg_C)/NOlp
		if HHZ if gqE return Lgp1
		elif SP begin
			if true continue
			elif true if 59.006e-13 Tu7()[5e97, yclP, IJ] <- GSRE
			elif "}" for Qn until false by vt
				string cv[4.949E-04,165.888] ## C~G.$E
			elif 61.486E17 LHm0()
			else if true if true return K6
			elif "'"1'"" continue
			else dynamic W5Yw[92E+60,59E+42] ## ~YB^ESKF)+ F(~}^/
			elif true for qIo until true by p82p
				x_t()
			elif "'"'"'"G" begin
				## GB=ZA(Y
				break
			end
			elif vFKG NyR(true)
			elif Tpe OnO(ZKX_)["`'"'"", true] <- HKX
			else return
			elif 2 if 49.695 var G4[1,970,494]
			elif true continue
			elif "7*" begin
				string HZiA <- true ## kvH8
			end
			elif 553.348 break
			elif true continue
			elif 66 return
			break
			## 3p(| m0~=?:OT+8Pe5*V
		end
		elif 73e-54 return
		elif 898 break
		elif false for Ap until "'"5" by 14.423
			return
		elif XXLh number hFz0[125,27.240e+43] ## fHi4}ty#=xX"1t_lu:l
		else if " " begin
			LMQ <- 4e43
		end
		elif "As" tb <- Xc
		elif false begin
		end
	end
func P8 (number cqc[44,9e+42,9.143e-75], string fuT)	return fT7

func mi ()	return true
'''
		expect = '''Error on line 2 col 39: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1704))

	def test_1705(self):
		input = '''
## Vt(sR]Q;I#_irF.kR/JJ
## q~- 4KtML^b`+vG
func jE (string bEE, number FAQP)
	begin
		## 4h[xV/)-G=aY]Le#2P+
		bool eP7 <- true
		dSbl(false, qCH, false)
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1705))

	def test_1706(self):
		input = '''
## RoHtp_s@i6=w$;d
func Gdd ()
	return jCD
## <fD]7`.an7>/e/_Ofv2
## #T[
func jJSa ()	return Ypy
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1706))

	def test_1707(self):
		input = '''
func wAG ()
	return 8.668
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1707))

	def test_1708(self):
		input = '''
string It <- IHLu ## w[>@GaUm-sbB|@JY!H
var RJe[94.541E24]
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1708))

	def test_1709(self):
		input = '''
## }VBIGR+eRP{Br61
number iz[1.286e47,9e-52,9E38] <- false ## lz=u4I
string cY
## JET~(y UuC&XU%o(
func OKa (var sl1R, var CbTW[827e+50,91.182], bool CZ7)
	return "'"T!"

'''
		expect = '''Error on line 6 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1709))

	def test_1710(self):
		input = '''
## abD%DeBj]
## 8H~VK68
dynamic D5Fg
func EJje (number X5l[6.494,46e-63])
	begin
		if fOU begin
		end
		elif true string FjJ_[45E96,3.267]
		elif 86 TV()
		elif true break
		elif 8E-81 continue
		elif QT sd[false, VeFL, "|'"^'""] <- 731e05
		return false
	end
'''
		expect = '''Error on line 7 col 5: fOU'''
		self.assertTrue(TestParser.test(input, expect, 1710))

	def test_1711(self):
		input = '''
var OJmf <- 11e49
func aM (bool go)
	return

## qI1U4Xwy 7
## F68`Dg(dB<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1711))

	def test_1712(self):
		input = '''
dynamic C2PC ## dp9WX}^wOfp
func kBF (bool SNu, dynamic hytP, bool N8)	begin
		if "+'"" break
		elif false FN_()
		elif g1J dynamic NN <- false ## vg*CrbhbL/tU0fX><
		elif 197.523E41 if false if "'"I" continue
		elif false if "K" PpF(lvyC)
		elif VR8 begin
			## ELK<Mc;)p!eh
			for tMPl until tsO by "Z"
				if "'"I'"" begin
					break
					for vb8 until false by 9.617e-58
						return nPqd
					## IB:jhq9B4X
				end
				elif true begin
					## WeMdm9V5VwD]Ze/A5v
					var lB[296.073,5] <- true
					return
				end
				elif true for qUA_ until 2.543E-41 by true
					for npzZ until false by ymFw
						break
				elif false return ";zNK"
				elif 595e+74 GMy()[false, leZa] <- true
				elif 0e79 begin
					if F1 return false
					elif cw for ZH until 7.722 by xhZq
						r95_("'"5", "'"")[true, PPoZ] <- 73
					elif St6 return 51E+71
					else if cA continue
					elif "'"7'"" begin
						return
					end
					elif XS QWYJ <- "f'""
					elif true for uf until iuZ by 884.707
						return
					elif 2e56 var jclI
					else return true
					## u*
				end
		end
		else return
		elif "^N'"" continue
		elif "]br'"4" break
		elif yow begin
		end
		elif 498E79 begin
		end
		elif "'"" dynamic LSU ## r@1.8n
		dynamic KIh2[77E-63] <- YQLY
		for Jl until "o'"e'"T" by wf27
			FwTD("g[7", 58e+46)
	end
## M_R:~p*`#rg2U
## M?nD0[;LkgJkn/2
func QN (var cFA5, string SNZO)	return
'''
		expect = '''Error on line 3 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1712))

	def test_1713(self):
		input = '''
func YqT (string JuVm)
	return

number e9J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1713))

	def test_1714(self):
		input = '''
func Hkf ()	begin
		break
	end

## `7d
## }u]vnlPP-#t
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1714))

	def test_1715(self):
		input = '''
## rQ#hrK1CJz1bFI
number EOSf <- 45 ## H"t
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1715))

	def test_1716(self):
		input = '''
## &wx$!wSQ{DB
func CxbI ()	begin
		## WLr16 %2
		## E?f_TE1V"31f.+t!f
	end
## +IR)BDTQy*-m?d3Bhb
func pW (var H9[22.903E+85,712.650E+90], var pn7)	begin
		## AZhy1K?rYV{
		begin
			tq(nFz, "'"'"", 119.155)
			## +E[KI}]HcMJ[Y3u],;rQ
			var ma ## +p26ml E(Ez5xlx
		end
	end

'''
		expect = '''Error on line 8 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1716))

	def test_1717(self):
		input = '''
bool PVo[5e89] <- "'" c'"a"
func lSoz (string CZ[65E73,1,383.782])	return

func vi7m (var iOl, dynamic t0)	return
func apq (string P2n[5.180], var Wf1)	return
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1717))

	def test_1718(self):
		input = '''
## q?vZNt;HY:>b
func kDf (dynamic Sjy, var W0[231.943,714,3], var wW[7,989.188E33,500.086E60])
	return

func vW_ ()	begin
	end
dynamic tP <- 18.545E-95
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1718))

	def test_1719(self):
		input = '''
func Kw (var AtVc[64.929e-30,5.130])	return true

## OpOc$]p
bool UvJ[512.259E+10] ## |67n([%oU
## xR]o4NfcaHN-5(
## S^ {`zb-! 
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1719))

	def test_1720(self):
		input = '''
bool iDR[56e+55,82E08] <- 8
## ^C
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1720))

	def test_1721(self):
		input = '''
## zquXXI1k%W#
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1721))

	def test_1722(self):
		input = '''
bool hp9[4e-65] <- bb ## g|EDwA^y%SB_EIz2
## /kPj/NabeauO
bool Pu[93.017e+69,81e18] <- "z'"j"
## z}NoRG]4b("}S0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1722))

	def test_1723(self):
		input = '''
string G7 ## CB7,f
##  1z@r0
## !rX6UNK
number lR6[65.913,6.850E-31,48.121] <- "'"" ## [uSt c;j({Plc
## 1s,TN?{
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1723))

	def test_1724(self):
		input = '''
string QLT[2.265e85] ## ZsZn|3)0v
## {c1]
func LO3b (dynamic BNo[613.464E84,28.766E+25,52.823e-17], number vHi0[96.544])
	return

'''
		expect = '''Error on line 4 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1724))

	def test_1725(self):
		input = '''
func O8 (dynamic zA, bool eyi, bool W1)	return
number eg <- true
func wT (string GGQa[53e-51,5e+56,0.518])	return false

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1725))

	def test_1726(self):
		input = '''
## hkA@*M%EbMXDwH#oY
## q"2T[{R,M!l
func HvWu (number r6[1.388E-47,341E21,91.417])
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1726))

	def test_1727(self):
		input = '''
func ZRX7 (string Y820[10])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1727))

	def test_1728(self):
		input = '''
## +gMM?f]w[{9FKHtvnz8
## D=o(
func fB_ (bool ZnZ, number B6d[598E73,618,2.685])
	begin
		string yI_[4.228,2.685E+74,7] <- 0.636e-94
	end
## "AG?~D##!
## i>LB*f]w,%H<MO
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1728))

	def test_1729(self):
		input = '''
## b?)*~>H^/rkUpI
func QAU6 ()	return false

dynamic a95v <- "-WO" ## 5AW?(?+z(
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1729))

	def test_1730(self):
		input = '''
## [fNl}A)w
bool yVS <- true
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1730))

	def test_1731(self):
		input = '''
bool mfp[1.660E-39,234.731e-80]
var yT[47,736] <- "'""
## {3Q.+NB8PKFlS{mc~
## "CD qJ;t#t`
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1731))

	def test_1732(self):
		input = '''
## -FbKJjrnEo?@
func ud (var icE[5.450e+28,0.014e02], bool q6[569.597e+74], number gln7[3E-67,42])	begin
		## ZPK orLj8-
		## G4<s~,abCbtRhai7
		## ~ZBm!gm"P5/h)q[x?,q-
	end

## jC&vP)|*L[:%J
dynamic dlh[3.637e-81,131] ## (ah:gG`ydz]Cp?6o+JXM
bool HCq
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1732))

	def test_1733(self):
		input = '''
func S2 (string qh[656.941E-89,5.024], string Vd[9,83.120,0E+62])	begin
		## L5ph9vdYIk yCT5M
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1733))

	def test_1734(self):
		input = '''
func Y0 (dynamic Oxy2)
	return
dynamic zC9
func xdx (bool sW[36], dynamic yMrv[216.751E+23,662E+37,5.750], bool K6G[7e+89])	return
## /[?@{&|Q
func V_Xi (dynamic Oz, bool PV[386.842E-95])	begin
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1734))

	def test_1735(self):
		input = '''
func oB ()
	return
func lm5 ()	return vCwR
number BMY <- true
func E9IW (var Gm2[43,154.540e65], bool eFmp)
	return
## (K_vhXGVS<(Ek& 
'''
		expect = '''Error on line 6 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1735))

	def test_1736(self):
		input = '''
## s_
## k$sr$H/Yl!/xP=
func vN (bool bd)
	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1736))

	def test_1737(self):
		input = '''
bool YIRK <- 821
func Lm (string Td01[209e+20,65,48.882], bool zn[80.187])	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1737))

	def test_1738(self):
		input = '''
bool Jl <- 249.096E-40
func bDa (dynamic wwB[942e+36], dynamic lJ7, bool xoQ[2.449,7.389])	return 8.182

## }9BD$:".mrY2.a#-
func flv (bool joAT[25e83,2.110], var Mw[7e+87,364E+41], var UuEj[8.331])
	return
## ]7~Vee
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1738))

	def test_1739(self):
		input = '''
## I
dynamic J43[68.831e31] ## *sz?X~GFU<(^!P
## Jad;VHMR$SK@y<*jMmh
## f7c[G1Bkj=~RRA8y,
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1739))

	def test_1740(self):
		input = '''
var yn <- dWO
func vr (string KVTi[6.792,7e+90], dynamic nxH4)	begin
		## )
		return true
		e8(889E+19, 1e+66, "M'"'";1")
	end
var snk <- 6 ## r:Oo<E>lCR<
func Bb (bool m5b[91.154E+57,4,14])
	return

'''
		expect = '''Error on line 3 col 35: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1740))

	def test_1741(self):
		input = '''
## 0
dynamic sKSR <- 17.861E+74
var su[106,268] ## 2a9{{=Q(7|/CfYc:
'''
		expect = '''Error on line 4 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1741))

	def test_1742(self):
		input = '''
string Ao ## +K1+p=?)xxXjgR
func qV2m (var Cm, var T25[68E-70,63.258E+90,82.731E+13], dynamic bXMc[756.061])
	return

func xe (dynamic sia[1E+11,57.300e-95], bool L5JO[2.386,8e+77,4.798e-48])
	return

'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1742))

	def test_1743(self):
		input = '''
## #-fmntUD7y8m3n
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1743))

	def test_1744(self):
		input = '''
func xbc (string vfNN[68.136,553.626], dynamic Olm3)
	begin
		## jj8$jV&{
		break
		Ip(fO9, "'"C")
	end
## ;U)DgF`a;
## s^|!wic]!:%xg
dynamic rbQ <- false ## 9lS`29bOUlu=5
'''
		expect = '''Error on line 2 col 39: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1744))

	def test_1745(self):
		input = '''
func au (dynamic MS5[4.075], var H69y)	begin
		begin
		end
		## rxyly0JF ln
	end

func RqRl (number nB[2.029E87,73e+83], var xF[343e11])	begin
	end
var ED ## {U$6It"Y
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1745))

	def test_1746(self):
		input = '''
## J3f>70[d
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1746))

	def test_1747(self):
		input = '''
func Xk ()
	begin
		## bKQ5hStVvY"wIN/;VT
		continue
		## Q#} ekHl$!"klqzc:
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1747))

	def test_1748(self):
		input = '''
## ?I%qt VY|
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1748))

	def test_1749(self):
		input = '''
string uDd <- "'"kDR"
bool Mkh8[61,782e-34]
## -x?{e;8k=#Ki
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1749))

	def test_1750(self):
		input = '''
func G0L (bool OJRL, string AUVv[28.827])
	return
## gq(8A12V 8v7I
func LZ (var tM, number pZoj, var Ir[77.774,9E-86,9])
	return

func lRkq (dynamic SEva[9e33], string u5Fu, var Moe7)	return Azz

'''
		expect = '''Error on line 5 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1750))

	def test_1751(self):
		input = '''
dynamic mnk[7,0e-55] <- k0qJ ## 4VhOtsx0ABj#-;`
func PU0 (dynamic RE1Y, dynamic kq)
	return true

func Um0 ()	return
'''
		expect = '''Error on line 2 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1751))

	def test_1752(self):
		input = '''
## *RmSp_ct;?.JfNi E9
number Oi[85.763e+60] ## c:2/%
dynamic ywHA[1,9.435,594.295E82] ## k1
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1752))

	def test_1753(self):
		input = '''
## ehsH%`$1=}Re
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1753))

	def test_1754(self):
		input = '''
bool ncp[2,5] ## .~Dot6;TUGj5GdL0I
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1754))

	def test_1755(self):
		input = '''
func eJh (string HS4m[57.526E-15,1.114E-09,280.329e87], dynamic yHXy[86E57], number g2a[35.996e+59,41,23.025])
	return
## 9-hg
func KV7M (number Ga, dynamic H78[4.023,74.374E+91,0E57])	begin
	end

'''
		expect = '''Error on line 2 col 56: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1755))

	def test_1756(self):
		input = '''
## 7>V31w
func KAlo (dynamic kw2e[28,91e+48])	return begp
string Ep9r[79.803e84] <- 70.899
var uJ
'''
		expect = '''Error on line 3 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1756))

	def test_1757(self):
		input = '''
## O*gLzti
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1757))

	def test_1758(self):
		input = '''
func yf ()
	return true

## Hg.lBtw6%1876mc
var d8j[3] <- true ## Oe1f
dynamic jN <- fc ## dpG,e]"tuJ{/fj@J
func aYkE (string PTBq[24.987e08,228E+32,227e+37], var iJFW)	begin
		## 6hYw &ll3S/r>0#CFG6^
		## CSjrsw`v~y
		## DbZwVZ=^t[^39x #w
	end
'''
		expect = '''Error on line 6 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1758))

	def test_1759(self):
		input = '''
bool Gm0 <- 2.165E-81
## +.O
var Y_aT[7,15e+60] <- "'"=xde" ## c"hP#.HAo}t)VNd=-}#
string Mefy[95e+40] <- true ## [A,ZH
'''
		expect = '''Error on line 4 col 8: ['''
		self.assertTrue(TestParser.test(input, expect, 1759))

	def test_1760(self):
		input = '''
func IkZ ()
	begin
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1760))

	def test_1761(self):
		input = '''
## T6wlJ!
## ~Ie:"!lw
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1761))

	def test_1762(self):
		input = '''
## +h,"K)1$
func Km (dynamic DPW[21.843e67], number GTd, string hN)	return cD

## 38$Ai;W%530>d2<kdyT$
'''
		expect = '''Error on line 3 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1762))

	def test_1763(self):
		input = '''
## R9$.Xv>9@IJ=Qa^Xu^
## {6%bmVZmA]ya~
## I"E
## 2VZ&JAW
bool Dpzx[2.511]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1763))

	def test_1764(self):
		input = '''
func yjK ()
	return

var VR[335e+21,3e+47] <- tY ## 4:Pp:
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1764))

	def test_1765(self):
		input = '''
## s2=GC^XXdT
## iY"H`vmhdZ<mBut?8&la
## dC#N[p1`fQDov_If>
func TVGw (dynamic GN9, bool nbT[42], var Ld[114e+59])
	return
'''
		expect = '''Error on line 5 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1765))

	def test_1766(self):
		input = '''
func HQ (string f6, dynamic K3yV)
	begin
		s7F <- "H"
		Cf <- "'"Q'"'"]"
		for r2 until ywZI by "'"'"Q'""
			if "{j" begin
				G7M <- true
				## v;-aC
				## rNYlbAK5b0j
			end
			elif 893 number ORo[38.048E27,77.529e+33] ## -%9&TMV4/R0*
			elif v8fC continue
			elif V5 begin
			end
			elif 0.364 for dE until 18.037e-61 by 27e40
				begin
					if false for Tx until false by 81
						if 7e+62 UQaQ(938.446, false)
					elif 817E83 for oM until ob by 0e+80
						return
					elif false for j7 until 407 by 3e+60
						if 1.050 begin
							bool ZC[7,4.234E-69] <- false ## f3c{$@C8jQSEdfrE
							## AV0
						end
						elif "'"'" H)" break
						elif NI pUX()
						elif false qMZ("'"U", FU)["#{'"e"] <- 1.921E51
					elif true return 6
					elif qm37 number gi ## kV[=+`3Gfxa72
					elif gT break
				end
			else begin
				## P6$w
				## {UqmXWE}Ll
			end
	end

string CYA <- cKyu ## ;VOYn{^
func AOmu (var CK[4.975E+56,924E25,6], number AhS[5e-77,1])
	begin
	end

func tx (dynamic nUoA[4e-36])
	return true
bool omJd[86] <- true ## R2R5/=F+Gg<
'''
		expect = '''Error on line 2 col 20: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1766))

	def test_1767(self):
		input = '''
bool VNJi
## Hz#ew_M({b.S*
func T1kS (var AR3[837E+10], bool gxUs)	return
'''
		expect = '''Error on line 4 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1767))

	def test_1768(self):
		input = '''
## hSAf3ShHa,T1h[i_eG
func iwp7 ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1768))

	def test_1769(self):
		input = '''
dynamic vgIs[6e49] <- "]'"z"
func x4 ()	begin
		## M>:Y^ZQJ+R}WA
	end
func A9ov ()	begin
	end
func vpv ()	return 79.587e+50

bool L2[905.656,6.348] ## Qr-h*!5`UeTV{jv%?Jt
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1769))

	def test_1770(self):
		input = '''
## ;F6iiuCo-71.B>5;
func xIK (bool ps4Y, dynamic FxNa, number NO[11.494,684.713E07])	return 67

## xvI,E3nhP
'''
		expect = '''Error on line 3 col 21: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1770))

	def test_1771(self):
		input = '''
string rXVx[7E+76] <- false
## %U<jS"KW>x|
func my (bool iuw[1e-76,9,3e-96])	return "I'""

bool lqwc[28e01,4E59,0]
## Xq9vY
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1771))

	def test_1772(self):
		input = '''
func yos (number HzV)	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1772))

	def test_1773(self):
		input = '''
## famt[o 9_61Y
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1773))

	def test_1774(self):
		input = '''
## dbrVL{
func vZY ()	begin
		for Oh_Z until "5" by 7.992
			begin
				if "5,'"55" return
				elif KWPM begin
				end
				elif true if ">'"" continue
				elif "Q'"m'"" p8MD()[7, 667.997e+33] <- "?F$"
				else bool HC9[633] <- "~'"'"'"'"" ## ^!6Qbf3q;)jZx:=iJ&g
			end
		## *wVKs=j^DY~A,q#?c
		uR(7E04, kJc, false)
	end
'''
		expect = '''Error on line 6 col 7: 5,'"55'''
		self.assertTrue(TestParser.test(input, expect, 1774))

	def test_1775(self):
		input = '''
## f" p$3dev+ 4wpI$e
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1775))

	def test_1776(self):
		input = '''
func vZ (var FXR[84e+44], number fAW[5,69.886e-81,477], bool tM[102e-08,141])
	begin
		return
	end
## 5h3,+oo}9?/.q0Ft;K
var eZ
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1776))

	def test_1777(self):
		input = '''
## J+6.hP0M4l2"I<(
func nsr (var E47G[493])
	return
## -vD2:
func B0Jm ()	begin
		m4W()["'"'"'"", "'"p,", 39E+39] <- false
		## 1*
		d1Y[oTn] <- npf
	end

func UuZJ (dynamic Ez[833.356], dynamic i9[8.820E66,9], dynamic gkf[6])
	begin
		if 3E+94 number UZ <- Di6L ## U%(}`kf<Bb9
		elif false break
		elif "h'"'"FN" continue
		## 2S
	end
'''
		expect = '''Error on line 3 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1777))

	def test_1778(self):
		input = '''
func UM5 (bool Ju[13.901E15])	return "#>L "
## ;1c1ds
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1778))

	def test_1779(self):
		input = '''
## ^6T<:<v?(Q<j80
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1779))

	def test_1780(self):
		input = '''
var Y3S[5E+11,933E+51] <- true ## Dm?)H<_uAWkM
## 9{Y{|^=j-L6
var Giu
## h]|}7_#P?rImW
'''
		expect = '''Error on line 2 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1780))

	def test_1781(self):
		input = '''
func x7U (bool xeU[39.558], dynamic tSO[3.519])
	return "'")}'""

## $5$/nF~
'''
		expect = '''Error on line 2 col 28: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1781))

	def test_1782(self):
		input = '''
number vnN[58.844e+28,907e+07,8e-25] ## _iU5{^1_fn
## R4L+*G
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1782))

	def test_1783(self):
		input = '''
dynamic fu[1.006e+08,5.489E11,837e+45]
## OV
number rga9[6.532,29,2E+21] <- rS8 ## n:
func Yd ()	return
dynamic ZU0i[521.608,28E24] <- true ## G"=S"V
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1783))

	def test_1784(self):
		input = '''
var LndC
dynamic eix[11e+20] <- K71
## p~g3ll/NzRwRO2NT}Z
func ul6 ()
	begin
	end

'''
		expect = '''Error on line 2 col 8: 
'''
		self.assertTrue(TestParser.test(input, expect, 1784))

	def test_1785(self):
		input = '''
func eaU (var DGH[357.737,11E-09], dynamic cgV[956.812,0.290], dynamic iR9p)
	return

var mB
## In*/uaIVEL
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1785))

	def test_1786(self):
		input = '''
func UQuB ()	begin
		## ^JmNe
		## E?[L&
	end

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1786))

	def test_1787(self):
		input = '''
func rF3H (var LE, string f1)	return "f'"Q"

## Ws0l_tX@1:|w_m{
func rkJj ()	return

bool Dp1[241e88,63.535,76e-89] <- 667 ## :HW,
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1787))

	def test_1788(self):
		input = '''
string xQn[845E+42,315.437,57.557E+65] <- MO5o ## zij}SkUMerens
func jjSf ()
	return r5f
var Bkl3 <- 2E-76 ## dgplrX?+e+R
func gA (string tE)	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1788))

	def test_1789(self):
		input = '''
##  *h
## xIIM1nVJo(J9
## *@v{x$
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1789))

	def test_1790(self):
		input = '''
## /gU1Qu
func V9Lm (string ey[70.697E+40,4.752e+08], number dRYy)
	return true

## _uifL
## K"Vz[+g
## W"!wM#2tRC3VYJ_Wt
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1790))

	def test_1791(self):
		input = '''
func cQII (var MnrF[14.085,8.702,4E-73], var Ag, number DvW[355.560,6.717E43])	begin
		## -y*aY>l$KwhGv_GQfcVh
		## 0H`mI]H+X*xwlcPC)6
	end
func nI_6 ()
	return
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1791))

	def test_1792(self):
		input = '''
func nr (dynamic gP[84.794,109.644E59], number woh, var qAV)	begin
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1792))

	def test_1793(self):
		input = '''
number tbJH[8.340e32,9]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1793))

	def test_1794(self):
		input = '''
func rD (var KH, number V2G[130.388E08,6E81,15], dynamic GGE[4.505])
	return
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1794))

	def test_1795(self):
		input = '''
## 5ee7h2^RBLUyUtOlkG
func Kbpn (number S1mB[7E+56,802E66], number Uy)
	return

func pc (dynamic FlD, dynamic zfoF, string UQs[0e+71,1.453E+20,4])
	return 28.415E23

'''
		expect = '''Error on line 6 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1795))

	def test_1796(self):
		input = '''
## =e4[%" r?~uSy;NWs*
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1796))

	def test_1797(self):
		input = '''
func tPkr (dynamic mLu)	begin
	end
dynamic QQyX[505.213e+76,0.932E10] ## "Kc~$>JVy#GRn
string l9N <- "'""
'''
		expect = '''Error on line 2 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1797))

	def test_1798(self):
		input = '''
## k
var zjK <- false ## ^K{gX*yy_8NI
func Dq ()
	return "'""

## xvt{qhCkp~C75j?;B
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1798))

	def test_1799(self):
		input = '''
func ZQE (bool eX[9E-98])	return zc1G

func eiC ()	begin
		for y2 until true by "Q'"'"'""
			break
		## ]F
	end
## #od
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1799))

	def test_1800(self):
		input = '''
## N
number Tu[231.082] <- 13.358E+23 ## 0
bool QJQV[0e10] <- false
var IOj
'''
		expect = '''Error on line 5 col 7: 
'''
		self.assertTrue(TestParser.test(input, expect, 1800))

	def test_1801(self):
		input = '''
string wIn[28.328e+22] <- false
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1801))

	def test_1802(self):
		input = '''
string gZ8[1.128e-89,5.194] ## IfT$GF1IDt".oSn
func d0Uj ()
	begin
		## ACi+T=!o
		for d_oD until Lbq by 94.253e99
			begin
				## !!H;GLp=y!
				if jG continue
				elif "'"C^'"'"" t7 <- 397.851e75
				elif "'"0'"" break
				else for ug4m until "00" by "'"'"?W'""
					tOvc(432.942, "'"'"'"", false)
			end
	end

dynamic xWwF[8,442.791]
'''
		expect = '''Error on line 9 col 7: jG'''
		self.assertTrue(TestParser.test(input, expect, 1802))

	def test_1803(self):
		input = '''
func O6 (number m4[9E+30,42.125,847.686], string hAt[6])	return false
dynamic dwrM ## rYSbO(P[odYc!]"Z~$o2
## Szlz&,o
func Fh (dynamic fypP, string xgfd[83.648E-57], dynamic pubZ[883E-89])	return 6.043

'''
		expect = '''Error on line 5 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1803))

	def test_1804(self):
		input = '''
func Rf (dynamic Ra[61E90,58.616])	begin
		continue
	end
func gY (var Y5aK[748.050e-34,68,520.061e+14], number GtS[54.023,94])
	begin
		## &WM#"J~
		for f4 until "'"'"'"B'"" by true
			fGS <- false
		## KY=1jnTOepX]]G
	end
## N=SM#[uFCGm,].P->Ui
func IU (var aev5, dynamic a3Qj, var ObX[95E-43,5])	begin
	end

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1804))

	def test_1805(self):
		input = '''
func biFY (var yf[8E-07])
	return
## ?JKY>L9,F$
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1805))

	def test_1806(self):
		input = '''
string nV ## u8+p
number Iat[38.607,607,485] <- o2nb
## ?r*
func zR1 (dynamic jxeP[616.761,4E+87])
	return "'">'""
func CAmf (string UrQ, number SMOi[9E+52], number C0)	return 273e+10

'''
		expect = '''Error on line 5 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1806))

	def test_1807(self):
		input = '''
func LiW ()	return "O"

number gY
bool VZt
## AI
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1807))

	def test_1808(self):
		input = '''
string FT <- false
## -X)FJ:>kH/pMM&J?b
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1808))

	def test_1809(self):
		input = '''
## wp{w
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1809))

	def test_1810(self):
		input = '''
number ilvF <- "n'"0'"'""
func tpN (bool Uj[394.992e-19,7.123e+92], string hOY, string rrTT[0.975,88e-62])	return
func PL (dynamic oDfU, var lQ43)
	begin
		##  F
		## U"X
	end

## S"-JjQC+mJF6iEht
func AfEr (dynamic Nh8h, dynamic bI5, bool ujV[33.570])
	return "'"'"0"
'''
		expect = '''Error on line 4 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1810))

	def test_1811(self):
		input = '''
func Iht (string OiTo, string OncG)	begin
		## V5
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1811))

	def test_1812(self):
		input = '''
func hI (bool LVrt, string J1pE)
	return 539

## !C
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1812))

	def test_1813(self):
		input = '''
func Dj (bool rkl, var LzfH[3e79,416.323])
	return

func n5 (var Zc[92.580,90.332,4e+29], string gO3[71.338e+07,136,46.284E84], number kMjU)
	return

var qkH[9.421,221.405e79,818] ## uUtc~.~Mo/8F!/
func Wr9 (dynamic Zk[0.683,9.729E+20], string L2PX)	return
## ?Q>r13;#Ha(n5{T(
'''
		expect = '''Error on line 2 col 19: var'''
		self.assertTrue(TestParser.test(input, expect, 1813))

	def test_1814(self):
		input = '''
## ND.H1B$<KGr|4e3{2)EU
var k9fN <- 15e-21 ## xx4uVb)Xk
string UgbS[7.994] ## -ts+
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1814))

	def test_1815(self):
		input = '''
func oB (string b6V[0.579e-93,803.059e+88], number DM)	return 26.470e-10
## jtR
bool ZaK ## 59 bSXF=}w
## //ttO<?^cS&Z;!lIW)o
## L]fVtNNbQ6lA]/F2a
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1815))

	def test_1816(self):
		input = '''
func q4M ()
	return
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1816))

	def test_1817(self):
		input = '''
string bhr[592,0,643e-38] <- true
string Thhs[50,81,4.227] ## b{{
func Zksh ()
	begin
	end
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1817))

	def test_1818(self):
		input = '''
dynamic H1[5.265,7,39e76] ## 8T-lgb/Yt#)
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1818))

	def test_1819(self):
		input = '''
var S9y7 ## x-2nc`.
func qi (number sSTj, string Y2)
	return true
func g2V (string ob[5,212E72])	return
'''
		expect = '''Error on line 2 col 19: 
'''
		self.assertTrue(TestParser.test(input, expect, 1819))

	def test_1820(self):
		input = '''
func dlHB (var ZK)	begin
	end
## `
'''
		expect = '''Error on line 2 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1820))

	def test_1821(self):
		input = '''
func GB (number nfn[5.163,2e+50,77.732e-12], var Ushp[6.887,223.313,924], bool Uq3R)
	return

## [glKc#cy7v~qLhv[
'''
		expect = '''Error on line 2 col 45: var'''
		self.assertTrue(TestParser.test(input, expect, 1821))

	def test_1822(self):
		input = '''
func p9PA ()
	return
bool oUs[749.586e+97,76.776e73]
dynamic jD00[3,78e-21,75.576] ## R!xWxWc(2cXUO^CtK@
bool fEhM <- "'"'"#" ## -F}V`Tld#9i!mjg{la
## i1 ZWFAWA~2&~J
'''
		expect = '''Error on line 5 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1822))

	def test_1823(self):
		input = '''
## ##
func XOK (string Yvx, number OX[9.528e91,939.452e+67], var C05y)
	return OjUQ

number oCx[632] ## zKM*aP/ji8acx4h -
var ZLpR
number Weh6[975e+35,6.987] ## }9)9Y3VzP;?~gg51
'''
		expect = '''Error on line 3 col 55: var'''
		self.assertTrue(TestParser.test(input, expect, 1823))

	def test_1824(self):
		input = '''
func HV (dynamic xgST[5E+23,6E+45])
	return false

func ko8 (bool Hpl[2.847E75], bool JqYY)	begin
	end

func jOG (bool vuHM[73.919E+18,25.003e+29,49E58], string GR, dynamic KFn[77e-07,3e29,2.932E88])
	begin
		## Y61_
		dynamic nmL4
	end
## 5&s;1ft=L=> 5Ue2x%Y
## 0iT,)QTN)Yq"MXG;c
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1824))

	def test_1825(self):
		input = '''
dynamic icwS[8,738.093,7.648] <- false ## T1Hr>.z~!4A{L1/Mj
dynamic ONS
'''
		expect = '''Error on line 2 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1825))

	def test_1826(self):
		input = '''
## iynE/o9XI2
dynamic lja[7.687e69] <- 1 ## #0x&jM2L^
func p_LL (string OIH, var Ud[540.421,460.874,8e81])
	begin
	end

func QX (bool YSL, string cfP[77.527e+82])
	return "Cj"

bool rZ <- "'"N'"" ## sYl(<-]
'''
		expect = '''Error on line 3 col 11: ['''
		self.assertTrue(TestParser.test(input, expect, 1826))

	def test_1827(self):
		input = '''
bool Aj[55.492E84] ## 0%q0 Enf(#*16Q%Q*
func Cr (var FK0[944e23,875.055E+78,817e-99], number GDyu)
	begin
		## Me.8PS0j*[tSVP{
		## JHjM"r4-?VBP~3@]#
	end
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1827))

	def test_1828(self):
		input = '''
## HX`9;HAP6*
dynamic vDyM[0e-05,873.775]
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1828))

	def test_1829(self):
		input = '''
## l"MNL+;O"B7HI&f*O
bool b2t <- 65.298e54
func ryDH ()
	return 4.924E+03

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1829))

	def test_1830(self):
		input = '''
## y&Bjtc3jR/J;@4"p>W}
func Xq (var sNZz, dynamic i6g[4], var Cv[14.551,238e-79,664.655e+22])
	begin
	end
var WO0[574,0,9.207e-19]
bool wMCc
## /*]^XSS
'''
		expect = '''Error on line 3 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1830))

	def test_1831(self):
		input = '''
## htWAW{GK@^<CUc!RU2w4
number NL ## 83e.%Nmm1umFN6
## i1/q?Zfm"@-be,Ny[.z
func yULD (number A9z, string pbDm, var lDJo[24E41])
	return
## r])Wt
'''
		expect = '''Error on line 5 col 36: var'''
		self.assertTrue(TestParser.test(input, expect, 1831))

	def test_1832(self):
		input = '''
## @FfB
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1832))

	def test_1833(self):
		input = '''
func i9 (number VT[13.938e+90,40.032e+57])
	begin
	end

func oQ ()
	return
func X9LD (dynamic Hc3x[9])	return

dynamic OCjz <- "'""
## &2B4}.2WF9ax[GLGM;
'''
		expect = '''Error on line 8 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1833))

	def test_1834(self):
		input = '''
number L6bF <- "'"'"" ## l20
func cE (number Ipw, bool Ss[76.403,828.451])
	return "'""

var Ovh ## 9n2-Cwk^BL2
## "5FGI}9R/do~!}[>d=D
func FBh (bool d8NB, dynamic NdM[3e-40,76.081E-67,8.596e-72], number BvPb[825.872])
	return " "

'''
		expect = '''Error on line 6 col 22: 
'''
		self.assertTrue(TestParser.test(input, expect, 1834))

	def test_1835(self):
		input = '''
func vO (var yCm[36.581,0.218], var BIak[88])
	return " ['"U"
## h
var JC[67.223,7.031e+18,975e+60] <- gt ## ~TfjMekj avn6eWTW9
## qQz,
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1835))

	def test_1836(self):
		input = '''
## CHEy6e}{((fy
## (xjI::sdal4
var TKa[9.405,5.793,7.391E-06] <- hZdZ ## Q&u[tH2=ZK
'''
		expect = '''Error on line 4 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1836))

	def test_1837(self):
		input = '''
func CAX (string Qgp, var vNsX)	return "'"'"B"

dynamic Mams <- 7.264E-18
## <Bs<
var mF ## J]smwD#H;XoRg01gD
func bXT (string lh2A)	return
'''
		expect = '''Error on line 2 col 22: var'''
		self.assertTrue(TestParser.test(input, expect, 1837))

	def test_1838(self):
		input = '''
## ML/>-6L@w"kCP%`4
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1838))

	def test_1839(self):
		input = '''
func qd (dynamic oN, dynamic h2[64,65.218e72])
	begin
	end
func ZO (dynamic cR)
	return 6E-97

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1839))

	def test_1840(self):
		input = '''
func Z8 (dynamic BD[8E+76,0,6E+41])	return

'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1840))

	def test_1841(self):
		input = '''
string rR <- 284
## 0Wd#g2#Udng4R
bool od <- 7.848 ## oHVRBAI<m_
string HJ[364E+43]
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1841))

	def test_1842(self):
		input = '''
func M_ ()
	begin
		## o;!,!r5*23n>jZb<RwH)
		## I{e@!/D`4W]Gm:HFF.;
	end

func RP (var hL[7.158E+31,56.979], string Sr7Z, dynamic ZW)	return

'''
		expect = '''Error on line 8 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1842))

	def test_1843(self):
		input = '''
bool lXc ## 4[ L<5XH-Z{P;;,*;<
func pK9 (number YP[121,71,61.532E31])	return

## f<
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1843))

	def test_1844(self):
		input = '''
## TD
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1844))

	def test_1845(self):
		input = '''
func t9 (number VYH[4.687e+95], bool RtnY[6,71e57,377.275])
	return 142E-65
bool au1F[4,5.009E95]
func nYy5 (var Wt[2], string IwG[627e81], var JNTS)	return false
## gv"JLwHEvud@P<.VZbcP
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1845))

	def test_1846(self):
		input = '''
string oF23 ## /blO8uaH
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1846))

	def test_1847(self):
		input = '''
dynamic Tg[687.278E+56,195.821e+49]
## eE~WZ
## mW &EJYG
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1847))

	def test_1848(self):
		input = '''
## a:By(DPtTcBKj,*=
## Yca
## Ye=ytEZ`XLi-{JG
bool buD <- kA2
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1848))

	def test_1849(self):
		input = '''
## H(fT`/eTCFYJv"{Z
func j18q ()
	return "'"'"'"'"<"

dynamic bsvO <- 405.568e09
func AUqu (dynamic vv0[6.822e-05,13,87])
	return gg
func wz (var rQ[39.060e-87,81.299], string K8lK[0E+05], number aBEm[7E+64,48e26,767e72])
	return true

'''
		expect = '''Error on line 7 col 11: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1849))

	def test_1850(self):
		input = '''
## pzy
func Ba ()	return "'"'""

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1850))

	def test_1851(self):
		input = '''
## Ghi; `U;jw
func Tsh (bool IqTh[992e67,4,2], bool lfe)
	begin
	end

var nyw[9,27.187E01,62]
func CF_K (var Qr4)	begin
		## ,.xdP%c5z5=jo>}N>d#6
		## m<YF^
		var clq0[258.013e-63] ## e1b
	end

func Vpw_ (dynamic d9r, string ryQ)	return "'""
'''
		expect = '''Error on line 7 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1851))

	def test_1852(self):
		input = '''
## Xo
## a8AWwOx9lTIP2Iy,@-
## #uT_[L=![+|zJ
'''
		expect = '''Error on line 5 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1852))

	def test_1853(self):
		input = '''
var XDg_ <- "H"
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1853))

	def test_1854(self):
		input = '''
## iOp1Oz
var flr ## `n!$/l]QhJ
func CzK8 (dynamic ii1[91e32], dynamic X0[882])
	begin
		## %uLB)0UKF .D3I)Zn]u
		## zz@/
		## w
	end
func tv6h ()
	return

'''
		expect = '''Error on line 3 col 21: 
'''
		self.assertTrue(TestParser.test(input, expect, 1854))

	def test_1855(self):
		input = '''
func xEpr (string AvI[6.136E+00,2e54,7.275E22], string nb, dynamic J3Ph)
	return 248E-80

## dy}8m}
func YOl (dynamic id[574.140,4,55], var i6R)
	begin
		Xqf <- oLO
	end

'''
		expect = '''Error on line 2 col 59: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1855))

	def test_1856(self):
		input = '''
func IOt (var KVB[62e20,895.413], dynamic uK)	begin
	end

## X_pW
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1856))

	def test_1857(self):
		input = '''
## ipCAulM8@RwwTFgA.V
var S6u[606.290E22,8.320E-27] <- ".Y" ## d+
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1857))

	def test_1858(self):
		input = '''
## 7pxJ`&$HS
func SB ()
	return wv
string FI[2.104,68.217E+90] <- pk
## >IqfR4%PDiaHd->tPc
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1858))

	def test_1859(self):
		input = '''
## <-|g%|
## X#+Zmo
func yI (string ta, var CGH, number BwH)	begin
		begin
			## .Q3o{/yB%YgC2{m;Oo?z
			## ,q33lb"t39e
		end
		var Wv5y <- "'"8T'"Q"
		break
	end

'''
		expect = '''Error on line 4 col 20: var'''
		self.assertTrue(TestParser.test(input, expect, 1859))

	def test_1860(self):
		input = '''
bool aMM <- "j'"Vj" ## ]KCxIca}>Wk
dynamic p9bJ <- false
string P86j[67,55e16] <- 1
dynamic EfJi[84.252E-16,296,107E-91] <- hu
## D1r^SWZsW5ib
'''
		expect = '''Error on line 5 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1860))

	def test_1861(self):
		input = '''
func IE ()
	begin
		break
		## )IKl|kquH3gk,QF
	end

## KZx?$W4SxQmPViT
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1861))

	def test_1862(self):
		input = '''
bool RP[51.647]
func IgC8 (var Ml[224.202E+94])	begin
		for q3Le until "'"7" by OCX
			if fH QjK_ <- false
			elif 958E-06 Dco("'"D", true)
			elif 163.740 begin
				for NaC until N0 by yW
					if true cZ["Prt"] <- false
					else for Lmii until 8.658E-68 by "'"c'"C"
						for fQ until ATbX by ";'"4'""
							for wjBs until dKr by false
								x7as(",")
				break
				cU0(true)[oEN, 2.689E+84] <- 32e-57
			end
			elif false if true return "p"
			elif 4.093 break
			else return "e"
			elif "'"" continue
			elif "9'"" if 762.033E30 Fts("X`'"}k", 466.394)
	end
'''
		expect = '''Error on line 3 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1862))

	def test_1863(self):
		input = '''
## 5!j6d6xhv
string EfRw <- 25e-28 ## gf!a4U$8hK^KpZ
func dSI (var qEMk, dynamic cx, string xw[56E27])
	return
bool z6n ## @ "vN
'''
		expect = '''Error on line 4 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1863))

	def test_1864(self):
		input = '''
number n1 ## vPL$ @2-Jv*5e80b
dynamic Td9p[25.932e-30,93.135E-60,676E57] ## I;Q%kED6nWM=
## 4OM?d;vw~54D*lbu
## K{7`({
'''
		expect = '''Error on line 3 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1864))

	def test_1865(self):
		input = '''
bool snUL[394E-00,88] ## a"Nvtl=>v6)
var bM9[23.403e-05,562.981,0.835] ## cN28"Xp
func iCZJ ()	return
func LiAI ()
	return

## l6uxO2CcBCTc>[E>Hs/B
'''
		expect = '''Error on line 3 col 7: ['''
		self.assertTrue(TestParser.test(input, expect, 1865))

	def test_1866(self):
		input = '''
func tH (number tv[9e+06])
	return 0
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1866))

	def test_1867(self):
		input = '''
dynamic q7[992,826] <- false ## ^a*/:QG(kz$X
var JQ ## XOf_-uX3o>a~`n1]8pd]
## 1$]v^C
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1867))

	def test_1868(self):
		input = '''
## !jRbA5|M#|
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1868))

	def test_1869(self):
		input = '''
dynamic HF[30.533,944.965] <- sc
func O60G (number cOHu, dynamic tYK, dynamic xuz[5.707,32,1.280e41])
	begin
		continue
		## S@?@$Q[pFOGuT
	end
func dY (dynamic ru_g[964.373,49.433])	return v0W
dynamic CAF[689E-43,556.907,90.547e-22] <- false ## 2IeR:{v71
'''
		expect = '''Error on line 2 col 10: ['''
		self.assertTrue(TestParser.test(input, expect, 1869))

	def test_1870(self):
		input = '''
## )Ef
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1870))

	def test_1871(self):
		input = '''
bool xER[6.747]
func iQ (number c8l[93.450E+30,0.936,46E-37], string pf, dynamic xOX)	return

string GB
func QI (number ayW[232.072e98,5.265], string pUT, string l7R[728.117])	return

var x5MH[0e-30,8,2.243E-72] <- Xv ## #zoz2w3_kD"Qa/9HciHN
'''
		expect = '''Error on line 3 col 57: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1871))

	def test_1872(self):
		input = '''
var zx[53.511e+75,226,659E78]
dynamic Qt[436e-76] <- Uk
func Gc0 ()
	return false

'''
		expect = '''Error on line 2 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1872))

	def test_1873(self):
		input = '''
## DynsJ$[.Q{Lm
bool ljRU ## hXf24*^?
## zc4IdRSz|-DOCrbdnk!X
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1873))

	def test_1874(self):
		input = '''
func Yn ()	return
func e3fM (bool D1XS, dynamic gKTM[9E+46,9,548.547E33], dynamic exHI[2,7])
	begin
		## T#+Gj<&vE&&D
		## 2A_}P!Xk34ZSY#`
		begin
			if false break
			else continue
			if 234.770e-60 return
			elif 46.156E+66 begin
				## EU;fcMQCP"/4DzFp@5-
				if true var w1q <- 8.922E18 ## &,s-5i5XOH4rBH
				elif YEz begin
					break
					if "'"'"'"" aS <- NX
					elif 96.292E-97 continue
					elif false break
				end
				## e{xE8k/]%y.(,m
			end
			elif "'"34" oS("*8E", "'"")
			elif "'"" break
			elif "Y'"k'"" if "'"" av4 <- 92E20
			elif "'"'"'"'"D" return
			elif "j'"'"-'"" begin
				break
				continue
				## tgkQ^Tbv_P:(bu
			end
			elif "11" number DP
			else if "'"B%'"" begin
				## uo1
				if "'"'"'"'"*" Y4 <- "}'"h^"
				elif 76e+27 number pfF[760.552E55,51e+79] ## 2C#OTQMFf/zCo
				elif "'"`" return MJ5W
				begin
				end
			end
			elif 8 yZf(64E07, PwWc, true)
			## ?!y/*[tI`>`F9pdN94
		end
	end
func beFX ()
	return false

func nY (string TSS, dynamic rOBb, dynamic EW[167.918,1E49,27])
	begin
		return
		if false QRl[862e+41, 917e+87, false] <- 3e-52
		elif SSE9 begin
			## PyEE+XX2sx-Jf7
			## [FY:p};-03 *4)F]V"
		end
		elif "'"3'"" begin
			jd(true, 347E+03)
		end
		elif "$'"" if 721 if sU for x5 until eciZ by zr
			continue
		elif 944.117 break
		elif false bool uN
		elif YlTc break
		elif "$'"'"'"" return false
		elif WoP WS(true, "'"'"", 19.543)
		elif true break
		else for urz1 until "'"='"OV" by "3'""
			string vACQ[51.002e11] <- false ## A;EsT"vx@7NQx+_nJ
		elif 47.290e33 for c1Pn until 585.907E+68 by true
			return
		## } $IWO;a;/kAUS!})#Qp
	end
## _I}.mz
'''
		expect = '''Error on line 3 col 22: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1874))

	def test_1875(self):
		input = '''
## cbw6);d6h.UBC7 b~T
func kNny ()
	begin
		begin
			## EM}B<M2H
			## !!j~F
		end
	end
string VKy[189E+28] <- "e)'"'"""
number hu
'''
		expect = ''''''
		self.assertTrue(TestParser.test(input, expect, 1875))

	def test_1876(self):
		input = '''
func aw (var IQ7, bool Tj, number ff[46.223,1.611,21])	return true
## 7#}4<!B6@jlP ;km&
## wOjw
dynamic g3PI <- Hddm
'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1876))

	def test_1877(self):
		input = '''
dynamic jjvN
func Knu (dynamic qt, bool NUv)	return "'"v'"'""

'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1877))

	def test_1878(self):
		input = '''
func yCFp (number cBj1, bool kS6[614,1.645], var d_r)	return
'''
		expect = '''Error on line 2 col 45: var'''
		self.assertTrue(TestParser.test(input, expect, 1878))

	def test_1879(self):
		input = '''
func IE ()	return

'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1879))

	def test_1880(self):
		input = '''
func W99 (number IBs[1.213e90,521,8E54], dynamic i2DR[7.383,3.586E+40,3], dynamic ePH)	return 18E+17
'''
		expect = '''Error on line 2 col 41: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1880))

	def test_1881(self):
		input = '''
bool rD[69]
var qE[43E61] <- jU ## .%$}:C=0AY,k
'''
		expect = '''Error on line 3 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1881))

	def test_1882(self):
		input = '''
## i+(JF<&-KDU=**uA"
string gGm[2.067E-40,237e+47,63]
## An^SMX6!e
string HpTJ
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1882))

	def test_1883(self):
		input = '''
## A+>OUCBPWSk5GNCCq&
## I~O<V|kpWnD!a
## aXT
func glf ()
	return N1w
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1883))

	def test_1884(self):
		input = '''
bool Yb[96.022,13e-80]
func qW (bool kwAn)
	return 534E-19

## hX>xF-xwm3O|;
## ;:ZI4eZWL!-8
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1884))

	def test_1885(self):
		input = '''
## BW/$ +r].b/pda%U8
bool Tf[68,6.989E+55] <- "I'"" ## T #
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1885))

	def test_1886(self):
		input = '''
## n;xEr[ZU2{
## xK7qSl@5~+ YVM
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1886))

	def test_1887(self):
		input = '''
func o4 (dynamic p4S7[116,23E-66], dynamic px[9e+11,12E+62], number e7gZ[64.508,7e21])
	return false
'''
		expect = '''Error on line 2 col 9: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1887))

	def test_1888(self):
		input = '''
dynamic CN
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1888))

	def test_1889(self):
		input = '''
## _S5N3+h9:1
func oI (number Vt[5E-31], number iR, number zdO3[160])
	return QBd
func JiXT (var PWD, var fL[780.601E39,422])
	return
dynamic Q2 ## JN{T
'''
		expect = '''Error on line 5 col 11: var'''
		self.assertTrue(TestParser.test(input, expect, 1889))

	def test_1890(self):
		input = '''
## t<tD`@;3R
## _CQVnuz(_>VyFf`W6NNJ
'''
		expect = '''Error on line 4 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1890))

	def test_1891(self):
		input = '''
func Dk (var LYB[59,5e45], bool ws5)	return 98

func jP (var xo, string U51S, dynamic wUc9)	begin
	end
## "kB+pL|!@zd/X
func cR (dynamic ci[71.820,63E28], bool wf)	return

'''
		expect = '''Error on line 2 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 1891))

	def test_1892(self):
		input = '''
dynamic gnnl <- UI
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1892))

	def test_1893(self):
		input = '''
func Ai6 (var usg[243.110,20.163E37], number Qxpa)	return
'''
		expect = '''Error on line 2 col 10: var'''
		self.assertTrue(TestParser.test(input, expect, 1893))

	def test_1894(self):
		input = '''
## y_qRf{j*IQ9;
var oT
'''
		expect = '''Error on line 3 col 6: 
'''
		self.assertTrue(TestParser.test(input, expect, 1894))

	def test_1895(self):
		input = '''
number y5J
'''
		expect = '''successful'''
		self.assertTrue(TestParser.test(input, expect, 1895))

	def test_1896(self):
		input = '''
number we[866,13E+13] ## _F$d7|d
dynamic jZ
dynamic hCh1[97e66]
var au[474E+82,3.715E+12,50.256] <- "O6'"f'"" ## .UC8DDfm9bp8O>pH4
'''
		expect = '''Error on line 4 col 12: ['''
		self.assertTrue(TestParser.test(input, expect, 1896))

	def test_1897(self):
		input = '''
## Pn6HkVc
## 0)J
string AbA ## Fb
var N5[646e+22] <- "'"~'"" ## k|;ZH?(y*j@V
## <GFp
'''
		expect = '''Error on line 5 col 6: ['''
		self.assertTrue(TestParser.test(input, expect, 1897))

	def test_1898(self):
		input = '''
bool Ri <- false ## MV,UqOXu[`!%hWjN
func l3K (dynamic qHy[87E+75,0,15.725E65])
	return
func l_ (dynamic Ek[6])	return QT7D
bool ph
'''
		expect = '''Error on line 3 col 10: dynamic'''
		self.assertTrue(TestParser.test(input, expect, 1898))

	def test_1899(self):
		input = '''
## E
'''
		expect = '''Error on line 3 col 0: <EOF>'''
		self.assertTrue(TestParser.test(input, expect, 1899))
