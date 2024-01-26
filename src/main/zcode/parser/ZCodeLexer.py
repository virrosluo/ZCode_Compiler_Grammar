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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u0196\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\6$\u00ff\n$\r$\16$\u0100\3$\7$\u0104\n$\f$")
        buf.write("\16$\u0107\13$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3")
        buf.write("*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3-\3-\3-\3-\3-\5-\u0125")
        buf.write("\n-\3-\3-\5-\u0129\n-\3.\6.\u012c\n.\r.\16.\u012d\3/\3")
        buf.write("/\7/\u0132\n/\f/\16/\u0135\13/\3\60\3\60\5\60\u0139\n")
        buf.write("\60\3\60\6\60\u013c\n\60\r\60\16\60\u013d\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\7\61\u0146\n\61\f\61\16\61\u0149\13")
        buf.write("\61\3\61\3\61\3\61\3\62\5\62\u014f\n\62\3\62\3\62\3\62")
        buf.write("\3\63\6\63\u0155\n\63\r\63\16\63\u0156\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\64\7\64\u015f\n\64\f\64\16\64\u0162\13\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u016c\n")
        buf.write("\65\f\65\16\65\u016f\13\65\3\65\3\65\3\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\7\66\u017a\n\66\f\66\16\66\u017d\13")
        buf.write("\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u0187")
        buf.write("\n\67\f\67\16\67\u018a\13\67\3\67\3\67\3\67\3\67\5\67")
        buf.write("\u0190\n\67\3\67\3\67\38\38\38\5\u0147\u016d\u0188\29")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[\2]\2_\2a/c\60e\61g\62i\63k\64m\65o\66\3\2")
        buf.write("\20\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\60\60\4\2GG")
        buf.write("gg\4\2--//\6\2\f\f\16\17))^^\t\2))^^ddhhppttvv\5\2\13")
        buf.write("\13\17\17\"\"\4\2\f\f\17\17\7\2\f\f\16\17$$))^^\4\2\f")
        buf.write("\f\16\17\5\2$$))^^\3\2$$\2\u01aa\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q")
        buf.write("\3\2\2\2\5x\3\2\2\2\7}\3\2\2\2\t\u0084\3\2\2\2\13\u008b")
        buf.write("\3\2\2\2\r\u008f\3\2\2\2\17\u0097\3\2\2\2\21\u009c\3\2")
        buf.write("\2\2\23\u00a0\3\2\2\2\25\u00a6\3\2\2\2\27\u00a9\3\2\2")
        buf.write("\2\31\u00af\3\2\2\2\33\u00b8\3\2\2\2\35\u00bb\3\2\2\2")
        buf.write("\37\u00c0\3\2\2\2!\u00c5\3\2\2\2#\u00cb\3\2\2\2%\u00cf")
        buf.write("\3\2\2\2\'\u00d2\3\2\2\2)\u00d4\3\2\2\2+\u00d6\3\2\2\2")
        buf.write("-\u00d8\3\2\2\2/\u00da\3\2\2\2\61\u00dc\3\2\2\2\63\u00e0")
        buf.write("\3\2\2\2\65\u00e4\3\2\2\2\67\u00e7\3\2\2\29\u00e9\3\2")
        buf.write("\2\2;\u00ec\3\2\2\2=\u00ee\3\2\2\2?\u00f1\3\2\2\2A\u00f3")
        buf.write("\3\2\2\2C\u00f6\3\2\2\2E\u00fa\3\2\2\2G\u00fe\3\2\2\2")
        buf.write("I\u0108\3\2\2\2K\u010a\3\2\2\2M\u010c\3\2\2\2O\u010e\3")
        buf.write("\2\2\2Q\u0110\3\2\2\2S\u0112\3\2\2\2U\u0117\3\2\2\2W\u011d")
        buf.write("\3\2\2\2Y\u0128\3\2\2\2[\u012b\3\2\2\2]\u012f\3\2\2\2")
        buf.write("_\u0136\3\2\2\2a\u013f\3\2\2\2c\u014e\3\2\2\2e\u0154\3")
        buf.write("\2\2\2g\u015a\3\2\2\2i\u0165\3\2\2\2k\u0173\3\2\2\2m\u0180")
        buf.write("\3\2\2\2o\u0193\3\2\2\2qr\7p\2\2rs\7w\2\2st\7o\2\2tu\7")
        buf.write("d\2\2uv\7g\2\2vw\7t\2\2w\4\3\2\2\2xy\7d\2\2yz\7q\2\2z")
        buf.write("{\7q\2\2{|\7n\2\2|\6\3\2\2\2}~\7u\2\2~\177\7v\2\2\177")
        buf.write("\u0080\7t\2\2\u0080\u0081\7k\2\2\u0081\u0082\7p\2\2\u0082")
        buf.write("\u0083\7i\2\2\u0083\b\3\2\2\2\u0084\u0085\7t\2\2\u0085")
        buf.write("\u0086\7g\2\2\u0086\u0087\7v\2\2\u0087\u0088\7w\2\2\u0088")
        buf.write("\u0089\7t\2\2\u0089\u008a\7p\2\2\u008a\n\3\2\2\2\u008b")
        buf.write("\u008c\7x\2\2\u008c\u008d\7c\2\2\u008d\u008e\7t\2\2\u008e")
        buf.write("\f\3\2\2\2\u008f\u0090\7f\2\2\u0090\u0091\7{\2\2\u0091")
        buf.write("\u0092\7p\2\2\u0092\u0093\7c\2\2\u0093\u0094\7o\2\2\u0094")
        buf.write("\u0095\7k\2\2\u0095\u0096\7e\2\2\u0096\16\3\2\2\2\u0097")
        buf.write("\u0098\7h\2\2\u0098\u0099\7w\2\2\u0099\u009a\7p\2\2\u009a")
        buf.write("\u009b\7e\2\2\u009b\20\3\2\2\2\u009c\u009d\7h\2\2\u009d")
        buf.write("\u009e\7q\2\2\u009e\u009f\7t\2\2\u009f\22\3\2\2\2\u00a0")
        buf.write("\u00a1\7w\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7v\2\2\u00a3")
        buf.write("\u00a4\7k\2\2\u00a4\u00a5\7n\2\2\u00a5\24\3\2\2\2\u00a6")
        buf.write("\u00a7\7d\2\2\u00a7\u00a8\7{\2\2\u00a8\26\3\2\2\2\u00a9")
        buf.write("\u00aa\7d\2\2\u00aa\u00ab\7t\2\2\u00ab\u00ac\7g\2\2\u00ac")
        buf.write("\u00ad\7c\2\2\u00ad\u00ae\7m\2\2\u00ae\30\3\2\2\2\u00af")
        buf.write("\u00b0\7e\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7p\2\2\u00b2")
        buf.write("\u00b3\7v\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5\7p\2\2\u00b5")
        buf.write("\u00b6\7w\2\2\u00b6\u00b7\7g\2\2\u00b7\32\3\2\2\2\u00b8")
        buf.write("\u00b9\7k\2\2\u00b9\u00ba\7h\2\2\u00ba\34\3\2\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7u\2\2\u00be")
        buf.write("\u00bf\7g\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write("\u00c2\7n\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7h\2\2\u00c4")
        buf.write(" \3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7\7g\2\2\u00c7")
        buf.write("\u00c8\7i\2\2\u00c8\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca")
        buf.write("\"\3\2\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7p\2\2\u00cd")
        buf.write("\u00ce\7f\2\2\u00ce$\3\2\2\2\u00cf\u00d0\7>\2\2\u00d0")
        buf.write("\u00d1\7/\2\2\u00d1&\3\2\2\2\u00d2\u00d3\7-\2\2\u00d3")
        buf.write("(\3\2\2\2\u00d4\u00d5\7/\2\2\u00d5*\3\2\2\2\u00d6\u00d7")
        buf.write("\7,\2\2\u00d7,\3\2\2\2\u00d8\u00d9\7\61\2\2\u00d9.\3\2")
        buf.write("\2\2\u00da\u00db\7\'\2\2\u00db\60\3\2\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7q\2\2\u00de\u00df\7v\2\2\u00df\62")
        buf.write("\3\2\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7f\2\2\u00e3\64\3\2\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\66\3\2\2\2\u00e7\u00e8\7?\2\2\u00e88\3\2")
        buf.write("\2\2\u00e9\u00ea\7#\2\2\u00ea\u00eb\7?\2\2\u00eb:\3\2")
        buf.write("\2\2\u00ec\u00ed\7>\2\2\u00ed<\3\2\2\2\u00ee\u00ef\7>")
        buf.write("\2\2\u00ef\u00f0\7?\2\2\u00f0>\3\2\2\2\u00f1\u00f2\7@")
        buf.write("\2\2\u00f2@\3\2\2\2\u00f3\u00f4\7@\2\2\u00f4\u00f5\7?")
        buf.write("\2\2\u00f5B\3\2\2\2\u00f6\u00f7\7\60\2\2\u00f7\u00f8\7")
        buf.write("\60\2\2\u00f8\u00f9\7\60\2\2\u00f9D\3\2\2\2\u00fa\u00fb")
        buf.write("\7?\2\2\u00fb\u00fc\7?\2\2\u00fcF\3\2\2\2\u00fd\u00ff")
        buf.write("\t\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u0105\3\2\2\2")
        buf.write("\u0102\u0104\t\3\2\2\u0103\u0102\3\2\2\2\u0104\u0107\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106H")
        buf.write("\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\7*\2\2\u0109")
        buf.write("J\3\2\2\2\u010a\u010b\7+\2\2\u010bL\3\2\2\2\u010c\u010d")
        buf.write("\7]\2\2\u010dN\3\2\2\2\u010e\u010f\7_\2\2\u010fP\3\2\2")
        buf.write("\2\u0110\u0111\7.\2\2\u0111R\3\2\2\2\u0112\u0113\7v\2")
        buf.write("\2\u0113\u0114\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116\7")
        buf.write("g\2\2\u0116T\3\2\2\2\u0117\u0118\7h\2\2\u0118\u0119\7")
        buf.write("c\2\2\u0119\u011a\7n\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\7g\2\2\u011cV\3\2\2\2\u011d\u011e\5[.\2\u011eX\3\2\2")
        buf.write("\2\u011f\u0120\5[.\2\u0120\u0121\5]/\2\u0121\u0129\3\2")
        buf.write("\2\2\u0122\u0124\5[.\2\u0123\u0125\5]/\2\u0124\u0123\3")
        buf.write("\2\2\2\u0124\u0125\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127")
        buf.write("\5_\60\2\u0127\u0129\3\2\2\2\u0128\u011f\3\2\2\2\u0128")
        buf.write("\u0122\3\2\2\2\u0129Z\3\2\2\2\u012a\u012c\t\4\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\\\3\2\2\2\u012f\u0133\t\5\2")
        buf.write("\2\u0130\u0132\t\4\2\2\u0131\u0130\3\2\2\2\u0132\u0135")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("^\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0138\t\6\2\2\u0137")
        buf.write("\u0139\t\7\2\2\u0138\u0137\3\2\2\2\u0138\u0139\3\2\2\2")
        buf.write("\u0139\u013b\3\2\2\2\u013a\u013c\t\4\2\2\u013b\u013a\3")
        buf.write("\2\2\2\u013c\u013d\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e")
        buf.write("\3\2\2\2\u013e`\3\2\2\2\u013f\u0147\7$\2\2\u0140\u0146")
        buf.write("\n\b\2\2\u0141\u0142\7^\2\2\u0142\u0146\t\t\2\2\u0143")
        buf.write("\u0144\7)\2\2\u0144\u0146\7$\2\2\u0145\u0140\3\2\2\2\u0145")
        buf.write("\u0141\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0149\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u014a\3")
        buf.write("\2\2\2\u0149\u0147\3\2\2\2\u014a\u014b\7$\2\2\u014b\u014c")
        buf.write("\b\61\2\2\u014cb\3\2\2\2\u014d\u014f\7t\2\2\u014e\u014d")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("\u0151\7\f\2\2\u0151\u0152\b\62\3\2\u0152d\3\2\2\2\u0153")
        buf.write("\u0155\t\n\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u0159\b\63\4\2\u0159f\3\2\2\2\u015a\u015b")
        buf.write("\7%\2\2\u015b\u015c\7%\2\2\u015c\u0160\3\2\2\2\u015d\u015f")
        buf.write("\n\13\2\2\u015e\u015d\3\2\2\2\u015f\u0162\3\2\2\2\u0160")
        buf.write("\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0163\u0164\b\64\4\2\u0164h\3\2\2")
        buf.write("\2\u0165\u016d\7$\2\2\u0166\u016c\n\f\2\2\u0167\u0168")
        buf.write("\7^\2\2\u0168\u016c\t\t\2\2\u0169\u016a\7)\2\2\u016a\u016c")
        buf.write("\7$\2\2\u016b\u0166\3\2\2\2\u016b\u0167\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u0170\u0171\t\r\2\2\u0171\u0172\b\65\5\2\u0172")
        buf.write("j\3\2\2\2\u0173\u017b\7$\2\2\u0174\u017a\n\f\2\2\u0175")
        buf.write("\u0176\7^\2\2\u0176\u017a\t\t\2\2\u0177\u0178\7)\2\2\u0178")
        buf.write("\u017a\7$\2\2\u0179\u0174\3\2\2\2\u0179\u0175\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d\u017b")
        buf.write("\3\2\2\2\u017e\u017f\b\66\6\2\u017fl\3\2\2\2\u0180\u0188")
        buf.write("\7$\2\2\u0181\u0187\n\16\2\2\u0182\u0183\7)\2\2\u0183")
        buf.write("\u0187\7$\2\2\u0184\u0185\7^\2\2\u0185\u0187\t\t\2\2\u0186")
        buf.write("\u0181\3\2\2\2\u0186\u0182\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u018a\3\2\2\2\u0188\u0189\3\2\2\2\u0188\u0186\3")
        buf.write("\2\2\2\u0189\u018f\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018c")
        buf.write("\7^\2\2\u018c\u0190\n\t\2\2\u018d\u018e\7)\2\2\u018e\u0190")
        buf.write("\n\17\2\2\u018f\u018b\3\2\2\2\u018f\u018d\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0192\b\67\7\2\u0192n\3\2\2\2\u0193")
        buf.write("\u0194\13\2\2\2\u0194\u0195\b8\b\2\u0195p\3\2\2\2\27\2")
        buf.write("\u0100\u0105\u0124\u0128\u012d\u0133\u0138\u013d\u0145")
        buf.write("\u0147\u014e\u0156\u0160\u016b\u016d\u0179\u017b\u0186")
        buf.write("\u0188\u018f\t\3\61\2\3\62\3\b\2\2\3\65\4\3\66\5\3\67")
        buf.write("\6\38\7")
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
    INT_LIT = 43
    REAL_LIT = 44
    STRING_LIT = 45
    NL = 46
    WS = 47
    COMMENT_LINE = 48
    NEWLINE_STRING = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_TOKEN = 52

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
            "FALSE_LIT", "INT_LIT", "REAL_LIT", "STRING_LIT", "NL", "WS", 
            "COMMENT_LINE", "NEWLINE_STRING", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
                  "SEPARATOR_KEYWORD", "TRUE_LIT", "FALSE_LIT", "INT_LIT", 
                  "REAL_LIT", "INTPART", "DECPART", "EXPPART", "STRING_LIT", 
                  "NL", "WS", "COMMENT_LINE", "NEWLINE_STRING", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

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
            actions[47] = self.STRING_LIT_action 
            actions[48] = self.NL_action 
            actions[51] = self.NEWLINE_STRING_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.ERROR_TOKEN_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('\r','')
     

    def NEWLINE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:-1])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     

    def ERROR_TOKEN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


