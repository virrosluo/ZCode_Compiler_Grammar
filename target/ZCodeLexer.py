# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0198\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$")
        buf.write("\6$\u00fd\n$\r$\16$\u00fe\3$\7$\u0102\n$\f$\16$\u0105")
        buf.write("\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u0122\n,\3,\3,\5")
        buf.write(",\u0126\n,\3-\6-\u0129\n-\r-\16-\u012a\3.\3.\7.\u012f")
        buf.write("\n.\f.\16.\u0132\13.\3/\3/\5/\u0136\n/\3/\6/\u0139\n/")
        buf.write("\r/\16/\u013a\3\60\5\60\u013e\n\60\3\60\3\60\3\60\3\61")
        buf.write("\6\61\u0144\n\61\r\61\16\61\u0145\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u014e\n\62\f\62\16\62\u0151\13\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u015b\n\63\7")
        buf.write("\63\u015d\n\63\f\63\16\63\u0160\13\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\5\64\u016a\n\64\7\64\u016c\n\64")
        buf.write("\f\64\16\64\u016f\13\64\3\64\3\64\3\64\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u0178\n\65\3\65\3\65\7\65\u017c\n\65\f\65\16")
        buf.write("\65\u017f\13\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u018c\n\66\7\66\u018e\n\66\f\66\16")
        buf.write("\66\u0191\13\66\3\66\3\66\3\66\3\67\3\67\3\67\4\u017d")
        buf.write("\u018f\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_.a/c\60e\61g\62i\63k\64")
        buf.write("m\65\3\2\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\60\60")
        buf.write("\4\2GGgg\4\2--//\5\2\13\13\17\17\"\"\4\2\f\f\17\17\7\2")
        buf.write("\f\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2$$\5\2$$))^^\4\2")
        buf.write("\f\f\16\17\2\u01b0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2_\3\2\2\2\2")
        buf.write("a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2")
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\3o\3\2\2\2\5v\3\2\2\2\7{\3\2\2")
        buf.write("\2\t\u0082\3\2\2\2\13\u0089\3\2\2\2\r\u008d\3\2\2\2\17")
        buf.write("\u0095\3\2\2\2\21\u009a\3\2\2\2\23\u009e\3\2\2\2\25\u00a4")
        buf.write("\3\2\2\2\27\u00a7\3\2\2\2\31\u00ad\3\2\2\2\33\u00b6\3")
        buf.write("\2\2\2\35\u00b9\3\2\2\2\37\u00be\3\2\2\2!\u00c3\3\2\2")
        buf.write("\2#\u00c9\3\2\2\2%\u00cd\3\2\2\2\'\u00d0\3\2\2\2)\u00d2")
        buf.write("\3\2\2\2+\u00d4\3\2\2\2-\u00d6\3\2\2\2/\u00d8\3\2\2\2")
        buf.write("\61\u00da\3\2\2\2\63\u00de\3\2\2\2\65\u00e2\3\2\2\2\67")
        buf.write("\u00e5\3\2\2\29\u00e7\3\2\2\2;\u00ea\3\2\2\2=\u00ec\3")
        buf.write("\2\2\2?\u00ef\3\2\2\2A\u00f1\3\2\2\2C\u00f4\3\2\2\2E\u00f8")
        buf.write("\3\2\2\2G\u00fc\3\2\2\2I\u0106\3\2\2\2K\u0108\3\2\2\2")
        buf.write("M\u010a\3\2\2\2O\u010c\3\2\2\2Q\u010e\3\2\2\2S\u0110\3")
        buf.write("\2\2\2U\u0115\3\2\2\2W\u0125\3\2\2\2Y\u0128\3\2\2\2[\u012c")
        buf.write("\3\2\2\2]\u0133\3\2\2\2_\u013d\3\2\2\2a\u0143\3\2\2\2")
        buf.write("c\u0149\3\2\2\2e\u0154\3\2\2\2g\u0163\3\2\2\2i\u0173\3")
        buf.write("\2\2\2k\u0185\3\2\2\2m\u0195\3\2\2\2op\7p\2\2pq\7w\2\2")
        buf.write("qr\7o\2\2rs\7d\2\2st\7g\2\2tu\7t\2\2u\4\3\2\2\2vw\7d\2")
        buf.write("\2wx\7q\2\2xy\7q\2\2yz\7n\2\2z\6\3\2\2\2{|\7u\2\2|}\7")
        buf.write("v\2\2}~\7t\2\2~\177\7k\2\2\177\u0080\7p\2\2\u0080\u0081")
        buf.write("\7i\2\2\u0081\b\3\2\2\2\u0082\u0083\7t\2\2\u0083\u0084")
        buf.write("\7g\2\2\u0084\u0085\7v\2\2\u0085\u0086\7w\2\2\u0086\u0087")
        buf.write("\7t\2\2\u0087\u0088\7p\2\2\u0088\n\3\2\2\2\u0089\u008a")
        buf.write("\7x\2\2\u008a\u008b\7c\2\2\u008b\u008c\7t\2\2\u008c\f")
        buf.write("\3\2\2\2\u008d\u008e\7f\2\2\u008e\u008f\7{\2\2\u008f\u0090")
        buf.write("\7p\2\2\u0090\u0091\7c\2\2\u0091\u0092\7o\2\2\u0092\u0093")
        buf.write("\7k\2\2\u0093\u0094\7e\2\2\u0094\16\3\2\2\2\u0095\u0096")
        buf.write("\7h\2\2\u0096\u0097\7w\2\2\u0097\u0098\7p\2\2\u0098\u0099")
        buf.write("\7e\2\2\u0099\20\3\2\2\2\u009a\u009b\7h\2\2\u009b\u009c")
        buf.write("\7q\2\2\u009c\u009d\7t\2\2\u009d\22\3\2\2\2\u009e\u009f")
        buf.write("\7w\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2")
        buf.write("\7k\2\2\u00a2\u00a3\7n\2\2\u00a3\24\3\2\2\2\u00a4\u00a5")
        buf.write("\7d\2\2\u00a5\u00a6\7{\2\2\u00a6\26\3\2\2\2\u00a7\u00a8")
        buf.write("\7d\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab")
        buf.write("\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\30\3\2\2\2\u00ad\u00ae")
        buf.write("\7e\2\2\u00ae\u00af\7q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1")
        buf.write("\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4")
        buf.write("\7w\2\2\u00b4\u00b5\7g\2\2\u00b5\32\3\2\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7h\2\2\u00b8\34\3\2\2\2\u00b9\u00ba")
        buf.write("\7g\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd")
        buf.write("\7g\2\2\u00bd\36\3\2\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0")
        buf.write("\7n\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7h\2\2\u00c2 \3")
        buf.write("\2\2\2\u00c3\u00c4\7d\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6")
        buf.write("\7i\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\"")
        buf.write("\3\2\2\2\u00c9\u00ca\7g\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc")
        buf.write("\7f\2\2\u00cc$\3\2\2\2\u00cd\u00ce\7>\2\2\u00ce\u00cf")
        buf.write("\7/\2\2\u00cf&\3\2\2\2\u00d0\u00d1\7-\2\2\u00d1(\3\2\2")
        buf.write("\2\u00d2\u00d3\7/\2\2\u00d3*\3\2\2\2\u00d4\u00d5\7,\2")
        buf.write("\2\u00d5,\3\2\2\2\u00d6\u00d7\7\61\2\2\u00d7.\3\2\2\2")
        buf.write("\u00d8\u00d9\7\'\2\2\u00d9\60\3\2\2\2\u00da\u00db\7p\2")
        buf.write("\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7v\2\2\u00dd\62\3\2")
        buf.write("\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7f\2\2\u00e1\64\3\2\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7t\2\2\u00e4\66\3\2\2\2\u00e5\u00e6\7?\2\2\u00e68\3\2")
        buf.write("\2\2\u00e7\u00e8\7#\2\2\u00e8\u00e9\7?\2\2\u00e9:\3\2")
        buf.write("\2\2\u00ea\u00eb\7>\2\2\u00eb<\3\2\2\2\u00ec\u00ed\7>")
        buf.write("\2\2\u00ed\u00ee\7?\2\2\u00ee>\3\2\2\2\u00ef\u00f0\7@")
        buf.write("\2\2\u00f0@\3\2\2\2\u00f1\u00f2\7@\2\2\u00f2\u00f3\7?")
        buf.write("\2\2\u00f3B\3\2\2\2\u00f4\u00f5\7\60\2\2\u00f5\u00f6\7")
        buf.write("\60\2\2\u00f6\u00f7\7\60\2\2\u00f7D\3\2\2\2\u00f8\u00f9")
        buf.write("\7?\2\2\u00f9\u00fa\7?\2\2\u00faF\3\2\2\2\u00fb\u00fd")
        buf.write("\t\2\2\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe")
        buf.write("\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0103\3\2\2\2")
        buf.write("\u0100\u0102\t\3\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3")
        buf.write("\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104H")
        buf.write("\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\7*\2\2\u0107")
        buf.write("J\3\2\2\2\u0108\u0109\7+\2\2\u0109L\3\2\2\2\u010a\u010b")
        buf.write("\7]\2\2\u010bN\3\2\2\2\u010c\u010d\7_\2\2\u010dP\3\2\2")
        buf.write("\2\u010e\u010f\7.\2\2\u010fR\3\2\2\2\u0110\u0111\7v\2")
        buf.write("\2\u0111\u0112\7t\2\2\u0112\u0113\7w\2\2\u0113\u0114\7")
        buf.write("g\2\2\u0114T\3\2\2\2\u0115\u0116\7h\2\2\u0116\u0117\7")
        buf.write("c\2\2\u0117\u0118\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a")
        buf.write("\7g\2\2\u011aV\3\2\2\2\u011b\u0126\5Y-\2\u011c\u011d\5")
        buf.write("Y-\2\u011d\u011e\5[.\2\u011e\u0126\3\2\2\2\u011f\u0121")
        buf.write("\5Y-\2\u0120\u0122\5[.\2\u0121\u0120\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\5]/\2\u0124\u0126")
        buf.write("\3\2\2\2\u0125\u011b\3\2\2\2\u0125\u011c\3\2\2\2\u0125")
        buf.write("\u011f\3\2\2\2\u0126X\3\2\2\2\u0127\u0129\t\4\2\2\u0128")
        buf.write("\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012bZ\3\2\2\2\u012c\u0130\t\5\2")
        buf.write("\2\u012d\u012f\t\4\2\2\u012e\u012d\3\2\2\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\\\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0135\t\6\2\2\u0134")
        buf.write("\u0136\t\7\2\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136\u0138\3\2\2\2\u0137\u0139\t\4\2\2\u0138\u0137\3")
        buf.write("\2\2\2\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b^\3\2\2\2\u013c\u013e\7t\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0140\7\f\2\2\u0140\u0141\b\60\2\2\u0141`\3\2\2\2\u0142")
        buf.write("\u0144\t\b\2\2\u0143\u0142\3\2\2\2\u0144\u0145\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\3")
        buf.write("\2\2\2\u0147\u0148\b\61\3\2\u0148b\3\2\2\2\u0149\u014a")
        buf.write("\7%\2\2\u014a\u014b\7%\2\2\u014b\u014f\3\2\2\2\u014c\u014e")
        buf.write("\n\t\2\2\u014d\u014c\3\2\2\2\u014e\u0151\3\2\2\2\u014f")
        buf.write("\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0152\u0153\b\62\3\2\u0153d\3\2\2")
        buf.write("\2\u0154\u015e\7$\2\2\u0155\u015d\n\n\2\2\u0156\u0157")
        buf.write("\7^\2\2\u0157\u015d\t\13\2\2\u0158\u015a\7)\2\2\u0159")
        buf.write("\u015b\t\f\2\2\u015a\u0159\3\2\2\2\u015a\u015b\3\2\2\2")
        buf.write("\u015b\u015d\3\2\2\2\u015c\u0155\3\2\2\2\u015c\u0156\3")
        buf.write("\2\2\2\u015c\u0158\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0161\u0162\b\63\4\2\u0162f\3\2\2\2\u0163")
        buf.write("\u016d\7$\2\2\u0164\u016c\n\n\2\2\u0165\u0166\7^\2\2\u0166")
        buf.write("\u016c\t\13\2\2\u0167\u0169\7)\2\2\u0168\u016a\t\f\2\2")
        buf.write("\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3")
        buf.write("\2\2\2\u016b\u0164\3\2\2\2\u016b\u0165\3\2\2\2\u016b\u0167")
        buf.write("\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u0170\u0171\7$\2\2\u0171\u0172\b\64\5\2\u0172h\3\2\2")
        buf.write("\2\u0173\u017d\7$\2\2\u0174\u017c\n\r\2\2\u0175\u0177")
        buf.write("\7)\2\2\u0176\u0178\t\f\2\2\u0177\u0176\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u017c\3\2\2\2\u0179\u017a\7^\2\2")
        buf.write("\u017a\u017c\t\13\2\2\u017b\u0174\3\2\2\2\u017b\u0175")
        buf.write("\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017d\u017b\3\2\2\2\u017e\u0180\3\2\2\2")
        buf.write("\u017f\u017d\3\2\2\2\u0180\u0181\7^\2\2\u0181\u0182\n")
        buf.write("\13\2\2\u0182\u0183\3\2\2\2\u0183\u0184\b\65\6\2\u0184")
        buf.write("j\3\2\2\2\u0185\u018f\7$\2\2\u0186\u018e\n\n\2\2\u0187")
        buf.write("\u0188\7^\2\2\u0188\u018e\t\13\2\2\u0189\u018b\7)\2\2")
        buf.write("\u018a\u018c\t\f\2\2\u018b\u018a\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c\u018e\3\2\2\2\u018d\u0186\3\2\2\2\u018d\u0187")
        buf.write("\3\2\2\2\u018d\u0189\3\2\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0192\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0192\u0193\t\16\2\2\u0193\u0194")
        buf.write("\b\66\7\2\u0194l\3\2\2\2\u0195\u0196\13\2\2\2\u0196\u0197")
        buf.write("\b\67\b\2\u0197n\3\2\2\2\32\2\u00fe\u0103\u0121\u0125")
        buf.write("\u012a\u0130\u0135\u013a\u013d\u0145\u014f\u015a\u015c")
        buf.write("\u015e\u0169\u016b\u016d\u0177\u017b\u017d\u018b\u018d")
        buf.write("\u018f\t\3\60\2\b\2\2\3\63\3\3\64\4\3\65\5\3\66\6\3\67")
        buf.write("\7")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUM_KEYWORD = 1
    BOOL_KEYWORD = 2
    STRING_KEYWORD = 3
    RETURN_KEYWORD = 4
    VAR_KEYWORD = 5
    DYNAMIC_KEYWORD = 6
    FUNC_KEYWORD = 7
    FOR_KEYWORD = 8
    UNTIL_KEYWORD = 9
    BY_KEYWORD = 10
    BREAK_KEYWORD = 11
    CONTINUE_KEYWORD = 12
    IF_KEYWORD = 13
    ELSE_KEYWORD = 14
    ELIF_KEYWORD = 15
    BEGIN_KEYWORD = 16
    END_KEYWORD = 17
    ASSIGN_OP = 18
    ADD_OP = 19
    SUB_OP = 20
    MUL_OP = 21
    DIV_OP = 22
    MOD_OP = 23
    NOT_OP = 24
    AND_OP = 25
    OR_OP = 26
    EQUAL_OP = 27
    INEQUAL_OP = 28
    LESS_OP = 29
    LESSEQUAL_OP = 30
    LARGE_OP = 31
    LARGEEQUAL_OP = 32
    CONCAT_OP = 33
    EQUAL_STR_OP = 34
    ID = 35
    LEFT_PARENTHESIS = 36
    RIGHT_PARENTHESIS = 37
    LEFT_BRACKET = 38
    RIGHT_BRACKET = 39
    SEPARATOR_KEYWORD = 40
    TRUE_LIT = 41
    FALSE_LIT = 42
    REAL_LIT = 43
    NL = 44
    WS = 45
    COMMENT_LINE = 46
    UNCLOSE_STRING = 47
    STRING_LIT = 48
    ILLEGAL_ESCAPE = 49
    NEWLINE_STRING = 50
    ERROR_TOKEN = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'<-'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", 
            "')'", "'['", "']'", "','", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "RETURN_KEYWORD", 
            "VAR_KEYWORD", "DYNAMIC_KEYWORD", "FUNC_KEYWORD", "FOR_KEYWORD", 
            "UNTIL_KEYWORD", "BY_KEYWORD", "BREAK_KEYWORD", "CONTINUE_KEYWORD", 
            "IF_KEYWORD", "ELSE_KEYWORD", "ELIF_KEYWORD", "BEGIN_KEYWORD", 
            "END_KEYWORD", "ASSIGN_OP", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
            "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", "INEQUAL_OP", 
            "LESS_OP", "LESSEQUAL_OP", "LARGE_OP", "LARGEEQUAL_OP", "CONCAT_OP", 
            "EQUAL_STR_OP", "ID", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
            "LEFT_BRACKET", "RIGHT_BRACKET", "SEPARATOR_KEYWORD", "TRUE_LIT", 
            "FALSE_LIT", "REAL_LIT", "NL", "WS", "COMMENT_LINE", "UNCLOSE_STRING", 
            "STRING_LIT", "ILLEGAL_ESCAPE", "NEWLINE_STRING", "ERROR_TOKEN" ]

    ruleNames = [ "NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", "RETURN_KEYWORD", 
                  "VAR_KEYWORD", "DYNAMIC_KEYWORD", "FUNC_KEYWORD", "FOR_KEYWORD", 
                  "UNTIL_KEYWORD", "BY_KEYWORD", "BREAK_KEYWORD", "CONTINUE_KEYWORD", 
                  "IF_KEYWORD", "ELSE_KEYWORD", "ELIF_KEYWORD", "BEGIN_KEYWORD", 
                  "END_KEYWORD", "ASSIGN_OP", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "DIV_OP", "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", 
                  "INEQUAL_OP", "LESS_OP", "LESSEQUAL_OP", "LARGE_OP", "LARGEEQUAL_OP", 
                  "CONCAT_OP", "EQUAL_STR_OP", "ID", "LEFT_PARENTHESIS", 
                  "RIGHT_PARENTHESIS", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "SEPARATOR_KEYWORD", "TRUE_LIT", "FALSE_LIT", "REAL_LIT", 
                  "INTPART", "DECPART", "EXPPART", "NL", "WS", "COMMENT_LINE", 
                  "UNCLOSE_STRING", "STRING_LIT", "ILLEGAL_ESCAPE", "NEWLINE_STRING", 
                  "ERROR_TOKEN" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.NL_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.STRING_LIT_action 
            actions[51] = self.ILLEGAL_ESCAPE_action 
            actions[52] = self.NEWLINE_STRING_action 
            actions[53] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('\r','')
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise UncloseString(self.text[1:])
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     

    def NEWLINE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:-1])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


