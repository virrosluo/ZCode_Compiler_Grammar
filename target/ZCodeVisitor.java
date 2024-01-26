// Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link ZCodeParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface ZCodeVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(ZCodeParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration(ZCodeParser.DeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#variable_stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVariable_stat(ZCodeParser.Variable_statContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#dtype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDtype(ZCodeParser.DtypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#explicit_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExplicit_declare(ZCodeParser.Explicit_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#idlist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdlist(ZCodeParser.IdlistContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#primitive_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitive_declare(ZCodeParser.Primitive_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#array_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_declare(ZCodeParser.Array_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#implicit_declare}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImplicit_declare(ZCodeParser.Implicit_declareContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#function_stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_stat(ZCodeParser.Function_statContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#function_definition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_definition(ZCodeParser.Function_definitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#function_declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_declaration(ZCodeParser.Function_declarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#param_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam_list(ZCodeParser.Param_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(ZCodeParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#block_stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock_stat(ZCodeParser.Block_statContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(ZCodeParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#comment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComment(ZCodeParser.CommentContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(ZCodeParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#relation_operation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelation_operation(ZCodeParser.Relation_operationContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#relational_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelational_expr(ZCodeParser.Relational_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#logical_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogical_expr(ZCodeParser.Logical_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#adding_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdding_expr(ZCodeParser.Adding_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#multiplying_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplying_expr(ZCodeParser.Multiplying_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#not_logical}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNot_logical(ZCodeParser.Not_logicalContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#sign_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSign_expr(ZCodeParser.Sign_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#index_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndex_expr(ZCodeParser.Index_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#parenthesis_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenthesis_expr(ZCodeParser.Parenthesis_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#term}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTerm(ZCodeParser.TermContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#array_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_expr(ZCodeParser.Array_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#function_expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction_expr(ZCodeParser.Function_exprContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#ifst_component}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfst_component(ZCodeParser.Ifst_componentContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#control_stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitControl_stat(ZCodeParser.Control_statContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#loop_stat}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoop_stat(ZCodeParser.Loop_statContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#loop_body_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoop_body_statement(ZCodeParser.Loop_body_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#assignment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignment(ZCodeParser.AssignmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#lhs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs(ZCodeParser.LhsContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#index_variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndex_variable(ZCodeParser.Index_variableContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#parenthesis_variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenthesis_variable(ZCodeParser.Parenthesis_variableContext ctx);
	/**
	 * Visit a parse tree produced by {@link ZCodeParser#lhs_variable}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs_variable(ZCodeParser.Lhs_variableContext ctx);
}