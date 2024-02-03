import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test1(self):
        input = """number hello[3] <- [1,2,3,[3]]
        dynamic world <- [1,2,3]
        number list[5] <- [5,4,3,2,1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,101))

    def test2(self):
        input = """number l1[1,3,2] <- [[[[1,2,3,4],[66.5,23.3,12.4,23.e3]],[1e-1, 2e-2, 3e-3]],[0]]
        bool l2[2] <- [[true,false,true,false,true]]
        string l3[20] <- [\"12345\",\"\",\"Saysomething\\n\"]
        dynamic dym <- [1,2,3]
        var abc <- [1,2,3,4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,102))

    def test3(self):
        input = """string question <- \"This is the testcase'\"Say hello world'\"\"

        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,103))

    def test4(self):
        input = """string str <- \"hello world\"
        string String <- \" Is this legit\\'?\"

        var abc <- [1,2,3]
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,104))

    def test5(self):
        input = """func testfunctiondeclare(string a)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,105))

    def test6(self):
        input = """func unclosedfunc(number b, string c)
                begin 
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,106))

    def test7(self):
        input = """func test()
                begin
                    bbbllll(a,b,) 
                end
        """
        expect = "Error on line 3 col 32: )"
        self.assertTrue(TestParser.test(input,expect,107))

    def test8(self):
        input = """func main(number a[10,10], bool b[10,20])
                return 1e-3
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,108))

    def test9(self):
        input = """func main() begin
            string a <- "Hello World"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,109))

    def test10(self):
        input = """func main() begin
            number a <-10e-3
            number b <- 10e-4
            bool c[1,2,3] <- [[1,2,3],2,3,4]
        
        end end



        """
        expect = "Error on line 6 col 12: end"
        self.assertTrue(TestParser.test(input,expect,110))

    def test11(self):
        input = """func main() begin
            number a <- [1,2,3]
        end 

        func t1() return "Hello World"

        func t2() begin

        end

        func t3()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,111))

    def test12(self):
        input = """func main() begin
        begin
        end
        end 
        func test() return 5.
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,112))

    def test13(self):
        input = """func main() 
        begin
            foo(1,2,f1(2,3,f2(3,4)))
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,113))

    def test14(self):
        input = """func main() 
        begin
            bool b <- true and true or true and not false
            printLine(b)
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,114))

    def test15(self):
        input = """func main() begin

            bool b <- true and (false and true)


            bool c <- b <> true
            printLine(c)
        end 
        """
        expect = "Error on line 6 col 25: >"
        self.assertTrue(TestParser.test(input,expect,115))

    def test16(self):
        input = """dynamic global
        var a <- "Say something"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,116))

    def test17(self):
        input = """a <- 1000
        """
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input,expect,117))

    def test18(self):
        input = """func main(dynamic a)
        begin 
            func f1(a, b) return -1
            func f2(bool a) 
        end
        """
        expect = "Error on line 1 col 10: dynamic"
        self.assertTrue(TestParser.test(input,expect,118))

    def test19(self):
        input = """func main(var a)
        begin 
            func f1(number b) return -1
            func f2(number a) 
        end
        """
        expect = "Error on line 1 col 10: var"
        self.assertTrue(TestParser.test(input,expect,119))

    def test20(self):
        input = """func main()
        begin 
            number c,d <- 100
        end
        """
        expect = "Error on line 3 col 20: ,"
        self.assertTrue(TestParser.test(input,expect,120))

    def test21(self):
        input = """func main()
        begin 
            b <- -1000E-10
            d <- 1 * 2 % 10 / 56.4E-2 + e
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,121))

    def test22(self):
        input = """func main() begin 
            number a <- "string"
            main()
            main()


            a <- number
        end
        """
        expect = "Error on line 7 col 17: number"
        self.assertTrue(TestParser.test(input,expect,122))

    def test23(self):
        input = """func main() begin 

            t,s <- (60 - 40 + (array[100,101,102,103])[3+foo(2,3)],20)
        end
        """
        expect = "Error on line 3 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,123))

    def test24(self):
        input = """func main() begin 
            c <- a...b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,124))

    def test25(self):
        input = """func main() begin 
            IF <- 1
            FoR <- "This string is for loop"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,125))

    def test26(self):
        input = """func main() begin 
            for i until ("saysomething" === "a") by 10
                printLine("hello world")
        end
        """
        expect = "Error on line 2 col 42: ="
        self.assertTrue(TestParser.test(input,expect,126))

    def test27(self):
        input = """func main() begin 
            for numb until numb < 0 by -1
            begin
                a[foo(2,3) + 3] <- (a[foo(2,3) + 3] + num) % ((2))
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,127))

    def test28(self):
        input = """func main() 
        begin 
            for i until i != 1000 by 2
                if (i/a=b) printLine(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,128))

    def test29(self):
        input = """func main() 
        begin 
            for a until foo(2,3)[temp1(20)] > 1000 by 5.3E-3 
            

            begin
            begin
            break
            continue
            begin
            end
        end
        """
        expect = "Error on line 13 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,129))

    def test30(self):
        input = """func main() begin 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,130))

    def test31(self):
        input = """func error() begin 
            for for until (num1*num2=0) by 10
            begin
            end
        end
        """
        expect = "Error on line 2 col 16: for"
        self.assertTrue(TestParser.test(input,expect,131))

    def test32(self):
        input = """func main() for i until true by 1 return 0
        """
        expect = "Error on line 1 col 12: for"
        self.assertTrue(TestParser.test(input,expect,132))

    def test33(self):
        input = """func main() 
        begin
            for i until (temp1*temp2%(temp3-temp4)=temp5) by 1e-3 
            begin
                if (fee()) then<-5
                elif (fee()) eles<-10
                else i<-i/2
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,133))

    def test34(self):
        input = """func main() begin
            for i until 1 by 1 begin
                begin
                    begin
                        begin
                            if (i%2=0) i<-i+1
                            elif (true) begin end
                            elif (true) begin
                            end
                            else i<-i+1
                        end
                    end
                end
            end
        end
        """
        expect = "Error on line 7 col 46: end"
        self.assertTrue(TestParser.test(input,expect,134))

    def test35(self):
        input = """func main() begin
        end
        func test(number a, number b[12]) begin
            for i until i<10 by 1 print(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,135))

    def test36(self):
        input = """func main() begin
            for i until i<0 by funcfunc()
                i <- i-1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,136))

    def test37(self):
        input = """func lossComponent() begin
            for i by 1
            begin 
            end
        end
        """
        expect = "Error on line 2 col 18: by"
        self.assertTrue(TestParser.test(input,expect,137))

    def test38(self):
        input = """func main() 
        begin
            for i until hi by funcfunc()
            begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,138))

    def test39(self):
        input = """func main() begin
            for i=2 until i < noneed by 1
            begin
            end
        end
        """
        expect = "Error on line 2 col 17: ="
        self.assertTrue(TestParser.test(input,expect,139))

    def test40(self):
        input = """func main() 
        begin
            for i until i < foo(2,3) by 1
                break
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,140))

    def test41(self):
        input = """func main() begin
            if (i = -1) break
            elif (i = 1) continue
            else continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,141))

    def test42(self):
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,142))

    def test43(self):
        input = """func main() begin
                return t1 and t2
        end
        func t1(number a, number b) return 

        func t2(bool c) begin
            begin
                begin
                    return abc
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,143))

    def test44(self):
        input = """
        func temp(bool a[1,2,3], string b[1,2,3]) return nothing__
        func temp2() return temp(temp())
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,144))

    def test45(self):
        input = """func main() begin
            number i <- 100
            number thres <- 100
            for i until i < thres by 10
                printLine(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,145))

    def test46(self):
        input = """
        func main() return a/b = 2/1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,146))

    def test47(self):
        input = """
        func main() begin
            for i until i <= arr_length() by 1 begin
                print(output)
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,147))

    def test48(self):
        input = """
        func error() begin
            for str a until a < 100 by 1 push(a)
        end
        """
        expect = "Error on line 3 col 20: a"
        self.assertTrue(TestParser.test(input,expect,148))

    def test49(self):
        input = """
        func main() begin
            number s <- calS(r)
        end

        func calS(number r, number pi) return 2*pi*r*r
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,149))

    def test50(self):
        input = """func main() begin
            if (a()) return 0
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,150))

    def test51(self):
        input = """func t1() begin
            for i until int() by 2
            begin
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,151))

    def test52(self):
        input = """func nothing() begin
            if () return 0
        end
        """
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input,expect,152))

    def test53(self):
        input = """func main() begin
            if (x < 5) 
                if (y < 10) print("Say hello")
                    if (true)
                        if(true) a()
            else print("Say no hello")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,153))

    def test54(self):
        input = """func main() begin
            for i until i < 10 by 1
                for j until j < 10 by 1
                    print("*")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,154))

    def test55(self):
        input = """func main() begin
            begin
                main()       
            end
            begin
                main()
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,155))

    def test56(self):
        input = """func main() begin
            string s <- \"abc\\n\\t'\"\"
            string ss <- \"123.\\t\\b\"
            s <- s...ss
            s <- s...ss
            return s
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,156))

    def test57(self):
        input = """func main() 
        begin
            begin
                return 2
            end
            begin
                return 1
            end
        end

        func factorial(number n) begin
            if (n = 0) return 1
            else return n * factorial(n-1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,157))

    def test58(self):
        input = """
        func main() 
        begin
            for i until i < 0 by 1
                if (num() > 1) inc(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,158))

    def test59(self):
        input = """ number a <- 1
        func inc(number a) return a+1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,159))

    def test60(self):
        input = """ func main() return

        func function() begin
            foo(a,b,temp()[2,foo(function(2,3))])
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,160))

    def test61(self):
        input = """ func main() return function
        func function() begin
            for a until (n1 + n2)*2 = 10 by 2
            begin
                foo(1) <- a[foo(1)] + n1 * n2
                begin
                    if (true) printline("a")
                    else printline("b")
                end
            end
        end
        """
        expect = "Error on line 5 col 23: <-"
        self.assertTrue(TestParser.test(input,expect,161))
    
    def test62(self):
        input = """func main()
        begin
            for i until i < 0 by i + 1



                begin
                    print("Hello World")
                    print("Say something")
                end


                
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,162))

    def test63(self):
        input = """func main()
        begin
            begin
                for i until i >= size(arr) by 1
                    print(ext(arr[i],arr[i]))
            end
        end

        func extract(string a, number b)
            return a[b]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,163))

    def test64(self):
        input = """func main() 
        
        
        begin                
            funccall(i, test)                
        end

        func funccall(number i, number test) 
        
        begin

            if (i = test) return true
                elif (i > test) return false 
                    elif ((i<test) and (test%i=0)) return true
                        else return false

        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,164))

    def test65(self):
        input = """func main() return
        a+b
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.test(input,expect,165))

    def test66(self):
        input = """func main() return f1(n1) and f2(n2) or f3(n3)
        func f1(number a)
        func f1(number a) begin
            return a
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,166))

    def test67(self):
        input = """func f1() return f1(f1(f1(f1(n1))))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,167))

    def test68(self):
        input = """func main() 


        begin
            number c
            c<-au*bc+100/1000

            return c[3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,168))

    def test69(self):
        input = """func main() begin
            number begin <- 1
            begin
            end
            begin
            end
        end
        """
        expect = "Error on line 2 col 19: begin"
        self.assertTrue(TestParser.test(input,expect,169))

    def test70(self):
        input = """


        func main() begin
            number numbers[5] <- [num[1],[2],[3]]
            print(\"We have array number: \",result)
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,170))

    def test71(self):
        input = """func testExpr() begin
            if ((a <= a) and (b!= b) or (d > d )) x <- 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,171))

    def test72(self):
        input = """func m1() begin
        begin
            saysomething()
            end
            begin
            helloworld()
        end
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,172))

    def test73(self):
        input = """func main() begin
            a <- -1-b-s-2-3-s*2*3*4/1/2/3
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,173))

    def test74(self):
        input = """func my_func() 
        
        begin
            foo(my_func, a/b, not my_func())
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,174))

    def test75(self):
        input = """func my_func() 
        
        
        begin

            x <- a[b[2],c[2]]
            a[[b[1 + c]]] <- x
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,175))

    def test76(self):
        input = """func main() begin
            var x <- readInteger()
            for x until x < 0 by -1 begin
                printInteger(res)
            end
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,176))

    def test77(self):
        input = """func my_func() begin
            x <- ((("Say"..." ")..."Something!")..."\\\\!!!\\\\")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,177))

    def test78(self):
        input = """func funct(number _, number __) begin
            s <- __()
        end

        func main() begin
            a <- _funct + __funct
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,178))

    def test79(self):
        input = """func main() begin
            aba1232 ->func()
        end

        """
        expect = "Error on line 2 col 20: -"
        self.assertTrue(TestParser.test(input,expect,179))

    def test80(self):
        input = """
        func main() begin
            ## this function to let program start
            ## This will help program run
            number a <- 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,180))

    def test81(self):
        input = """number a<-main(50)
        a <- main(a) + main(a*2+main(a))
        func main(number a) begin
            return a*2+1
        end
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.test(input,expect,181))

    def test82(self):
        input = """number a<-func(50)
        func(a)
        """
        expect = "Error on line 1 col 10: func"
        self.assertTrue(TestParser.test(input,expect,182))

    def test83(self):
        input = """func main(number a) begin
            begin
                return foo[5,foo(123)]
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,183))

    def test84(self):
        input = """func main() begin
        printLine("----")
        printLine(func())
        end
        """
        expect = "Error on line 3 col 18: func"
        self.assertTrue(TestParser.test(input,expect,184))

    def test85(self):
        input = """func main() begin
            number,bool a <- true
        end
        """
        expect = "Error on line 2 col 18: ,"
        self.assertTrue(TestParser.test(input,expect,185))

    def test86(self):
        input = """declaration <- foo(123) 

        """
        expect = "Error on line 1 col 0: declaration"
        self.assertTrue(TestParser.test(input,expect,186))

    def test87(self):
        input = """func main() begin
            for i until i >= 2 by 1 
            begin
                for j until j >= 3 by 1 
                begin
                    begin
                        return 0
                    end
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,187))

    def test88(self):
        input = """func main() begin
            var a <- [1,2,3]
            for a until len_a >= 10 by 0 begin
                arr[0] <- x
            end
            arr[a[1]] <- x
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,188))

    def test89(self):
        input = """func main() 
        begin
            number x <- main()
            begin
                x <- main()
                begin
                    x <- main()
                end
                x <- main()
            end
            x <- main()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,189))

    def test90(self):
        input = """
func isPrime(number x)

func main()
begin
	number x <- readNumber()
	if (isPrime(x)) printString("Yes")
	else printString("No")
end

func isPrime(number x) begin
	if (x <= 1) return false
	var i <- 2
	for i until i > x / 2 by 1
	begin
		if (x % i = 0) return false
	end
	return true
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,190))

    def test91(self):
        input = """
func areDivisors(number num1, number num2)
	return ((num1 % num2 = 0) or (num2 % num1 = 0))

func main() begin
	var num1 <- readNumber()
	var num2 <- readNumber()
	if (areDivisors(num1, num2)) printString("Yes")
	else printString("No")
end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,191))

    def test92(self):
        input = """func main() 
        begin
            number a_1 <- funcfunc()
            for a_1 until exp = 1000 and not exp2 by a + arr[0] begin
                return 
            end
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test93(self):
        input = """
        func main() begin
            number a <- foo(b1(1, 3), b2(5))
            bool b <- ((a or false) and true) or (not a)
            number c[4, 3] 
            c <- temp(a, b, (a - 2 * a - 3), foo((a * b), a + b))
            var d <- c[1,2] + c[2,3] - c[3,4]
            return d
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,193))

    def test94(self):
        input = """func foo(number a[5.12, 3.22e-14], string b)
begin
	var i <- 0
	for i until i >= 5 by 1
	begin
		a[i] <- i * i + 5
	end
	return -1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,194))

    def test95(self):
        input = """func main() 
        begin
            if (true) begin
                if (true) begin
                    x <- true
                end 
                else begin
                    x <- false
                end
            end 
            else begin
                x <- -false
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,195))

    def test96(self):
        input = """func foo(number a[5.12, 3.22e-14], bool b)
begin
	var i <- 0
	for i until i >= 5 by 1
	begin
		a[i] <- i * i + 5
	end
	return -1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,196))

    def test97(self):
        input = """func main() begin
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        string a[1,2,3] <- ["Hello", "World"]
        number b[1] <- a[1][2][3]
        bool c[1] <- [[true, false], [false, true], true]
    end


    """
        expect = "Error on line 4 col 27: ["
        self.assertTrue(TestParser.test(input,expect,197))

    def test98(self):
        input = """func main()
begin
	if (true) begin
		printLine()
		if (foo() = 2) printLine("True")
		else
		begin


			if (fee() = 1) printLine(1)
			elif (fee() = 2) printLine(2)
			elif (fee() = 3) begin
				if (foo() = 1)
				begin 
				end

				else 
				begin


					printLine(4)
				end
			end
		end
	end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,198))

    def test99(self):
        input = """func main() 
        begin
            x <- 10
            i <- 0
            for i until i > x by x-2
                if (true) break
                elif (x <= 1) continue
                elif (a[10,2+3] < a(1,true)[1,2-2,3*4]) printLine("elif 2nd")
                else i <- printLine("Hi")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,199))

    def test100(self):
        input = """func main() begin
            begin
                begin
                    for i until i < 0 by true
                    begin
                    end
                end
                begin
                    for i until i > 0 by false
                    begin
                    end
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

