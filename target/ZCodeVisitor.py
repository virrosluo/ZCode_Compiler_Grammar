# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#declaration.
    def visitDeclaration(self, ctx:ZCodeParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#variable_stat.
    def visitVariable_stat(self, ctx:ZCodeParser.Variable_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dtype.
    def visitDtype(self, ctx:ZCodeParser.DtypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#explicit_declare.
    def visitExplicit_declare(self, ctx:ZCodeParser.Explicit_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#idlist.
    def visitIdlist(self, ctx:ZCodeParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primitive_declare.
    def visitPrimitive_declare(self, ctx:ZCodeParser.Primitive_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_declare.
    def visitArray_declare(self, ctx:ZCodeParser.Array_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_declare.
    def visitImplicit_declare(self, ctx:ZCodeParser.Implicit_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_stat.
    def visitFunction_stat(self, ctx:ZCodeParser.Function_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_definition.
    def visitFunction_definition(self, ctx:ZCodeParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_declaration.
    def visitFunction_declaration(self, ctx:ZCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stat.
    def visitBlock_stat(self, ctx:ZCodeParser.Block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#comment.
    def visitComment(self, ctx:ZCodeParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relation_operation.
    def visitRelation_operation(self, ctx:ZCodeParser.Relation_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_expr.
    def visitRelational_expr(self, ctx:ZCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logical_expr.
    def visitLogical_expr(self, ctx:ZCodeParser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#adding_expr.
    def visitAdding_expr(self, ctx:ZCodeParser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multiplying_expr.
    def visitMultiplying_expr(self, ctx:ZCodeParser.Multiplying_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#not_logical.
    def visitNot_logical(self, ctx:ZCodeParser.Not_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_expr.
    def visitIndex_expr(self, ctx:ZCodeParser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parenthesis_expr.
    def visitParenthesis_expr(self, ctx:ZCodeParser.Parenthesis_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#term.
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_expr.
    def visitArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_expr.
    def visitFunction_expr(self, ctx:ZCodeParser.Function_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifst_component.
    def visitIfst_component(self, ctx:ZCodeParser.Ifst_componentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#control_stat.
    def visitControl_stat(self, ctx:ZCodeParser.Control_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#loop_stat.
    def visitLoop_stat(self, ctx:ZCodeParser.Loop_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#loop_body_statement.
    def visitLoop_body_statement(self, ctx:ZCodeParser.Loop_body_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignment.
    def visitAssignment(self, ctx:ZCodeParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_variable.
    def visitIndex_variable(self, ctx:ZCodeParser.Index_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parenthesis_variable.
    def visitParenthesis_variable(self, ctx:ZCodeParser.Parenthesis_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs_variable.
    def visitLhs_variable(self, ctx:ZCodeParser.Lhs_variableContext):
        return self.visitChildren(ctx)



del ZCodeParser