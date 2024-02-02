# Generated from d://antlr4//sample//Assignment1//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decllist.
    def enterDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decllist.
    def exitDecllist(self, ctx:ZCodeParser.DecllistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statlist.
    def enterStatlist(self, ctx:ZCodeParser.StatlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statlist.
    def exitStatlist(self, ctx:ZCodeParser.StatlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statmnt.
    def enterStatmnt(self, ctx:ZCodeParser.StatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statmnt.
    def exitStatmnt(self, ctx:ZCodeParser.StatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#declstatmnt.
    def enterDeclstatmnt(self, ctx:ZCodeParser.DeclstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#declstatmnt.
    def exitDeclstatmnt(self, ctx:ZCodeParser.DeclstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vardecl.
    def enterVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vardecl.
    def exitVardecl(self, ctx:ZCodeParser.VardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#keyvardecl.
    def enterKeyvardecl(self, ctx:ZCodeParser.KeyvardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#keyvardecl.
    def exitKeyvardecl(self, ctx:ZCodeParser.KeyvardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dynamicdecl.
    def enterDynamicdecl(self, ctx:ZCodeParser.DynamicdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dynamicdecl.
    def exitDynamicdecl(self, ctx:ZCodeParser.DynamicdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#singledecl.
    def enterSingledecl(self, ctx:ZCodeParser.SingledeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#singledecl.
    def exitSingledecl(self, ctx:ZCodeParser.SingledeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#singlevardecl.
    def enterSinglevardecl(self, ctx:ZCodeParser.SinglevardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#singlevardecl.
    def exitSinglevardecl(self, ctx:ZCodeParser.SinglevardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arraydecl.
    def enterArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arraydecl.
    def exitArraydecl(self, ctx:ZCodeParser.ArraydeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayid.
    def enterArrayid(self, ctx:ZCodeParser.ArrayidContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayid.
    def exitArrayid(self, ctx:ZCodeParser.ArrayidContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arraydim.
    def enterArraydim(self, ctx:ZCodeParser.ArraydimContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arraydim.
    def exitArraydim(self, ctx:ZCodeParser.ArraydimContext):
        pass


    # Enter a parse tree produced by ZCodeParser#listdim.
    def enterListdim(self, ctx:ZCodeParser.ListdimContext):
        pass

    # Exit a parse tree produced by ZCodeParser#listdim.
    def exitListdim(self, ctx:ZCodeParser.ListdimContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arrayvalue.
    def enterArrayvalue(self, ctx:ZCodeParser.ArrayvalueContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arrayvalue.
    def exitArrayvalue(self, ctx:ZCodeParser.ArrayvalueContext):
        pass


    # Enter a parse tree produced by ZCodeParser#itemlist.
    def enterItemlist(self, ctx:ZCodeParser.ItemlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#itemlist.
    def exitItemlist(self, ctx:ZCodeParser.ItemlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#item.
    def enterItem(self, ctx:ZCodeParser.ItemContext):
        pass

    # Exit a parse tree produced by ZCodeParser#item.
    def exitItem(self, ctx:ZCodeParser.ItemContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funcdecl.
    def enterFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funcdecl.
    def exitFuncdecl(self, ctx:ZCodeParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#tempfuncdecl.
    def enterTempfuncdecl(self, ctx:ZCodeParser.TempfuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#tempfuncdecl.
    def exitTempfuncdecl(self, ctx:ZCodeParser.TempfuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#realfuncdecl.
    def enterRealfuncdecl(self, ctx:ZCodeParser.RealfuncdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#realfuncdecl.
    def exitRealfuncdecl(self, ctx:ZCodeParser.RealfuncdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramdecl.
    def enterParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramdecl.
    def exitParamdecl(self, ctx:ZCodeParser.ParamdeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramprime.
    def enterParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramprime.
    def exitParamprime(self, ctx:ZCodeParser.ParamprimeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramlist.
    def enterParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramlist.
    def exitParamlist(self, ctx:ZCodeParser.ParamlistContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#body.
    def enterBody(self, ctx:ZCodeParser.BodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#body.
    def exitBody(self, ctx:ZCodeParser.BodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstatmnt.
    def enterAssignstatmnt(self, ctx:ZCodeParser.AssignstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstatmnt.
    def exitAssignstatmnt(self, ctx:ZCodeParser.AssignstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifstatmnt.
    def enterIfstatmnt(self, ctx:ZCodeParser.IfstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifstatmnt.
    def exitIfstatmnt(self, ctx:ZCodeParser.IfstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_list.
    def enterElif_list(self, ctx:ZCodeParser.Elif_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_list.
    def exitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_stat.
    def enterElif_stat(self, ctx:ZCodeParser.Elif_statContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_stat.
    def exitElif_stat(self, ctx:ZCodeParser.Elif_statContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstatmnt.
    def enterForstatmnt(self, ctx:ZCodeParser.ForstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstatmnt.
    def exitForstatmnt(self, ctx:ZCodeParser.ForstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakstatmnt.
    def enterBreakstatmnt(self, ctx:ZCodeParser.BreakstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakstatmnt.
    def exitBreakstatmnt(self, ctx:ZCodeParser.BreakstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continuestatmnt.
    def enterContinuestatmnt(self, ctx:ZCodeParser.ContinuestatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continuestatmnt.
    def exitContinuestatmnt(self, ctx:ZCodeParser.ContinuestatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnstatmnt.
    def enterReturnstatmnt(self, ctx:ZCodeParser.ReturnstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnstatmnt.
    def exitReturnstatmnt(self, ctx:ZCodeParser.ReturnstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funccallstatmnt.
    def enterFunccallstatmnt(self, ctx:ZCodeParser.FunccallstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funccallstatmnt.
    def exitFunccallstatmnt(self, ctx:ZCodeParser.FunccallstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramprime_call.
    def enterParamprime_call(self, ctx:ZCodeParser.Paramprime_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramprime_call.
    def exitParamprime_call(self, ctx:ZCodeParser.Paramprime_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramlist_call.
    def enterParamlist_call(self, ctx:ZCodeParser.Paramlist_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramlist_call.
    def exitParamlist_call(self, ctx:ZCodeParser.Paramlist_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_call.
    def enterParam_call(self, ctx:ZCodeParser.Param_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_call.
    def exitParam_call(self, ctx:ZCodeParser.Param_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#funccall.
    def enterFunccall(self, ctx:ZCodeParser.FunccallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#funccall.
    def exitFunccall(self, ctx:ZCodeParser.FunccallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockstatmnt.
    def enterBlockstatmnt(self, ctx:ZCodeParser.BlockstatmntContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockstatmnt.
    def exitBlockstatmnt(self, ctx:ZCodeParser.BlockstatmntContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stringexp.
    def enterStringexp(self, ctx:ZCodeParser.StringexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stringexp.
    def exitStringexp(self, ctx:ZCodeParser.StringexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relationalexp.
    def enterRelationalexp(self, ctx:ZCodeParser.RelationalexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relationalexp.
    def exitRelationalexp(self, ctx:ZCodeParser.RelationalexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logicalexp.
    def enterLogicalexp(self, ctx:ZCodeParser.LogicalexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logicalexp.
    def exitLogicalexp(self, ctx:ZCodeParser.LogicalexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#addingexp.
    def enterAddingexp(self, ctx:ZCodeParser.AddingexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#addingexp.
    def exitAddingexp(self, ctx:ZCodeParser.AddingexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multiexp.
    def enterMultiexp(self, ctx:ZCodeParser.MultiexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multiexp.
    def exitMultiexp(self, ctx:ZCodeParser.MultiexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#notexp.
    def enterNotexp(self, ctx:ZCodeParser.NotexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#notexp.
    def exitNotexp(self, ctx:ZCodeParser.NotexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#subexp.
    def enterSubexp(self, ctx:ZCodeParser.SubexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#subexp.
    def exitSubexp(self, ctx:ZCodeParser.SubexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexp.
    def enterIndexp(self, ctx:ZCodeParser.IndexpContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexp.
    def exitIndexp(self, ctx:ZCodeParser.IndexpContext):
        pass


    # Enter a parse tree produced by ZCodeParser#operand.
    def enterOperand(self, ctx:ZCodeParser.OperandContext):
        pass

    # Exit a parse tree produced by ZCodeParser#operand.
    def exitOperand(self, ctx:ZCodeParser.OperandContext):
        pass


    # Enter a parse tree produced by ZCodeParser#typ.
    def enterTyp(self, ctx:ZCodeParser.TypContext):
        pass

    # Exit a parse tree produced by ZCodeParser#typ.
    def exitTyp(self, ctx:ZCodeParser.TypContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexepr.
    def enterIndexepr(self, ctx:ZCodeParser.IndexeprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexepr.
    def exitIndexepr(self, ctx:ZCodeParser.IndexeprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#exp_list.
    def enterExp_list(self, ctx:ZCodeParser.Exp_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#exp_list.
    def exitExp_list(self, ctx:ZCodeParser.Exp_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newlinelist_null.
    def enterNewlinelist_null(self, ctx:ZCodeParser.Newlinelist_nullContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newlinelist_null.
    def exitNewlinelist_null(self, ctx:ZCodeParser.Newlinelist_nullContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newlinelist.
    def enterNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newlinelist.
    def exitNewlinelist(self, ctx:ZCodeParser.NewlinelistContext):
        pass



del ZCodeParser