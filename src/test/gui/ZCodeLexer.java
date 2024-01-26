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
		TRUE_LIT=41, FALSE_LIT=42, INT_LIT=43, REAL_LIT=44, STRING_LIT=45, NL=46, 
		WS=47, COMMENT_LINE=48, NEWLINE_STRING=49, UNCLOSE_STRING=50, ILLEGAL_ESCAPE=51, 
		ERROR_TOKEN=52;
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
			"RIGHT_BRACKET", "SEPARATOR_KEYWORD", "TRUE_LIT", "FALSE_LIT", "INT_LIT", 
			"REAL_LIT", "INTPART", "DECPART", "EXPPART", "STRING_LIT", "NL", "WS", 
			"COMMENT_LINE", "NEWLINE_STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"ERROR_TOKEN"
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
			"'true'", "'false'", null, null, null, "'\n'"
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
			"INT_LIT", "REAL_LIT", "STRING_LIT", "NL", "WS", "COMMENT_LINE", "NEWLINE_STRING", 
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66\u0189\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b"+
		"\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3"+
		"\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26"+
		"\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33"+
		"\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3"+
		"!\3\"\3\"\3\"\3\"\3#\3#\3#\3$\6$\u00ff\n$\r$\16$\u0100\3$\7$\u0104\n$"+
		"\f$\16$\u0107\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3+\3"+
		"+\3+\3+\3+\3+\3,\3,\3-\3-\3-\3-\3-\5-\u0125\n-\3-\3-\5-\u0129\n-\3.\6"+
		".\u012c\n.\r.\16.\u012d\3/\3/\7/\u0132\n/\f/\16/\u0135\13/\3\60\3\60\5"+
		"\60\u0139\n\60\3\60\6\60\u013c\n\60\r\60\16\60\u013d\3\61\3\61\3\61\3"+
		"\61\3\61\3\61\7\61\u0146\n\61\f\61\16\61\u0149\13\61\3\61\3\61\3\62\3"+
		"\62\3\63\6\63\u0150\n\63\r\63\16\63\u0151\3\63\3\63\3\64\3\64\3\64\3\64"+
		"\7\64\u015a\n\64\f\64\16\64\u015d\13\64\3\64\3\64\3\65\3\65\3\65\3\65"+
		"\3\65\3\65\7\65\u0167\n\65\f\65\16\65\u016a\13\65\3\66\3\66\3\66\3\66"+
		"\3\66\3\66\7\66\u0172\n\66\f\66\16\66\u0175\13\66\3\67\3\67\3\67\3\67"+
		"\3\67\3\67\7\67\u017d\n\67\f\67\16\67\u0180\13\67\3\67\3\67\3\67\3\67"+
		"\5\67\u0186\n\67\38\38\5\u0147\u0168\u017e\29\3\3\5\4\7\5\t\6\13\7\r\b"+
		"\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26"+
		"+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S"+
		"+U,W-Y.[\2]\2_\2a/c\60e\61g\62i\63k\64m\65o\66\3\2\17\5\2C\\aac|\6\2\62"+
		";C\\aac|\3\2\62;\3\2\60\60\4\2GGgg\4\2--//\6\2\f\f\16\17))^^\t\2))^^d"+
		"dhhppttvv\5\2\13\13\17\17\"\"\4\2\f\f\17\17\7\2\f\f\16\17$$))^^\5\2$$"+
		"))^^\3\2$$\2\u019c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13"+
		"\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2"+
		"\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2"+
		"!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3"+
		"\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2"+
		"\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E"+
		"\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2"+
		"\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2"+
		"\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q"+
		"\3\2\2\2\5x\3\2\2\2\7}\3\2\2\2\t\u0084\3\2\2\2\13\u008b\3\2\2\2\r\u008f"+
		"\3\2\2\2\17\u0097\3\2\2\2\21\u009c\3\2\2\2\23\u00a0\3\2\2\2\25\u00a6\3"+
		"\2\2\2\27\u00a9\3\2\2\2\31\u00af\3\2\2\2\33\u00b8\3\2\2\2\35\u00bb\3\2"+
		"\2\2\37\u00c0\3\2\2\2!\u00c5\3\2\2\2#\u00cb\3\2\2\2%\u00cf\3\2\2\2\'\u00d2"+
		"\3\2\2\2)\u00d4\3\2\2\2+\u00d6\3\2\2\2-\u00d8\3\2\2\2/\u00da\3\2\2\2\61"+
		"\u00dc\3\2\2\2\63\u00e0\3\2\2\2\65\u00e4\3\2\2\2\67\u00e7\3\2\2\29\u00e9"+
		"\3\2\2\2;\u00ec\3\2\2\2=\u00ee\3\2\2\2?\u00f1\3\2\2\2A\u00f3\3\2\2\2C"+
		"\u00f6\3\2\2\2E\u00fa\3\2\2\2G\u00fe\3\2\2\2I\u0108\3\2\2\2K\u010a\3\2"+
		"\2\2M\u010c\3\2\2\2O\u010e\3\2\2\2Q\u0110\3\2\2\2S\u0112\3\2\2\2U\u0117"+
		"\3\2\2\2W\u011d\3\2\2\2Y\u0128\3\2\2\2[\u012b\3\2\2\2]\u012f\3\2\2\2_"+
		"\u0136\3\2\2\2a\u013f\3\2\2\2c\u014c\3\2\2\2e\u014f\3\2\2\2g\u0155\3\2"+
		"\2\2i\u0160\3\2\2\2k\u016b\3\2\2\2m\u0176\3\2\2\2o\u0187\3\2\2\2qr\7p"+
		"\2\2rs\7w\2\2st\7o\2\2tu\7d\2\2uv\7g\2\2vw\7t\2\2w\4\3\2\2\2xy\7d\2\2"+
		"yz\7q\2\2z{\7q\2\2{|\7n\2\2|\6\3\2\2\2}~\7u\2\2~\177\7v\2\2\177\u0080"+
		"\7t\2\2\u0080\u0081\7k\2\2\u0081\u0082\7p\2\2\u0082\u0083\7i\2\2\u0083"+
		"\b\3\2\2\2\u0084\u0085\7t\2\2\u0085\u0086\7g\2\2\u0086\u0087\7v\2\2\u0087"+
		"\u0088\7w\2\2\u0088\u0089\7t\2\2\u0089\u008a\7p\2\2\u008a\n\3\2\2\2\u008b"+
		"\u008c\7x\2\2\u008c\u008d\7c\2\2\u008d\u008e\7t\2\2\u008e\f\3\2\2\2\u008f"+
		"\u0090\7f\2\2\u0090\u0091\7{\2\2\u0091\u0092\7p\2\2\u0092\u0093\7c\2\2"+
		"\u0093\u0094\7o\2\2\u0094\u0095\7k\2\2\u0095\u0096\7e\2\2\u0096\16\3\2"+
		"\2\2\u0097\u0098\7h\2\2\u0098\u0099\7w\2\2\u0099\u009a\7p\2\2\u009a\u009b"+
		"\7e\2\2\u009b\20\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e\7q\2\2\u009e\u009f"+
		"\7t\2\2\u009f\22\3\2\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3"+
		"\7v\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5\7n\2\2\u00a5\24\3\2\2\2\u00a6\u00a7"+
		"\7d\2\2\u00a7\u00a8\7{\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab"+
		"\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7m\2\2\u00ae"+
		"\30\3\2\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7p\2\2\u00b2"+
		"\u00b3\7v\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7w\2\2"+
		"\u00b6\u00b7\7g\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7"+
		"h\2\2\u00ba\34\3\2\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be"+
		"\7u\2\2\u00be\u00bf\7g\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2"+
		"\7n\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7h\2\2\u00c4 \3\2\2\2\u00c5\u00c6"+
		"\7d\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7i\2\2\u00c8\u00c9\7k\2\2\u00c9"+
		"\u00ca\7p\2\2\u00ca\"\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7p\2\2\u00cd"+
		"\u00ce\7f\2\2\u00ce$\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0\u00d1\7/\2\2\u00d1"+
		"&\3\2\2\2\u00d2\u00d3\7-\2\2\u00d3(\3\2\2\2\u00d4\u00d5\7/\2\2\u00d5*"+
		"\3\2\2\2\u00d6\u00d7\7,\2\2\u00d7,\3\2\2\2\u00d8\u00d9\7\61\2\2\u00d9"+
		".\3\2\2\2\u00da\u00db\7\'\2\2\u00db\60\3\2\2\2\u00dc\u00dd\7p\2\2\u00dd"+
		"\u00de\7q\2\2\u00de\u00df\7v\2\2\u00df\62\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1"+
		"\u00e2\7p\2\2\u00e2\u00e3\7f\2\2\u00e3\64\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5"+
		"\u00e6\7t\2\2\u00e6\66\3\2\2\2\u00e7\u00e8\7?\2\2\u00e88\3\2\2\2\u00e9"+
		"\u00ea\7#\2\2\u00ea\u00eb\7?\2\2\u00eb:\3\2\2\2\u00ec\u00ed\7>\2\2\u00ed"+
		"<\3\2\2\2\u00ee\u00ef\7>\2\2\u00ef\u00f0\7?\2\2\u00f0>\3\2\2\2\u00f1\u00f2"+
		"\7@\2\2\u00f2@\3\2\2\2\u00f3\u00f4\7@\2\2\u00f4\u00f5\7?\2\2\u00f5B\3"+
		"\2\2\2\u00f6\u00f7\7\60\2\2\u00f7\u00f8\7\60\2\2\u00f8\u00f9\7\60\2\2"+
		"\u00f9D\3\2\2\2\u00fa\u00fb\7?\2\2\u00fb\u00fc\7?\2\2\u00fcF\3\2\2\2\u00fd"+
		"\u00ff\t\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u00fe\3\2"+
		"\2\2\u0100\u0101\3\2\2\2\u0101\u0105\3\2\2\2\u0102\u0104\t\3\2\2\u0103"+
		"\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2"+
		"\2\2\u0106H\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\7*\2\2\u0109J\3\2"+
		"\2\2\u010a\u010b\7+\2\2\u010bL\3\2\2\2\u010c\u010d\7]\2\2\u010dN\3\2\2"+
		"\2\u010e\u010f\7_\2\2\u010fP\3\2\2\2\u0110\u0111\7.\2\2\u0111R\3\2\2\2"+
		"\u0112\u0113\7v\2\2\u0113\u0114\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116"+
		"\7g\2\2\u0116T\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119\7c\2\2\u0119\u011a"+
		"\7n\2\2\u011a\u011b\7u\2\2\u011b\u011c\7g\2\2\u011cV\3\2\2\2\u011d\u011e"+
		"\5[.\2\u011eX\3\2\2\2\u011f\u0120\5[.\2\u0120\u0121\5]/\2\u0121\u0129"+
		"\3\2\2\2\u0122\u0124\5[.\2\u0123\u0125\5]/\2\u0124\u0123\3\2\2\2\u0124"+
		"\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\5_\60\2\u0127\u0129\3\2"+
		"\2\2\u0128\u011f\3\2\2\2\u0128\u0122\3\2\2\2\u0129Z\3\2\2\2\u012a\u012c"+
		"\t\4\2\2\u012b\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2\u012d"+
		"\u012e\3\2\2\2\u012e\\\3\2\2\2\u012f\u0133\t\5\2\2\u0130\u0132\t\4\2\2"+
		"\u0131\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134"+
		"\3\2\2\2\u0134^\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0138\t\6\2\2\u0137"+
		"\u0139\t\7\2\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2"+
		"\2\2\u013a\u013c\t\4\2\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d"+
		"\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e`\3\2\2\2\u013f\u0147\7$\2\2\u0140"+
		"\u0146\n\b\2\2\u0141\u0142\7^\2\2\u0142\u0146\t\t\2\2\u0143\u0144\7)\2"+
		"\2\u0144\u0146\7$\2\2\u0145\u0140\3\2\2\2\u0145\u0141\3\2\2\2\u0145\u0143"+
		"\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0148"+
		"\u014a\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\7$\2\2\u014bb\3\2\2\2\u014c"+
		"\u014d\7\f\2\2\u014dd\3\2\2\2\u014e\u0150\t\n\2\2\u014f\u014e\3\2\2\2"+
		"\u0150\u0151\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0153"+
		"\3\2\2\2\u0153\u0154\b\63\2\2\u0154f\3\2\2\2\u0155\u0156\7%\2\2\u0156"+
		"\u0157\7%\2\2\u0157\u015b\3\2\2\2\u0158\u015a\n\13\2\2\u0159\u0158\3\2"+
		"\2\2\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c"+
		"\u015e\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f\b\64\2\2\u015fh\3\2\2\2"+
		"\u0160\u0168\7$\2\2\u0161\u0167\n\f\2\2\u0162\u0163\7^\2\2\u0163\u0167"+
		"\t\t\2\2\u0164\u0165\7)\2\2\u0165\u0167\7$\2\2\u0166\u0161\3\2\2\2\u0166"+
		"\u0162\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u016a\3\2\2\2\u0168\u0169\3\2"+
		"\2\2\u0168\u0166\3\2\2\2\u0169j\3\2\2\2\u016a\u0168\3\2\2\2\u016b\u0173"+
		"\7$\2\2\u016c\u0172\n\f\2\2\u016d\u016e\7^\2\2\u016e\u0172\t\t\2\2\u016f"+
		"\u0170\7)\2\2\u0170\u0172\7$\2\2\u0171\u016c\3\2\2\2\u0171\u016d\3\2\2"+
		"\2\u0171\u016f\3\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174"+
		"\3\2\2\2\u0174l\3\2\2\2\u0175\u0173\3\2\2\2\u0176\u017e\7$\2\2\u0177\u017d"+
		"\n\r\2\2\u0178\u0179\7)\2\2\u0179\u017d\7$\2\2\u017a\u017b\7^\2\2\u017b"+
		"\u017d\t\t\2\2\u017c\u0177\3\2\2\2\u017c\u0178\3\2\2\2\u017c\u017a\3\2"+
		"\2\2\u017d\u0180\3\2\2\2\u017e\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017f"+
		"\u0185\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7^\2\2\u0182\u0186\n\t"+
		"\2\2\u0183\u0184\7)\2\2\u0184\u0186\n\16\2\2\u0185\u0181\3\2\2\2\u0185"+
		"\u0183\3\2\2\2\u0186n\3\2\2\2\u0187\u0188\13\2\2\2\u0188p\3\2\2\2\26\2"+
		"\u0100\u0105\u0124\u0128\u012d\u0133\u0138\u013d\u0145\u0147\u0151\u015b"+
		"\u0166\u0168\u0171\u0173\u017c\u017e\u0185\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}