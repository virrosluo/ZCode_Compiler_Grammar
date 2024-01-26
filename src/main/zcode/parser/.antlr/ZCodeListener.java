// Generated from d://antlr4//sample//Assignment1//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ZCodeParser}.
 */
public interface ZCodeListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(ZCodeParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(ZCodeParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#variable_stat}.
	 * @param ctx the parse tree
	 */
	void enterVariable_stat(ZCodeParser.Variable_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#variable_stat}.
	 * @param ctx the parse tree
	 */
	void exitVariable_stat(ZCodeParser.Variable_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#dtype}.
	 * @param ctx the parse tree
	 */
	void enterDtype(ZCodeParser.DtypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#dtype}.
	 * @param ctx the parse tree
	 */
	void exitDtype(ZCodeParser.DtypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#explicit_declare}.
	 * @param ctx the parse tree
	 */
	void enterExplicit_declare(ZCodeParser.Explicit_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#explicit_declare}.
	 * @param ctx the parse tree
	 */
	void exitExplicit_declare(ZCodeParser.Explicit_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#idlist}.
	 * @param ctx the parse tree
	 */
	void enterIdlist(ZCodeParser.IdlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#idlist}.
	 * @param ctx the parse tree
	 */
	void exitIdlist(ZCodeParser.IdlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#primitive_declare}.
	 * @param ctx the parse tree
	 */
	void enterPrimitive_declare(ZCodeParser.Primitive_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#primitive_declare}.
	 * @param ctx the parse tree
	 */
	void exitPrimitive_declare(ZCodeParser.Primitive_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_declare}.
	 * @param ctx the parse tree
	 */
	void enterArray_declare(ZCodeParser.Array_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_declare}.
	 * @param ctx the parse tree
	 */
	void exitArray_declare(ZCodeParser.Array_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#implicit_declare}.
	 * @param ctx the parse tree
	 */
	void enterImplicit_declare(ZCodeParser.Implicit_declareContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#implicit_declare}.
	 * @param ctx the parse tree
	 */
	void exitImplicit_declare(ZCodeParser.Implicit_declareContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_stat}.
	 * @param ctx the parse tree
	 */
	void enterFunction_stat(ZCodeParser.Function_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_stat}.
	 * @param ctx the parse tree
	 */
	void exitFunction_stat(ZCodeParser.Function_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void enterFunction_definition(ZCodeParser.Function_definitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_definition}.
	 * @param ctx the parse tree
	 */
	void exitFunction_definition(ZCodeParser.Function_definitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void enterFunction_declaration(ZCodeParser.Function_declarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_declaration}.
	 * @param ctx the parse tree
	 */
	void exitFunction_declaration(ZCodeParser.Function_declarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 */
	void enterParam_list(ZCodeParser.Param_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 */
	void exitParam_list(ZCodeParser.Param_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(ZCodeParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(ZCodeParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#block_stat}.
	 * @param ctx the parse tree
	 */
	void enterBlock_stat(ZCodeParser.Block_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#block_stat}.
	 * @param ctx the parse tree
	 */
	void exitBlock_stat(ZCodeParser.Block_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#comment}.
	 * @param ctx the parse tree
	 */
	void enterComment(ZCodeParser.CommentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#comment}.
	 * @param ctx the parse tree
	 */
	void exitComment(ZCodeParser.CommentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ZCodeParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ZCodeParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#relation_operation}.
	 * @param ctx the parse tree
	 */
	void enterRelation_operation(ZCodeParser.Relation_operationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#relation_operation}.
	 * @param ctx the parse tree
	 */
	void exitRelation_operation(ZCodeParser.Relation_operationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#relational_expr}.
	 * @param ctx the parse tree
	 */
	void enterRelational_expr(ZCodeParser.Relational_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#relational_expr}.
	 * @param ctx the parse tree
	 */
	void exitRelational_expr(ZCodeParser.Relational_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#logical_expr}.
	 * @param ctx the parse tree
	 */
	void enterLogical_expr(ZCodeParser.Logical_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#logical_expr}.
	 * @param ctx the parse tree
	 */
	void exitLogical_expr(ZCodeParser.Logical_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#adding_expr}.
	 * @param ctx the parse tree
	 */
	void enterAdding_expr(ZCodeParser.Adding_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#adding_expr}.
	 * @param ctx the parse tree
	 */
	void exitAdding_expr(ZCodeParser.Adding_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#multiplying_expr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplying_expr(ZCodeParser.Multiplying_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#multiplying_expr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplying_expr(ZCodeParser.Multiplying_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#not_logical}.
	 * @param ctx the parse tree
	 */
	void enterNot_logical(ZCodeParser.Not_logicalContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#not_logical}.
	 * @param ctx the parse tree
	 */
	void exitNot_logical(ZCodeParser.Not_logicalContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#sign_expr}.
	 * @param ctx the parse tree
	 */
	void enterSign_expr(ZCodeParser.Sign_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#sign_expr}.
	 * @param ctx the parse tree
	 */
	void exitSign_expr(ZCodeParser.Sign_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#index_expr}.
	 * @param ctx the parse tree
	 */
	void enterIndex_expr(ZCodeParser.Index_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#index_expr}.
	 * @param ctx the parse tree
	 */
	void exitIndex_expr(ZCodeParser.Index_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#parenthesis_expr}.
	 * @param ctx the parse tree
	 */
	void enterParenthesis_expr(ZCodeParser.Parenthesis_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#parenthesis_expr}.
	 * @param ctx the parse tree
	 */
	void exitParenthesis_expr(ZCodeParser.Parenthesis_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(ZCodeParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(ZCodeParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#array_expr}.
	 * @param ctx the parse tree
	 */
	void enterArray_expr(ZCodeParser.Array_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#array_expr}.
	 * @param ctx the parse tree
	 */
	void exitArray_expr(ZCodeParser.Array_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#function_expr}.
	 * @param ctx the parse tree
	 */
	void enterFunction_expr(ZCodeParser.Function_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#function_expr}.
	 * @param ctx the parse tree
	 */
	void exitFunction_expr(ZCodeParser.Function_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#ifst_component}.
	 * @param ctx the parse tree
	 */
	void enterIfst_component(ZCodeParser.Ifst_componentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#ifst_component}.
	 * @param ctx the parse tree
	 */
	void exitIfst_component(ZCodeParser.Ifst_componentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#control_stat}.
	 * @param ctx the parse tree
	 */
	void enterControl_stat(ZCodeParser.Control_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#control_stat}.
	 * @param ctx the parse tree
	 */
	void exitControl_stat(ZCodeParser.Control_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#loop_stat}.
	 * @param ctx the parse tree
	 */
	void enterLoop_stat(ZCodeParser.Loop_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#loop_stat}.
	 * @param ctx the parse tree
	 */
	void exitLoop_stat(ZCodeParser.Loop_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#loop_body_statement}.
	 * @param ctx the parse tree
	 */
	void enterLoop_body_statement(ZCodeParser.Loop_body_statementContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#loop_body_statement}.
	 * @param ctx the parse tree
	 */
	void exitLoop_body_statement(ZCodeParser.Loop_body_statementContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(ZCodeParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(ZCodeParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(ZCodeParser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(ZCodeParser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#index_variable}.
	 * @param ctx the parse tree
	 */
	void enterIndex_variable(ZCodeParser.Index_variableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#index_variable}.
	 * @param ctx the parse tree
	 */
	void exitIndex_variable(ZCodeParser.Index_variableContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#parenthesis_variable}.
	 * @param ctx the parse tree
	 */
	void enterParenthesis_variable(ZCodeParser.Parenthesis_variableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#parenthesis_variable}.
	 * @param ctx the parse tree
	 */
	void exitParenthesis_variable(ZCodeParser.Parenthesis_variableContext ctx);
	/**
	 * Enter a parse tree produced by {@link ZCodeParser#lhs_variable}.
	 * @param ctx the parse tree
	 */
	void enterLhs_variable(ZCodeParser.Lhs_variableContext ctx);
	/**
	 * Exit a parse tree produced by {@link ZCodeParser#lhs_variable}.
	 * @param ctx the parse tree
	 */
	void exitLhs_variable(ZCodeParser.Lhs_variableContext ctx);
}