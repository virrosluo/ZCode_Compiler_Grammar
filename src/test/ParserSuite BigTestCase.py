import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
	def test_785(self):
		input = '''
func eAq (number Y1iY, string KGc[856,743.802,41.009])
	begin
		continue
		## OO}[s]3Wl.ffQ$Y{}
		for BP1 until "'"=g" by SG
			if (90.589)
			if ("`'"Nb#") if (udq2)
			if (91) HY <- qW
			elif (4)
			bool nX0 <- false ## ?
			elif ("|")
			begin
				## dviG("4=a_9&
				rM6(HMw)
			end
			elif (false)
			return "z"
			elif (false)
			if (bk)
			string o9x[635,57.197] <- KHK
			elif (true)
			XSuc <- cQLG
			elif (false)
			string KUT <- false
			elif (LLIk)
			for B0 until "'"i'"" by "='"JN"
				begin
				end
			elif ("'"'"Y_'"") for lp1F until mKA by "'"5R"
				break
			elif (true)
			if (false) continue
			elif ("!'"!") number Wf ## RUvY,rD1Om9
			elif (9) LR(547.583, zPm)
			elif ("'"'"`")
			begin
				begin
					begin
						break
					end
					continue
					## *nSGS
				end
				if (false)
				if (RQW)
				break
				elif (true)
				string dyw <- iDf0
				elif (false) for nWyT until "'"h" by G1C
					break
				elif (ti)
				continue
				elif (115)
				return 0.198e-69
				elif (ai)
				begin
					## WC!Jcda bl/np|GB
				end
				elif (bL) return true
				else c3L(false)["'"oe'"", true] <- 2e-20
				break
			end
			elif ("'"-'"")
			return true
			elif (bY0k)
			begin
				## 0V
				for DCt until false by true
					C_Fz(K9Kf, iu7w)
				## Ou({~0o$tz-l1t?C
			end
			elif (3)
			break
			elif (" '"") return
			elif (false)
			if (6) return "'"N'""
			elif (P1)
			continue
			elif ("K'"A")
			break
			elif (false) return
			elif (898E-05)
			begin
				## `+IQ~B6LwZJuI(9_T}SG
				## Z/
			end
			else continue
			elif (SHc) sb()[false, Egu] <- "'"'"'"D"
			else uXzl(93e22, true, "'"2Ne")[true, 4e+15] <- "'"TZB3"
	end

func Rt (var Jg[7.100,50], string MH3[546e05,8.763E+03], number AsoI[961e-77,6])	return true
## BU&~3t
'''
		expect = '''Error on line 93 col 9: var'''
		self.assertTrue(TestParser.test(input, expect, 785))
