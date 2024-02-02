import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_parser_2000(self):
        self.assertTrue(TestParser.test('''func weloveppl(number a,\n\n\nnumber b\n\n\n)\n''','''Error on line 1 col 24: \n''',2000))

    def test_parser_2001(self):
        self.assertTrue(TestParser.test(''' func main() return\nfunc function() begin\n    for a[5][foo(7)] until (num1 + num2)*2 = 10 by 2\n    begin\n        a[0][a[5][foo(7)]] <- a[0][a[5][foo(7)]] + num2 * num1\n        num2 <- num2 + num1\n    end\nend\n''','''Error on line 3 col 9: [''',2001))

    def test_parser_2002(self):
        self.assertTrue(TestParser.test('''func A(int a,\nint b,\nintc,\n)\nreturn 1\n''','''Error on line 1 col 7: int''',2002))

    def test_parser_2003(self):
        self.assertTrue(TestParser.test('''func a() begin\na[5]<- [[1 ,2,3, 4 ],2] \nend\n''','''successful''',2003))

    def test_parser_2004(self):
        self.assertTrue(TestParser.test('''\nfunc zvz ()\n\treturn "\'"\'"\'""\nvar E2\nfunc Ow (number nj[65,484.398,0], number t2T[5,4.602], string DlM)\n\tbegin\n\t\t## Ok/MVZydJT1QZnKsLj^\n\t\t## )`+b?/tNH$\n\t\t## gydY46Y"P\n\tend\nfunc R1v6 (var A4a[5.355,0.199])\n\treturn 9.105\nfunc Ztn ()\n\treturn\n\n''','''Error on line 4 col 6: \n''',2004))

    def test_parser_2005(self):
        self.assertTrue(TestParser.test('''func foo() begin \na[3*3+9] <- 8 \nend''','''Error on line 3 col 3: <EOF>''',2005))

    def test_parser_2006(self):
        self.assertTrue(TestParser.test('''func a() begin\nfoo()[0] <- a + b * 2\nend''','''Error on line 3 col 3: <EOF>''',2006))

    def test_parser_2007(self):
        self.assertTrue(TestParser.test('''func a() begin\narr[2] <- []\nend''','''Error on line 2 col 11: ]''',2007))

    def test_parser_2008(self):
        self.assertTrue(TestParser.test('''func a() begin \narr[2,3] <- ["hello",[2,3 ]]\nend''','''Error on line 3 col 3: <EOF>''',2008))

    def test_parser_2009(self):
        self.assertTrue(TestParser.test('''func a() begin \na[3 + foo(2)] <- a[b[2,3]]+ 4 \nend''','''Error on line 3 col 3: <EOF>''',2009))

    def test_parser_2010(self):
        self.assertTrue(TestParser.test('''## With newline at the end of funcdecl\nfunc a() begin\nnumber a[5] <- [1, 2, 3, 4, 5]\nnumber b[2, 3] <- [[1, 2, 3], [4, 5, 6]]\nend\n''','''successful''',2010))

    def test_parser_2011(self):
        self.assertTrue(TestParser.test('''## Without newline\nfunc a() begin\nnumber a[5] <- [1, 2, 3, 4, 5]\nnumber b[2, 3] <- [[1, 2, 3], [4, 5, 6]]\nend\nend''','''Error on line 6 col 0: end''',2011))

    def test_parser_2012(self):
        self.assertTrue(TestParser.test('''func foo(number a[5], string b)\n             begin\nvar i <- 0\nfor i until i >= 5 by 1 begin\na[i] <- i * i + 5 end\nreturn -1 end''','''Error on line 5 col 18: end''',2012))

    def test_parser_2013(self):
        self.assertTrue(TestParser.test('''func foo(number a[5], string b)\nbegin\nvar i <- 0\nfor i until i >= 5 by 1 begin\n\n\n\n\n\nbegin\na[i] <- i * i + 5 \nend\nend\nreturn -1 \nend\n''','''successful''',2013))

    def test_parser_2014(self):
        self.assertTrue(TestParser.test('''## Should be syntax error (no nested function declarations)\nfunc foo(bool b)\nbegin\nfunc goo() \n\n\n\n\n\nbegin\nend\nend\n''','''Error on line 4 col 0: func''',2014))

    def test_parser_2015(self):
        self.assertTrue(TestParser.test('''\nfunc a(bool _a) \nbegin\nabc<- 5\na[5,2]<-3.14e5\n\nbegin\nc[2,2]<-12 *7+5/ foo(0 )+a[7   ,2]\nend\n\n\n\n\n\n\n\n\n\n\n\nend''','''Error on line 21 col 3: <EOF>''',2015))

    def test_parser_2016(self):
        self.assertTrue(TestParser.test('''func _(bool _)\n\n\n\n\n\n\n\n\n\n\nbegin\nif 12*5 begin\nabc<-foo(goo(12*5), 7+2)+arr[2,2]\nend\nelif "..."..."..."+"..."=="..." return arr[2]\n\n\n\n\n\n\n\nelse begin\nfoo(17, arr[23], goo(5), ".."..."..", not - arr[2] % 7)\nend\n\nend\n''','''successful''',2016))

    def test_parser_2017(self):
        self.assertTrue(TestParser.test('''func _(bool _)\n\n\n\n\n\n\n\n\n\n\nbegin\n\n\nif 12*5 begin\nabc<-foo(goo(12*5), 7+2)+arr[2,2]\nend\nelif "..."..."..."+"..."=="..." return arr[2]\n\n\n\n\n\n\n\nelse begin\nfoo(17, arr[23], goo(5), ".."..."..", not - arr[2] % 7)\n## if (abc) abc<-foo[12]*12 + 7\nend\n\nend''','''Error on line 31 col 3: <EOF>''',2017))

    def test_parser_2018(self):
        self.assertTrue(TestParser.test('''func _()\n\n\n\nfor a until 23+37 by foo(27)%arr[3] begin\n\nbegin\nend\n\n\n\n\nbegin\na<-a+1\n\n\na<-b+1+2+3+4*5%arr[7]\nend\nbegin\nvar i <- 0\nfor i until i >= 10 by 1\n        writeNumbe(i)\n        break\n        continue\n        return\n        return -1\n        return a\n        return foo(foofooofoo(), foo(foo()))\nend\nbegin\nreturn\nend\nend''','''Error on line 5 col 0: for''',2018))

    def test_parser_2019(self):
        self.assertTrue(TestParser.test('''func _() begin\nvar x <- 1++1\nend''','''Error on line 2 col 11: +''',2019))

    def test_parser_2020(self):
        self.assertTrue(TestParser.test('''for number i <- 0 until i = 10 by 1''','''Error on line 1 col 0: for''',2020))

    def test_parser_2021(self):
        self.assertTrue(TestParser.test('''func areDivisors(number num1, number num2)\n    return ((num1 % num2 = 0) or (num2 % num1 = 0))\n\nfunc main()\n    begin\n        var num1 <- readNumber() \n        var num2 <- readNumber()\n\n        if (areDivisors(num1, num2)) writeString("Yes")\n        else writeString("No")\n    end\n\nfunc isPrime(number x)\n    begin\n        if (x <= 1) return false \n        var i <- 2\n        for i until i > x / 2 by 1 \n        begin\n            if (x % i = 0) return false\n        end\n        return true\n    end\n''','''successful''',2021))

    def test_parser_2022(self):
        self.assertTrue(TestParser.test('''func isPrime(number x) ## Error on line 8 col 3: <EOF>\n\nfunc main()\n    begin\n        number x <- readNumber()\n        if (isPrime(x)) writeString("Yes") \n        else writeString("No")\nend\n''','''successful''',2022))

    def test_parser_2023(self):
        self.assertTrue(TestParser.test('''func test(number z <- 1)''','''Error on line 1 col 19: <-''',2023))

    def test_parser_2024(self):
        input = """func main() begin
            __a_1_2 ->
            12
        end
        
        """
        expect = "Error on line 2 col 20: -"
        self.assertTrue(TestParser.test(input,expect, 2024))