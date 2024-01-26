import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # def test_simple_string(self):
    #     "test simple string"
    #     self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))

    # def test_complex_string(self):
    #     "test complex string"
    #     self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))

        def test_0_noerror(self):
            self.assertTrue(TestLexer.test("""func(number a, number b)
begin
	number c <- a
	a <- b
	b <- c
	## Hello World $## Say something
end""", """func,(,number,a,,,number,b,),
,begin,
,number,c,<-,a,
,a,<-,b,
,b,<-,c,
,## Hello World $## Say something,
,end,<EOF>""", "0_noerror"))
        
        def test_1(self):
            self.assertTrue(TestLexer.test("""string a <- \"Hello World \\t and what's boy \\n \\\\ Said: '\"Hello Bro'\"\";""", """string,a,<-,Illegal Escape In String: Hello World \\t and what's""", "1"))
        
        def test_10(self):
            self.assertTrue(TestLexer.test("""func areDivisors(number num1, number num2)
	return (num1 % num2 = 0 or num2 % num1 = 0)

func main()
begin
	var num1 <- readNumber()
	var num2 <- readNumber()
	if areDivisors(num1, num2) printString(\"Yes\")
	else printString(\"No\\''t\")
end""", """func,areDivisors,(,number,num1,,,number,num2,),
,return,(,num1,%,num2,=,0,or,num2,%,num1,=,0,),
,
,func,main,(,),
,begin,
,var,num1,<-,readNumber,(,),
,var,num2,<-,readNumber,(,),
,if,areDivisors,(,num1,,,num2,),printString,(,Yes,),
,else,printString,(,Illegal Escape In String: No\\''t""", "10"))
        
        def test_11(self):
            self.assertTrue(TestLexer.test("""123acd123
Hello World \"\\n\\r\\n\\h\\\\\\'\\b\\t\\r\\f\"""", """123,acd123,
,Hello,World,Illegal Escape In String: \\n\\r\\n\\h""", "11"))
        
        def test_12(self):
            self.assertTrue(TestLexer.test("""_andor123 ifelse123_345
Hello World \"--->\\>\"""", """_andor123,ifelse123_345,
,Hello,World,Illegal Escape In String: --->\\>""", "12"))
        
        def test_13(self):
            self.assertTrue(TestLexer.test("""WoW iDentity_Whatnew # This is new bro""", """WoW,iDentity_Whatnew,Error Token #""", "13"))
        
        def test_14(self):
            self.assertTrue(TestLexer.test("""I_<3 You chucamo
\"""", """I_,<,3,You,chucamo,
,Unclosed String: """, "14"))
        
        def test_15(self):
            self.assertTrue(TestLexer.test("""array[WITH_lots,_0f_(separators)]
[\"Hello World\\]\"]""", """array,[,WITH_lots,,,_0f_,(,separators,),],
,[,Illegal Escape In String: Hello World\\]""", "15"))
        
        def test_16_newline(self):
            self.assertTrue(TestLexer.test("""th1s 1s a t33nc0d3 t3stc4s3 w1th a r0ck3t <>3
\"hello \\r\\t\\n
\"\"\" \"\" \"\"\"""", """th1s,1,s,a,t33nc0d3,t3stc4s3,w1th,a,r0ck3t,<,>,3,
,Unclosed String: hello \\r\\t\\n""", "16_newline"))
        
        def test_17(self):
            self.assertTrue(TestLexer.test("""begin
	number r
	number s
	r <- 2.0
	number a[5]
	number b[5]
	s <- r * r * 3e-5.2
	a[0] <- s
end""", """begin,
,number,r,
,number,s,
,r,<-,2.0,
,number,a,[,5,],
,number,b,[,5,],
,s,<-,r,*,r,*,3e-5,Error Token .""", "17"))
        
        def test_18(self):
            self.assertTrue(TestLexer.test("""var i <- 0
for i until i >= 10 by 1
	print i
	10.e-5423
	\"...'a\"""", """var,i,<-,0,
,for,i,until,i,>=,10,by,1,
,print,i,
,10.e-5423,
,Illegal Escape In String: ...'a""", "18"))
        
        def test_19(self):
            self.assertTrue(TestLexer.test("""for <number-variable> until <condition expression> by <update-expression>
<statement>
string a <- \"Hello\\r""", """for,<,number,-,variable,>,until,<,condition,expression,>,by,<,update,-,expression,>,
,<,statement,>,
,string,a,<-,Unclosed String: Hello\\r""", "19"))
        
        def test_2(self):
            self.assertTrue(TestLexer.test("""str a <- \"ABC\\t\",
\"""", """str,a,<-,ABC\\t,,,
,Unclosed String: """, "2"))
        
        def test_20(self):
            self.assertTrue(TestLexer.test("""12327312.29381923817313E-203120312
.12e-3""", """12327312.29381923817313E-203120312,
,Error Token .""", "20"))
        
        def test_21_newline(self):
            self.assertTrue(TestLexer.test("""531.E-3 > 290.123E-3 = 2.<239.12
if \"hello world \\'\" = \"
begin
	\"say something\"
end""", """531.E-3,>,290.123E-3,=,2.,<,239.12,
,if,hello world \\',=,Unclosed String: """, "21_newline"))
        
        def test_22(self):
            self.assertTrue(TestLexer.test("""I l0wq Nwsaw_23@abc swq 2123 0.23, 1823., 238912E+23, 1231E-23""", """I,l0wq,Nwsaw_23,Error Token @""", "22"))
        
        def test_23(self):
            self.assertTrue(TestLexer.test("""Create SuperString [0.2312,000.0001E-30,123123.123123,0.,932891.E-230][10]
\"var number string begin for if else""", """Create,SuperString,[,0.2312,,,000.0001E-30,,,123123.123123,,,0.,,,932891.E-230,],[,10,],
,Unclosed String: var number string begin for if else""", "23"))
        
        def test_24(self):
            self.assertTrue(TestLexer.test(""" How about \"a string with numbers like '\"1.123e-3'\", '\"0.23E-50'\"?\", it should be \"\\\\fine\\\\'\"\", isn't it? """, """How,about,a string with numbers like '\"1.123e-3'\", '\"0.23E-50'\"?,,,it,should,be,\\\\fine\\\\'\",,,isn,Error Token '""", "24"))
        
        def test_25(self):
            self.assertTrue(TestLexer.test("""\"a\\'b'a\"""", """Illegal Escape In String: a\\'b'a""", "25"))
        
        def test_26(self):
            self.assertTrue(TestLexer.test("""true false number not and or continue if else elif begin end bool string return var dynamic func for until by break
' hello""", """true,false,number,not,and,or,continue,if,else,elif,begin,end,bool,string,return,var,dynamic,func,for,until,by,break,
,Error Token '""", "26"))
        
        def test_27_newline(self):
            self.assertTrue(TestLexer.test("""+-*/%= <- != < <= > >= ... ==
\"if true begin printHello World end
\"""", """+,-,*,/,%,=,<-,!=,<,<=,>,>=,...,==,
,Unclosed String: if true begin printHello World end""", "27_newline"))
        
        def test_28_comment(self):
            self.assertTrue(TestLexer.test("""[(,,)]##Hello World What's boy
\"##What's boy\"""", """[,(,,,,,),],##Hello World What's boy,
,Illegal Escape In String: ##What's""", "28_comment"))
        
        def test_29(self):
            self.assertTrue(TestLexer.test("""&""", """Error Token &""", "29"))
        
        def test_30(self):
            self.assertTrue(TestLexer.test("""A __ aa AZ abc __a __AA aE123_ a233 _1 A1 B__2__C
string _123E23 <- \"if true begin say something end ## This is comment\\'\"
\"""", """A,__,aa,AZ,abc,__a,__AA,aE123_,a233,_1,A1,B__2__C,
,string,_123E23,<-,if true begin say something end ## This is comment\\',
,Unclosed String: """, "30"))
        
        def test_31(self):
            self.assertTrue(TestLexer.test("""\"\\b \\f \\r \\n \\t \\\\ Super \\b \\f \\r \\n \\t \\\\  man\\b \\f \\r \\n \\t \\\\\"
\" Hello What\\'s up '\"t""", """\\b \\f \\r \\n \\t \\\\ Super \\b \\f \\r \\n \\t \\\\  man\\b \\f \\r \\n \\t \\\\,
,Unclosed String:  Hello What\\'s up '\"t""", "31"))
        
        def test_32(self):
            self.assertTrue(TestLexer.test("""23.542E-2032 ## This is the 32nd test case
 abcd123#""", """23.542E-2032,## This is the 32nd test case,
,abcd123,Error Token #""", "32"))
        
        def test_33(self):
            self.assertTrue(TestLexer.test("""3123erfdos25123..3""", """3123,erfdos25123,Error Token .""", "33"))
        
        def test_34(self):
            self.assertTrue(TestLexer.test("""=>=>*%%TH4NKS,_________L4ST___________T3STC4S3____________F0R____________[1D3NT1F13R]_______%%*<=<=
\"%%$#@%#$#@%&%\"
\"""", """=,>=,>,*,%,%,TH4NKS,,,_________L4ST___________T3STC4S3____________F0R____________,[,1,D3NT1F13R,],_______,%,%,*,<=,<=,
,%%$#@%#$#@%&%,
,Unclosed String: """, "34"))
        
        def test_35(self):
            self.assertTrue(TestLexer.test("""\"oopsie, I forget to put the '\" at the end of the string @__@ \\'""", """Unclosed String: oopsie, I forget to put the '\" at the end of the string @__@ \\'""", "35"))
        
        def test_36(self):
            self.assertTrue(TestLexer.test("""Here is a string \"[string\\t\\b'\"]\", but is this one \"\" a string too?""", """Here,is,a,string,[string\\t\\b'\"],,,but,is,this,one,,a,string,too,Error Token ?""", "36"))
        
        def test_37(self):
            self.assertTrue(TestLexer.test("""\"my hcmut mail is '\"huy.la1809@hcmut.edu.vn'\"\"!""", """my hcmut mail is '\"huy.la1809@hcmut.edu.vn'\",Error Token !""", "37"))
        
        def test_38(self):
            self.assertTrue(TestLexer.test("""Enough with hard tests, lets try a simple one \"hello, my name is '\"Virros Luo'\" @\\\\__/@, that's how people call me! @\\__/@\"""", """Enough,with,hard,tests,,,lets,try,a,simple,one,Illegal Escape In String: hello, my name is '\"Virros Luo'\" @\\\\__/@, that's""", "38"))
        
        def test_39(self):
            self.assertTrue(TestLexer.test("""test some weird char: \"%%##@@!!\\\\\"""", """test,some,weird,char,Error Token :""", "39"))
        
        def test_3_newline(self):
            self.assertTrue(TestLexer.test("""funcfunc(number a, number b)
begin
\"begin say something 
\"\"
end""", """funcfunc,(,number,a,,,number,b,),
,begin,
,Unclosed String: begin say something """, "3_newline"))
        
        def test_4(self):
            self.assertTrue(TestLexer.test("""string a <- \"Hello \\\";""", """string,a,<-,Illegal Escape In String: Hello \\\"""", "4"))
        
        def test_40(self):
            self.assertTrue(TestLexer.test("""test with character \"$$!=()\\\\f\\\\'\\\\\\\\\"""", """test,with,character,Illegal Escape In String: $$!=()\\\\f\\\\'\\""", "40"))
        
        def test_41(self):
            self.assertTrue(TestLexer.test("""Now we will test with another string \"\\b\\f@\\'\\'""", """Now,we,will,test,with,another,string,Unclosed String: \\b\\f@\\'\\'""", "41"))
        
        def test_42(self):
            self.assertTrue(TestLexer.test(""" This is a sequence of escapse string \"\\b\\f\\r\\n\\t\\'\\\\'\"\"? """, """This,is,a,sequence,of,escapse,string,\\b\\f\\r\\n\\t\\'\\\\'\",Error Token ?""", "42"))
        
        def test_43_stringlit(self):
            self.assertTrue(TestLexer.test("""I will use a multiple slash for this testcase \"\\\\\\\\\\\\\\\"""", """I,will,use,a,multiple,slash,for,this,testcase,Illegal Escape In String: \\\\\\\\\\\\\\\"""", "43_stringlit"))
        
        def test_44(self):
            self.assertTrue(TestLexer.test(""" \"a\\\\b\\'c\\bd\\f'\\\\a\" """, """Illegal Escape In String: a\\\\b\\'c\\bd\\f'\\""", "44"))
        
        def test_45_stringlit(self):
            self.assertTrue(TestLexer.test("""Now test with a new string \"\\b\\f@\\''\"""", """Now,test,with,a,new,string,Unclosed String: \\b\\f@\\''\"""", "45_stringlit"))
        
        def test_46(self):
            self.assertTrue(TestLexer.test("""\"let's buy a roll royce\"""", """Illegal Escape In String: let's""", "46"))
        
        def test_47_stringlit(self):
            self.assertTrue(TestLexer.test("""\"OHH, this is a weird string @__@ '\"""", """Unclosed String: OHH, this is a weird string @__@ '\"""", "47_stringlit"))
        
        def test_48(self):
            self.assertTrue(TestLexer.test(""" printf(\"\\\\alice\\' d03n tn3 hill 0f \\flowers\")*$""", """printf,(,\\\\alice\\' d03n tn3 hill 0f \\flowers,),*,Error Token $""", "48"))
        
        def test_49_stringlit(self):
            self.assertTrue(TestLexer.test(""" Is it estimated as a single quotation \"'\"?""", """Is,it,estimated,as,a,single,quotation,Unclosed String: '\"?""", "49_stringlit"))
        
        def test_5(self):
            self.assertTrue(TestLexer.test("""string a <- \"Hello World '\";""", """string,a,<-,Unclosed String: Hello World '\";""", "5"))
        
        def test_50(self):
            self.assertTrue(TestLexer.test("""Test again with a list 0f null strings \"\"\"\"\"\"\"\"\"""", """Test,again,with,a,list,0,f,null,strings,,,,,Unclosed String: """, "50"))
        
        def test_51(self):
            self.assertTrue(TestLexer.test("""Now we will test with some keywords is true, false, while, if, else ...!""", """Now,we,will,test,with,some,keywords,is,true,,,false,,,while,,,if,,,else,...,Error Token !""", "51"))
        
        def test_52(self):
            self.assertTrue(TestLexer.test("""Now we will test with some value 0 199 12. 12.323 12.3e-3 12.3e039 .12 .12e3 .12e-3 .12e039
12e-3 12.e-3 .""", """Now,we,will,test,with,some,value,0,199,12.,12.323,12.3e-3,12.3e039,Error Token .""", "52"))
        
        def test_53(self):
            self.assertTrue(TestLexer.test("""Now we will test again with a lot of comma,,,,
,,,,
,
?""", """Now,we,will,test,again,with,a,lot,of,comma,,,,,,,,,
,,,,,,,,,
,,,
,Error Token ?""", "53"))
        
        def test_54(self):
            self.assertTrue(TestLexer.test("""Now here we will test with newline testcase
this
number
true
fal
se
f
o
r
i
f
e
l
s
e
12.
23
e_23_
e
-33@""", """Now,here,we,will,test,with,newline,testcase,
,this,
,number,
,true,
,fal,
,se,
,f,
,o,
,r,
,i,
,f,
,e,
,l,
,s,
,e,
,12.,
,23,
,e_23_,
,e,
,-,33,Error Token @""", "54"))
        
        def test_55_eof(self):
            self.assertTrue(TestLexer.test("""This will catch a EOF string
\"Hello world this is end of file""", """This,will,catch,a,EOF,string,
,Unclosed String: Hello world this is end of file""", "55_eof"))
        
        def test_56_eof(self):
            self.assertTrue(TestLexer.test("""This is another end of file string too
\"What\\'s boy and this is have an error '\"""", """This,is,another,end,of,file,string,too,
,Unclosed String: What\\'s boy and this is have an error '\"""", "56_eof"))
        
        def test_57_newline(self):
            self.assertTrue(TestLexer.test("""This is test for newline in string
\"Hello 
World\"""", """This,is,test,for,newline,in,string,
,Unclosed String: Hello """, "57_newline"))
        
        def test_58_newline(self):
            self.assertTrue(TestLexer.test("""This is also another newline string
\"Hello World bro \\n but we also want to enter new line by enter
\"""", """This,is,also,another,newline,string,
,Unclosed String: Hello World bro \\n but we also want to enter new line by enter""", "58_newline"))
        
        def test_59_error(self):
            input = '''"\f'"\n\t"'''
            expected = '''Unclosed String: '''
            self.assertTrue(TestLexer.test(input, expected, "59_error"))
        
        def test_6(self):
            self.assertTrue(TestLexer.test("""func main()
begin
	number a <- 10e-3;
	number b <- 10.0;
	string c <- \"Hello World \\r What's up boy'\"\";
	return a + b;
end""", """func,main,(,),
,begin,
,number,a,<-,10e-3,Error Token ;""", "6"))
        
        def test_60(self):
            self.assertTrue(TestLexer.test("""ToDay is my birthday H4pPY B1rThd@y""", """ToDay,is,my,birthday,H4pPY,B1rThd,Error Token @""", "60"))
        
        def test_61_hardnl(self):
            self.assertTrue(TestLexer.test("""A new type of invalid string
\"Hello World and my name is \\
'\"""", """A,new,type,of,invalid,string,Unclosed String: Hello World and my name is \\""", "61_hardnl"))
        
        def test_62(self):
            self.assertTrue(TestLexer.test("""This advertisement is 1 Love <3 Y0U S0 M*ch <3!""", """This,advertisement,is,1,Love,<,3,Y0U,S0,M,*,ch,<,3,Error Token !""", "62"))
        
        def test_63(self):
            self.assertTrue(TestLexer.test("""2 5M 2N 3D20T S4NDW1CH!!!""", """2,5,M,2,N,3,D20T,S4NDW1CH,Error Token !""", "63"))
        
        def test_64_hardnl(self):
            self.assertTrue(TestLexer.test("""This will be new hard string
\"Hello '
\"""", """This,will,be,new,hard,string,Unclosed String: Hello '""", "64_hardnl"))
        
        def test_65(self):
            self.assertTrue(TestLexer.test("""Tomorrow, i will talk to him \"1 would like to go playing game <3\" but I w.ll break""", """Tomorrow,,,i,will,talk,to,him,1 would like to go playing game <3,but,I,w,Error Token .""", "65"))
        
        def test_66_newline(self):
            self.assertTrue(TestLexer.test("""\"Test with to many escape sequence '\",\\b,\\t,\\r is no easy talk!
""", """Unclosed String: Test with to many escape sequence '\",\\b,\\t,\\r is no easy talk!""", "66_newline"))
        
        def test_67(self):
            self.assertTrue(TestLexer.test("""I will draw a train with character
IIII[  ]-[   ]-[   ]-[   ]IIII@@@@""", """I,will,draw,a,train,with,character,
,IIII,[,],-,[,],-,[,],-,[,],IIII,Error Token @""", "67"))
        
        def test_68(self):
            self.assertTrue(TestLexer.test("""This input will get many \"If i want to include char '\" in the string, i need to add a single quote '\"""", """This,input,will,get,many,Unclosed String: If i want to include char '\" in the string, i need to add a single quote '\"""", "68"))
        
        def test_69(self):
            self.assertTrue(TestLexer.test("""ID[\"2153379\", virrosluo]!""", """ID,[,2153379,,,virrosluo,],Error Token !""", "69"))
        
        def test_7(self):
            self.assertTrue(TestLexer.test("""string a <- \"Hello World'a\";""", """string,a,<-,Illegal Escape In String: Hello World'a""", "7"))
        
        def test_70(self):
            self.assertTrue(TestLexer.test("""This is testcase from my teacher
1.0 1e-12 1.0e-12 0.001 .01 .e""", """This,is,testcase,from,my,teacher,
,1.0,1e-12,1.0e-12,0.001,Error Token .""", "70"))
        
        def test_71(self):
            self.assertTrue(TestLexer.test("""This testcase also in number 12.e-3 12.d-3,12e!""", """This,testcase,also,in,number,12.e-3,12.,d,-,3,,,12,e,Error Token !""", "71"))
        
        def test_72_newline(self):
            self.assertTrue(TestLexer.test("""This will have new endline string

\"Hello world what \\'sboy




\"""", """This,will,have,new,endline,string,
,
,Unclosed String: Hello world what \\'sboy""", "72_newline"))
        
        def test_73_newline(self):
            self.assertTrue(TestLexer.test("""this will end of file but not yet close string
\"Hello World \\n\\t\\b\\f""", """this,will,end,of,file,but,not,yet,close,string,
,Unclosed String: Hello World \\n\\t\\b\\f""", "73_newline"))
        
        def test_74(self):
            self.assertTrue(TestLexer.test("""\"i love anime super
saiyan \\t\"""", """Unclosed String: i love anime super""", "74"))
        
        def test_75(self):
            self.assertTrue(TestLexer.test("""The Book HaryPotter said \"the more ch@r@cters there are, the harder that witcher can remember\\'\"!""", """The,Book,HaryPotter,said,the more ch@r@cters there are, the harder that witcher can remember\\',Error Token !""", "75"))
        
        def test_76(self):
            self.assertTrue(TestLexer.test("""This will test some special case with escape and newline
\"Witcher in Hary Potter \\t\\r\\n\\'    \"!""", """This,will,test,some,special,case,with,escape,and,newline,
,Witcher in Hary Potter \\t\\r\\n\\'    ,Error Token !""", "76"))
        
        def test_77(self):
            self.assertTrue(TestLexer.test("""Some people say that: \"Life is hard\"""", """Some,people,say,that,Error Token :""", "77"))
        
        def test_78(self):
            self.assertTrue(TestLexer.test("""dict [\"Life is hard\":\"Is It True\"]""", """dict,[,Life is hard,Error Token :""", "78"))
        
        def test_79(self):
            self.assertTrue(TestLexer.test("""`1234567890-=""", """Error Token `""", "79"))
        
        def test_80(self):
            self.assertTrue(TestLexer.test("""~!@#$%^&*()_+""", """Error Token ~""", "80"))
        
        def test_81(self):
            self.assertTrue(TestLexer.test("""########$%^&*(\"Say something\"
\"Say Something\"$""", """########$%^&*(\"Say something\",
,Say Something,Error Token $""", "81"))
        
        def test_82(self):
            self.assertTrue(TestLexer.test("""The song = == 
\"I Wonder how, i wonder why\"
hi
== = == = == = ^""", """The,song,=,==,
,I Wonder how, i wonder why,
,hi,
,==,=,==,=,==,=,Error Token ^""", "82"))
        
        def test_83(self):
            self.assertTrue(TestLexer.test("""Dad said to me that \"I used to have a superman toy name '\"Tiga'\" But now i lose it...\"
...
+++
---
\"================ 
================\"""", """Dad,said,to,me,that,I used to have a superman toy name '\"Tiga'\" But now i lose it...,
,...,
,+,+,+,
,-,-,-,
,Unclosed String: ================ """, "83"))
        
        def test_84(self):
            self.assertTrue(TestLexer.test("""The teacher said the meter went up to 67.0e-4;
if it reachs 70.0e-3, it will \\\\\\\\""", """The,teacher,said,the,meter,went,up,to,67.0e-4,Error Token ;""", "84"))
        
        def test_85(self):
            self.assertTrue(TestLexer.test("""This is the testcase 85th in my set testcases	so ... +-=0987654321`""", """This,is,the,testcase,85,th,in,my,set,testcases,so,...,+,-,=,0987654321,Error Token `""", "85"))
        
        def test_86(self):
            self.assertTrue(TestLexer.test("""This testcase i will test on
var<-[[1,2,3],[4,5,6],[7,8,9]];""", """This,testcase,i,will,test,on,
,var,<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],,,[,7,,,8,,,9,],],Error Token ;""", "86"))
        
        def test_87(self):
            self.assertTrue(TestLexer.test("""This case is concat string in normal programming language
\"string\" + \"string\\n\\r'\"\" == \"stringstring\\b\\'\\t
""", """This,case,is,concat,string,in,normal,programming,language,
,string,+,string\\n\\r'\",==,Unclosed String: stringstring\\b\\'\\t""", "87"))
        
        def test_88(self):
            self.assertTrue(TestLexer.test("""In this testcase i will draw the raining to let u see
\"////\\'////\\'////\\\\\\\\\\\"""", """In,this,testcase,i,will,draw,the,raining,to,let,u,see,
,Illegal Escape In String: ////\\'////\\'////\\\\\\\\\\\"""", "88"))
        
        def test_89(self):
            self.assertTrue(TestLexer.test("""string advertisement <- \"What's that pokemon huh\"""", """string,advertisement,<-,Illegal Escape In String: What's""", "89"))
        
        def test_8_comma(self):
            self.assertTrue(TestLexer.test("""string Hello_World_02 <- \"'\"Hello Guy'\", my name is '\"superman'\"\";\\""", """string,Hello_World_02,<-,'\"Hello Guy'\", my name is '\"superman'\",Error Token ;""", "8_comma"))
        
        def test_9(self):
            self.assertTrue(TestLexer.test("""string Hello_World_02 <- \"'\"Hello Guy'\", my name is '\"superman'\"\\\"\";""", """string,Hello_World_02,<-,Illegal Escape In String: '\"Hello Guy'\", my name is '\"superman'\"\\\"""", "9"))
        
        def test_90(self):
            self.assertTrue(TestLexer.test("""\"\\b\"...\"\\n\"...\"\\r\"...\"\\f\"...\"\\t\"...\"\\\\\"...\"'\"\"..""", """\\b,...,\\n,...,\\r,...,\\f,...,\\t,...,\\\\,...,'\",Error Token .""", "90"))
        
        def test_91(self):
            self.assertTrue(TestLexer.test("""test 
with 
another 
array 
test
4.E+4[a[22,33,44,55],b[11,aa22,\"\\'\",],'\"]""", """test,
,with,
,another,
,array,
,test,
,4.E+4,[,a,[,22,,,33,,,44,,,55,],,,b,[,11,,,aa22,,,\\',,,],,,Error Token '""", "91"))
        
        def test_92(self):
            self.assertTrue(TestLexer.test("""(Google), (Facebook), [OpenAI] are the three big company in 41 fiEld $$$""", """(,Google,),,,(,Facebook,),,,[,OpenAI,],are,the,three,big,company,in,41,fiEld,Error Token $""", "92"))
        
        def test_93(self):
            self.assertTrue(TestLexer.test("""This is all special character a@#$%^&&*""", """This,is,all,special,character,a,Error Token @""", "93"))
        
        def test_94(self):
            self.assertTrue(TestLexer.test("""[3e-14, 3e-13] how much number in that ?""", """[,3e-14,,,3e-13,],how,much,number,in,that,Error Token ?""", "94"))
        
        def test_95_comma(self):
            self.assertTrue(TestLexer.test("""array alpha[55,66,77]<-[[12,23,34],[5e-2,6.15E-1,70.],true,false,\"who am i? \\n\"];""", """array,alpha,[,55,,,66,,,77,],<-,[,[,12,,,23,,,34,],,,[,5e-2,,,6.15E-1,,,70.,],,,true,,,false,,,who am i? \\n,],Error Token ;""", "95_comma"))
        
        def test_96(self):
            self.assertTrue(TestLexer.test("""Night+Anime+Rainy is perfect!!!!""", """Night,+,Anime,+,Rainy,is,perfect,Error Token !""", "96"))
        
        def test_97(self):
            self.assertTrue(TestLexer.test("""The EOF is represent for End of File \"  ...   
\"""", """The,EOF,is,represent,for,End,of,File,Unclosed String:   ...   """, "97"))
        
        def test_98_noerror(self):
            self.assertTrue(TestLexer.test("""When we catch \"3rr0r\" we should f1x th1s error With end of String""", """When,we,catch,3rr0r,we,should,f1x,th1s,error,With,end,of,String,<EOF>""", "98_noerror"))
        
        def test_99_noerror(self):
            self.assertTrue(TestLexer.test("""Last testcase so we will test with escape string
\"\\\\,\\t,\\b,\\f,\\','\" is no error but if we do not close string will have error \"""", """Last,testcase,so,we,will,test,with,escape,string,
,\\\\,\\t,\\b,\\f,\\','\" is no error but if we do not close string will have error ,<EOF>""", "99_noerror"))