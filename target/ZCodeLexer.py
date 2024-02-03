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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01ad\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"")
        buf.write("\3\"\3\"\3#\3#\3#\3$\6$\u0103\n$\r$\16$\u0104\3$\7$\u0108")
        buf.write("\n$\f$\16$\u010b\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\5,\u0128")
        buf.write("\n,\3,\3,\5,\u012c\n,\3-\6-\u012f\n-\r-\16-\u0130\3.\3")
        buf.write(".\7.\u0135\n.\f.\16.\u0138\13.\3/\3/\5/\u013c\n/\3/\6")
        buf.write("/\u013f\n/\r/\16/\u0140\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\6\64\u0155\n\64\r\64\16\64\u0156\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\7\65\u015f\n\65\f\65\16\65\u0162\13\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u016c\n")
        buf.write("\66\7\66\u016e\n\66\f\66\16\66\u0171\13\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\3\67\3\67\3\67\5\67\u017b\n\67\7\67\u017d")
        buf.write("\n\67\f\67\16\67\u0180\13\67\3\67\3\67\3\67\38\38\38\3")
        buf.write("8\38\38\58\u018b\n8\78\u018d\n8\f8\168\u0190\138\38\3")
        buf.write("8\38\58\u0195\n8\38\38\39\39\39\39\59\u019d\n9\39\39\7")
        buf.write("9\u01a1\n9\f9\169\u01a4\139\39\39\39\39\39\3:\3:\3:\4")
        buf.write("\u018e\u01a2\2;\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_.a/c\60e\61g\62i\63")
        buf.write("k\64m\65o\66q\67s8\3\2\16\5\2C\\aac|\6\2\62;C\\aac|\3")
        buf.write("\2\62;\3\2\60\60\4\2GGgg\4\2--//\4\2\13\13\"\"\4\2\f\f")
        buf.write("\17\17\7\2\f\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2$$\4\2")
        buf.write("\f\f\16\17\2\u01c5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
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
        buf.write("\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2")
        buf.write("\2\3u\3\2\2\2\5|\3\2\2\2\7\u0081\3\2\2\2\t\u0088\3\2\2")
        buf.write("\2\13\u008f\3\2\2\2\r\u0093\3\2\2\2\17\u009b\3\2\2\2\21")
        buf.write("\u00a0\3\2\2\2\23\u00a4\3\2\2\2\25\u00aa\3\2\2\2\27\u00ad")
        buf.write("\3\2\2\2\31\u00b3\3\2\2\2\33\u00bc\3\2\2\2\35\u00bf\3")
        buf.write("\2\2\2\37\u00c4\3\2\2\2!\u00c9\3\2\2\2#\u00cf\3\2\2\2")
        buf.write("%\u00d3\3\2\2\2\'\u00d6\3\2\2\2)\u00d8\3\2\2\2+\u00da")
        buf.write("\3\2\2\2-\u00dc\3\2\2\2/\u00de\3\2\2\2\61\u00e0\3\2\2")
        buf.write("\2\63\u00e4\3\2\2\2\65\u00e8\3\2\2\2\67\u00eb\3\2\2\2")
        buf.write("9\u00ed\3\2\2\2;\u00f0\3\2\2\2=\u00f2\3\2\2\2?\u00f5\3")
        buf.write("\2\2\2A\u00f7\3\2\2\2C\u00fa\3\2\2\2E\u00fe\3\2\2\2G\u0102")
        buf.write("\3\2\2\2I\u010c\3\2\2\2K\u010e\3\2\2\2M\u0110\3\2\2\2")
        buf.write("O\u0112\3\2\2\2Q\u0114\3\2\2\2S\u0116\3\2\2\2U\u011b\3")
        buf.write("\2\2\2W\u012b\3\2\2\2Y\u012e\3\2\2\2[\u0132\3\2\2\2]\u0139")
        buf.write("\3\2\2\2_\u0142\3\2\2\2a\u0148\3\2\2\2c\u014b\3\2\2\2")
        buf.write("e\u0150\3\2\2\2g\u0154\3\2\2\2i\u015a\3\2\2\2k\u0165\3")
        buf.write("\2\2\2m\u0174\3\2\2\2o\u0184\3\2\2\2q\u0198\3\2\2\2s\u01aa")
        buf.write("\3\2\2\2uv\7p\2\2vw\7w\2\2wx\7o\2\2xy\7d\2\2yz\7g\2\2")
        buf.write("z{\7t\2\2{\4\3\2\2\2|}\7d\2\2}~\7q\2\2~\177\7q\2\2\177")
        buf.write("\u0080\7n\2\2\u0080\6\3\2\2\2\u0081\u0082\7u\2\2\u0082")
        buf.write("\u0083\7v\2\2\u0083\u0084\7t\2\2\u0084\u0085\7k\2\2\u0085")
        buf.write("\u0086\7p\2\2\u0086\u0087\7i\2\2\u0087\b\3\2\2\2\u0088")
        buf.write("\u0089\7t\2\2\u0089\u008a\7g\2\2\u008a\u008b\7v\2\2\u008b")
        buf.write("\u008c\7w\2\2\u008c\u008d\7t\2\2\u008d\u008e\7p\2\2\u008e")
        buf.write("\n\3\2\2\2\u008f\u0090\7x\2\2\u0090\u0091\7c\2\2\u0091")
        buf.write("\u0092\7t\2\2\u0092\f\3\2\2\2\u0093\u0094\7f\2\2\u0094")
        buf.write("\u0095\7{\2\2\u0095\u0096\7p\2\2\u0096\u0097\7c\2\2\u0097")
        buf.write("\u0098\7o\2\2\u0098\u0099\7k\2\2\u0099\u009a\7e\2\2\u009a")
        buf.write("\16\3\2\2\2\u009b\u009c\7h\2\2\u009c\u009d\7w\2\2\u009d")
        buf.write("\u009e\7p\2\2\u009e\u009f\7e\2\2\u009f\20\3\2\2\2\u00a0")
        buf.write("\u00a1\7h\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3\7t\2\2\u00a3")
        buf.write("\22\3\2\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7p\2\2\u00a6")
        buf.write("\u00a7\7v\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9\7n\2\2\u00a9")
        buf.write("\24\3\2\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac\7{\2\2\u00ac")
        buf.write("\26\3\2\2\2\u00ad\u00ae\7d\2\2\u00ae\u00af\7t\2\2\u00af")
        buf.write("\u00b0\7g\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2\7m\2\2\u00b2")
        buf.write("\30\3\2\2\2\u00b3\u00b4\7e\2\2\u00b4\u00b5\7q\2\2\u00b5")
        buf.write("\u00b6\7p\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7k\2\2\u00b8")
        buf.write("\u00b9\7p\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\32\3\2\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7h\2\2\u00be")
        buf.write("\34\3\2\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1\7n\2\2\u00c1")
        buf.write("\u00c2\7u\2\2\u00c2\u00c3\7g\2\2\u00c3\36\3\2\2\2\u00c4")
        buf.write("\u00c5\7g\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7k\2\2\u00c7")
        buf.write("\u00c8\7h\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7d\2\2\u00ca")
        buf.write("\u00cb\7g\2\2\u00cb\u00cc\7i\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\"\3\2\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write("\u00d1\7p\2\2\u00d1\u00d2\7f\2\2\u00d2$\3\2\2\2\u00d3")
        buf.write("\u00d4\7>\2\2\u00d4\u00d5\7/\2\2\u00d5&\3\2\2\2\u00d6")
        buf.write("\u00d7\7-\2\2\u00d7(\3\2\2\2\u00d8\u00d9\7/\2\2\u00d9")
        buf.write("*\3\2\2\2\u00da\u00db\7,\2\2\u00db,\3\2\2\2\u00dc\u00dd")
        buf.write("\7\61\2\2\u00dd.\3\2\2\2\u00de\u00df\7\'\2\2\u00df\60")
        buf.write("\3\2\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\62\3\2\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7p\2\2\u00e6\u00e7\7f\2\2\u00e7\64\3\2\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\66\3\2\2\2\u00eb\u00ec")
        buf.write("\7?\2\2\u00ec8\3\2\2\2\u00ed\u00ee\7#\2\2\u00ee\u00ef")
        buf.write("\7?\2\2\u00ef:\3\2\2\2\u00f0\u00f1\7>\2\2\u00f1<\3\2\2")
        buf.write("\2\u00f2\u00f3\7>\2\2\u00f3\u00f4\7?\2\2\u00f4>\3\2\2")
        buf.write("\2\u00f5\u00f6\7@\2\2\u00f6@\3\2\2\2\u00f7\u00f8\7@\2")
        buf.write("\2\u00f8\u00f9\7?\2\2\u00f9B\3\2\2\2\u00fa\u00fb\7\60")
        buf.write("\2\2\u00fb\u00fc\7\60\2\2\u00fc\u00fd\7\60\2\2\u00fdD")
        buf.write("\3\2\2\2\u00fe\u00ff\7?\2\2\u00ff\u0100\7?\2\2\u0100F")
        buf.write("\3\2\2\2\u0101\u0103\t\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0109\3\2\2\2\u0106\u0108\t\3\2\2\u0107\u0106\3")
        buf.write("\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010aH\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010d")
        buf.write("\7*\2\2\u010dJ\3\2\2\2\u010e\u010f\7+\2\2\u010fL\3\2\2")
        buf.write("\2\u0110\u0111\7]\2\2\u0111N\3\2\2\2\u0112\u0113\7_\2")
        buf.write("\2\u0113P\3\2\2\2\u0114\u0115\7.\2\2\u0115R\3\2\2\2\u0116")
        buf.write("\u0117\7v\2\2\u0117\u0118\7t\2\2\u0118\u0119\7w\2\2\u0119")
        buf.write("\u011a\7g\2\2\u011aT\3\2\2\2\u011b\u011c\7h\2\2\u011c")
        buf.write("\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e\u011f\7u\2\2\u011f")
        buf.write("\u0120\7g\2\2\u0120V\3\2\2\2\u0121\u012c\5Y-\2\u0122\u0123")
        buf.write("\5Y-\2\u0123\u0124\5[.\2\u0124\u012c\3\2\2\2\u0125\u0127")
        buf.write("\5Y-\2\u0126\u0128\5[.\2\u0127\u0126\3\2\2\2\u0127\u0128")
        buf.write("\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\5]/\2\u012a\u012c")
        buf.write("\3\2\2\2\u012b\u0121\3\2\2\2\u012b\u0122\3\2\2\2\u012b")
        buf.write("\u0125\3\2\2\2\u012cX\3\2\2\2\u012d\u012f\t\4\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131Z\3\2\2\2\u0132\u0136\t\5\2")
        buf.write("\2\u0133\u0135\t\4\2\2\u0134\u0133\3\2\2\2\u0135\u0138")
        buf.write("\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\\\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013b\t\6\2\2\u013a")
        buf.write("\u013c\t\7\2\2\u013b\u013a\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013c\u013e\3\2\2\2\u013d\u013f\t\4\2\2\u013e\u013d\3")
        buf.write("\2\2\2\u013f\u0140\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141^\3\2\2\2\u0142\u0143\7\17\2\2\u0143\u0144")
        buf.write("\7\17\2\2\u0144\u0145\7\f\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0147\b\60\2\2\u0147`\3\2\2\2\u0148\u0149\7\17\2\2\u0149")
        buf.write("\u014a\b\61\3\2\u014ab\3\2\2\2\u014b\u014c\7\17\2\2\u014c")
        buf.write("\u014d\7\f\2\2\u014d\u014e\3\2\2\2\u014e\u014f\b\62\4")
        buf.write("\2\u014fd\3\2\2\2\u0150\u0151\7\f\2\2\u0151\u0152\b\63")
        buf.write("\5\2\u0152f\3\2\2\2\u0153\u0155\t\b\2\2\u0154\u0153\3")
        buf.write("\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0159\b\64\6\2\u0159")
        buf.write("h\3\2\2\2\u015a\u015b\7%\2\2\u015b\u015c\7%\2\2\u015c")
        buf.write("\u0160\3\2\2\2\u015d\u015f\n\t\2\2\u015e\u015d\3\2\2\2")
        buf.write("\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3")
        buf.write("\2\2\2\u0161\u0163\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0164")
        buf.write("\b\65\6\2\u0164j\3\2\2\2\u0165\u016f\7$\2\2\u0166\u016e")
        buf.write("\n\n\2\2\u0167\u0168\7^\2\2\u0168\u016e\t\13\2\2\u0169")
        buf.write("\u016b\7)\2\2\u016a\u016c\t\f\2\2\u016b\u016a\3\2\2\2")
        buf.write("\u016b\u016c\3\2\2\2\u016c\u016e\3\2\2\2\u016d\u0166\3")
        buf.write("\2\2\2\u016d\u0167\3\2\2\2\u016d\u0169\3\2\2\2\u016e\u0171")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0172\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\b\66\7")
        buf.write("\2\u0173l\3\2\2\2\u0174\u017e\7$\2\2\u0175\u017d\n\n\2")
        buf.write("\2\u0176\u0177\7^\2\2\u0177\u017d\t\13\2\2\u0178\u017a")
        buf.write("\7)\2\2\u0179\u017b\t\f\2\2\u017a\u0179\3\2\2\2\u017a")
        buf.write("\u017b\3\2\2\2\u017b\u017d\3\2\2\2\u017c\u0175\3\2\2\2")
        buf.write("\u017c\u0176\3\2\2\2\u017c\u0178\3\2\2\2\u017d\u0180\3")
        buf.write("\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0181")
        buf.write("\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7$\2\2\u0182")
        buf.write("\u0183\b\67\b\2\u0183n\3\2\2\2\u0184\u018e\7$\2\2\u0185")
        buf.write("\u018d\n\n\2\2\u0186\u0187\7^\2\2\u0187\u018d\t\13\2\2")
        buf.write("\u0188\u018a\7)\2\2\u0189\u018b\t\f\2\2\u018a\u0189\3")
        buf.write("\2\2\2\u018a\u018b\3\2\2\2\u018b\u018d\3\2\2\2\u018c\u0185")
        buf.write("\3\2\2\2\u018c\u0186\3\2\2\2\u018c\u0188\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018f\3\2\2\2\u018e\u018c\3\2\2\2")
        buf.write("\u018f\u0194\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7")
        buf.write("\17\2\2\u0192\u0195\7\f\2\2\u0193\u0195\t\r\2\2\u0194")
        buf.write("\u0191\3\2\2\2\u0194\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0197\b8\t\2\u0197p\3\2\2\2\u0198\u01a2\7$\2\2")
        buf.write("\u0199\u01a1\n\n\2\2\u019a\u019c\7)\2\2\u019b\u019d\t")
        buf.write("\f\2\2\u019c\u019b\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u01a1")
        buf.write("\3\2\2\2\u019e\u019f\7^\2\2\u019f\u01a1\t\13\2\2\u01a0")
        buf.write("\u0199\3\2\2\2\u01a0\u019a\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a1\u01a4\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a2\u01a0\3")
        buf.write("\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6")
        buf.write("\7^\2\2\u01a6\u01a7\n\13\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01a9\b9\n\2\u01a9r\3\2\2\2\u01aa\u01ab\13\2\2\2\u01ab")
        buf.write("\u01ac\b:\13\2\u01act\3\2\2\2\32\2\u0104\u0109\u0127\u012b")
        buf.write("\u0130\u0136\u013b\u0140\u0156\u0160\u016b\u016d\u016f")
        buf.write("\u017a\u017c\u017e\u018a\u018c\u018e\u0194\u019c\u01a0")
        buf.write("\u01a2\f\3\60\2\3\61\3\3\62\4\3\63\5\b\2\2\3\66\6\3\67")
        buf.write("\7\38\b\39\t\3:\n")
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
    NL1 = 44
    NL2 = 45
    NL3 = 46
    NL4 = 47
    WS = 48
    COMMENT_LINE = 49
    UNCLOSE_STRING = 50
    STRING_LIT = 51
    NEWLINE_STRING = 52
    ILLEGAL_ESCAPE = 53
    ERROR_TOKEN = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'<-'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", 
            "')'", "'['", "']'", "','", "'true'", "'false'", "'\r\r\n'", 
            "'\r'", "'\r\n'", "'\n'" ]

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
            "FALSE_LIT", "REAL_LIT", "NL1", "NL2", "NL3", "NL4", "WS", "COMMENT_LINE", 
            "UNCLOSE_STRING", "STRING_LIT", "NEWLINE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_TOKEN" ]

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
                  "INTPART", "DECPART", "EXPPART", "NL1", "NL2", "NL3", 
                  "NL4", "WS", "COMMENT_LINE", "UNCLOSE_STRING", "STRING_LIT", 
                  "NEWLINE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
            actions[46] = self.NL1_action 
            actions[47] = self.NL2_action 
            actions[48] = self.NL3_action 
            actions[49] = self.NL4_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.STRING_LIT_action 
            actions[54] = self.NEWLINE_STRING_action 
            actions[55] = self.ILLEGAL_ESCAPE_action 
            actions[56] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NL1_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = "\n"
     

    def NL2_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = "\n"
     

    def NL3_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = "\n"
     

    def NL4_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = "\n"
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:])
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text[1:-1]
     

    def NEWLINE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            raise UncloseString(self.text[1:].replace('\r', '').replace('\n','').replace('\f', ''))
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:
            raise ErrorToken(self.text)
     


