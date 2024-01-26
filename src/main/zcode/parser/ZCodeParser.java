// Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ZCodeParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NUM_KEYWORD=1, BOOL_KEYWORD=2, STRING_KEYWORD=3, RETURN_KEYWORD=4, VAR_KEYWORD=5, 
		DYNAMIC_KEYWORD=6, FUNC_KEYWORD=7, FOR_KEYWORD=8, UNTIL_KEYWORD=9, BY_KEYWORD=10, 
		BREAK_KEYWORD=11, CONTINUE_KEYWORD=12, IF_KEYWORD=13, ELSE_KEYWORD=14, 
		ELIF_KEYWORD=15, BEGIN_KEYWORD=16, END_KEYWORD=17, ASSIGN_OP=18, ADD_OP=19, 
		SUB_OP=20, MUL_OP=21, DIV_OP=22, MOD_OP=23, NOT_OP=24, AND_OP=25, OR_OP=26, 
		EQUAL_OP=27, INEQUAL_OP=28, LESS_OP=29, LESSEQUAL_OP=30, LARGE_OP=31, 
		LARGEEQUAL_OP=32, CONCAT_OP=33, EQUAL_STR_OP=34, ID=35, LEFT_PARENTHESIS=36, 
		RIGHT_PARENTHESIS=37, LEFT_BRACKET=38, RIGHT_BRACKET=39, SEPARATOR_KEYWORD=40, 
		SEMICOLON_KEYWORD=41, TRUE_LIT=42, FALSE_LIT=43, INT_LIT=44, REAL_LIT=45, 
		STRING_LIT=46, WS=47, COMMENT_LINE=48, UNCLOSE_STRING=49, ILLEGAL_ESCAPE=50, 
		ERROR_TOKEN=51;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_variable_stat = 2, RULE_dtype = 3, 
		RULE_explicit_declare = 4, RULE_idlist = 5, RULE_primitive_declare = 6, 
		RULE_array_declare = 7, RULE_value_list = 8, RULE_implicit_declare = 9, 
		RULE_function_stat = 10, RULE_function_definition = 11, RULE_function_declaration = 12, 
		RULE_param_list = 13, RULE_parameter = 14, RULE_block_stat = 15, RULE_statement = 16, 
		RULE_expression = 17, RULE_relation_operation = 18, RULE_relational_expr = 19, 
		RULE_logical_expr = 20, RULE_adding_expr = 21, RULE_multiplying_expr = 22, 
		RULE_not_logical = 23, RULE_sign_expr = 24, RULE_index_expr = 25, RULE_index_value = 26, 
		RULE_parenthesis_expr = 27, RULE_term = 28, RULE_function_expr = 29, RULE_ifst_component = 30, 
		RULE_control_stat = 31, RULE_loop_stat = 32, RULE_loop_body_statement = 33, 
		RULE_assignment = 34;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "variable_stat", "dtype", "explicit_declare", 
			"idlist", "primitive_declare", "array_declare", "value_list", "implicit_declare", 
			"function_stat", "function_definition", "function_declaration", "param_list", 
			"parameter", "block_stat", "statement", "expression", "relation_operation", 
			"relational_expr", "logical_expr", "adding_expr", "multiplying_expr", 
			"not_logical", "sign_expr", "index_expr", "index_value", "parenthesis_expr", 
			"term", "function_expr", "ifst_component", "control_stat", "loop_stat", 
			"loop_body_statement", "assignment"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
			"'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", "'if'", 
			"'else'", "'elif'", "'begin'", "'end'", "'<-'", "'+'", "'-'", "'*'", 
			"'/'", "'%'", "'not'", "'and'", "'or'", "'='", "'!='", "'<'", "'<='", 
			"'>'", "'>='", "'...'", "'=='", null, "'('", "')'", "'['", "']'", "','", 
			"';'", "'true'", "'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "RETURN_KEYWORD", 
			"VAR_KEYWORD", "DYNAMIC_KEYWORD", "FUNC_KEYWORD", "FOR_KEYWORD", "UNTIL_KEYWORD", 
			"BY_KEYWORD", "BREAK_KEYWORD", "CONTINUE_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", 
			"ELIF_KEYWORD", "BEGIN_KEYWORD", "END_KEYWORD", "ASSIGN_OP", "ADD_OP", 
			"SUB_OP", "MUL_OP", "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", 
			"EQUAL_OP", "INEQUAL_OP", "LESS_OP", "LESSEQUAL_OP", "LARGE_OP", "LARGEEQUAL_OP", 
			"CONCAT_OP", "EQUAL_STR_OP", "ID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
			"LEFT_BRACKET", "RIGHT_BRACKET", "SEPARATOR_KEYWORD", "SEMICOLON_KEYWORD", 
			"TRUE_LIT", "FALSE_LIT", "INT_LIT", "REAL_LIT", "STRING_LIT", "WS", "COMMENT_LINE", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "ZCode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ZCodeParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ZCodeParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUM_KEYWORD) | (1L << BOOL_KEYWORD) | (1L << STRING_KEYWORD) | (1L << RETURN_KEYWORD) | (1L << VAR_KEYWORD) | (1L << DYNAMIC_KEYWORD) | (1L << FUNC_KEYWORD) | (1L << FOR_KEYWORD) | (1L << IF_KEYWORD) | (1L << BEGIN_KEYWORD) | (1L << SUB_OP) | (1L << NOT_OP) | (1L << ID) | (1L << LEFT_PARENTHESIS) | (1L << TRUE_LIT) | (1L << FALSE_LIT) | (1L << INT_LIT) | (1L << REAL_LIT) | (1L << STRING_LIT))) != 0)) {
				{
				{
				setState(70);
				declaration();
				}
				}
				setState(75);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(76);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public Variable_statContext variable_stat() {
			return getRuleContext(Variable_statContext.class,0);
		}
		public Block_statContext block_stat() {
			return getRuleContext(Block_statContext.class,0);
		}
		public Function_statContext function_stat() {
			return getRuleContext(Function_statContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitDeclaration(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(81);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				variable_stat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(79);
				block_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(80);
				function_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Variable_statContext extends ParserRuleContext {
		public Explicit_declareContext explicit_declare() {
			return getRuleContext(Explicit_declareContext.class,0);
		}
		public Implicit_declareContext implicit_declare() {
			return getRuleContext(Implicit_declareContext.class,0);
		}
		public Variable_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable_stat; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitVariable_stat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Variable_statContext variable_stat() throws RecognitionException {
		Variable_statContext _localctx = new Variable_statContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_variable_stat);
		try {
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_KEYWORD:
			case BOOL_KEYWORD:
			case STRING_KEYWORD:
				enterOuterAlt(_localctx, 1);
				{
				setState(83);
				explicit_declare();
				}
				break;
			case VAR_KEYWORD:
			case DYNAMIC_KEYWORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(84);
				implicit_declare();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DtypeContext extends ParserRuleContext {
		public TerminalNode NUM_KEYWORD() { return getToken(ZCodeParser.NUM_KEYWORD, 0); }
		public TerminalNode BOOL_KEYWORD() { return getToken(ZCodeParser.BOOL_KEYWORD, 0); }
		public TerminalNode STRING_KEYWORD() { return getToken(ZCodeParser.STRING_KEYWORD, 0); }
		public DtypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dtype; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitDtype(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DtypeContext dtype() throws RecognitionException {
		DtypeContext _localctx = new DtypeContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_dtype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUM_KEYWORD) | (1L << BOOL_KEYWORD) | (1L << STRING_KEYWORD))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Explicit_declareContext extends ParserRuleContext {
		public Array_declareContext array_declare() {
			return getRuleContext(Array_declareContext.class,0);
		}
		public Primitive_declareContext primitive_declare() {
			return getRuleContext(Primitive_declareContext.class,0);
		}
		public Explicit_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_explicit_declare; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitExplicit_declare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Explicit_declareContext explicit_declare() throws RecognitionException {
		Explicit_declareContext _localctx = new Explicit_declareContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_explicit_declare);
		try {
			setState(91);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				array_declare();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(90);
				primitive_declare();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IdlistContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(ZCodeParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(ZCodeParser.ID, i);
		}
		public List<TerminalNode> SEPARATOR_KEYWORD() { return getTokens(ZCodeParser.SEPARATOR_KEYWORD); }
		public TerminalNode SEPARATOR_KEYWORD(int i) {
			return getToken(ZCodeParser.SEPARATOR_KEYWORD, i);
		}
		public IdlistContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idlist; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitIdlist(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdlistContext idlist() throws RecognitionException {
		IdlistContext _localctx = new IdlistContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_idlist);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(ID);
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEPARATOR_KEYWORD) {
				{
				{
				setState(94);
				match(SEPARATOR_KEYWORD);
				setState(95);
				match(ID);
				}
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Primitive_declareContext extends ParserRuleContext {
		public DtypeContext dtype() {
			return getRuleContext(DtypeContext.class,0);
		}
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode ASSIGN_OP() { return getToken(ZCodeParser.ASSIGN_OP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Primitive_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitive_declare; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitPrimitive_declare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Primitive_declareContext primitive_declare() throws RecognitionException {
		Primitive_declareContext _localctx = new Primitive_declareContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_primitive_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			dtype();
			setState(102);
			idlist();
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN_OP) {
				{
				setState(103);
				match(ASSIGN_OP);
				setState(104);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_declareContext extends ParserRuleContext {
		public DtypeContext dtype() {
			return getRuleContext(DtypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public List<TerminalNode> LEFT_BRACKET() { return getTokens(ZCodeParser.LEFT_BRACKET); }
		public TerminalNode LEFT_BRACKET(int i) {
			return getToken(ZCodeParser.LEFT_BRACKET, i);
		}
		public List<TerminalNode> INT_LIT() { return getTokens(ZCodeParser.INT_LIT); }
		public TerminalNode INT_LIT(int i) {
			return getToken(ZCodeParser.INT_LIT, i);
		}
		public List<TerminalNode> RIGHT_BRACKET() { return getTokens(ZCodeParser.RIGHT_BRACKET); }
		public TerminalNode RIGHT_BRACKET(int i) {
			return getToken(ZCodeParser.RIGHT_BRACKET, i);
		}
		public List<TerminalNode> SEPARATOR_KEYWORD() { return getTokens(ZCodeParser.SEPARATOR_KEYWORD); }
		public TerminalNode SEPARATOR_KEYWORD(int i) {
			return getToken(ZCodeParser.SEPARATOR_KEYWORD, i);
		}
		public TerminalNode ASSIGN_OP() { return getToken(ZCodeParser.ASSIGN_OP, 0); }
		public Value_listContext value_list() {
			return getRuleContext(Value_listContext.class,0);
		}
		public Array_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_declare; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitArray_declare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_declareContext array_declare() throws RecognitionException {
		Array_declareContext _localctx = new Array_declareContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_array_declare);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			dtype();
			setState(108);
			match(ID);
			setState(109);
			match(LEFT_BRACKET);
			setState(110);
			match(INT_LIT);
			setState(115);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEPARATOR_KEYWORD) {
				{
				{
				setState(111);
				match(SEPARATOR_KEYWORD);
				setState(112);
				match(INT_LIT);
				}
				}
				setState(117);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(118);
			match(RIGHT_BRACKET);
			setState(124);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGN_OP) {
				{
				setState(119);
				match(ASSIGN_OP);
				setState(120);
				match(LEFT_BRACKET);
				setState(121);
				value_list();
				setState(122);
				match(RIGHT_BRACKET);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Value_listContext extends ParserRuleContext {
		public TerminalNode LEFT_BRACKET() { return getToken(ZCodeParser.LEFT_BRACKET, 0); }
		public List<Value_listContext> value_list() {
			return getRuleContexts(Value_listContext.class);
		}
		public Value_listContext value_list(int i) {
			return getRuleContext(Value_listContext.class,i);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(ZCodeParser.RIGHT_BRACKET, 0); }
		public List<TerminalNode> SEPARATOR_KEYWORD() { return getTokens(ZCodeParser.SEPARATOR_KEYWORD); }
		public TerminalNode SEPARATOR_KEYWORD(int i) {
			return getToken(ZCodeParser.SEPARATOR_KEYWORD, i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Value_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitValue_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Value_listContext value_list() throws RecognitionException {
		Value_listContext _localctx = new Value_listContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_value_list);
		try {
			int _alt;
			setState(144);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_BRACKET:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				match(LEFT_BRACKET);
				setState(127);
				value_list();
				setState(128);
				match(RIGHT_BRACKET);
				setState(133);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(129);
						match(SEPARATOR_KEYWORD);
						setState(130);
						value_list();
						}
						} 
					}
					setState(135);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
				}
				}
				break;
			case SUB_OP:
			case NOT_OP:
			case ID:
			case LEFT_PARENTHESIS:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				expression();
				setState(141);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(137);
						match(SEPARATOR_KEYWORD);
						setState(138);
						value_list();
						}
						} 
					}
					setState(143);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,9,_ctx);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Implicit_declareContext extends ParserRuleContext {
		public TerminalNode VAR_KEYWORD() { return getToken(ZCodeParser.VAR_KEYWORD, 0); }
		public IdlistContext idlist() {
			return getRuleContext(IdlistContext.class,0);
		}
		public TerminalNode ASSIGN_OP() { return getToken(ZCodeParser.ASSIGN_OP, 0); }
		public List<Value_listContext> value_list() {
			return getRuleContexts(Value_listContext.class);
		}
		public Value_listContext value_list(int i) {
			return getRuleContext(Value_listContext.class,i);
		}
		public TerminalNode DYNAMIC_KEYWORD() { return getToken(ZCodeParser.DYNAMIC_KEYWORD, 0); }
		public Implicit_declareContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_implicit_declare; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitImplicit_declare(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Implicit_declareContext implicit_declare() throws RecognitionException {
		Implicit_declareContext _localctx = new Implicit_declareContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_implicit_declare);
		int _la;
		try {
			int _alt;
			setState(164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR_KEYWORD:
				enterOuterAlt(_localctx, 1);
				{
				setState(146);
				match(VAR_KEYWORD);
				setState(147);
				idlist();
				setState(148);
				match(ASSIGN_OP);
				setState(150); 
				_errHandler.sync(this);
				_alt = 1;
				do {
					switch (_alt) {
					case 1:
						{
						{
						setState(149);
						value_list();
						}
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(152); 
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
				} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
				}
				break;
			case DYNAMIC_KEYWORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(154);
				match(DYNAMIC_KEYWORD);
				setState(155);
				idlist();
				setState(162);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGN_OP) {
					{
					setState(156);
					match(ASSIGN_OP);
					setState(158); 
					_errHandler.sync(this);
					_alt = 1;
					do {
						switch (_alt) {
						case 1:
							{
							{
							setState(157);
							value_list();
							}
							}
							break;
						default:
							throw new NoViableAltException(this);
						}
						setState(160); 
						_errHandler.sync(this);
						_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
					} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
					}
				}

				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_statContext extends ParserRuleContext {
		public Function_definitionContext function_definition() {
			return getRuleContext(Function_definitionContext.class,0);
		}
		public Function_declarationContext function_declaration() {
			return getRuleContext(Function_declarationContext.class,0);
		}
		public Function_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_stat; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitFunction_stat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_statContext function_stat() throws RecognitionException {
		Function_statContext _localctx = new Function_statContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_function_stat);
		try {
			setState(168);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(166);
				function_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(167);
				function_declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_definitionContext extends ParserRuleContext {
		public TerminalNode FUNC_KEYWORD() { return getToken(ZCodeParser.FUNC_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(ZCodeParser.LEFT_PARENTHESIS, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(ZCodeParser.RIGHT_PARENTHESIS, 0); }
		public Block_statContext block_stat() {
			return getRuleContext(Block_statContext.class,0);
		}
		public Function_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_definition; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitFunction_definition(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_definitionContext function_definition() throws RecognitionException {
		Function_definitionContext _localctx = new Function_definitionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_function_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			match(FUNC_KEYWORD);
			setState(171);
			match(ID);
			setState(172);
			match(LEFT_PARENTHESIS);
			setState(173);
			param_list();
			setState(174);
			match(RIGHT_PARENTHESIS);
			setState(175);
			block_stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declarationContext extends ParserRuleContext {
		public TerminalNode FUNC_KEYWORD() { return getToken(ZCodeParser.FUNC_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(ZCodeParser.LEFT_PARENTHESIS, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(ZCodeParser.RIGHT_PARENTHESIS, 0); }
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitFunction_declaration(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_function_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(177);
			match(FUNC_KEYWORD);
			setState(178);
			match(ID);
			setState(179);
			match(LEFT_PARENTHESIS);
			setState(180);
			param_list();
			setState(181);
			match(RIGHT_PARENTHESIS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_listContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public List<TerminalNode> SEPARATOR_KEYWORD() { return getTokens(ZCodeParser.SEPARATOR_KEYWORD); }
		public TerminalNode SEPARATOR_KEYWORD(int i) {
			return getToken(ZCodeParser.SEPARATOR_KEYWORD, i);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitParam_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_param_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			parameter();
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEPARATOR_KEYWORD) {
				{
				{
				setState(184);
				match(SEPARATOR_KEYWORD);
				setState(185);
				parameter();
				}
				}
				setState(190);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public TerminalNode NUM_KEYWORD() { return getToken(ZCodeParser.NUM_KEYWORD, 0); }
		public TerminalNode STRING_KEYWORD() { return getToken(ZCodeParser.STRING_KEYWORD, 0); }
		public TerminalNode BOOL_KEYWORD() { return getToken(ZCodeParser.BOOL_KEYWORD, 0); }
		public TerminalNode VAR_KEYWORD() { return getToken(ZCodeParser.VAR_KEYWORD, 0); }
		public TerminalNode DYNAMIC_KEYWORD() { return getToken(ZCodeParser.DYNAMIC_KEYWORD, 0); }
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitParameter(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_parameter);
		int _la;
		try {
			setState(194);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RIGHT_PARENTHESIS:
			case SEPARATOR_KEYWORD:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case NUM_KEYWORD:
			case BOOL_KEYWORD:
			case STRING_KEYWORD:
			case VAR_KEYWORD:
			case DYNAMIC_KEYWORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(192);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUM_KEYWORD) | (1L << BOOL_KEYWORD) | (1L << STRING_KEYWORD) | (1L << VAR_KEYWORD) | (1L << DYNAMIC_KEYWORD))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(193);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_statContext extends ParserRuleContext {
		public TerminalNode BEGIN_KEYWORD() { return getToken(ZCodeParser.BEGIN_KEYWORD, 0); }
		public TerminalNode END_KEYWORD() { return getToken(ZCodeParser.END_KEYWORD, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Block_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stat; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitBlock_stat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Block_statContext block_stat() throws RecognitionException {
		Block_statContext _localctx = new Block_statContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_block_stat);
		int _la;
		try {
			setState(205);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case BEGIN_KEYWORD:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(BEGIN_KEYWORD);
				setState(200);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << NUM_KEYWORD) | (1L << BOOL_KEYWORD) | (1L << STRING_KEYWORD) | (1L << RETURN_KEYWORD) | (1L << VAR_KEYWORD) | (1L << DYNAMIC_KEYWORD) | (1L << FOR_KEYWORD) | (1L << IF_KEYWORD) | (1L << SUB_OP) | (1L << NOT_OP) | (1L << ID) | (1L << LEFT_PARENTHESIS) | (1L << TRUE_LIT) | (1L << FALSE_LIT) | (1L << INT_LIT) | (1L << REAL_LIT) | (1L << STRING_LIT))) != 0)) {
					{
					{
					setState(197);
					statement();
					}
					}
					setState(202);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(203);
				match(END_KEYWORD);
				}
				break;
			case NUM_KEYWORD:
			case BOOL_KEYWORD:
			case STRING_KEYWORD:
			case RETURN_KEYWORD:
			case VAR_KEYWORD:
			case DYNAMIC_KEYWORD:
			case FOR_KEYWORD:
			case IF_KEYWORD:
			case SUB_OP:
			case NOT_OP:
			case ID:
			case LEFT_PARENTHESIS:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(204);
				statement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public Control_statContext control_stat() {
			return getRuleContext(Control_statContext.class,0);
		}
		public Loop_statContext loop_stat() {
			return getRuleContext(Loop_statContext.class,0);
		}
		public Variable_statContext variable_stat() {
			return getRuleContext(Variable_statContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public TerminalNode RETURN_KEYWORD() { return getToken(ZCodeParser.RETURN_KEYWORD, 0); }
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_statement);
		try {
			setState(214);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(207);
				control_stat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(208);
				loop_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(209);
				variable_stat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(210);
				expression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(211);
				assignment();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(212);
				match(RETURN_KEYWORD);
				setState(213);
				expression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public List<Relational_exprContext> relational_expr() {
			return getRuleContexts(Relational_exprContext.class);
		}
		public Relational_exprContext relational_expr(int i) {
			return getRuleContext(Relational_exprContext.class,i);
		}
		public TerminalNode CONCAT_OP() { return getToken(ZCodeParser.CONCAT_OP, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_expression);
		try {
			setState(221);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(216);
				relational_expr();
				setState(217);
				match(CONCAT_OP);
				setState(218);
				relational_expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(220);
				relational_expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Relation_operationContext extends ParserRuleContext {
		public TerminalNode EQUAL_OP() { return getToken(ZCodeParser.EQUAL_OP, 0); }
		public TerminalNode EQUAL_STR_OP() { return getToken(ZCodeParser.EQUAL_STR_OP, 0); }
		public TerminalNode INEQUAL_OP() { return getToken(ZCodeParser.INEQUAL_OP, 0); }
		public TerminalNode LESS_OP() { return getToken(ZCodeParser.LESS_OP, 0); }
		public TerminalNode LARGE_OP() { return getToken(ZCodeParser.LARGE_OP, 0); }
		public TerminalNode LESSEQUAL_OP() { return getToken(ZCodeParser.LESSEQUAL_OP, 0); }
		public TerminalNode LARGEEQUAL_OP() { return getToken(ZCodeParser.LARGEEQUAL_OP, 0); }
		public Relation_operationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relation_operation; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitRelation_operation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Relation_operationContext relation_operation() throws RecognitionException {
		Relation_operationContext _localctx = new Relation_operationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_relation_operation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQUAL_OP) | (1L << INEQUAL_OP) | (1L << LESS_OP) | (1L << LESSEQUAL_OP) | (1L << LARGE_OP) | (1L << LARGEEQUAL_OP) | (1L << EQUAL_STR_OP))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Relational_exprContext extends ParserRuleContext {
		public List<Logical_exprContext> logical_expr() {
			return getRuleContexts(Logical_exprContext.class);
		}
		public Logical_exprContext logical_expr(int i) {
			return getRuleContext(Logical_exprContext.class,i);
		}
		public Relation_operationContext relation_operation() {
			return getRuleContext(Relation_operationContext.class,0);
		}
		public Relational_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitRelational_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Relational_exprContext relational_expr() throws RecognitionException {
		Relational_exprContext _localctx = new Relational_exprContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_relational_expr);
		try {
			setState(230);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(225);
				logical_expr(0);
				setState(226);
				relation_operation();
				setState(227);
				logical_expr(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(229);
				logical_expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logical_exprContext extends ParserRuleContext {
		public Adding_exprContext adding_expr() {
			return getRuleContext(Adding_exprContext.class,0);
		}
		public Logical_exprContext logical_expr() {
			return getRuleContext(Logical_exprContext.class,0);
		}
		public TerminalNode AND_OP() { return getToken(ZCodeParser.AND_OP, 0); }
		public TerminalNode OR_OP() { return getToken(ZCodeParser.OR_OP, 0); }
		public Logical_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitLogical_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logical_exprContext logical_expr() throws RecognitionException {
		return logical_expr(0);
	}

	private Logical_exprContext logical_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Logical_exprContext _localctx = new Logical_exprContext(_ctx, _parentState);
		Logical_exprContext _prevctx = _localctx;
		int _startState = 40;
		enterRecursionRule(_localctx, 40, RULE_logical_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(233);
			adding_expr(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(240);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Logical_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_logical_expr);
					setState(235);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(236);
					_la = _input.LA(1);
					if ( !(_la==AND_OP || _la==OR_OP) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(237);
					adding_expr(0);
					}
					} 
				}
				setState(242);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Adding_exprContext extends ParserRuleContext {
		public Multiplying_exprContext multiplying_expr() {
			return getRuleContext(Multiplying_exprContext.class,0);
		}
		public Adding_exprContext adding_expr() {
			return getRuleContext(Adding_exprContext.class,0);
		}
		public TerminalNode ADD_OP() { return getToken(ZCodeParser.ADD_OP, 0); }
		public TerminalNode SUB_OP() { return getToken(ZCodeParser.SUB_OP, 0); }
		public Adding_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_adding_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitAdding_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Adding_exprContext adding_expr() throws RecognitionException {
		return adding_expr(0);
	}

	private Adding_exprContext adding_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Adding_exprContext _localctx = new Adding_exprContext(_ctx, _parentState);
		Adding_exprContext _prevctx = _localctx;
		int _startState = 42;
		enterRecursionRule(_localctx, 42, RULE_adding_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(244);
			multiplying_expr(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(251);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Adding_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_adding_expr);
					setState(246);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(247);
					_la = _input.LA(1);
					if ( !(_la==ADD_OP || _la==SUB_OP) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(248);
					multiplying_expr(0);
					}
					} 
				}
				setState(253);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Multiplying_exprContext extends ParserRuleContext {
		public Not_logicalContext not_logical() {
			return getRuleContext(Not_logicalContext.class,0);
		}
		public Multiplying_exprContext multiplying_expr() {
			return getRuleContext(Multiplying_exprContext.class,0);
		}
		public TerminalNode MUL_OP() { return getToken(ZCodeParser.MUL_OP, 0); }
		public TerminalNode DIV_OP() { return getToken(ZCodeParser.DIV_OP, 0); }
		public TerminalNode MOD_OP() { return getToken(ZCodeParser.MOD_OP, 0); }
		public Multiplying_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplying_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitMultiplying_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Multiplying_exprContext multiplying_expr() throws RecognitionException {
		return multiplying_expr(0);
	}

	private Multiplying_exprContext multiplying_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Multiplying_exprContext _localctx = new Multiplying_exprContext(_ctx, _parentState);
		Multiplying_exprContext _prevctx = _localctx;
		int _startState = 44;
		enterRecursionRule(_localctx, 44, RULE_multiplying_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(255);
			not_logical();
			}
			_ctx.stop = _input.LT(-1);
			setState(262);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Multiplying_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_multiplying_expr);
					setState(257);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(258);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL_OP) | (1L << DIV_OP) | (1L << MOD_OP))) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(259);
					not_logical();
					}
					} 
				}
				setState(264);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,25,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Not_logicalContext extends ParserRuleContext {
		public TerminalNode NOT_OP() { return getToken(ZCodeParser.NOT_OP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Sign_exprContext sign_expr() {
			return getRuleContext(Sign_exprContext.class,0);
		}
		public Not_logicalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_not_logical; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitNot_logical(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Not_logicalContext not_logical() throws RecognitionException {
		Not_logicalContext _localctx = new Not_logicalContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_not_logical);
		try {
			setState(268);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(265);
				match(NOT_OP);
				setState(266);
				expression();
				}
				break;
			case SUB_OP:
			case ID:
			case LEFT_PARENTHESIS:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(267);
				sign_expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Sign_exprContext extends ParserRuleContext {
		public TerminalNode SUB_OP() { return getToken(ZCodeParser.SUB_OP, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Index_exprContext index_expr() {
			return getRuleContext(Index_exprContext.class,0);
		}
		public Sign_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sign_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitSign_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Sign_exprContext sign_expr() throws RecognitionException {
		Sign_exprContext _localctx = new Sign_exprContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_sign_expr);
		try {
			setState(273);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUB_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(270);
				match(SUB_OP);
				setState(271);
				expression();
				}
				break;
			case ID:
			case LEFT_PARENTHESIS:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(272);
				index_expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_exprContext extends ParserRuleContext {
		public Parenthesis_exprContext parenthesis_expr() {
			return getRuleContext(Parenthesis_exprContext.class,0);
		}
		public TerminalNode LEFT_BRACKET() { return getToken(ZCodeParser.LEFT_BRACKET, 0); }
		public Index_valueContext index_value() {
			return getRuleContext(Index_valueContext.class,0);
		}
		public TerminalNode RIGHT_BRACKET() { return getToken(ZCodeParser.RIGHT_BRACKET, 0); }
		public Index_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitIndex_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Index_exprContext index_expr() throws RecognitionException {
		Index_exprContext _localctx = new Index_exprContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_index_expr);
		try {
			setState(281);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(275);
				parenthesis_expr();
				setState(276);
				match(LEFT_BRACKET);
				setState(277);
				index_value();
				setState(278);
				match(RIGHT_BRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(280);
				parenthesis_expr();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_valueContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> SEPARATOR_KEYWORD() { return getTokens(ZCodeParser.SEPARATOR_KEYWORD); }
		public TerminalNode SEPARATOR_KEYWORD(int i) {
			return getToken(ZCodeParser.SEPARATOR_KEYWORD, i);
		}
		public Index_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_value; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitIndex_value(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Index_valueContext index_value() throws RecognitionException {
		Index_valueContext _localctx = new Index_valueContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_index_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			expression();
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEPARATOR_KEYWORD) {
				{
				{
				setState(284);
				match(SEPARATOR_KEYWORD);
				setState(285);
				expression();
				}
				}
				setState(290);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Parenthesis_exprContext extends ParserRuleContext {
		public TerminalNode LEFT_PARENTHESIS() { return getToken(ZCodeParser.LEFT_PARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(ZCodeParser.RIGHT_PARENTHESIS, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Index_exprContext index_expr() {
			return getRuleContext(Index_exprContext.class,0);
		}
		public Parenthesis_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenthesis_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitParenthesis_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Parenthesis_exprContext parenthesis_expr() throws RecognitionException {
		Parenthesis_exprContext _localctx = new Parenthesis_exprContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_parenthesis_expr);
		try {
			setState(299);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEFT_PARENTHESIS:
				enterOuterAlt(_localctx, 1);
				{
				setState(291);
				match(LEFT_PARENTHESIS);
				setState(292);
				expression();
				setState(293);
				match(RIGHT_PARENTHESIS);
				}
				break;
			case ID:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 2);
				{
				setState(295);
				term();
				setState(297);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
				case 1:
					{
					setState(296);
					index_expr();
					}
					break;
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public TerminalNode REAL_LIT() { return getToken(ZCodeParser.REAL_LIT, 0); }
		public TerminalNode INT_LIT() { return getToken(ZCodeParser.INT_LIT, 0); }
		public TerminalNode TRUE_LIT() { return getToken(ZCodeParser.TRUE_LIT, 0); }
		public TerminalNode FALSE_LIT() { return getToken(ZCodeParser.FALSE_LIT, 0); }
		public Function_exprContext function_expr() {
			return getRuleContext(Function_exprContext.class,0);
		}
		public TerminalNode STRING_LIT() { return getToken(ZCodeParser.STRING_LIT, 0); }
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitTerm(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_term);
		try {
			setState(308);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(301);
				match(REAL_LIT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(302);
				match(INT_LIT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(303);
				match(TRUE_LIT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(304);
				match(FALSE_LIT);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(305);
				function_expr();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(306);
				match(STRING_LIT);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(307);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_exprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public TerminalNode LEFT_PARENTHESIS() { return getToken(ZCodeParser.LEFT_PARENTHESIS, 0); }
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(ZCodeParser.RIGHT_PARENTHESIS, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> SEPARATOR_KEYWORD() { return getTokens(ZCodeParser.SEPARATOR_KEYWORD); }
		public TerminalNode SEPARATOR_KEYWORD(int i) {
			return getToken(ZCodeParser.SEPARATOR_KEYWORD, i);
		}
		public Function_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_expr; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitFunction_expr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Function_exprContext function_expr() throws RecognitionException {
		Function_exprContext _localctx = new Function_exprContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_function_expr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			match(ID);
			setState(311);
			match(LEFT_PARENTHESIS);
			setState(313);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SUB_OP) | (1L << NOT_OP) | (1L << ID) | (1L << LEFT_PARENTHESIS) | (1L << TRUE_LIT) | (1L << FALSE_LIT) | (1L << INT_LIT) | (1L << REAL_LIT) | (1L << STRING_LIT))) != 0)) {
				{
				setState(312);
				expression();
				}
			}

			setState(319);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEPARATOR_KEYWORD) {
				{
				{
				setState(315);
				match(SEPARATOR_KEYWORD);
				setState(316);
				expression();
				}
				}
				setState(321);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(322);
			match(RIGHT_PARENTHESIS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ifst_componentContext extends ParserRuleContext {
		public TerminalNode LEFT_PARENTHESIS() { return getToken(ZCodeParser.LEFT_PARENTHESIS, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RIGHT_PARENTHESIS() { return getToken(ZCodeParser.RIGHT_PARENTHESIS, 0); }
		public Block_statContext block_stat() {
			return getRuleContext(Block_statContext.class,0);
		}
		public Ifst_componentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifst_component; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitIfst_component(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Ifst_componentContext ifst_component() throws RecognitionException {
		Ifst_componentContext _localctx = new Ifst_componentContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_ifst_component);
		try {
			setState(332);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(324);
				match(LEFT_PARENTHESIS);
				setState(325);
				expression();
				setState(326);
				match(RIGHT_PARENTHESIS);
				setState(327);
				block_stat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(329);
				expression();
				setState(330);
				block_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Control_statContext extends ParserRuleContext {
		public TerminalNode IF_KEYWORD() { return getToken(ZCodeParser.IF_KEYWORD, 0); }
		public List<Ifst_componentContext> ifst_component() {
			return getRuleContexts(Ifst_componentContext.class);
		}
		public Ifst_componentContext ifst_component(int i) {
			return getRuleContext(Ifst_componentContext.class,i);
		}
		public List<TerminalNode> ELIF_KEYWORD() { return getTokens(ZCodeParser.ELIF_KEYWORD); }
		public TerminalNode ELIF_KEYWORD(int i) {
			return getToken(ZCodeParser.ELIF_KEYWORD, i);
		}
		public TerminalNode ELSE_KEYWORD() { return getToken(ZCodeParser.ELSE_KEYWORD, 0); }
		public Block_statContext block_stat() {
			return getRuleContext(Block_statContext.class,0);
		}
		public Control_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_control_stat; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitControl_stat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Control_statContext control_stat() throws RecognitionException {
		Control_statContext _localctx = new Control_statContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_control_stat);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			match(IF_KEYWORD);
			setState(335);
			ifst_component();
			setState(340);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(336);
					match(ELIF_KEYWORD);
					setState(337);
					ifst_component();
					}
					} 
				}
				setState(342);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,36,_ctx);
			}
			setState(345);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,37,_ctx) ) {
			case 1:
				{
				setState(343);
				match(ELSE_KEYWORD);
				setState(344);
				block_stat();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Loop_statContext extends ParserRuleContext {
		public TerminalNode FOR_KEYWORD() { return getToken(ZCodeParser.FOR_KEYWORD, 0); }
		public TerminalNode ID() { return getToken(ZCodeParser.ID, 0); }
		public TerminalNode UNTIL_KEYWORD() { return getToken(ZCodeParser.UNTIL_KEYWORD, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode BY_KEYWORD() { return getToken(ZCodeParser.BY_KEYWORD, 0); }
		public Loop_body_statementContext loop_body_statement() {
			return getRuleContext(Loop_body_statementContext.class,0);
		}
		public TerminalNode BEGIN_KEYWORD() { return getToken(ZCodeParser.BEGIN_KEYWORD, 0); }
		public TerminalNode END_KEYWORD() { return getToken(ZCodeParser.END_KEYWORD, 0); }
		public Loop_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop_stat; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitLoop_stat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Loop_statContext loop_stat() throws RecognitionException {
		Loop_statContext _localctx = new Loop_statContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_loop_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(347);
			match(FOR_KEYWORD);
			setState(348);
			match(ID);
			setState(349);
			match(UNTIL_KEYWORD);
			setState(350);
			expression();
			setState(351);
			match(BY_KEYWORD);
			setState(352);
			expression();
			setState(358);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_KEYWORD:
			case BOOL_KEYWORD:
			case STRING_KEYWORD:
			case RETURN_KEYWORD:
			case VAR_KEYWORD:
			case DYNAMIC_KEYWORD:
			case FOR_KEYWORD:
			case BREAK_KEYWORD:
			case CONTINUE_KEYWORD:
			case IF_KEYWORD:
			case SUB_OP:
			case NOT_OP:
			case ID:
			case LEFT_PARENTHESIS:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				{
				setState(353);
				loop_body_statement();
				}
				break;
			case BEGIN_KEYWORD:
				{
				{
				setState(354);
				match(BEGIN_KEYWORD);
				setState(355);
				loop_body_statement();
				setState(356);
				match(END_KEYWORD);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Loop_body_statementContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode BREAK_KEYWORD() { return getToken(ZCodeParser.BREAK_KEYWORD, 0); }
		public TerminalNode CONTINUE_KEYWORD() { return getToken(ZCodeParser.CONTINUE_KEYWORD, 0); }
		public Loop_body_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop_body_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitLoop_body_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Loop_body_statementContext loop_body_statement() throws RecognitionException {
		Loop_body_statementContext _localctx = new Loop_body_statementContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_loop_body_statement);
		try {
			setState(363);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM_KEYWORD:
			case BOOL_KEYWORD:
			case STRING_KEYWORD:
			case RETURN_KEYWORD:
			case VAR_KEYWORD:
			case DYNAMIC_KEYWORD:
			case FOR_KEYWORD:
			case IF_KEYWORD:
			case SUB_OP:
			case NOT_OP:
			case ID:
			case LEFT_PARENTHESIS:
			case TRUE_LIT:
			case FALSE_LIT:
			case INT_LIT:
			case REAL_LIT:
			case STRING_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(360);
				statement();
				}
				break;
			case BREAK_KEYWORD:
				enterOuterAlt(_localctx, 2);
				{
				setState(361);
				match(BREAK_KEYWORD);
				}
				break;
			case CONTINUE_KEYWORD:
				enterOuterAlt(_localctx, 3);
				{
				setState(362);
				match(CONTINUE_KEYWORD);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ASSIGN_OP() { return getToken(ZCodeParser.ASSIGN_OP, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ZCodeVisitor ) return ((ZCodeVisitor<? extends T>)visitor).visitAssignment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			expression();
			setState(366);
			match(ASSIGN_OP);
			setState(367);
			expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 20:
			return logical_expr_sempred((Logical_exprContext)_localctx, predIndex);
		case 21:
			return adding_expr_sempred((Adding_exprContext)_localctx, predIndex);
		case 22:
			return multiplying_expr_sempred((Multiplying_exprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean logical_expr_sempred(Logical_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean adding_expr_sempred(Adding_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean multiplying_expr_sempred(Multiplying_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65\u0174\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\3\2\7\2J\n\2\f\2\16\2M\13\2\3\2\3\2\3\3\3\3\3"+
		"\3\5\3T\n\3\3\4\3\4\5\4X\n\4\3\5\3\5\3\6\3\6\5\6^\n\6\3\7\3\7\3\7\7\7"+
		"c\n\7\f\7\16\7f\13\7\3\b\3\b\3\b\3\b\5\bl\n\b\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\7\tt\n\t\f\t\16\tw\13\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\177\n\t\3\n\3\n\3"+
		"\n\3\n\3\n\7\n\u0086\n\n\f\n\16\n\u0089\13\n\3\n\3\n\3\n\7\n\u008e\n\n"+
		"\f\n\16\n\u0091\13\n\5\n\u0093\n\n\3\13\3\13\3\13\3\13\6\13\u0099\n\13"+
		"\r\13\16\13\u009a\3\13\3\13\3\13\3\13\6\13\u00a1\n\13\r\13\16\13\u00a2"+
		"\5\13\u00a5\n\13\5\13\u00a7\n\13\3\f\3\f\5\f\u00ab\n\f\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00bd\n"+
		"\17\f\17\16\17\u00c0\13\17\3\20\3\20\3\20\5\20\u00c5\n\20\3\21\3\21\7"+
		"\21\u00c9\n\21\f\21\16\21\u00cc\13\21\3\21\3\21\5\21\u00d0\n\21\3\22\3"+
		"\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d9\n\22\3\23\3\23\3\23\3\23\3\23"+
		"\5\23\u00e0\n\23\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00e9\n\25\3"+
		"\26\3\26\3\26\3\26\3\26\3\26\7\26\u00f1\n\26\f\26\16\26\u00f4\13\26\3"+
		"\27\3\27\3\27\3\27\3\27\3\27\7\27\u00fc\n\27\f\27\16\27\u00ff\13\27\3"+
		"\30\3\30\3\30\3\30\3\30\3\30\7\30\u0107\n\30\f\30\16\30\u010a\13\30\3"+
		"\31\3\31\3\31\5\31\u010f\n\31\3\32\3\32\3\32\5\32\u0114\n\32\3\33\3\33"+
		"\3\33\3\33\3\33\3\33\5\33\u011c\n\33\3\34\3\34\3\34\7\34\u0121\n\34\f"+
		"\34\16\34\u0124\13\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u012c\n\35\5"+
		"\35\u012e\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u0137\n\36\3\37"+
		"\3\37\3\37\5\37\u013c\n\37\3\37\3\37\7\37\u0140\n\37\f\37\16\37\u0143"+
		"\13\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \5 \u014f\n \3!\3!\3!\3!\7!\u0155"+
		"\n!\f!\16!\u0158\13!\3!\3!\5!\u015c\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\""+
		"\3\"\3\"\3\"\5\"\u0169\n\"\3#\3#\3#\5#\u016e\n#\3$\3$\3$\3$\3$\2\5*,."+
		"%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF"+
		"\2\b\3\2\3\5\4\2\3\5\7\b\4\2\35\"$$\3\2\33\34\3\2\25\26\3\2\27\31\2\u0183"+
		"\2K\3\2\2\2\4S\3\2\2\2\6W\3\2\2\2\bY\3\2\2\2\n]\3\2\2\2\f_\3\2\2\2\16"+
		"g\3\2\2\2\20m\3\2\2\2\22\u0092\3\2\2\2\24\u00a6\3\2\2\2\26\u00aa\3\2\2"+
		"\2\30\u00ac\3\2\2\2\32\u00b3\3\2\2\2\34\u00b9\3\2\2\2\36\u00c4\3\2\2\2"+
		" \u00cf\3\2\2\2\"\u00d8\3\2\2\2$\u00df\3\2\2\2&\u00e1\3\2\2\2(\u00e8\3"+
		"\2\2\2*\u00ea\3\2\2\2,\u00f5\3\2\2\2.\u0100\3\2\2\2\60\u010e\3\2\2\2\62"+
		"\u0113\3\2\2\2\64\u011b\3\2\2\2\66\u011d\3\2\2\28\u012d\3\2\2\2:\u0136"+
		"\3\2\2\2<\u0138\3\2\2\2>\u014e\3\2\2\2@\u0150\3\2\2\2B\u015d\3\2\2\2D"+
		"\u016d\3\2\2\2F\u016f\3\2\2\2HJ\5\4\3\2IH\3\2\2\2JM\3\2\2\2KI\3\2\2\2"+
		"KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2NO\7\2\2\3O\3\3\2\2\2PT\5\6\4\2QT\5 \21"+
		"\2RT\5\26\f\2SP\3\2\2\2SQ\3\2\2\2SR\3\2\2\2T\5\3\2\2\2UX\5\n\6\2VX\5\24"+
		"\13\2WU\3\2\2\2WV\3\2\2\2X\7\3\2\2\2YZ\t\2\2\2Z\t\3\2\2\2[^\5\20\t\2\\"+
		"^\5\16\b\2][\3\2\2\2]\\\3\2\2\2^\13\3\2\2\2_d\7%\2\2`a\7*\2\2ac\7%\2\2"+
		"b`\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2e\r\3\2\2\2fd\3\2\2\2gh\5\b\5"+
		"\2hk\5\f\7\2ij\7\24\2\2jl\5$\23\2ki\3\2\2\2kl\3\2\2\2l\17\3\2\2\2mn\5"+
		"\b\5\2no\7%\2\2op\7(\2\2pu\7.\2\2qr\7*\2\2rt\7.\2\2sq\3\2\2\2tw\3\2\2"+
		"\2us\3\2\2\2uv\3\2\2\2vx\3\2\2\2wu\3\2\2\2x~\7)\2\2yz\7\24\2\2z{\7(\2"+
		"\2{|\5\22\n\2|}\7)\2\2}\177\3\2\2\2~y\3\2\2\2~\177\3\2\2\2\177\21\3\2"+
		"\2\2\u0080\u0081\7(\2\2\u0081\u0082\5\22\n\2\u0082\u0087\7)\2\2\u0083"+
		"\u0084\7*\2\2\u0084\u0086\5\22\n\2\u0085\u0083\3\2\2\2\u0086\u0089\3\2"+
		"\2\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0093\3\2\2\2\u0089"+
		"\u0087\3\2\2\2\u008a\u008f\5$\23\2\u008b\u008c\7*\2\2\u008c\u008e\5\22"+
		"\n\2\u008d\u008b\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u008d\3\2\2\2\u008f"+
		"\u0090\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0092\u0080\3\2"+
		"\2\2\u0092\u008a\3\2\2\2\u0093\23\3\2\2\2\u0094\u0095\7\7\2\2\u0095\u0096"+
		"\5\f\7\2\u0096\u0098\7\24\2\2\u0097\u0099\5\22\n\2\u0098\u0097\3\2\2\2"+
		"\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u00a7"+
		"\3\2\2\2\u009c\u009d\7\b\2\2\u009d\u00a4\5\f\7\2\u009e\u00a0\7\24\2\2"+
		"\u009f\u00a1\5\22\n\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a0"+
		"\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a5\3\2\2\2\u00a4\u009e\3\2\2\2\u00a4"+
		"\u00a5\3\2\2\2\u00a5\u00a7\3\2\2\2\u00a6\u0094\3\2\2\2\u00a6\u009c\3\2"+
		"\2\2\u00a7\25\3\2\2\2\u00a8\u00ab\5\30\r\2\u00a9\u00ab\5\32\16\2\u00aa"+
		"\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\27\3\2\2\2\u00ac\u00ad\7\t\2"+
		"\2\u00ad\u00ae\7%\2\2\u00ae\u00af\7&\2\2\u00af\u00b0\5\34\17\2\u00b0\u00b1"+
		"\7\'\2\2\u00b1\u00b2\5 \21\2\u00b2\31\3\2\2\2\u00b3\u00b4\7\t\2\2\u00b4"+
		"\u00b5\7%\2\2\u00b5\u00b6\7&\2\2\u00b6\u00b7\5\34\17\2\u00b7\u00b8\7\'"+
		"\2\2\u00b8\33\3\2\2\2\u00b9\u00be\5\36\20\2\u00ba\u00bb\7*\2\2\u00bb\u00bd"+
		"\5\36\20\2\u00bc\u00ba\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2"+
		"\u00be\u00bf\3\2\2\2\u00bf\35\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c5"+
		"\3\2\2\2\u00c2\u00c3\t\3\2\2\u00c3\u00c5\7%\2\2\u00c4\u00c1\3\2\2\2\u00c4"+
		"\u00c2\3\2\2\2\u00c5\37\3\2\2\2\u00c6\u00ca\7\22\2\2\u00c7\u00c9\5\"\22"+
		"\2\u00c8\u00c7\3\2\2\2\u00c9\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb"+
		"\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cd\u00d0\7\23\2\2"+
		"\u00ce\u00d0\5\"\22\2\u00cf\u00c6\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0!\3"+
		"\2\2\2\u00d1\u00d9\5@!\2\u00d2\u00d9\5B\"\2\u00d3\u00d9\5\6\4\2\u00d4"+
		"\u00d9\5$\23\2\u00d5\u00d9\5F$\2\u00d6\u00d7\7\6\2\2\u00d7\u00d9\5$\23"+
		"\2\u00d8\u00d1\3\2\2\2\u00d8\u00d2\3\2\2\2\u00d8\u00d3\3\2\2\2\u00d8\u00d4"+
		"\3\2\2\2\u00d8\u00d5\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9#\3\2\2\2\u00da"+
		"\u00db\5(\25\2\u00db\u00dc\7#\2\2\u00dc\u00dd\5(\25\2\u00dd\u00e0\3\2"+
		"\2\2\u00de\u00e0\5(\25\2\u00df\u00da\3\2\2\2\u00df\u00de\3\2\2\2\u00e0"+
		"%\3\2\2\2\u00e1\u00e2\t\4\2\2\u00e2\'\3\2\2\2\u00e3\u00e4\5*\26\2\u00e4"+
		"\u00e5\5&\24\2\u00e5\u00e6\5*\26\2\u00e6\u00e9\3\2\2\2\u00e7\u00e9\5*"+
		"\26\2\u00e8\u00e3\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9)\3\2\2\2\u00ea\u00eb"+
		"\b\26\1\2\u00eb\u00ec\5,\27\2\u00ec\u00f2\3\2\2\2\u00ed\u00ee\f\4\2\2"+
		"\u00ee\u00ef\t\5\2\2\u00ef\u00f1\5,\27\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4"+
		"\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3+\3\2\2\2\u00f4"+
		"\u00f2\3\2\2\2\u00f5\u00f6\b\27\1\2\u00f6\u00f7\5.\30\2\u00f7\u00fd\3"+
		"\2\2\2\u00f8\u00f9\f\4\2\2\u00f9\u00fa\t\6\2\2\u00fa\u00fc\5.\30\2\u00fb"+
		"\u00f8\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2"+
		"\2\2\u00fe-\3\2\2\2\u00ff\u00fd\3\2\2\2\u0100\u0101\b\30\1\2\u0101\u0102"+
		"\5\60\31\2\u0102\u0108\3\2\2\2\u0103\u0104\f\4\2\2\u0104\u0105\t\7\2\2"+
		"\u0105\u0107\5\60\31\2\u0106\u0103\3\2\2\2\u0107\u010a\3\2\2\2\u0108\u0106"+
		"\3\2\2\2\u0108\u0109\3\2\2\2\u0109/\3\2\2\2\u010a\u0108\3\2\2\2\u010b"+
		"\u010c\7\32\2\2\u010c\u010f\5$\23\2\u010d\u010f\5\62\32\2\u010e\u010b"+
		"\3\2\2\2\u010e\u010d\3\2\2\2\u010f\61\3\2\2\2\u0110\u0111\7\26\2\2\u0111"+
		"\u0114\5$\23\2\u0112\u0114\5\64\33\2\u0113\u0110\3\2\2\2\u0113\u0112\3"+
		"\2\2\2\u0114\63\3\2\2\2\u0115\u0116\58\35\2\u0116\u0117\7(\2\2\u0117\u0118"+
		"\5\66\34\2\u0118\u0119\7)\2\2\u0119\u011c\3\2\2\2\u011a\u011c\58\35\2"+
		"\u011b\u0115\3\2\2\2\u011b\u011a\3\2\2\2\u011c\65\3\2\2\2\u011d\u0122"+
		"\5$\23\2\u011e\u011f\7*\2\2\u011f\u0121\5$\23\2\u0120\u011e\3\2\2\2\u0121"+
		"\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\67\3\2\2"+
		"\2\u0124\u0122\3\2\2\2\u0125\u0126\7&\2\2\u0126\u0127\5$\23\2\u0127\u0128"+
		"\7\'\2\2\u0128\u012e\3\2\2\2\u0129\u012b\5:\36\2\u012a\u012c\5\64\33\2"+
		"\u012b\u012a\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012e\3\2\2\2\u012d\u0125"+
		"\3\2\2\2\u012d\u0129\3\2\2\2\u012e9\3\2\2\2\u012f\u0137\7/\2\2\u0130\u0137"+
		"\7.\2\2\u0131\u0137\7,\2\2\u0132\u0137\7-\2\2\u0133\u0137\5<\37\2\u0134"+
		"\u0137\7\60\2\2\u0135\u0137\7%\2\2\u0136\u012f\3\2\2\2\u0136\u0130\3\2"+
		"\2\2\u0136\u0131\3\2\2\2\u0136\u0132\3\2\2\2\u0136\u0133\3\2\2\2\u0136"+
		"\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137;\3\2\2\2\u0138\u0139\7%\2\2\u0139"+
		"\u013b\7&\2\2\u013a\u013c\5$\23\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2"+
		"\2\2\u013c\u0141\3\2\2\2\u013d\u013e\7*\2\2\u013e\u0140\5$\23\2\u013f"+
		"\u013d\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2"+
		"\2\2\u0142\u0144\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0145\7\'\2\2\u0145"+
		"=\3\2\2\2\u0146\u0147\7&\2\2\u0147\u0148\5$\23\2\u0148\u0149\7\'\2\2\u0149"+
		"\u014a\5 \21\2\u014a\u014f\3\2\2\2\u014b\u014c\5$\23\2\u014c\u014d\5 "+
		"\21\2\u014d\u014f\3\2\2\2\u014e\u0146\3\2\2\2\u014e\u014b\3\2\2\2\u014f"+
		"?\3\2\2\2\u0150\u0151\7\17\2\2\u0151\u0156\5> \2\u0152\u0153\7\21\2\2"+
		"\u0153\u0155\5> \2\u0154\u0152\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154"+
		"\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015b\3\2\2\2\u0158\u0156\3\2\2\2\u0159"+
		"\u015a\7\20\2\2\u015a\u015c\5 \21\2\u015b\u0159\3\2\2\2\u015b\u015c\3"+
		"\2\2\2\u015cA\3\2\2\2\u015d\u015e\7\n\2\2\u015e\u015f\7%\2\2\u015f\u0160"+
		"\7\13\2\2\u0160\u0161\5$\23\2\u0161\u0162\7\f\2\2\u0162\u0168\5$\23\2"+
		"\u0163\u0169\5D#\2\u0164\u0165\7\22\2\2\u0165\u0166\5D#\2\u0166\u0167"+
		"\7\23\2\2\u0167\u0169\3\2\2\2\u0168\u0163\3\2\2\2\u0168\u0164\3\2\2\2"+
		"\u0169C\3\2\2\2\u016a\u016e\5\"\22\2\u016b\u016e\7\r\2\2\u016c\u016e\7"+
		"\16\2\2\u016d\u016a\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016c\3\2\2\2\u016e"+
		"E\3\2\2\2\u016f\u0170\5$\23\2\u0170\u0171\7\24\2\2\u0171\u0172\5$\23\2"+
		"\u0172G\3\2\2\2*KSW]dku~\u0087\u008f\u0092\u009a\u00a2\u00a4\u00a6\u00aa"+
		"\u00be\u00c4\u00ca\u00cf\u00d8\u00df\u00e8\u00f2\u00fd\u0108\u010e\u0113"+
		"\u011b\u0122\u012b\u012d\u0136\u013b\u0141\u014e\u0156\u015b\u0168\u016d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}