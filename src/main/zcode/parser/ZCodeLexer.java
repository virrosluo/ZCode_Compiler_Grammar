// Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ZCodeLexer extends Lexer {
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
		TRUE_LIT=41, FALSE_LIT=42, REAL_LIT=43, NL=44, WS=45, COMMENT_LINE=46, 
		UNCLOSE_STRING=47, STRING_LIT=48, ILLEGAL_ESCAPE=49, NEWLINE_STRING=50, 
		ERROR_TOKEN=51;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "RETURN_KEYWORD", "VAR_KEYWORD", 
			"DYNAMIC_KEYWORD", "FUNC_KEYWORD", "FOR_KEYWORD", "UNTIL_KEYWORD", "BY_KEYWORD", 
			"BREAK_KEYWORD", "CONTINUE_KEYWORD", "IF_KEYWORD", "ELSE_KEYWORD", "ELIF_KEYWORD", 
			"BEGIN_KEYWORD", "END_KEYWORD", "ASSIGN_OP", "ADD_OP", "SUB_OP", "MUL_OP", 
			"DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "INEQUAL_OP", 
			"LESS_OP", "LESSEQUAL_OP", "LARGE_OP", "LARGEEQUAL_OP", "CONCAT_OP", 
			"EQUAL_STR_OP", "ID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", 
			"RIGHT_BRACKET", "SEPARATOR_KEYWORD", "TRUE_LIT", "FALSE_LIT", "REAL_LIT", 
			"INTPART", "DECPART", "EXPPART", "NL", "WS", "COMMENT_LINE", "UNCLOSE_STRING", 
			"STRING_LIT", "ILLEGAL_ESCAPE", "NEWLINE_STRING", "ERROR_TOKEN"
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
			"'true'", "'false'", null, "'\n'"
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
			"LEFT_BRACKET", "RIGHT_BRACKET", "SEPARATOR_KEYWORD", "TRUE_LIT", "FALSE_LIT", 
			"REAL_LIT", "NL", "WS", "COMMENT_LINE", "UNCLOSE_STRING", "STRING_LIT", 
			"ILLEGAL_ESCAPE", "NEWLINE_STRING", "ERROR_TOKEN"
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


	public ZCodeLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ZCode.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65\u018d\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3"+
		"\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3"+
		"\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f"+
		"\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27"+
		"\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33"+
		"\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\""+
		"\3\"\3\"\3\"\3#\3#\3#\3$\6$\u00fd\n$\r$\16$\u00fe\3$\7$\u0102\n$\f$\16"+
		"$\u0105\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3"+
		"+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u0122\n,\3,\3,\5,\u0126\n,\3-\6-\u0129\n"+
		"-\r-\16-\u012a\3.\3.\7.\u012f\n.\f.\16.\u0132\13.\3/\3/\5/\u0136\n/\3"+
		"/\6/\u0139\n/\r/\16/\u013a\3\60\3\60\3\61\6\61\u0140\n\61\r\61\16\61\u0141"+
		"\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u014a\n\62\f\62\16\62\u014d\13\62"+
		"\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u0157\n\63\7\63\u0159\n"+
		"\63\f\63\16\63\u015c\13\63\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0164\n"+
		"\64\7\64\u0166\n\64\f\64\16\64\u0169\13\64\3\64\3\64\3\65\3\65\3\65\3"+
		"\65\5\65\u0171\n\65\3\65\3\65\7\65\u0175\n\65\f\65\16\65\u0178\13\65\3"+
		"\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0183\n\66\7\66\u0185"+
		"\n\66\f\66\16\66\u0188\13\66\3\66\3\66\3\67\3\67\4\u0176\u0186\28\3\3"+
		"\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21"+
		"!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!"+
		"A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_.a/c\60e\61g\62i\63k\64m\65\3\2\17"+
		"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\60\60\4\2GGgg\4\2--//\5\2\13\13"+
		"\17\17\"\"\4\2\f\f\17\17\7\2\f\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2$$\5"+
		"\2$$))^^\4\2\f\f\16\17\2\u01a4\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t"+
		"\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2"+
		"\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2"+
		"\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2"+
		"+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2"+
		"\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2"+
		"C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3"+
		"\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2_\3\2\2\2\2a\3\2\2"+
		"\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3"+
		"o\3\2\2\2\5v\3\2\2\2\7{\3\2\2\2\t\u0082\3\2\2\2\13\u0089\3\2\2\2\r\u008d"+
		"\3\2\2\2\17\u0095\3\2\2\2\21\u009a\3\2\2\2\23\u009e\3\2\2\2\25\u00a4\3"+
		"\2\2\2\27\u00a7\3\2\2\2\31\u00ad\3\2\2\2\33\u00b6\3\2\2\2\35\u00b9\3\2"+
		"\2\2\37\u00be\3\2\2\2!\u00c3\3\2\2\2#\u00c9\3\2\2\2%\u00cd\3\2\2\2\'\u00d0"+
		"\3\2\2\2)\u00d2\3\2\2\2+\u00d4\3\2\2\2-\u00d6\3\2\2\2/\u00d8\3\2\2\2\61"+
		"\u00da\3\2\2\2\63\u00de\3\2\2\2\65\u00e2\3\2\2\2\67\u00e5\3\2\2\29\u00e7"+
		"\3\2\2\2;\u00ea\3\2\2\2=\u00ec\3\2\2\2?\u00ef\3\2\2\2A\u00f1\3\2\2\2C"+
		"\u00f4\3\2\2\2E\u00f8\3\2\2\2G\u00fc\3\2\2\2I\u0106\3\2\2\2K\u0108\3\2"+
		"\2\2M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010e\3\2\2\2S\u0110\3\2\2\2U\u0115"+
		"\3\2\2\2W\u0125\3\2\2\2Y\u0128\3\2\2\2[\u012c\3\2\2\2]\u0133\3\2\2\2_"+
		"\u013c\3\2\2\2a\u013f\3\2\2\2c\u0145\3\2\2\2e\u0150\3\2\2\2g\u015d\3\2"+
		"\2\2i\u016c\3\2\2\2k\u017c\3\2\2\2m\u018b\3\2\2\2op\7p\2\2pq\7w\2\2qr"+
		"\7o\2\2rs\7d\2\2st\7g\2\2tu\7t\2\2u\4\3\2\2\2vw\7d\2\2wx\7q\2\2xy\7q\2"+
		"\2yz\7n\2\2z\6\3\2\2\2{|\7u\2\2|}\7v\2\2}~\7t\2\2~\177\7k\2\2\177\u0080"+
		"\7p\2\2\u0080\u0081\7i\2\2\u0081\b\3\2\2\2\u0082\u0083\7t\2\2\u0083\u0084"+
		"\7g\2\2\u0084\u0085\7v\2\2\u0085\u0086\7w\2\2\u0086\u0087\7t\2\2\u0087"+
		"\u0088\7p\2\2\u0088\n\3\2\2\2\u0089\u008a\7x\2\2\u008a\u008b\7c\2\2\u008b"+
		"\u008c\7t\2\2\u008c\f\3\2\2\2\u008d\u008e\7f\2\2\u008e\u008f\7{\2\2\u008f"+
		"\u0090\7p\2\2\u0090\u0091\7c\2\2\u0091\u0092\7o\2\2\u0092\u0093\7k\2\2"+
		"\u0093\u0094\7e\2\2\u0094\16\3\2\2\2\u0095\u0096\7h\2\2\u0096\u0097\7"+
		"w\2\2\u0097\u0098\7p\2\2\u0098\u0099\7e\2\2\u0099\20\3\2\2\2\u009a\u009b"+
		"\7h\2\2\u009b\u009c\7q\2\2\u009c\u009d\7t\2\2\u009d\22\3\2\2\2\u009e\u009f"+
		"\7w\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7k\2\2\u00a2"+
		"\u00a3\7n\2\2\u00a3\24\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5\u00a6\7{\2\2\u00a6"+
		"\26\3\2\2\2\u00a7\u00a8\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa"+
		"\u00ab\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\30\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae"+
		"\u00af\7q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7k\2\2"+
		"\u00b2\u00b3\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7g\2\2\u00b5\32\3\2"+
		"\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7h\2\2\u00b8\34\3\2\2\2\u00b9\u00ba"+
		"\7g\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd"+
		"\36\3\2\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7k\2\2\u00c1"+
		"\u00c2\7h\2\2\u00c2 \3\2\2\2\u00c3\u00c4\7d\2\2\u00c4\u00c5\7g\2\2\u00c5"+
		"\u00c6\7i\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\"\3\2\2\2\u00c9"+
		"\u00ca\7g\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7f\2\2\u00cc$\3\2\2\2\u00cd"+
		"\u00ce\7>\2\2\u00ce\u00cf\7/\2\2\u00cf&\3\2\2\2\u00d0\u00d1\7-\2\2\u00d1"+
		"(\3\2\2\2\u00d2\u00d3\7/\2\2\u00d3*\3\2\2\2\u00d4\u00d5\7,\2\2\u00d5,"+
		"\3\2\2\2\u00d6\u00d7\7\61\2\2\u00d7.\3\2\2\2\u00d8\u00d9\7\'\2\2\u00d9"+
		"\60\3\2\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7v\2\2\u00dd"+
		"\62\3\2\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7f\2\2\u00e1"+
		"\64\3\2\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4\66\3\2\2\2\u00e5"+
		"\u00e6\7?\2\2\u00e68\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8\u00e9\7?\2\2\u00e9"+
		":\3\2\2\2\u00ea\u00eb\7>\2\2\u00eb<\3\2\2\2\u00ec\u00ed\7>\2\2\u00ed\u00ee"+
		"\7?\2\2\u00ee>\3\2\2\2\u00ef\u00f0\7@\2\2\u00f0@\3\2\2\2\u00f1\u00f2\7"+
		"@\2\2\u00f2\u00f3\7?\2\2\u00f3B\3\2\2\2\u00f4\u00f5\7\60\2\2\u00f5\u00f6"+
		"\7\60\2\2\u00f6\u00f7\7\60\2\2\u00f7D\3\2\2\2\u00f8\u00f9\7?\2\2\u00f9"+
		"\u00fa\7?\2\2\u00faF\3\2\2\2\u00fb\u00fd\t\2\2\2\u00fc\u00fb\3\2\2\2\u00fd"+
		"\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0103\3\2"+
		"\2\2\u0100\u0102\t\3\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103"+
		"\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104H\3\2\2\2\u0105\u0103\3\2\2\2"+
		"\u0106\u0107\7*\2\2\u0107J\3\2\2\2\u0108\u0109\7+\2\2\u0109L\3\2\2\2\u010a"+
		"\u010b\7]\2\2\u010bN\3\2\2\2\u010c\u010d\7_\2\2\u010dP\3\2\2\2\u010e\u010f"+
		"\7.\2\2\u010fR\3\2\2\2\u0110\u0111\7v\2\2\u0111\u0112\7t\2\2\u0112\u0113"+
		"\7w\2\2\u0113\u0114\7g\2\2\u0114T\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117"+
		"\7c\2\2\u0117\u0118\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a"+
		"V\3\2\2\2\u011b\u0126\5Y-\2\u011c\u011d\5Y-\2\u011d\u011e\5[.\2\u011e"+
		"\u0126\3\2\2\2\u011f\u0121\5Y-\2\u0120\u0122\5[.\2\u0121\u0120\3\2\2\2"+
		"\u0121\u0122\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\5]/\2\u0124\u0126"+
		"\3\2\2\2\u0125\u011b\3\2\2\2\u0125\u011c\3\2\2\2\u0125\u011f\3\2\2\2\u0126"+
		"X\3\2\2\2\u0127\u0129\t\4\2\2\u0128\u0127\3\2\2\2\u0129\u012a\3\2\2\2"+
		"\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012bZ\3\2\2\2\u012c\u0130\t"+
		"\5\2\2\u012d\u012f\t\4\2\2\u012e\u012d\3\2\2\2\u012f\u0132\3\2\2\2\u0130"+
		"\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\\\3\2\2\2\u0132\u0130\3\2\2\2"+
		"\u0133\u0135\t\6\2\2\u0134\u0136\t\7\2\2\u0135\u0134\3\2\2\2\u0135\u0136"+
		"\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0139\t\4\2\2\u0138\u0137\3\2\2\2\u0139"+
		"\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b^\3\2\2\2"+
		"\u013c\u013d\7\f\2\2\u013d`\3\2\2\2\u013e\u0140\t\b\2\2\u013f\u013e\3"+
		"\2\2\2\u0140\u0141\3\2\2\2\u0141\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142"+
		"\u0143\3\2\2\2\u0143\u0144\b\61\2\2\u0144b\3\2\2\2\u0145\u0146\7%\2\2"+
		"\u0146\u0147\7%\2\2\u0147\u014b\3\2\2\2\u0148\u014a\n\t\2\2\u0149\u0148"+
		"\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c"+
		"\u014e\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\b\62\2\2\u014fd\3\2\2\2"+
		"\u0150\u015a\7$\2\2\u0151\u0159\n\n\2\2\u0152\u0153\7^\2\2\u0153\u0159"+
		"\t\13\2\2\u0154\u0156\7)\2\2\u0155\u0157\t\f\2\2\u0156\u0155\3\2\2\2\u0156"+
		"\u0157\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u0151\3\2\2\2\u0158\u0152\3\2"+
		"\2\2\u0158\u0154\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a"+
		"\u015b\3\2\2\2\u015bf\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u0167\7$\2\2\u015e"+
		"\u0166\n\n\2\2\u015f\u0160\7^\2\2\u0160\u0166\t\13\2\2\u0161\u0163\7)"+
		"\2\2\u0162\u0164\t\f\2\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164"+
		"\u0166\3\2\2\2\u0165\u015e\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0161\3\2"+
		"\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168"+
		"\u016a\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016b\7$\2\2\u016bh\3\2\2\2\u016c"+
		"\u0176\7$\2\2\u016d\u0175\n\r\2\2\u016e\u0170\7)\2\2\u016f\u0171\t\f\2"+
		"\2\u0170\u016f\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0175\3\2\2\2\u0172\u0173"+
		"\7^\2\2\u0173\u0175\t\13\2\2\u0174\u016d\3\2\2\2\u0174\u016e\3\2\2\2\u0174"+
		"\u0172\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0177\3\2\2\2\u0176\u0174\3\2"+
		"\2\2\u0177\u0179\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\7^\2\2\u017a"+
		"\u017b\n\13\2\2\u017bj\3\2\2\2\u017c\u0186\7$\2\2\u017d\u0185\n\n\2\2"+
		"\u017e\u017f\7^\2\2\u017f\u0185\t\13\2\2\u0180\u0182\7)\2\2\u0181\u0183"+
		"\t\f\2\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184"+
		"\u017d\3\2\2\2\u0184\u017e\3\2\2\2\u0184\u0180\3\2\2\2\u0185\u0188\3\2"+
		"\2\2\u0186\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0189\3\2\2\2\u0188"+
		"\u0186\3\2\2\2\u0189\u018a\t\16\2\2\u018al\3\2\2\2\u018b\u018c\13\2\2"+
		"\2\u018cn\3\2\2\2\31\2\u00fe\u0103\u0121\u0125\u012a\u0130\u0135\u013a"+
		"\u0141\u014b\u0156\u0158\u015a\u0163\u0165\u0167\u0170\u0174\u0176\u0182"+
		"\u0184\u0186\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}