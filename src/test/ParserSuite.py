import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def testdeclare1(self):
        input = """number abc[5] <- [[1,2,3,4,5]]
        dynamic a
        number list[5] <- [5,4,3,2,1]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def testdeclare2(self):
        input = """number list[5,6] <- [[[[5,4,3,2,1],[66.78,77.e-4,89.1,50.00]],[5.e-4,65.9E+3,20.6E-3]],[1E-78]]
        bool test[5] <- [[[true,false,true,false,true]]]
        string abc[20] <- [\"abcdefg\",\"\",\"123@\\n\"]
        number a[5] <- [[[[1]]]]
        dynamic dym
        var abc <- "a string with numbers like \'\"1.123e-3\'\", \'\"0.23E-50\'\"?\"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def testdeclare3(self):
        input = """string question <- \"What do you think about the idea of '\"going to work on Sunday?'\"\"


        string reply <- \"As long as I\\'m paid, anything is fine!\"

        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def testdeclare4(self):
        input = """string str <- \"hello world\"
        string String <- \" Is this legit\\'?\"

        var abc <- [1,2,3]
        
        """
        expect = "Error on line 4 col 19: ["
        self.assertTrue(TestParser.test(input,expect,204))

    def testdeclare5(self):
        input = """func testing1(string a)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def testdeclare6(self):
        input = """func abc(number a[5], string b)
                begin 
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,206))

    def testdeclare7(self):
        input = """func main()
                begin
                    func numb(number a, number b)
                    func str(string a, string b[10,20])
                    func boolean(bool a, bool b,) 
                end
        """
        expect = "Error on line 5 col 48: )"
        self.assertTrue(TestParser.test(input,expect,207))

    def testdeclare8(self):
        input = """func main(number a[10], bool b[10])
                return 123+-15.45e-30
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

    def testdeclare9(self):
        input = """func main() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def testdeclare10(self):
        input = """func main() begin
            number a<-10
            string b[1] <- [\"hello\"]
            bool c[1,2,3] <- [[[true,false],[true,false]],[[true,false],[true,false]],[[true,false],[true,false]]]
        
        end end



        """
        expect = "Error on line 6 col 12: end"
        self.assertTrue(TestParser.test(input,expect,210))

    def testdeclare11(self):
        input = """func main() begin

            func test1() return

            func test2() begin

            end

            func test3()
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def testdeclare12(self):
        input = """func main() begin
        end 
        func test1() begin
        end
        func test2() return 123.
        func test3() 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))

    def testdeclare13(self):
        input = """func main() begin
            foo(1,2,foo1(2,3,foo3(3,4)))
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def testdeclare14(self):
        input = """func main() begin
            number a <- f(123,456) + f(true,false)[50][60+70%122]
            bool b <- true and false or false and not true
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

    def testdeclare15(self):
        input = """func main() begin

            bool b <- true and false != 1


            bool c <- b <> true

        end 
        """
        expect = "Error on line 6 col 25: >"
        self.assertTrue(TestParser.test(input,expect,215))

    def testdeclare16(self):
        input = """dynamic global
        var a <- \"const\"
        func main() begin


        



        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def testdeclare17(self):
        input = """x <- 1000
        """
        expect = "Error on line 1 col 0: x"
        self.assertTrue(TestParser.test(input,expect,217))

    def testdeclare18(self):
        input = """func main(var a)
        begin 
            func main(number b) return -1
            func main(bool a) 
        end
        """
        expect = "Error on line 1 col 10: var"
        self.assertTrue(TestParser.test(input,expect,218))

    def testdeclare19(self):
        input = """func main(dynamic a)
        begin 
            number test <- 1e-10 
        end
        """
        expect = "Error on line 1 col 10: dynamic"
        self.assertTrue(TestParser.test(input,expect,219))

    def testdeclare20(self):
        input = """func main()
        begin 
            number a,b <- 100
        end
        """
        expect = "Error on line 3 col 20: ,"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_assign1(self):
        input = """func main()
        begin 
            a <- 100
            b <- -1000E-10
            c <- true and false
            d <- a * b % 10 / 56.4E-2
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_assign2(self):
        input = """func main() begin 
            a <- \"\"


            a[4+foo(23)/1.34E-3] <- \"hello\"

            a <- number
        end
        """
        expect = "Error on line 7 col 17: number"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_assign3(self):
        input = """func main() begin 
            a <- 50
            b,c <- (60 - 40 + array[100][3+foo(2,3)],20)
        end
        """
        expect = "Error on line 3 col 13: ,"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_assign4(self):
        input = """func main() begin 
            string a <- \" One two three\"
            string b <- \"  \\'go\\'! \"
            c <- a...b
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_assign5(self):
        input = """func main() begin 
            IF <- 1000
            FoR <- \"string\"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_for1(self):
        input = """func main() begin 
            for i until i%x=0 by 10
                i <- i+5
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_for2(self):
        input = """func main() begin 
            for numb until numb < 0 by -1e-3
            begin
                value <- value * 10
                a[5][foo(2,3)] <- (a[5][foo(2,3)] + numb) % (1e9+5)
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_for3(self):
        input = """func main() begin 
            for int until int != 1000 by 2
                if (int/a=b) callsupport(int)
        end
        func callsupport(number i)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_for4(self):
        input = """func main() begin 
            for (a+foo(2,3))[4+temp(5,10)][temp1(20)] until (a+foo(2,3))[4+temp(5,10)][temp1(20)] > 1000 by 5.3E-3 begin
                i <- i * 10
                if (i % 20 = 0) break
                    else calltemp()
            end
        end
        """
        expect = "Error on line 2 col 16: ("
        self.assertTrue(TestParser.test(input,expect,229))

    def test_for5(self):
        input = """func main() begin 
            for i until i+x=100 by 10
                x <- x+1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))

    def test_for6(self):
        input = """func main() begin 
            for for until (num1*num2=0) by 10
            begin
                num1 <- 10
                num2 <- num2 - num1
            end
        end
        """
        expect = "Error on line 2 col 16: for"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_for7(self):
        input = """func main() for i until temp1+temp2*(temp3-temp4)=temp5 by 1 return 0
        """
        expect = "Error on line 1 col 12: for"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_for8(self):
        input = """func main() begin
                for i until temp1*temp2%(temp3-temp4)=temp5 by 1e-3 begin
                if (i%x=1) then<-5
                elif (i%x=2) eles<-10
                else i<-i/2
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_for9(self):
        input = """func main() begin
            for i until i/2=0 by 20 begin
                begin
                    begin
                        begin
                            if (i%2=0) i<-i+1
                        end
                    end
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_for10(self):
        input = """func main() begin
            func test(number a, number b[12]) begin
                for i until i<10 by 1 print(i)
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

    def test_for11(self):
        input = """func main() begin
            for i until i<0
                i <- i-1
        end
        """
        expect = "Error on line 2 col 28: \n"
        self.assertTrue(TestParser.test(input,expect,236))

    def test_for12(self):
        input = """func main() begin
            for i by 1
                if (i < 1000) break
        end
        """
        expect = "Error on line 2 col 18: by"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_for13(self):
        input = """func main() begin
            for i until -i by 1 print(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_for14(self):
        input = """func main() begin
            for i=2 until i < foo(2,3) by 1
                i <- i + foo(2,3)[3,4]
        end
        """
        expect = "Error on line 2 col 17: ="
        self.assertTrue(TestParser.test(input,expect,239))

    def test_for15(self):
        input = """func main() begin
            for i until i < foo(2,3) by (num2+num3)%num4


                a[2,i] <- a[i,2]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_break_continue_return1(self):
        input = """func main() begin
            for i until -i by -num2
                if (i = -num2) break
                else continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_break_continue_return2(self):
        input = """func main() begin
            for i until i < 10 by i
                continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_break_continue_return3(self):
        input = """func main() begin
                return
        end
        func temp(number a1, number a2) return 
        func temp2(bool b1) begin
            begin
                begin
                    return 
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_break_continue_return4(self):
        input = """func main() begin
                return something 
        end
        func temp(number a1, number a2) return noth_
        func temp2() return -a[2+temp(2,3)][10]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_break_continue_return5(self):
        input = """func main() begin
            number i <- 10
            number thres <- 100
            for i until i < thres by 10
                if (i/temp1=temp2) return temp1+temp2-temp3
                elif (i/temp3=0) break
                else continue
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))

    def testgeneral1(self):
        input = """number a <- adding(10)

        number b <- a + adding(-10e-3)
        func main() return a/b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def testgeneral2(self):
        input = """number arr[5] <- [1,2,3,4]
        func main() begin
            for i until i <= size(arr) by 1 begin
                number output <- arr[i]
                print(output)
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def testgeneral3(self):
        input = """number a<-100
        func main() begin
            for int i until i < 100 by 1 push(i)
        end
        """
        expect = "Error on line 3 col 20: i"
        self.assertTrue(TestParser.test(input,expect,248))

    def testgeneral4(self):
        input = """number r <- 5
        number pi <- 3.1415
        func main() begin
            number s <- calcS(r,pi)
            if (s < 10) return \"small\"
            else return \"big\"
        end

        func calcS(number r, number pi) return 2*pi*r*r
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def testgeneral5(self):
        input = """func main() begin
            if (s())return 0
            else return 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))

    def testgeneral6(self):
        input = """func main() begin
            for i until by 1 
                break
        end
        """
        expect = "Error on line 2 col 24: by"
        self.assertTrue(TestParser.test(input,expect,251))

    def testgeneral7(self):
        input = """func main() begin
            if ()return 0
            else return 1
        end
        """
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.test(input,expect,252))

    def testgeneral8(self):
        input = """func main() begin
            if (x < 5) 
                if (y < 10) print("x is less than 5 and y is less than 10")
                    else print("x is less than 5 and y is greater than or equal to 10")
            else print("x is greater than or equal to 5")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))

    def testgeneral9(self):
        input = """func main() begin
            for i until i< num1 by 1
                for j until j<num2 by 1
                    print(i,j)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def testgeneral10(self):
        input = """func main() begin
            func function(number a1) begin
                func function1(number a2) begin
                    func function2(number a3) begin
                    end
                end 
            end
             
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def testgeneral11(self):
        input = """func main() begin
            string s <- \"abc\\n\\t'\"\"
            string ss <- \"123.\\t\\b\"
            s <- s...ss
            s <- s...ss
            return s
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))

    def testgeneral12(self):
        input = """func main() begin
            number a <- 20
            return fac(a)
        end
        func fac(number n) begin
            if (n = 0) return 1
            else return n * fac(n-1)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))

    def testgeneral13(self):
        input = """func main() begin
            for i until num1 < 0 by num1
                if (num1 > 1) inc(i)
                else dec(i) 
        end
        func inc(number a) return a+1
        func dec(number a) return a-1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))

    def testgeneral14(self):
        input = """ number a <- 1
        func main() begin
                if (a > 1) return 1
                else begin
                    inc(a)
                    func inc(number a) return a+1
                end
        end
        func inc(number a) return a+1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,259))

    def testgeneral15(self):
        input = """ func main() return
        func function() begin
            a <- a*b*c+d/12
            foo(a,b,(a+b)[2,foo(2,3)])
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))

    def testgeneral16(self):
        input = """ func main() return
        func function() begin
            for a[5][foo(7)] until (num1 + num2)*2 = 10 by 2
            begin
                a[0][a[5][foo(7)]] <- a[0][a[5][foo(7)]] + num2 * num1
                num2 <- num2 + num1
            end
        end
        """
        expect = "Error on line 3 col 17: ["
        self.assertTrue(TestParser.test(input,expect,261))
    
    def testgeneral17(self):
        input = """func main()
        begin
            for i until i < 0 by i + 1



                begin
                    a <- a + 1 * 1000 / (-1000e-13)
                    b <- a % (1000) / (a+54e31)
                end


                
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def testgeneral18(self):
        input = """string strarr[3] <- [\"123E.-3\",\"hello\"...\"world\",\"\\n\\b\\f\"]
        number numarr[3] <- [3+4,3-1*23,20.3+12.7+1.]
        func main()
        begin
            for i until i>=size(strarr) by 1
                print(extract(strarr[i],numarr[i]))
        end

        func extract(string a, number b)
            return a[b]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def testgeneral19(self):
        input = """func main() 
        
        
        begin
            for i until funccall(i,20) by 1
                continue
                
            func funccall(number i, number test)
                
        end

        func funccall(number i, number test) begin
            if (i = test) return true
                elif (i > test) return false 
                elif ((i<test) and (test%i=0)) return true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def testgeneral20(self):
        input = """func main() return
        a+b
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.test(input,expect,265))

    def testgeneral21(self):
        input = """func main() return funccall(number1) and funccall(number2) or funccall(number3)
        func funccall(number a)
        func funccall(number a) begin
            return true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))

    def testgeneral22(self):
        input = """func main() return funccall(funccall(funcall(funccall(number1))))
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def testgeneral23(self):
        input = """func main() 


        begin


            number au<-100
            var bc<--2e-3
            number c
            c<-au*bc+100/1000
            number arr[4] <- [au,bc,c,au+bc+c]

            return arr[3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def testgeneral24(self):
        input = """func main() begin
            number begin <- 100
        end
        """
        expect = "Error on line 2 col 19: begin"
        self.assertTrue(TestParser.test(input,expect,269))

    def testgeneral25(self):
        input = """func sum(number arr[10]) begin
            var total <- 0
            for i until len(arr) by 1 begin
                total <- total + arr[i]
            end
            return total
        end


        func main() begin
            number numbers[5] <- [1,2,3,4,5]
            var result <- sum(numbers)
            print(\"The sum of the numbers is: \",result)
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def testgeneral25(self):
        input = """func sum(number arr[10]) begin
            var total <- 0
            for i until len(arr) by 1 begin
                total <- total + arr[i]
            end
            return total
        end


        func main() begin
            number numbers[5] <- [1,2,3,4,5]
            var result <- sum(numbers)
            print(\"The sum of the numbers is: \",result)
        end 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def testgeneral26(self):
        input = """func main() begin
            if ((a <= b) and (b != c) or (d > e)) x <- 1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))

    def testgeneral27(self):
        input = """func main() begin

            a <- true or false and not false
            return a or 1
        end

        

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))

    def testgeneral28(self):
        input = """func main() begin
            a <- -b + not c - -d * not e
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))

    def testgeneral29(self):
        input = """func my_func() 
        
        begin
            foo(2+3, a/b, not false)
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))

    def testgeneral30(self):
        input = """func my_func() 
        
        
        begin

            x <- a[b[1 + c]]
            a[[b[1 + c]]] <- 123
        end

        """
        expect = "Error on line 7 col 14: ["
        self.assertTrue(TestParser.test(input,expect,275))

    def testgeneral31(self):
        input = """func main() begin
            var x <- readInteger()
            var res <- 0
            for x until x < 0 by -1 begin
                res <- res + x
            end
            printInteger(res)
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))

    def testgeneral32(self):
        input = """func my_func() begin
            x <- (((\"Hello\"...\" \")...\"world!\")...\"abc\\b\\\\\")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))

    def testgeneral33(self):
        input = """func funct(number _, number __) begin
            s <- 3
        end

        func main() begin
            a[1+2,2*3] <- _ + __
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def testgeneral34(self):
        input = """func main() begin
            __a_1_2 ->
            12
        end

        """
        expect = "Error on line 2 col 21: >"
        self.assertTrue(TestParser.test(input,expect,279))

    def testgeneral35(self):
        input = """func test(number a) begin
            return 1 - main(1, a, b)
        end

        func main() begin
            ## This is the main function
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def testgeneral36(self):
        input = """number a<-main(50)
        a <- main(a) + main(a*2+main(a))
        func main(number a) begin
            return a*2+1
        end
        """
        expect = "Error on line 2 col 8: a"
        self.assertTrue(TestParser.test(input,expect,281))

    def testgeneral37(self):
        input = """number a<-main(50)
        main(a)
        func main(number a) begin
            return a*2+1
        end
        """
        expect = "Error on line 2 col 8: main"
        self.assertTrue(TestParser.test(input,expect,282))

    def testgeneral38(self):
        input = """func main(number a) begin
            return (a+foo(123))[1][2][3][4][5,foo(123)]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def testgeneral39(self):
        input = """func main() begin
            printString(\"---*---\")
            printString(\"--***--\")
            printString(\"-*****-\")
            printString(\"-******\")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def testgeneral40(self):
        input = """func main() begin
            number,string a,b <- 123,\"hello world\"
        end
        """
        expect = "Error on line 2 col 18: ,"
        self.assertTrue(TestParser.test(input,expect,285))

    def testgeneral41(self):
        input = """a <- foo(123) 

        """
        expect = "Error on line 1 col 0: a"
        self.assertTrue(TestParser.test(input,expect,286))

    def testgeneral42(self):
        input = """func main() begin
            number a[2, 3] <- [[1,2,3],[4,5,6]]
            for i until i >= 2 by 1 begin
                for j until j >= 3 by 1 begin
                    a[i, j] <- i + j
                end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def testgeneral43(self):
        input = """func main() begin
            var x <- 1
            for x until x >= 10 by 0 begin
                x <- x * 2
            end
            arr[0] <- x
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def testgeneral44(self):
        input = """func main() begin
            number x <- 3
            begin
                x <- y * x
                begin
                    number x <- 0
                    x <- x - 1
                end
                x <- foo(x)
            end
            printInteger(x)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))

    def testgeneral45(self):
        input = """func main(number a, number b) begin
            if (a+b != x) begin
                return a+b
            end
            else begin
                return a-b
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def testgeneral46(self):
        input = """func main() begin
            if (abc >= 234 and not def) begin
                _var <- arr[1, 5]
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def testgeneral47(self):
        input = """func main() begin
            number a_1 <- funcfunc()
            for a_1 until exp = 1000 and not exp2 by a + arr[0] begin
                return 
            end
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def testgeneral48(self):
        input = """func main() begin
            number a <- foo(bar(1 + 2, 3 * 4), baz(5 - 6))
            bool b <- ((a or false) and true) or not a
            number c[4, 3] 
            c <- temp(a, b, (a + b - 2 * a - 3 * b), foo((a * b), a + b))
            var d <- c[2, 0] + c[3, 1] - c[2, 2]
            return d
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def testgeneral49(self):
        input = """func main() begin
            func main() begin
                return true and not (false and \"NA\")
            end
        end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))

    def testgeneral50(self):
        input = """func main() begin
            if (a = 1) begin
                if (b = 2) begin
                    x <- 1
                end 
                else begin
                    x <- 0
                end
            end 
            else begin
                x <- -1
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def testgeneral51(self):
        input = """func findIndex(string s1, string s2) begin
            number i <- find(s1, s2, 0)
            printInteger(i)
            for i until i = -1 by 0 begin
                i <- find(s1, s2, i + 1)
                if (i = -1) break
                printInteger(i)
            end
        end

        func main() begin
            string s1 <- \"Truong Dai Hoc Bach Khoa HCMUT.\"
            string s2 <- \"a\"
            findIndex(s1, s2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))

    def testgeneral52(self):
        input = """func fibo(number n) begin
            if (n <= 2) return 1
            number f1 <- 0
            number f2 <- 1
            number f3 <- f1 + f2
            number i <- 2
            for i until i > n by 1 begin
                f3 <- f1 + f2
                f1 <- f2
                f2 <- f3
            end
            return f3
        end
        func main() begin 
            return fibo(50)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))

    def testgeneral53(self):
        input = """func main() begin
            a[3 + foo(2)] <- a[b[2, foo(2,true and false,foo(1,2,\"happy\"))]] + ab[4,(60-7)/23,6]
            a[6+foo(123)] <- a[5]
            a[1][2][10+foo(123)*1000] <- (foo1(123,456,4e-3)+foo2(234,abc))[1][4][foo3(123)]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,298))

    def testgeneral54(self):
        input = """func main() begin
            x <- 10
            i <- 0
            for i until i > x by x-2
                if (i >= 1) break
                elif (x <= 1) continue
                elif (a[10,2+3] < (a-b)[1,2-2,3*4]) funcfunc(1,2,3)
                else i <- i*10
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))

    def testgeneral55(self):
        input = """func main() begin
            begin
                for i until i < 0 by i + 1
                    begin
                        continue
                        break
                        break
                        return true
                    end
                for i until i > 0 by i - 1
                    begin
                        continue
                        break
                        break
                        return false
                    end
            end
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

        