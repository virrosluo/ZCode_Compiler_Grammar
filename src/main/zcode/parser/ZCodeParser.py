# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01ed\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\7\2X\n")
        buf.write("\2\f\2\16\2[\13\2\3\2\3\2\3\3\3\3\3\3\5\3b\n\3\3\4\3\4")
        buf.write("\6\4f\n\4\r\4\16\4g\3\4\3\4\6\4l\n\4\r\4\16\4m\5\4p\n")
        buf.write("\4\3\5\3\5\3\6\3\6\5\6v\n\6\3\7\3\7\3\7\7\7{\n\7\f\7\16")
        buf.write("\7~\13\7\3\b\3\b\3\b\3\b\5\b\u0084\n\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\7\t\u008c\n\t\f\t\16\t\u008f\13\t\3\t\3\t\3\t")
        buf.write("\5\t\u0094\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write("\u009f\n\n\5\n\u00a1\n\n\3\13\3\13\3\13\6\13\u00a6\n\13")
        buf.write("\r\13\16\13\u00a7\5\13\u00aa\n\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\7\f\u00b2\n\f\f\f\16\f\u00b5\13\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00c2\n\16\f\16\16")
        buf.write("\16\u00c5\13\16\5\16\u00c7\n\16\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\7\20\u00cf\n\20\f\20\16\20\u00d2\13\20\3\20\3")
        buf.write("\20\6\20\u00d6\n\20\r\20\16\20\u00d7\3\20\5\20\u00db\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\6\21\u00e3\n\21\r\21")
        buf.write("\16\21\u00e4\3\21\3\21\3\21\5\21\u00ea\n\21\3\21\6\21")
        buf.write("\u00ed\n\21\r\21\16\21\u00ee\3\21\5\21\u00f2\n\21\3\22")
        buf.write("\3\22\6\22\u00f6\n\22\r\22\16\22\u00f7\3\23\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u00ff\n\23\3\24\3\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u0108\n\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\7\26\u0110\n\26\f\26\16\26\u0113\13\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\7\27\u011b\n\27\f\27\16\27\u011e\13\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0126\n\30\f\30\16")
        buf.write("\30\u0129\13\30\3\31\3\31\3\31\5\31\u012e\n\31\3\32\3")
        buf.write("\32\3\32\5\32\u0133\n\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\7\33\u013d\n\33\f\33\16\33\u0140\13\33\3\33")
        buf.write("\3\33\7\33\u0144\n\33\f\33\16\33\u0147\13\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u014e\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u0158\n\35\3\36\3\36\3\36\3\36")
        buf.write("\7\36\u015e\n\36\f\36\16\36\u0161\13\36\5\36\u0163\n\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\7\37\u016c\n\37\f")
        buf.write("\37\16\37\u016f\13\37\5\37\u0171\n\37\3\37\3\37\3 \3 ")
        buf.write("\3 \3 \7 \u0179\n \f \16 \u017c\13 \3 \3 \3 \3 \7 \u0182")
        buf.write("\n \f \16 \u0185\13 \3 \3 \5 \u0189\n \3!\3!\3!\3!\7!")
        buf.write("\u018f\n!\f!\16!\u0192\13!\3!\3!\5!\u0196\n!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\7\"\u019f\n\"\f\"\16\"\u01a2\13\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u01a8\n\"\f\"\16\"\u01ab\13\"\3\"\3")
        buf.write("\"\6\"\u01af\n\"\r\"\16\"\u01b0\5\"\u01b3\n\"\3#\3#\3")
        buf.write("#\6#\u01b8\n#\r#\16#\u01b9\3#\3#\6#\u01be\n#\r#\16#\u01bf")
        buf.write("\5#\u01c2\n#\3$\3$\3$\3$\6$\u01c8\n$\r$\16$\u01c9\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3&\7&\u01d6\n&\f&\16&\u01d9\13")
        buf.write("&\3&\3&\7&\u01dd\n&\f&\16&\u01e0\13&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u01e7\n\'\3(\3(\5(\u01eb\n(\3(\2\7*,.\64J)\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLN\2\7\3\2\3\5\4\2\35\"$$\3\2\33\34\3\2\25")
        buf.write("\26\3\2\27\31\2\u020d\2S\3\2\2\2\4a\3\2\2\2\6o\3\2\2\2")
        buf.write("\bq\3\2\2\2\nu\3\2\2\2\fw\3\2\2\2\16\177\3\2\2\2\20\u0085")
        buf.write("\3\2\2\2\22\u00a0\3\2\2\2\24\u00a9\3\2\2\2\26\u00ab\3")
        buf.write("\2\2\2\30\u00b8\3\2\2\2\32\u00c6\3\2\2\2\34\u00c8\3\2")
        buf.write("\2\2\36\u00da\3\2\2\2 \u00f1\3\2\2\2\"\u00f3\3\2\2\2$")
        buf.write("\u00fe\3\2\2\2&\u0100\3\2\2\2(\u0107\3\2\2\2*\u0109\3")
        buf.write("\2\2\2,\u0114\3\2\2\2.\u011f\3\2\2\2\60\u012d\3\2\2\2")
        buf.write("\62\u0132\3\2\2\2\64\u0134\3\2\2\2\66\u014d\3\2\2\28\u0157")
        buf.write("\3\2\2\2:\u0159\3\2\2\2<\u0166\3\2\2\2>\u0188\3\2\2\2")
        buf.write("@\u018a\3\2\2\2B\u0197\3\2\2\2D\u01c1\3\2\2\2F\u01c3\3")
        buf.write("\2\2\2H\u01cb\3\2\2\2J\u01cd\3\2\2\2L\u01e6\3\2\2\2N\u01ea")
        buf.write("\3\2\2\2PR\7\60\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3")
        buf.write("\2\2\2TY\3\2\2\2US\3\2\2\2VX\5\4\3\2WV\3\2\2\2X[\3\2\2")
        buf.write("\2YW\3\2\2\2YZ\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\2\2\3")
        buf.write("]\3\3\2\2\2^b\5\6\4\2_b\5\36\20\2`b\5\24\13\2a^\3\2\2")
        buf.write("\2a_\3\2\2\2a`\3\2\2\2b\5\3\2\2\2ce\5\n\6\2df\7\60\2\2")
        buf.write("ed\3\2\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2hp\3\2\2\2ik\5")
        buf.write("\22\n\2jl\7\60\2\2kj\3\2\2\2lm\3\2\2\2mk\3\2\2\2mn\3\2")
        buf.write("\2\2np\3\2\2\2oc\3\2\2\2oi\3\2\2\2p\7\3\2\2\2qr\t\2\2")
        buf.write("\2r\t\3\2\2\2sv\5\20\t\2tv\5\16\b\2us\3\2\2\2ut\3\2\2")
        buf.write("\2v\13\3\2\2\2w|\7%\2\2xy\7*\2\2y{\7%\2\2zx\3\2\2\2{~")
        buf.write("\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\r\3\2\2\2~|\3\2\2\2\177")
        buf.write("\u0080\5\b\5\2\u0080\u0083\5\f\7\2\u0081\u0082\7\24\2")
        buf.write("\2\u0082\u0084\5$\23\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\17\3\2\2\2\u0085\u0086\5\b\5\2\u0086\u0087")
        buf.write("\7%\2\2\u0087\u0088\7(\2\2\u0088\u008d\5$\23\2\u0089\u008a")
        buf.write("\7*\2\2\u008a\u008c\5$\23\2\u008b\u0089\3\2\2\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0093\7")
        buf.write(")\2\2\u0091\u0092\7\24\2\2\u0092\u0094\5$\23\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\21\3\2\2\2\u0095\u0096")
        buf.write("\7\7\2\2\u0096\u0097\5\f\7\2\u0097\u0098\7\24\2\2\u0098")
        buf.write("\u0099\5$\23\2\u0099\u00a1\3\2\2\2\u009a\u009b\7\b\2\2")
        buf.write("\u009b\u009e\5\f\7\2\u009c\u009d\7\24\2\2\u009d\u009f")
        buf.write("\5$\23\2\u009e\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a1\3\2\2\2\u00a0\u0095\3\2\2\2\u00a0\u009a\3\2\2\2")
        buf.write("\u00a1\23\3\2\2\2\u00a2\u00aa\5\26\f\2\u00a3\u00a5\5\30")
        buf.write("\r\2\u00a4\u00a6\7\60\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a2\3\2\2\2\u00a9\u00a3\3\2\2\2")
        buf.write("\u00aa\25\3\2\2\2\u00ab\u00ac\7\t\2\2\u00ac\u00ad\7%\2")
        buf.write("\2\u00ad\u00ae\7&\2\2\u00ae\u00af\5\32\16\2\u00af\u00b3")
        buf.write("\7\'\2\2\u00b0\u00b2\7\60\2\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\5")
        buf.write("\36\20\2\u00b7\27\3\2\2\2\u00b8\u00b9\7\t\2\2\u00b9\u00ba")
        buf.write("\7%\2\2\u00ba\u00bb\7&\2\2\u00bb\u00bc\5\32\16\2\u00bc")
        buf.write("\u00bd\7\'\2\2\u00bd\31\3\2\2\2\u00be\u00c3\5\34\17\2")
        buf.write("\u00bf\u00c0\7*\2\2\u00c0\u00c2\5\34\17\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c4\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c6\u00be\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\33\3\2")
        buf.write("\2\2\u00c8\u00c9\t\2\2\2\u00c9\u00ca\7%\2\2\u00ca\35\3")
        buf.write("\2\2\2\u00cb\u00cc\7\22\2\2\u00cc\u00d0\7\60\2\2\u00cd")
        buf.write("\u00cf\5 \21\2\u00ce\u00cd\3\2\2\2\u00cf\u00d2\3\2\2\2")
        buf.write("\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\3")
        buf.write("\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d5\7\23\2\2\u00d4")
        buf.write("\u00d6\7\60\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3\2\2")
        buf.write("\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00db")
        buf.write("\3\2\2\2\u00d9\u00db\5 \21\2\u00da\u00cb\3\2\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db\37\3\2\2\2\u00dc\u00f2\5@!\2\u00dd")
        buf.write("\u00f2\5B\"\2\u00de\u00f2\5\6\4\2\u00df\u00f2\5\24\13")
        buf.write("\2\u00e0\u00e2\5$\23\2\u00e1\u00e3\7\60\2\2\u00e2\u00e1")
        buf.write("\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00f2\3\2\2\2\u00e6\u00f2\5F$\2\u00e7")
        buf.write("\u00e9\7\6\2\2\u00e8\u00ea\5$\23\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00ed\7")
        buf.write("\60\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f2\3\2\2\2")
        buf.write("\u00f0\u00f2\5\"\22\2\u00f1\u00dc\3\2\2\2\u00f1\u00dd")
        buf.write("\3\2\2\2\u00f1\u00de\3\2\2\2\u00f1\u00df\3\2\2\2\u00f1")
        buf.write("\u00e0\3\2\2\2\u00f1\u00e6\3\2\2\2\u00f1\u00e7\3\2\2\2")
        buf.write("\u00f1\u00f0\3\2\2\2\u00f2!\3\2\2\2\u00f3\u00f5\7\62\2")
        buf.write("\2\u00f4\u00f6\7\60\2\2\u00f5\u00f4\3\2\2\2\u00f6\u00f7")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("#\3\2\2\2\u00f9\u00fa\5(\25\2\u00fa\u00fb\7#\2\2\u00fb")
        buf.write("\u00fc\5(\25\2\u00fc\u00ff\3\2\2\2\u00fd\u00ff\5(\25\2")
        buf.write("\u00fe\u00f9\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff%\3\2\2")
        buf.write("\2\u0100\u0101\t\3\2\2\u0101\'\3\2\2\2\u0102\u0103\5*")
        buf.write("\26\2\u0103\u0104\5&\24\2\u0104\u0105\5*\26\2\u0105\u0108")
        buf.write("\3\2\2\2\u0106\u0108\5*\26\2\u0107\u0102\3\2\2\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108)\3\2\2\2\u0109\u010a\b\26\1\2\u010a")
        buf.write("\u010b\5,\27\2\u010b\u0111\3\2\2\2\u010c\u010d\f\4\2\2")
        buf.write("\u010d\u010e\t\4\2\2\u010e\u0110\5,\27\2\u010f\u010c\3")
        buf.write("\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112+\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115")
        buf.write("\b\27\1\2\u0115\u0116\5.\30\2\u0116\u011c\3\2\2\2\u0117")
        buf.write("\u0118\f\4\2\2\u0118\u0119\t\5\2\2\u0119\u011b\5.\30\2")
        buf.write("\u011a\u0117\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3")
        buf.write("\2\2\2\u011c\u011d\3\2\2\2\u011d-\3\2\2\2\u011e\u011c")
        buf.write("\3\2\2\2\u011f\u0120\b\30\1\2\u0120\u0121\5\60\31\2\u0121")
        buf.write("\u0127\3\2\2\2\u0122\u0123\f\4\2\2\u0123\u0124\t\6\2\2")
        buf.write("\u0124\u0126\5\60\31\2\u0125\u0122\3\2\2\2\u0126\u0129")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("/\3\2\2\2\u0129\u0127\3\2\2\2\u012a\u012b\7\32\2\2\u012b")
        buf.write("\u012e\5$\23\2\u012c\u012e\5\62\32\2\u012d\u012a\3\2\2")
        buf.write("\2\u012d\u012c\3\2\2\2\u012e\61\3\2\2\2\u012f\u0130\7")
        buf.write("\26\2\2\u0130\u0133\5$\23\2\u0131\u0133\5\64\33\2\u0132")
        buf.write("\u012f\3\2\2\2\u0132\u0131\3\2\2\2\u0133\63\3\2\2\2\u0134")
        buf.write("\u0135\b\33\1\2\u0135\u0136\5\66\34\2\u0136\u0145\3\2")
        buf.write("\2\2\u0137\u0138\f\4\2\2\u0138\u0139\7(\2\2\u0139\u013e")
        buf.write("\5$\23\2\u013a\u013b\7*\2\2\u013b\u013d\5$\23\2\u013c")
        buf.write("\u013a\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e\3")
        buf.write("\2\2\2\u0141\u0142\7)\2\2\u0142\u0144\3\2\2\2\u0143\u0137")
        buf.write("\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\65\3\2\2\2\u0147\u0145\3\2\2\2\u0148")
        buf.write("\u0149\7&\2\2\u0149\u014a\5$\23\2\u014a\u014b\7\'\2\2")
        buf.write("\u014b\u014e\3\2\2\2\u014c\u014e\58\35\2\u014d\u0148\3")
        buf.write("\2\2\2\u014d\u014c\3\2\2\2\u014e\67\3\2\2\2\u014f\u0158")
        buf.write("\7.\2\2\u0150\u0158\7-\2\2\u0151\u0158\7+\2\2\u0152\u0158")
        buf.write("\7,\2\2\u0153\u0158\7/\2\2\u0154\u0158\7%\2\2\u0155\u0158")
        buf.write("\5<\37\2\u0156\u0158\5:\36\2\u0157\u014f\3\2\2\2\u0157")
        buf.write("\u0150\3\2\2\2\u0157\u0151\3\2\2\2\u0157\u0152\3\2\2\2")
        buf.write("\u0157\u0153\3\2\2\2\u0157\u0154\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0157\u0156\3\2\2\2\u01589\3\2\2\2\u0159\u0162")
        buf.write("\7(\2\2\u015a\u015f\5$\23\2\u015b\u015c\7*\2\2\u015c\u015e")
        buf.write("\5$\23\2\u015d\u015b\3\2\2\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0163\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0162\u015a\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\7)\2\2\u0165;\3")
        buf.write("\2\2\2\u0166\u0167\7%\2\2\u0167\u0170\7&\2\2\u0168\u016d")
        buf.write("\5$\23\2\u0169\u016a\7*\2\2\u016a\u016c\5$\23\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u0170\u0168\3\2\2\2\u0170\u0171\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172\u0173\7\'\2\2\u0173=\3\2\2\2\u0174\u0175")
        buf.write("\7&\2\2\u0175\u0176\5$\23\2\u0176\u017a\7\'\2\2\u0177")
        buf.write("\u0179\7\60\2\2\u0178\u0177\3\2\2\2\u0179\u017c\3\2\2")
        buf.write("\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017d")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017d\u017e\5\36\20\2\u017e")
        buf.write("\u0189\3\2\2\2\u017f\u0183\5$\23\2\u0180\u0182\7\60\2")
        buf.write("\2\u0181\u0180\3\2\2\2\u0182\u0185\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0186\3\2\2\2\u0185")
        buf.write("\u0183\3\2\2\2\u0186\u0187\5\36\20\2\u0187\u0189\3\2\2")
        buf.write("\2\u0188\u0174\3\2\2\2\u0188\u017f\3\2\2\2\u0189?\3\2")
        buf.write("\2\2\u018a\u018b\7\17\2\2\u018b\u0190\5> \2\u018c\u018d")
        buf.write("\7\21\2\2\u018d\u018f\5> \2\u018e\u018c\3\2\2\2\u018f")
        buf.write("\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2")
        buf.write("\u0191\u0195\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0194\7")
        buf.write("\20\2\2\u0194\u0196\5\36\20\2\u0195\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196A\3\2\2\2\u0197\u0198\7\n\2\2\u0198")
        buf.write("\u0199\7%\2\2\u0199\u019a\7\13\2\2\u019a\u019b\5$\23\2")
        buf.write("\u019b\u019c\7\f\2\2\u019c\u01a0\5$\23\2\u019d\u019f\7")
        buf.write("\60\2\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01b2\3\2\2\2")
        buf.write("\u01a2\u01a0\3\2\2\2\u01a3\u01b3\5D#\2\u01a4\u01a5\7\22")
        buf.write("\2\2\u01a5\u01a9\7\60\2\2\u01a6\u01a8\5D#\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ac\u01ae\7\23\2\2\u01ad\u01af\7\60\2\2\u01ae\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2\u01a3\3\2\2\2")
        buf.write("\u01b2\u01a4\3\2\2\2\u01b3C\3\2\2\2\u01b4\u01c2\5 \21")
        buf.write("\2\u01b5\u01b7\7\r\2\2\u01b6\u01b8\7\60\2\2\u01b7\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01c2\3\2\2\2\u01bb\u01bd\7\16\2")
        buf.write("\2\u01bc\u01be\7\60\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01c2\3\2\2\2\u01c1\u01b4\3\2\2\2\u01c1\u01b5\3\2\2\2")
        buf.write("\u01c1\u01bb\3\2\2\2\u01c2E\3\2\2\2\u01c3\u01c4\5$\23")
        buf.write("\2\u01c4\u01c5\7\24\2\2\u01c5\u01c7\5$\23\2\u01c6\u01c8")
        buf.write("\7\60\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01caG\3\2\2\2\u01cb")
        buf.write("\u01cc\5J&\2\u01ccI\3\2\2\2\u01cd\u01ce\b&\1\2\u01ce\u01cf")
        buf.write("\5L\'\2\u01cf\u01de\3\2\2\2\u01d0\u01d1\f\4\2\2\u01d1")
        buf.write("\u01d2\7(\2\2\u01d2\u01d7\5$\23\2\u01d3\u01d4\7*\2\2\u01d4")
        buf.write("\u01d6\5$\23\2\u01d5\u01d3\3\2\2\2\u01d6\u01d9\3\2\2\2")
        buf.write("\u01d7\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01da\3")
        buf.write("\2\2\2\u01d9\u01d7\3\2\2\2\u01da\u01db\7)\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01d0\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01dfK\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e1\u01e2\7&\2\2\u01e2\u01e3\5$\23\2")
        buf.write("\u01e3\u01e4\7\'\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e7\5")
        buf.write("N(\2\u01e6\u01e1\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7M\3")
        buf.write("\2\2\2\u01e8\u01eb\7%\2\2\u01e9\u01eb\5<\37\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01e9\3\2\2\2\u01ebO\3\2\2\2<SYagmou|\u0083")
        buf.write("\u008d\u0093\u009e\u00a0\u00a7\u00a9\u00b3\u00c3\u00c6")
        buf.write("\u00d0\u00d7\u00da\u00e4\u00e9\u00ee\u00f1\u00f7\u00fe")
        buf.write("\u0107\u0111\u011c\u0127\u012d\u0132\u013e\u0145\u014d")
        buf.write("\u0157\u015f\u0162\u016d\u0170\u017a\u0183\u0188\u0190")
        buf.write("\u0195\u01a0\u01a9\u01b0\u01b2\u01b9\u01bf\u01c1\u01c9")
        buf.write("\u01d7\u01de\u01e6\u01ea")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'return'", 
                     "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'<-'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "','", "'true'", 
                     "'false'" ]

    symbolicNames = [ "<INVALID>", "NUM_KEYWORD", "BOOL_KEYWORD", "STRING_KEYWORD", 
                      "RETURN_KEYWORD", "VAR_KEYWORD", "DYNAMIC_KEYWORD", 
                      "FUNC_KEYWORD", "FOR_KEYWORD", "UNTIL_KEYWORD", "BY_KEYWORD", 
                      "BREAK_KEYWORD", "CONTINUE_KEYWORD", "IF_KEYWORD", 
                      "ELSE_KEYWORD", "ELIF_KEYWORD", "BEGIN_KEYWORD", "END_KEYWORD", 
                      "ASSIGN_OP", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                      "MOD_OP", "NOT_OP", "AND_OP", "OR_OP", "EQUAL_OP", 
                      "INEQUAL_OP", "LESS_OP", "LESSEQUAL_OP", "LARGE_OP", 
                      "LARGEEQUAL_OP", "CONCAT_OP", "EQUAL_STR_OP", "ID", 
                      "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "SEPARATOR_KEYWORD", "TRUE_LIT", 
                      "FALSE_LIT", "INT_LIT", "REAL_LIT", "STRING_LIT", 
                      "NL", "WS", "COMMENT_LINE", "NEWLINE_STRING", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variable_stat = 2
    RULE_dtype = 3
    RULE_explicit_declare = 4
    RULE_idlist = 5
    RULE_primitive_declare = 6
    RULE_array_declare = 7
    RULE_implicit_declare = 8
    RULE_function_stat = 9
    RULE_function_definition = 10
    RULE_function_declaration = 11
    RULE_param_list = 12
    RULE_parameter = 13
    RULE_block_stat = 14
    RULE_statement = 15
    RULE_comment = 16
    RULE_expression = 17
    RULE_relation_operation = 18
    RULE_relational_expr = 19
    RULE_logical_expr = 20
    RULE_adding_expr = 21
    RULE_multiplying_expr = 22
    RULE_not_logical = 23
    RULE_sign_expr = 24
    RULE_index_expr = 25
    RULE_parenthesis_expr = 26
    RULE_term = 27
    RULE_array_expr = 28
    RULE_function_expr = 29
    RULE_ifst_component = 30
    RULE_control_stat = 31
    RULE_loop_stat = 32
    RULE_loop_body_statement = 33
    RULE_assignment = 34
    RULE_lhs = 35
    RULE_index_variable = 36
    RULE_parenthesis_variable = 37
    RULE_lhs_variable = 38

    ruleNames =  [ "program", "declaration", "variable_stat", "dtype", "explicit_declare", 
                   "idlist", "primitive_declare", "array_declare", "implicit_declare", 
                   "function_stat", "function_definition", "function_declaration", 
                   "param_list", "parameter", "block_stat", "statement", 
                   "comment", "expression", "relation_operation", "relational_expr", 
                   "logical_expr", "adding_expr", "multiplying_expr", "not_logical", 
                   "sign_expr", "index_expr", "parenthesis_expr", "term", 
                   "array_expr", "function_expr", "ifst_component", "control_stat", 
                   "loop_stat", "loop_body_statement", "assignment", "lhs", 
                   "index_variable", "parenthesis_variable", "lhs_variable" ]

    EOF = Token.EOF
    NUM_KEYWORD=1
    BOOL_KEYWORD=2
    STRING_KEYWORD=3
    RETURN_KEYWORD=4
    VAR_KEYWORD=5
    DYNAMIC_KEYWORD=6
    FUNC_KEYWORD=7
    FOR_KEYWORD=8
    UNTIL_KEYWORD=9
    BY_KEYWORD=10
    BREAK_KEYWORD=11
    CONTINUE_KEYWORD=12
    IF_KEYWORD=13
    ELSE_KEYWORD=14
    ELIF_KEYWORD=15
    BEGIN_KEYWORD=16
    END_KEYWORD=17
    ASSIGN_OP=18
    ADD_OP=19
    SUB_OP=20
    MUL_OP=21
    DIV_OP=22
    MOD_OP=23
    NOT_OP=24
    AND_OP=25
    OR_OP=26
    EQUAL_OP=27
    INEQUAL_OP=28
    LESS_OP=29
    LESSEQUAL_OP=30
    LARGE_OP=31
    LARGEEQUAL_OP=32
    CONCAT_OP=33
    EQUAL_STR_OP=34
    ID=35
    LEFT_PARENTHESIS=36
    RIGHT_PARENTHESIS=37
    LEFT_BRACKET=38
    RIGHT_BRACKET=39
    SEPARATOR_KEYWORD=40
    TRUE_LIT=41
    FALSE_LIT=42
    INT_LIT=43
    REAL_LIT=44
    STRING_LIT=45
    NL=46
    WS=47
    COMMENT_LINE=48
    NEWLINE_STRING=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51
    ERROR_TOKEN=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 78
                self.match(ZCodeParser.NL)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD) | (1 << ZCodeParser.RETURN_KEYWORD) | (1 << ZCodeParser.VAR_KEYWORD) | (1 << ZCodeParser.DYNAMIC_KEYWORD) | (1 << ZCodeParser.FUNC_KEYWORD) | (1 << ZCodeParser.FOR_KEYWORD) | (1 << ZCodeParser.IF_KEYWORD) | (1 << ZCodeParser.BEGIN_KEYWORD) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.LEFT_PARENTHESIS) | (1 << ZCodeParser.LEFT_BRACKET) | (1 << ZCodeParser.TRUE_LIT) | (1 << ZCodeParser.FALSE_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.REAL_LIT) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.COMMENT_LINE))) != 0):
                self.state = 84
                self.declaration()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_statContext,0)


        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def function_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Function_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.variable_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.block_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.function_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Explicit_declareContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def implicit_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Implicit_declareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_stat" ):
                return visitor.visitVariable_stat(self)
            else:
                return visitor.visitChildren(self)




    def variable_stat(self):

        localctx = ZCodeParser.Variable_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_stat)
        self._la = 0 # Token type
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.explicit_declare()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 98
                    self.match(ZCodeParser.NL)
                    self.state = 101 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            elif token in [ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.implicit_declare()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 104
                    self.match(ZCodeParser.NL)
                    self.state = 107 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_KEYWORD(self):
            return self.getToken(ZCodeParser.NUM_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(ZCodeParser.BOOL_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(ZCodeParser.STRING_KEYWORD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_dtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDtype" ):
                return visitor.visitDtype(self)
            else:
                return visitor.visitChildren(self)




    def dtype(self):

        localctx = ZCodeParser.DtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declareContext,0)


        def primitive_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Primitive_declareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_explicit_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_declare" ):
                return visitor.visitExplicit_declare(self)
            else:
                return visitor.visitChildren(self)




    def explicit_declare(self):

        localctx = ZCodeParser.Explicit_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_explicit_declare)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.array_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.primitive_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ID)
            else:
                return self.getToken(ZCodeParser.ID, i)

        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = ZCodeParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ZCodeParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SEPARATOR_KEYWORD:
                self.state = 118
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 119
                self.match(ZCodeParser.ID)
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dtype(self):
            return self.getTypedRuleContext(ZCodeParser.DtypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(ZCodeParser.IdlistContext,0)


        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_primitive_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_declare" ):
                return visitor.visitPrimitive_declare(self)
            else:
                return visitor.visitChildren(self)




    def primitive_declare(self):

        localctx = ZCodeParser.Primitive_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primitive_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.dtype()
            self.state = 126
            self.idlist()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OP:
                self.state = 127
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 128
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dtype(self):
            return self.getTypedRuleContext(ZCodeParser.DtypeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = ZCodeParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.dtype()
            self.state = 132
            self.match(ZCodeParser.ID)
            self.state = 133
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 134
            self.expression()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.SEPARATOR_KEYWORD:
                self.state = 135
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 136
                self.expression()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(ZCodeParser.RIGHT_BRACKET)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN_OP:
                self.state = 143
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 144
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KEYWORD(self):
            return self.getToken(ZCodeParser.VAR_KEYWORD, 0)

        def idlist(self):
            return self.getTypedRuleContext(ZCodeParser.IdlistContext,0)


        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def DYNAMIC_KEYWORD(self):
            return self.getToken(ZCodeParser.DYNAMIC_KEYWORD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_declare" ):
                return visitor.visitImplicit_declare(self)
            else:
                return visitor.visitChildren(self)




    def implicit_declare(self):

        localctx = ZCodeParser.Implicit_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicit_declare)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(ZCodeParser.VAR_KEYWORD)
                self.state = 148
                self.idlist()
                self.state = 149
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 150
                self.expression()
                pass
            elif token in [ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(ZCodeParser.DYNAMIC_KEYWORD)
                self.state = 153
                self.idlist()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN_OP:
                    self.state = 154
                    self.match(ZCodeParser.ASSIGN_OP)
                    self.state = 155
                    self.expression()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definition(self):
            return self.getTypedRuleContext(ZCodeParser.Function_definitionContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_stat" ):
                return visitor.visitFunction_stat(self)
            else:
                return visitor.visitChildren(self)




    def function_stat(self):

        localctx = ZCodeParser.Function_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_stat)
        self._la = 0 # Token type
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.function_declaration()
                self.state = 163 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 162
                    self.match(ZCodeParser.NL)
                    self.state = 165 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KEYWORD(self):
            return self.getToken(ZCodeParser.FUNC_KEYWORD, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = ZCodeParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZCodeParser.FUNC_KEYWORD)
            self.state = 170
            self.match(ZCodeParser.ID)
            self.state = 171
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 172
            self.param_list()
            self.state = 173
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 174
                self.match(ZCodeParser.NL)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.block_stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC_KEYWORD(self):
            return self.getToken(ZCodeParser.FUNC_KEYWORD, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def param_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ZCodeParser.FUNC_KEYWORD)
            self.state = 183
            self.match(ZCodeParser.ID)
            self.state = 184
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 185
            self.param_list()
            self.state = 186
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ParameterContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ParameterContext,i)


        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD))) != 0):
                self.state = 188
                self.parameter()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.SEPARATOR_KEYWORD:
                    self.state = 189
                    self.match(ZCodeParser.SEPARATOR_KEYWORD)
                    self.state = 190
                    self.parameter()
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def NUM_KEYWORD(self):
            return self.getToken(ZCodeParser.NUM_KEYWORD, 0)

        def STRING_KEYWORD(self):
            return self.getToken(ZCodeParser.STRING_KEYWORD, 0)

        def BOOL_KEYWORD(self):
            return self.getToken(ZCodeParser.BOOL_KEYWORD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 199
            self.match(ZCodeParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_KEYWORD(self):
            return self.getToken(ZCodeParser.BEGIN_KEYWORD, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def END_KEYWORD(self):
            return self.getToken(ZCodeParser.END_KEYWORD, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stat" ):
                return visitor.visitBlock_stat(self)
            else:
                return visitor.visitChildren(self)




    def block_stat(self):

        localctx = ZCodeParser.Block_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_block_stat)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(ZCodeParser.BEGIN_KEYWORD)
                self.state = 202
                self.match(ZCodeParser.NL)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD) | (1 << ZCodeParser.RETURN_KEYWORD) | (1 << ZCodeParser.VAR_KEYWORD) | (1 << ZCodeParser.DYNAMIC_KEYWORD) | (1 << ZCodeParser.FUNC_KEYWORD) | (1 << ZCodeParser.FOR_KEYWORD) | (1 << ZCodeParser.IF_KEYWORD) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.LEFT_PARENTHESIS) | (1 << ZCodeParser.LEFT_BRACKET) | (1 << ZCodeParser.TRUE_LIT) | (1 << ZCodeParser.FALSE_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.REAL_LIT) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.COMMENT_LINE))) != 0):
                    self.state = 203
                    self.statement()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 209
                self.match(ZCodeParser.END_KEYWORD)
                self.state = 211 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 210
                    self.match(ZCodeParser.NL)
                    self.state = 213 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            elif token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.INT_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT, ZCodeParser.COMMENT_LINE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def control_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Control_statContext,0)


        def loop_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_statContext,0)


        def variable_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_statContext,0)


        def function_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Function_statContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def assignment(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentContext,0)


        def RETURN_KEYWORD(self):
            return self.getToken(ZCodeParser.RETURN_KEYWORD, 0)

        def comment(self):
            return self.getTypedRuleContext(ZCodeParser.CommentContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.control_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.loop_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.variable_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self.function_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 222
                self.expression()
                self.state = 224 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 223
                    self.match(ZCodeParser.NL)
                    self.state = 226 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 229
                self.match(ZCodeParser.RETURN_KEYWORD)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.LEFT_PARENTHESIS) | (1 << ZCodeParser.LEFT_BRACKET) | (1 << ZCodeParser.TRUE_LIT) | (1 << ZCodeParser.FALSE_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.REAL_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                    self.state = 230
                    self.expression()


                self.state = 234 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 233
                    self.match(ZCodeParser.NL)
                    self.state = 236 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 238
                self.comment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT_LINE(self):
            return self.getToken(ZCodeParser.COMMENT_LINE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = ZCodeParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.COMMENT_LINE)
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 242
                self.match(ZCodeParser.NL)
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_exprContext,i)


        def CONCAT_OP(self):
            return self.getToken(ZCodeParser.CONCAT_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.relational_expr()
                self.state = 248
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 249
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.relational_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relation_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_OP(self):
            return self.getToken(ZCodeParser.EQUAL_OP, 0)

        def EQUAL_STR_OP(self):
            return self.getToken(ZCodeParser.EQUAL_STR_OP, 0)

        def INEQUAL_OP(self):
            return self.getToken(ZCodeParser.INEQUAL_OP, 0)

        def LESS_OP(self):
            return self.getToken(ZCodeParser.LESS_OP, 0)

        def LARGE_OP(self):
            return self.getToken(ZCodeParser.LARGE_OP, 0)

        def LESSEQUAL_OP(self):
            return self.getToken(ZCodeParser.LESSEQUAL_OP, 0)

        def LARGEEQUAL_OP(self):
            return self.getToken(ZCodeParser.LARGEEQUAL_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relation_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation_operation" ):
                return visitor.visitRelation_operation(self)
            else:
                return visitor.visitChildren(self)




    def relation_operation(self):

        localctx = ZCodeParser.Relation_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_relation_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_OP) | (1 << ZCodeParser.INEQUAL_OP) | (1 << ZCodeParser.LESS_OP) | (1 << ZCodeParser.LESSEQUAL_OP) | (1 << ZCodeParser.LARGE_OP) | (1 << ZCodeParser.LARGEEQUAL_OP) | (1 << ZCodeParser.EQUAL_STR_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_exprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_exprContext,i)


        def relation_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Relation_operationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_expr" ):
                return visitor.visitRelational_expr(self)
            else:
                return visitor.visitChildren(self)




    def relational_expr(self):

        localctx = ZCodeParser.Relational_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational_expr)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.logical_expr(0)
                self.state = 257
                self.relation_operation()
                self.state = 258
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.logical_expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_exprContext,0)


        def logical_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_exprContext,0)


        def AND_OP(self):
            return self.getToken(ZCodeParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(ZCodeParser.OR_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expr" ):
                return visitor.visitLogical_expr(self)
            else:
                return visitor.visitChildren(self)



    def logical_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 266
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 267
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 268
                    self.adding_expr(0) 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_exprContext,0)


        def adding_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_exprContext,0)


        def ADD_OP(self):
            return self.getToken(ZCodeParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_adding_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_expr" ):
                return visitor.visitAdding_expr(self)
            else:
                return visitor.visitChildren(self)



    def adding_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Adding_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 277
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 278
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 279
                    self.multiplying_expr(0) 
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_logical(self):
            return self.getTypedRuleContext(ZCodeParser.Not_logicalContext,0)


        def multiplying_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_exprContext,0)


        def MUL_OP(self):
            return self.getToken(ZCodeParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(ZCodeParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(ZCodeParser.MOD_OP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_expr" ):
                return visitor.visitMultiplying_expr(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiplying_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.not_logical()
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 288
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 289
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 290
                    self.not_logical() 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_logicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT_OP(self):
            return self.getToken(ZCodeParser.NOT_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def sign_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_not_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_logical" ):
                return visitor.visitNot_logical(self)
            else:
                return visitor.visitChildren(self)




    def not_logical(self):

        localctx = ZCodeParser.Not_logicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_not_logical)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(ZCodeParser.NOT_OP)
                self.state = 297
                self.expression()
                pass
            elif token in [ZCodeParser.SUB_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.INT_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.sign_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB_OP(self):
            return self.getToken(ZCodeParser.SUB_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_expr" ):
                return visitor.visitSign_expr(self)
            else:
                return visitor.visitChildren(self)




    def sign_expr(self):

        localctx = ZCodeParser.Sign_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_sign_expr)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(ZCodeParser.SUB_OP)
                self.state = 302
                self.expression()
                pass
            elif token in [ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.INT_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.index_expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenthesis_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_exprContext,0)


        def index_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Index_exprContext,0)


        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)



    def index_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Index_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_index_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.parenthesis_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 323
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expr)
                    self.state = 309
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 310
                    self.match(ZCodeParser.LEFT_BRACKET)
                    self.state = 311
                    self.expression()
                    self.state = 316
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZCodeParser.SEPARATOR_KEYWORD:
                        self.state = 312
                        self.match(ZCodeParser.SEPARATOR_KEYWORD)
                        self.state = 313
                        self.expression()
                        self.state = 318
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 319
                    self.match(ZCodeParser.RIGHT_BRACKET) 
                self.state = 325
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Parenthesis_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def term(self):
            return self.getTypedRuleContext(ZCodeParser.TermContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parenthesis_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis_expr" ):
                return visitor.visitParenthesis_expr(self)
            else:
                return visitor.visitChildren(self)




    def parenthesis_expr(self):

        localctx = ZCodeParser.Parenthesis_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_parenthesis_expr)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.match(ZCodeParser.LEFT_PARENTHESIS)
                self.state = 327
                self.expression()
                self.state = 328
                self.match(ZCodeParser.RIGHT_PARENTHESIS)
                pass
            elif token in [ZCodeParser.ID, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.INT_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.term()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL_LIT(self):
            return self.getToken(ZCodeParser.REAL_LIT, 0)

        def INT_LIT(self):
            return self.getToken(ZCodeParser.INT_LIT, 0)

        def TRUE_LIT(self):
            return self.getToken(ZCodeParser.TRUE_LIT, 0)

        def FALSE_LIT(self):
            return self.getToken(ZCodeParser.FALSE_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(ZCodeParser.STRING_LIT, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def function_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_exprContext,0)


        def array_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Array_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = ZCodeParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_term)
        try:
            self.state = 341
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(ZCodeParser.REAL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.match(ZCodeParser.INT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.match(ZCodeParser.TRUE_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                self.match(ZCodeParser.FALSE_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 337
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 338
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 339
                self.function_expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 340
                self.array_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expr" ):
                return visitor.visitArray_expr(self)
            else:
                return visitor.visitChildren(self)




    def array_expr(self):

        localctx = ZCodeParser.Array_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.LEFT_PARENTHESIS) | (1 << ZCodeParser.LEFT_BRACKET) | (1 << ZCodeParser.TRUE_LIT) | (1 << ZCodeParser.FALSE_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.REAL_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 344
                self.expression()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.SEPARATOR_KEYWORD:
                    self.state = 345
                    self.match(ZCodeParser.SEPARATOR_KEYWORD)
                    self.state = 346
                    self.expression()
                    self.state = 351
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 354
            self.match(ZCodeParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_expr" ):
                return visitor.visitFunction_expr(self)
            else:
                return visitor.visitChildren(self)




    def function_expr(self):

        localctx = ZCodeParser.Function_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(ZCodeParser.ID)
            self.state = 357
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.LEFT_PARENTHESIS) | (1 << ZCodeParser.LEFT_BRACKET) | (1 << ZCodeParser.TRUE_LIT) | (1 << ZCodeParser.FALSE_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.REAL_LIT) | (1 << ZCodeParser.STRING_LIT))) != 0):
                self.state = 358
                self.expression()
                self.state = 363
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.SEPARATOR_KEYWORD:
                    self.state = 359
                    self.match(ZCodeParser.SEPARATOR_KEYWORD)
                    self.state = 360
                    self.expression()
                    self.state = 365
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 368
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifst_componentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ifst_component

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfst_component" ):
                return visitor.visitIfst_component(self)
            else:
                return visitor.visitChildren(self)




    def ifst_component(self):

        localctx = ZCodeParser.Ifst_componentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifst_component)
        self._la = 0 # Token type
        try:
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.match(ZCodeParser.LEFT_PARENTHESIS)
                self.state = 371
                self.expression()
                self.state = 372
                self.match(ZCodeParser.RIGHT_PARENTHESIS)
                self.state = 376
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 373
                    self.match(ZCodeParser.NL)
                    self.state = 378
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 379
                self.block_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.expression()
                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 382
                    self.match(ZCodeParser.NL)
                    self.state = 387
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 388
                self.block_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Control_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEYWORD(self):
            return self.getToken(ZCodeParser.IF_KEYWORD, 0)

        def ifst_component(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Ifst_componentContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Ifst_componentContext,i)


        def ELIF_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF_KEYWORD)
            else:
                return self.getToken(ZCodeParser.ELIF_KEYWORD, i)

        def ELSE_KEYWORD(self):
            return self.getToken(ZCodeParser.ELSE_KEYWORD, 0)

        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_control_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_stat" ):
                return visitor.visitControl_stat(self)
            else:
                return visitor.visitChildren(self)




    def control_stat(self):

        localctx = ZCodeParser.Control_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_control_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(ZCodeParser.IF_KEYWORD)
            self.state = 393
            self.ifst_component()
            self.state = 398
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 394
                    self.match(ZCodeParser.ELIF_KEYWORD)
                    self.state = 395
                    self.ifst_component() 
                self.state = 400
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 401
                self.match(ZCodeParser.ELSE_KEYWORD)
                self.state = 402
                self.block_stat()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR_KEYWORD(self):
            return self.getToken(ZCodeParser.FOR_KEYWORD, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL_KEYWORD(self):
            return self.getToken(ZCodeParser.UNTIL_KEYWORD, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY_KEYWORD(self):
            return self.getToken(ZCodeParser.BY_KEYWORD, 0)

        def loop_body_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Loop_body_statementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Loop_body_statementContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def BEGIN_KEYWORD(self):
            return self.getToken(ZCodeParser.BEGIN_KEYWORD, 0)

        def END_KEYWORD(self):
            return self.getToken(ZCodeParser.END_KEYWORD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stat" ):
                return visitor.visitLoop_stat(self)
            else:
                return visitor.visitChildren(self)




    def loop_stat(self):

        localctx = ZCodeParser.Loop_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_loop_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(ZCodeParser.FOR_KEYWORD)
            self.state = 406
            self.match(ZCodeParser.ID)
            self.state = 407
            self.match(ZCodeParser.UNTIL_KEYWORD)
            self.state = 408
            self.expression()
            self.state = 409
            self.match(ZCodeParser.BY_KEYWORD)
            self.state = 410
            self.expression()
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 411
                self.match(ZCodeParser.NL)
                self.state = 416
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 432
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.BREAK_KEYWORD, ZCodeParser.CONTINUE_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.INT_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT, ZCodeParser.COMMENT_LINE]:
                self.state = 417
                self.loop_body_statement()
                pass
            elif token in [ZCodeParser.BEGIN_KEYWORD]:
                self.state = 418
                self.match(ZCodeParser.BEGIN_KEYWORD)
                self.state = 419
                self.match(ZCodeParser.NL)
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD) | (1 << ZCodeParser.RETURN_KEYWORD) | (1 << ZCodeParser.VAR_KEYWORD) | (1 << ZCodeParser.DYNAMIC_KEYWORD) | (1 << ZCodeParser.FUNC_KEYWORD) | (1 << ZCodeParser.FOR_KEYWORD) | (1 << ZCodeParser.BREAK_KEYWORD) | (1 << ZCodeParser.CONTINUE_KEYWORD) | (1 << ZCodeParser.IF_KEYWORD) | (1 << ZCodeParser.SUB_OP) | (1 << ZCodeParser.NOT_OP) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.LEFT_PARENTHESIS) | (1 << ZCodeParser.LEFT_BRACKET) | (1 << ZCodeParser.TRUE_LIT) | (1 << ZCodeParser.FALSE_LIT) | (1 << ZCodeParser.INT_LIT) | (1 << ZCodeParser.REAL_LIT) | (1 << ZCodeParser.STRING_LIT) | (1 << ZCodeParser.COMMENT_LINE))) != 0):
                    self.state = 420
                    self.loop_body_statement()
                    self.state = 425
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 426
                self.match(ZCodeParser.END_KEYWORD)
                self.state = 428 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 427
                    self.match(ZCodeParser.NL)
                    self.state = 430 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_body_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def BREAK_KEYWORD(self):
            return self.getToken(ZCodeParser.BREAK_KEYWORD, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def CONTINUE_KEYWORD(self):
            return self.getToken(ZCodeParser.CONTINUE_KEYWORD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_body_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_body_statement" ):
                return visitor.visitLoop_body_statement(self)
            else:
                return visitor.visitChildren(self)




    def loop_body_statement(self):

        localctx = ZCodeParser.Loop_body_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_loop_body_statement)
        self._la = 0 # Token type
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.INT_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT, ZCodeParser.COMMENT_LINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.statement()
                pass
            elif token in [ZCodeParser.BREAK_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
                self.match(ZCodeParser.BREAK_KEYWORD)
                self.state = 437 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 436
                    self.match(ZCodeParser.NL)
                    self.state = 439 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            elif token in [ZCodeParser.CONTINUE_KEYWORD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(ZCodeParser.CONTINUE_KEYWORD)
                self.state = 443 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 442
                    self.match(ZCodeParser.NL)
                    self.state = 445 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ZCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.expression()
            self.state = 450
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 451
            self.expression()
            self.state = 453 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 452
                self.match(ZCodeParser.NL)
                self.state = 455 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Index_variableContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = ZCodeParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.index_variable(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenthesis_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_variableContext,0)


        def index_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Index_variableContext,0)


        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def SEPARATOR_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.SEPARATOR_KEYWORD)
            else:
                return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_index_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_variable" ):
                return visitor.visitIndex_variable(self)
            else:
                return visitor.visitChildren(self)



    def index_variable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Index_variableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_index_variable, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.parenthesis_variable()
            self._ctx.stop = self._input.LT(-1)
            self.state = 476
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Index_variableContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_variable)
                    self.state = 462
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 463
                    self.match(ZCodeParser.LEFT_BRACKET)
                    self.state = 464
                    self.expression()
                    self.state = 469
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZCodeParser.SEPARATOR_KEYWORD:
                        self.state = 465
                        self.match(ZCodeParser.SEPARATOR_KEYWORD)
                        self.state = 466
                        self.expression()
                        self.state = 471
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 472
                    self.match(ZCodeParser.RIGHT_BRACKET) 
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Parenthesis_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.LEFT_PARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def lhs_variable(self):
            return self.getTypedRuleContext(ZCodeParser.Lhs_variableContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parenthesis_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis_variable" ):
                return visitor.visitParenthesis_variable(self)
            else:
                return visitor.visitChildren(self)




    def parenthesis_variable(self):

        localctx = ZCodeParser.Parenthesis_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_parenthesis_variable)
        try:
            self.state = 484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 479
                self.match(ZCodeParser.LEFT_PARENTHESIS)
                self.state = 480
                self.expression()
                self.state = 481
                self.match(ZCodeParser.RIGHT_PARENTHESIS)
                pass
            elif token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 483
                self.lhs_variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_variableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def function_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_lhs_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_variable" ):
                return visitor.visitLhs_variable(self)
            else:
                return visitor.visitChildren(self)




    def lhs_variable(self):

        localctx = ZCodeParser.Lhs_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_lhs_variable)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.function_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[20] = self.logical_expr_sempred
        self._predicates[21] = self.adding_expr_sempred
        self._predicates[22] = self.multiplying_expr_sempred
        self._predicates[25] = self.index_expr_sempred
        self._predicates[36] = self.index_variable_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_expr_sempred(self, localctx:Logical_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_expr_sempred(self, localctx:Adding_exprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_expr_sempred(self, localctx:Multiplying_exprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def index_expr_sempred(self, localctx:Index_exprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def index_variable_sempred(self, localctx:Index_variableContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




