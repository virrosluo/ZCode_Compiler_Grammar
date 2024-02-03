import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    ############# TEST COMMENT #############
    def testcomment1(self):
        input = "## This is the first test case"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input,expect,101))

    def testcomment2(self):
        input = "1.23e-1 ## This is the second test case \n abcd123#"
        expect = "1.23e-1,\n,abcd123,Error Token #"
        self.assertTrue(TestLexer.test(input,expect,102))

    def testcomment3(self):
        input = "something123 ## This should not be allowed"
        expect = "something123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,103))

    ############# TEST IDENTIFIERS #############
    def testidentifier1(self):
        input = "123acd123..3"
        expect = "123,acd123,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,104))

    def testidentifier2(self):
        input = "_andor123 ifelse123_345!"
        expect = "_andor123,ifelse123_345,Error Token !"
        self.assertTrue(TestLexer.test(input,expect,105))

    def testidentifier3(self):
        input = "WoW iDentity_Whatnew?"
        expect = "WoW,iDentity_Whatnew,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,106))
    
    def testidentifier4(self):
        input = "I_<3 You chucamo"
        expect = "I_,<,3,You,chucamo,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,107))

    def testidentifier5(self):
        input = "array[WITH_lots,_0f_(separ@tors)]"
        expect = "array,[,WITH_lots,,,_0f_,(,separ,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,108))

    def testidentifier6(self):
        input = "th1s 1s a t33nc0d3 t3stc4s3 w1th a r0ck3t <>3"
        expect = "th1s,1,s,a,t33nc0d3,t3stc4s3,w1th,a,r0ck3t,<,>,3,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,109))
    
    def testidentifier(self):
        input = "=>=>*%%TH4NKS,_________L4ST___________T3STC4S3____________F0R____________[1D3NT1F13R]_______%%*<=<="
        expect = "=,>=,>,*,%,%,TH4NKS,,,_________L4ST___________T3STC4S3____________F0R____________,[,1,D3NT1F13R,],_______,%,%,*,<=,<=,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,110))

    ############# TEST NUMBER LITERALS #############
    def testnumber1(self):
        input = "1234."
        expect = "1234.,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,111))

    def testnumber2(self):
        input = "1234.0000000000005678901123"
        expect = "1234.0000000000005678901123,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,112))

    def testnumber3(self):
        input = "50.E-6<70.123e-3=3.<6060.12"
        expect = "50.E-6,<,70.123e-3,=,3.,<,6060.12,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,113))
    
    def testnumber4(self):
        input = "I l0ve Numb3r such as 0.13, 13., 13.31, 13.3113E+1, 133.11E-13"
        expect = "I,l0ve,Numb3r,such,as,0.13,,,13.,,,13.31,,,13.3113E+1,,,133.11E-13,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,114))
  
    def testnumber5(self):
        input = "Create array [0.708,0.000001E-30, 12312344558990.78312345, 0.,85087.E-30][10]!1.23"
        expect = "Create,array,[,0.708,,,0.000001E-30,,,12312344558990.78312345,,,0.,,,85087.E-30,],[,10,],Error Token !"
        self.assertTrue(TestLexer.test(input,expect,115))

    def testnumber6(self):
        input = "D0 Y0u Kn0w 123.e-12+321.0e-12=444.E-12 am@zing"
        expect = "D0,Y0u,Kn0w,123.e-12,+,321.0e-12,=,444.E-12,am,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,116))
    
    def testnumber7(self):
        input = "Pl34s3 Wr1t3 A r4Nd0M 3xpr3ss10n such 4s 3e-3*12.4E+3=78.e-8."
        expect = "Pl34s3,Wr1t3,A,r4Nd0M,3,xpr3ss10n,such,4,s,3e-3,*,12.4E+3,=,78.e-8,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,117))

    def testnumber8(self):
        input = "G1v3 m3 th3 4nsw3r f0r th1s <qu3st1on>:1.24+1.6=?"
        expect = "G1v3,m3,th3,4,nsw3r,f0r,th1s,<,qu3st1on,>,Error Token :"
        self.assertTrue(TestLexer.test(input,expect,118))

    def testnumber9(self):
        input = "wh4t 1s th3 4nsw3r 1f a=4.567, b=0199999990, c=70.0001, d=50.03E-4, e=12.E-4, E=74.e13, [(a+b)%c-(d*e)]/E?"
        expect = "wh4t,1,s,th3,4,nsw3r,1,f,a,=,4.567,,,b,=,0199999990,,,c,=,70.0001,,,d,=,50.03E-4,,,e,=,12.E-4,,,E,=,74.e13,,,[,(,a,+,b,),%,c,-,(,d,*,e,),],/,E,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,119))

    def testnumber10(self):
        input = "0.123__*__6e-3__+__534__-__0__<__0E-3__/__4.321e-23__%__5.6531E+11==True__or__not?"
        expect = "0.123,__,*,__6e,-,3,__,+,__534__,-,__0__,<,__0E,-,3,__,/,__4,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,120))

    ############# OPERATORS, SEPARATORS #############
    def testopset1(self):
        input = "(>__<)(*__*)(=__=)(+__+)($__$)"
        expect = "(,>,__,<,),(,*,__,*,),(,=,__,=,),(,+,__,+,),(,Error Token $"
        self.assertTrue(TestLexer.test(input,expect,121))
    
    def testopset2(self):
        input = "a+++++++b+++++++++c=?"
        expect = "a,+,+,+,+,+,+,+,b,+,+,+,+,+,+,+,+,+,c,=,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,122))
    
    def testopset3(self):
        input = "String a<-b...c...d..e"
        expect = "String,a,<-,b,...,c,...,d,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,123))

    def testopset4(self):
        input = "not(a and b) or c!=d and (not(e) || not (a))"
        expect = "not,(,a,and,b,),or,c,!=,d,and,(,not,(,e,),Error Token |"
        self.assertTrue(TestLexer.test(input,expect,124))

    def testopset5(self):
        input = "number stuID<-12345678, number maxScore<-8.2, stuScore[stuID]>maxScore?maxScore<-stuScore[stuID]:;"
        expect = "number,stuID,<-,12345678,,,number,maxScore,<-,8.2,,,stuScore,[,stuID,],>,maxScore,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,125))

    def testopset6(self):
        input = "//////......******<[<]0[>]>******......\\\\\\"
        expect = "/,/,/,/,/,/,...,...,*,*,*,*,*,*,<,[,<,],0,[,>,],>,*,*,*,*,*,*,...,...,Error Token \\"
        self.assertTrue(TestLexer.test(input,expect,126))

    def testopset7(self):
        input = "a<-1.2e-50,b<-456,c<-1247E-3,d<-1,e<-75e-2,((a%b)+2*c)/d-e=?"
        expect = "a,<-,1.2e-50,,,b,<-,456,,,c,<-,1247E-3,,,d,<-,1,,,e,<-,75e-2,,,(,(,a,%,b,),+,2,*,c,),/,d,-,e,=,Error Token ?"
        self.assertTrue(TestLexer.test(input,expect,127))

    def testopset8(self):
        input = "d3v1c3 h4ck3d,a*b=k3y,@adm1n<-pr0v0k3"
        expect = "d3v1c3,h4ck3d,,,a,*,b,=,k3y,,,Error Token @"
        self.assertTrue(TestLexer.test(input,expect,128))

    def testopset9(self):
        input = "r3v3rs3d,-to+,*to/,=to!=,g00dby3!"
        expect = "r3v3rs3d,,,-,to,+,,,*,to,/,,,=,to,!=,,,g00dby3,Error Token !"
        self.assertTrue(TestLexer.test(input,expect,129))

    def testopset10(self):
        input = "last+op+testcase[-]()%__%,70to->.."
        expect = "last,+,op,+,testcase,[,-,],(,),%,__,%,,,70,to,-,>,Error Token ."
        self.assertTrue(TestLexer.test(input,expect,130))

    ############# STRING LITERALS #############
        
    def teststringlit1(self):
        input = """ This is \"the first string testcase\"! """
        expect = """This,is,the first string testcase,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,131))

    def teststringlit2(self):
        input = """ This is \"an another string test case\" with \"one or more strings\" and \"include special ch@r@ct3rs such as \\b or \\'\"! """
        expect = "This,is,an another string test case,with,one or more strings,and,include special ch@r@ct3rs such as \\b or \\',Error Token !"
        self.assertTrue(TestLexer.test(input,expect,132))
    
    def teststringlit3(self):
        input = """ How about \"a string with numbers like \'\"1.123e-3'\", \'\"0.23E-50'\"?\", it should be \"\\\\fine\\\\\'\"\", isn't it? """
        expect = """How,about,a string with numbers like '\"1.123e-3'\", '\"0.23E-50'\"?,,,it,should,be,\\\\fine\\\\'\",,,isn,Error Token '"""
        self.assertTrue(TestLexer.test(input, expect, 133))

    def teststringlit4(self):
        input = """ string hello <- \"Hello World\\t\"!"""
        expect = """string,hello,<-,Hello World\\t,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,134))   
    
    def teststringlit5(self):
        input = """ \"a\\'b'a\" """
        expect = """a\\'b'a,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,135))  

    def teststringlit6(self):
        input = """ Lets test with a list of null strings \"\"\"\"\"\"\"\"\""""
        expect = """Lets,test,with,a,list,of,null,strings,,,,,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,136))  

    def teststringlit7(self):
        input = """ What if there is a single quotation mark \"'\"?"""
        expect = """What,if,there,is,a,single,quotation,mark,Unclosed String: '\"?"""
        self.assertTrue(TestLexer.test(input,expect,137))  
    
    def teststringlit8(self):
        input = """ print(\"What does '\"love'\" mean?\");"""
        expect = """print,(,What does '\"love'\" mean?,),Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,138))  
    
    def teststringlit9(self):
        input = """ print(\"\\\\rollin\\' d0wn th3 h1ll of \\flowers\");"""
        expect = """print,(,\\\\rollin\\' d0wn th3 h1ll of \\flowers,),Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,139))  

    def teststringlit10(self):
        input = """ \"Let's play \\rollercoaster!\" """
        expect = """Let's play \\rollercoaster!,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,140))  
    
    def teststringlit11(self):
        input = """ \"a\\\\b\\'c\\bd\\f'\\\\a\" """
        expect = """a\\\\b\\'c\\bd\\f'\\\\a,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,141))  

    def teststringlit12(self):
        input = """ What if the string has multiple slashes like \"\\\\\\\\\\\\\\\"? """
        expect = """What,if,the,string,has,multiple,slashes,like,Illegal Escape In String: \\\\\\\\\\\\\\\""""
        self.assertTrue(TestLexer.test(input,expect,142))  
    
    def teststringlit13(self):
        input = """ What if the string has multiple escape sequences like \"\\b\\f\\r\\n\\t\\'\\\\'\"\"? """
        expect = """What,if,the,string,has,multiple,escape,sequences,like,\\b\\f\\r\\n\\t\\'\\\\'\",Error Token ?"""
        self.assertTrue(TestLexer.test(input,expect,143))  

    def teststringlit14(self):
        input = """ Lets test with some symbols \"\\b\\f@\\''\""""
        expect = """Lets,test,with,some,symbols,Unclosed String: \\b\\f@\\''\""""
        self.assertTrue(TestLexer.test(input,expect,144))  

    def teststringlit15(self):
        input = """ Lets test with some symbols \"$$!=()\\f\\'\\\\\""""
        expect = """Lets,test,with,some,symbols,$$!=()\\f\\'\\\\,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,145))  

    def teststringlit16(self):
        input = """ Lets test with some symbols: \"%%##@@!!\\\\\""""
        expect = """Lets,test,with,some,symbols,Error Token :"""
        self.assertTrue(TestLexer.test(input,expect,146))  
    
    def teststringlit17(self):
        input = """ Enough with hard tests, lets try a simple one \"hello, my name is '\"Sky'\" @\\\\__/@, that's how people call me! @\\__/@\""""
        expect = """Enough,with,hard,tests,,,lets,try,a,simple,one,Illegal Escape In String: hello, my name is '\"Sky'\" @\\\\__/@, that's how people call me! @\\_"""
        self.assertTrue(TestLexer.test(input,expect,147))  

    def teststringlit18(self):
        input = """ \"my email is '\"huy.nguyen229@hcmut.edu.vn'\"\"!"""
        expect = """my email is '\"huy.nguyen229@hcmut.edu.vn'\",Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,148))  

    def teststringlit19(self):
        input = """ Here is a string \"[string\\t\\b'"]\", but is this one \"\" a string too?"""
        expect = """Here,is,a,string,[string\\t\\b'"],,,but,is,this,one,,a,string,too,Error Token ?"""
        self.assertTrue(TestLexer.test(input,expect,149)) 

    def teststringlit20(self):
        input = """ \"oopsie, I forgot to close the string @__@ '\""""
        expect = """Unclosed String: oopsie, I forgot to close the string @__@ '\""""
        self.assertTrue(TestLexer.test(input,expect,150)) 

    ############# GENERAL TESTCASES #############
    
    def testgeneral1(self):
        input = """ lets work with some keywords like true, false, while, if, else,...!"""
        expect = """lets,work,with,some,keywords,like,true,,,false,,,while,,,if,,,else,,,...,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,151)) 

    def testgeneral2(self):
        input = """ How about lots of comma,,,,,,? """
        expect = """How,about,lots,of,comma,,,,,,,,,,,,,Error Token ?"""
        self.assertTrue(TestLexer.test(input,expect,152)) 

    def testgeneral3(self):
        input = """A
        
        
        """
        expect = "A,\n,\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expect,153)) 

    def testgeneral4(self):
        input = """ Love <3 You So Much <3"""
        expect = """Love,<,3,You,So,Much,<,3,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,154))

    def testgeneral5(self):
        input = """ 1 4M 4N 1D10T S4NDW1CH!!! """
        expect = """1,4,M,4,N,1,D10T,S4NDW1CH,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,155))  

    def testgeneral6(self):
        input = """ Yesterday, she told me \"1 would like to go sk11ng <3\" but I'm broke """
        expect = """Yesterday,,,she,told,me,1 would like to go sk11ng <3,but,I,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,156))  

    def testgeneral7(self):
        input = """ \"Managing the escape sequences such as '\",\\b,\\t,\\r is no easy task!"""
        expect = """Unclosed String: Managing the escape sequences such as '\",\\b,\\t,\\r is no easy task!"""
        self.assertTrue(TestLexer.test(input,expect,157))  

    def testgeneral8(self):
        input = """ \"Managing the escape sequences such as '\",\\b,\\t,\\r is no easy task!"""
        expect = """Unclosed String: Managing the escape sequences such as '\",\\b,\\t,\\r is no easy task!"""
        self.assertTrue(TestLexer.test(input,expect,158))  

    def testgeneral9(self):
        input = """ There is a train IIIIIIIIII[     ]-[     ]-[     ]-[     ]IIIIIIIIIIII@"""
        expect = """There,is,a,train,IIIIIIIIII,[,],-,[,],-,[,],-,[,],IIIIIIIIIIII,Error Token @"""
        self.assertTrue(TestLexer.test(input,expect,159))  

    def testgeneral10(self):
        input = """ The teachers told me \"If you want to include the character '\" in the string, remember to add a single quotation mark before it like this \\''\"\""""
        expect = """The,teachers,told,me,If you want to include the character '\" in the string, remember to add a single quotation mark before it like this \\''\",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,160))  

    def testgeneral11(self):
        input = """ This is how to draw the smiley face \":-)\", and this is how to draw the sad face \":-\\\""""
        expect = """This,is,how,to,draw,the,smiley,face,:-),,,and,this,is,how,to,draw,the,sad,face,Illegal Escape In String: :-\\\""""
        self.assertTrue(TestLexer.test(input,expect,161))  

    def testgeneral12(self):
        input = """ ID[\"2I52591\" + \"sky\"] """
        expect = """ID,[,2I52591,+,sky,],<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,162))  

    def testgeneral13(self):
        input = """ One wiseman once said \"the more ch@r@ct3rs there are, the harder mathematics is'\"..."""
        expect = """One,wiseman,once,said,Unclosed String: the more ch@r@ct3rs there are, the harder mathematics is'\"..."""
        self.assertTrue(TestLexer.test(input,expect,163))  

    def testgeneral14(self):
        input = """ I wonder why, I wonder how?..."""
        expect = """I,wonder,why,,,I,wonder,how,Error Token ?"""
        self.assertTrue(TestLexer.test(input,expect,164))  

    def testgeneral15(self):
        input = """ \"Life is hard\", it is all about > $$$ <"""
        expect = """Life is hard,,,it,is,all,about,>,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,165)) 

    def testgeneral16(self):
        input = """ Mom said \"I used to be called '\"The Empress\" cause I was too beautiful \""""
        expect = """Mom,said,I used to be called '\"The Empress,cause,I,was,too,beautiful,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,166)) 

    def testgeneral17(self):
        input = """ Dad replied \" Isn't it because you were always too hard on your exes?\". Someone will not have dinner to day, I'm sure about that!"""
        expect = """Dad,replied, Isn't it because you were always too hard on your exes?,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,167)) 
        
    def testgeneral18(self):
        input = """ \"Good afternoon,\\n, your bank account has \\b 12.5 cents left"""
        expect = """Unclosed String: Good afternoon,\\n, your bank account has \\b 12.5 cents left"""
        self.assertTrue(TestLexer.test(input,expect,168)) 

    def testgeneral19(self):
        input = """ He said \"The meter went up to 67.0e-4; \\n if it reachs 70.0e-3, it will \\\\kaboom!!!/'\""""
        expect = """He,said,Unclosed String: The meter went up to 67.0e-4; \\n if it reachs 70.0e-3, it will \\\\kaboom!!!/'\""""
        self.assertTrue(TestLexer.test(input,expect,169)) 

    def testgeneral20(self):
        input = """ There are 70 testcases already, which means only 30 to go!"""
        expect = """There,are,70,testcases,already,,,which,means,only,30,to,go,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,170)) 

    def testgeneral21(self):
        input = """ var<-[[1,2,3],[4,5,6],[7,8,9]];"""
        expect = """var,<-,[,[,1,,,2,,,3,],,,[,4,,,5,,,6,],,,[,7,,,8,,,9,],],Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,171)) 

    def testgeneral22(self):
        input = """\"string\" + \"string\\b\\'\" == \"stringstring\\b\\'"""
        expect = """string,+,string\\b\\',==,Unclosed String: stringstring\\b\\'"""
        self.assertTrue(TestLexer.test(input,expect,172)) 
    
    def testgeneral23(self):
        input = """ \"it is raining so hard ////\\'////\\'////\\\\\\\""""
        expect = """Illegal Escape In String: it is raining so hard ////\\'////\\'////\\\\\\\""""
        self.assertTrue(TestLexer.test(input,expect,173)) 

    def testgeneral24(self):
        input = """ \"How is this possible?!\", said the boy, shaking in the corner of the room.."""
        expect = """How is this possible?!,,,said,the,boy,,,shaking,in,the,corner,of,the,room,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,174)) 

    def testgeneral25(self):
        input = """ string a <- \"who's that pokemon?\""""
        expect = """string,a,<-,who's that pokemon?,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,175)) 
    
    def testgeneral26(self):
        input = """ \"\\b\"...\"\\f\"...\"\\n\"...\"\\r\"...\"\\t\"...\"\\\\\"...\"'\"\"...\"\"...this's the end."""
        expect = """\\b,...,\\f,...,\\n,...,\\r,...,\\t,...,\\\\,...,'\",...,,...,this,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,176)) 

    def testgeneral27(self):
        input = """ 3.E+3[a[3.4,5],b[1,a2,\"\\'\"],\"'\"]"""
        expect = """3.E+3,[,a,[,3.4,,,5,],,,b,[,1,,,a2,,,\\',],,,Unclosed String: '\"]"""
        self.assertTrue(TestLexer.test(input,expect,177)) 

    def testgeneral28(self):
        input = """\"broker1: stopped\", \"broker2: stopped at '\"22:00UTC-7'\"\", err@r not found"""
        expect = """broker1: stopped,,,broker2: stopped at '\"22:00UTC-7'\",,,err,Error Token @"""
        self.assertTrue(TestLexer.test(input,expect,178)) 

    def testgeneral29(self):
        input = """(Facebook) and [Tiktok] are the two most famou$ social medias"""
        expect = """(,Facebook,),and,[,Tiktok,],are,the,two,most,famou,Error Token $"""
        self.assertTrue(TestLexer.test(input,expect,179)) 

    def testgeneral30(self):
        input = """\"I am thinking about @#$%^&*(\'")\\;\""""
        expect = """Illegal Escape In String: I am thinking about @#$%^&*(\'")\\;"""
        self.assertTrue(TestLexer.test(input,expect,180)) 

    def testgeneral31(self):
        input = """Between 3e-14 a\nnd 3.8E-10, which one is smaller?"""
        expect = """Between,3e-14,a,\n,nd,3.8E-10,,,which,one,is,smaller,Error Token ?"""
        self.assertTrue(TestLexer.test(input,expect,181)) 

    def testgeneral32(self):
        input = """array alpha[5,6,7]<-[[1,2,3],[5e-45,6.12345E-10,70.],true,true,\"what am I to you? \\n\"];"""
        expect = """array,alpha,[,5,,,6,,,7,],<-,[,[,1,,,2,,,3,],,,[,5e-45,,,6.12345E-10,,,70.,],,,true,,,true,,,what am I to you? \\n,],Error Token ;"""
        self.assertTrue(TestLexer.test(input,expect,182)) 

    def testgeneral33(self):
        input = """bool boolean1 <- string2...string3 <= string3...string4...string5"""
        expect = """bool,boolean1,<-,string2,...,string3,<=,string3,...,string4,...,string5,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,183)) 

    def testgeneral34(self):
        input = """\"FAKER, WHAT \\t WAS \\t THATTTTTTTTTT ?!\", said the commentator during the match."""
        expect = """FAKER, WHAT \\t WAS \\t THATTTTTTTTTT ?!,,,said,the,commentator,during,the,match,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,184)) 

    def testgeneral35(self):
        input = """\"One teacher once said '\"Are you sure that 1+1 equals to 2?'\""""
        expect = """Unclosed String: One teacher once said '\"Are you sure that 1+1 equals to 2?'\""""
        self.assertTrue(TestLexer.test(input,expect,185)) 

    def testgeneral36(self):
        input = """Night+Rainy+No deadline==Perfect!"""
        expect = """Night,+,Rainy,+,No,deadline,==,Perfect,Error Token !"""
        self.assertTrue(TestLexer.test(input,expect,186)) 

    def testgeneral37(self):
        input = """\"Do you use '\"Thre@d?'\"\", my girlfriend asked me, but I have no idea what is \"Thre@d\""""
        expect = """Do you use '\"Thre@d?'\",,,my,girlfriend,asked,me,,,but,I,have,no,idea,what,is,Thre@d,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,187)) 

    def testgeneral38(self):
        input = """The <EOF> sign is for marking the end of the testcase, in case there is no Error Token."""
        expect = """The,<,EOF,>,sign,is,for,marking,the,end,of,the,testcase,,,in,case,there,is,no,Error,Token,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,188)) 

    def testgeneral39(self):
        input = """When you encounter an \"3rr0r\", you should \"R4Is3 the 3rr0r\" with the preset message"""
        expect = """When,you,encounter,an,3rr0r,,,you,should,R4Is3 the 3rr0r,with,the,preset,message,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,189)) 

    def testgeneral40(self):
        input = """f\nor,whi\nle,fu\nnc,dyna\nmic,i\nf,bo\n\nol,num\n\nber,el\n\n\nif"""
        expect = """f,\n,or,,,whi,\n,le,,,fu,\n,nc,,,dyna,\n,mic,,,i,\n,f,,,bo,\n,\n,ol,,,num,\n,\n,ber,,,el,\n,\n,\n,if,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,190)) 

    def testgeneral41(self):
        input = """\"Fill the string with escapes like '\"\\\\,\\t,\\b,\\f,\\''\" is likely to lead to errors\""""
        expect = """Fill the string with escapes like '\"\\\\,\\t,\\b,\\f,\\''\" is likely to lead to errors,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,191)) 

    def testgeneral42(self):
        input = """\"The teacher told me to \"try my best\" in the competition, so I should not upset him!\""""
        expect = """The teacher told me to ,try,my,best, in the competition, so I should not upset him!,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,192)) 

    def testgeneral43(self):
        input = """I do not know how should I behave when I am in front of [[[her]]]...."""
        expect = """I,do,not,know,how,should,I,behave,when,I,am,in,front,of,[,[,[,her,],],],...,Error Token ."""
        self.assertTrue(TestLexer.test(input,expect,193)) 

    def testgeneral44(self):
        input = """\"'\"Do you want to go out with me?'\" \\n '\"hell no'\"\", that's kinda sad"""
        expect = """'\"Do you want to go out with me?'\" \\n '\"hell no'\",,,that,Error Token '"""
        self.assertTrue(TestLexer.test(input,expect,194)) 

    def testgeneral45(self):
        input = """My mother told me \"Don\\'t close the door when you go out!"""
        expect = """My,mother,told,me,Unclosed String: Don\\'t close the door when you go out!"""
        self.assertTrue(TestLexer.test(input,expect,195)) 

    def testgeneral46(self):
        input = """[[4pm]],[[22 degree celcius]],[[height 22000m]],[[before impact: 20seconds]]"""
        expect = """[,[,4,pm,],],,,[,[,22,degree,celcius,],],,,[,[,height,22000,m,],],,,[,[,before,impact,Error Token :"""
        self.assertTrue(TestLexer.test(input,expect,196)) 

    def testgeneral47(self):
        input = """my favorite anime is \"\\t NAR
        UTO \\t\", you should try it out!"""
        expect = """my,favorite,anime,is,Unclosed String: \\t NAR"""
        self.assertTrue(TestLexer.test(input,expect,197)) 

    def testgeneral48(self):
        input = """arr[3,4,5]<-(for arr[i] < 0 until i>0)[[3,4,5]]"""
        expect = """arr,[,3,,,4,,,5,],<-,(,for,arr,[,i,],<,0,until,i,>,0,),[,[,3,,,4,,,5,],],<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,198)) 

    def testgeneral49(self):
        input = """\"\"abc\"\"abc\"\",\"\"\"\"\"\"\""""
        expect = """,abc,,abc,,,,,,,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect,199)) 

    def testgeneral50(self):
        input = """\"\"Finally, we reached the end\"\",SkySky"""
        expect = """,Finally,,,we,reached,the,end,,,,SkySky,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect,200)) 