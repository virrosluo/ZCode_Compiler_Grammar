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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\u01b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3m\n\3\3\4\3\4\3\5\3\5\3\5\3\5\5\5u\n\5")
        buf.write("\3\6\3\6\3\6\3\6\5\6{\n\6\3\7\3\7\5\7\177\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u0087\n\b\3\t\3\t\3\n\3\n\5\n\u008d")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u0094\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u009e\n\f\3\r\3\r\3\r\5\r")
        buf.write("\u00a3\n\r\3\16\3\16\3\16\3\16\5\16\u00a9\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b4\n\17")
        buf.write("\5\17\u00b6\n\17\3\20\3\20\5\20\u00ba\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c4\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u00d1")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u00d8\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00e3\n\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00f0\n\26\3\27\3\27\3\27\3\27\5\27\u00f6\n\27\3")
        buf.write("\30\3\30\3\30\5\30\u00fb\n\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\5\35\u0113\n\35\3\36\3")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\5\37\u011c\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \7 \u0124\n \f \16 \u0127\13 \3!\3!\3!\3!\3!")
        buf.write("\3!\7!\u012f\n!\f!\16!\u0132\13!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\7\"\u013a\n\"\f\"\16\"\u013d\13\"\3#\3#\3#\5#\u0142")
        buf.write("\n#\3$\3$\3$\5$\u0147\n$\3%\3%\5%\u014b\n%\3%\3%\3%\3")
        buf.write("%\3%\5%\u0152\n%\3&\3&\3&\3&\3&\5&\u0159\n&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\5\'\u0162\n\'\3(\3(\3(\3(\3)\3)\3)")
        buf.write("\3)\3)\3*\3*\3*\3*\5*\u0171\n*\3+\3+\3+\3+\3+\5+\u0178")
        buf.write("\n+\3,\3,\3,\3-\3-\3-\3-\3-\5-\u0182\n-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\5.\u018c\n.\3/\3/\3/\3/\3/\5/\u0193\n/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\5\60\u019b\n\60\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u01ac\n\62\3\62\3\62\3\62\3\62\3\62\2")
        buf.write("\5>@B\63\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b\2\b\4\2..\60\61")
        buf.write("\3\2\3\5\4\2\35\"$$\3\2\33\34\3\2\25\26\3\2\27\31\2\u01b2")
        buf.write("\2d\3\2\2\2\4l\3\2\2\2\6n\3\2\2\2\bt\3\2\2\2\nz\3\2\2")
        buf.write("\2\f~\3\2\2\2\16\u0086\3\2\2\2\20\u0088\3\2\2\2\22\u008c")
        buf.write("\3\2\2\2\24\u008e\3\2\2\2\26\u0095\3\2\2\2\30\u00a2\3")
        buf.write("\2\2\2\32\u00a8\3\2\2\2\34\u00b5\3\2\2\2\36\u00b9\3\2")
        buf.write("\2\2 \u00bb\3\2\2\2\"\u00c5\3\2\2\2$\u00d0\3\2\2\2&\u00d7")
        buf.write("\3\2\2\2(\u00e2\3\2\2\2*\u00ef\3\2\2\2,\u00f5\3\2\2\2")
        buf.write(".\u00f7\3\2\2\2\60\u00fe\3\2\2\2\62\u0101\3\2\2\2\64\u0104")
        buf.write("\3\2\2\2\66\u010a\3\2\2\28\u0112\3\2\2\2:\u0114\3\2\2")
        buf.write("\2<\u011b\3\2\2\2>\u011d\3\2\2\2@\u0128\3\2\2\2B\u0133")
        buf.write("\3\2\2\2D\u0141\3\2\2\2F\u0146\3\2\2\2H\u0151\3\2\2\2")
        buf.write("J\u0158\3\2\2\2L\u0161\3\2\2\2N\u0163\3\2\2\2P\u0167\3")
        buf.write("\2\2\2R\u0170\3\2\2\2T\u0177\3\2\2\2V\u0179\3\2\2\2X\u0181")
        buf.write("\3\2\2\2Z\u0183\3\2\2\2\\\u0192\3\2\2\2^\u0194\3\2\2\2")
        buf.write("`\u019c\3\2\2\2b\u01ab\3\2\2\2de\5\b\5\2ef\5\4\3\2fg\7")
        buf.write("\2\2\3g\3\3\2\2\2hi\5\f\7\2ij\5\4\3\2jm\3\2\2\2km\5\f")
        buf.write("\7\2lh\3\2\2\2lk\3\2\2\2m\5\3\2\2\2no\t\2\2\2o\7\3\2\2")
        buf.write("\2pq\5\6\4\2qr\5\b\5\2ru\3\2\2\2su\3\2\2\2tp\3\2\2\2t")
        buf.write("s\3\2\2\2u\t\3\2\2\2vw\5\6\4\2wx\5\n\6\2x{\3\2\2\2y{\5")
        buf.write("\6\4\2zv\3\2\2\2zy\3\2\2\2{\13\3\2\2\2|\177\5\16\b\2}")
        buf.write("\177\5\36\20\2~|\3\2\2\2~}\3\2\2\2\177\r\3\2\2\2\u0080")
        buf.write("\u0081\5\22\n\2\u0081\u0082\5\n\6\2\u0082\u0087\3\2\2")
        buf.write("\2\u0083\u0084\5\34\17\2\u0084\u0085\5\n\6\2\u0085\u0087")
        buf.write("\3\2\2\2\u0086\u0080\3\2\2\2\u0086\u0083\3\2\2\2\u0087")
        buf.write("\17\3\2\2\2\u0088\u0089\t\3\2\2\u0089\21\3\2\2\2\u008a")
        buf.write("\u008d\5\26\f\2\u008b\u008d\5\24\13\2\u008c\u008a\3\2")
        buf.write("\2\2\u008c\u008b\3\2\2\2\u008d\23\3\2\2\2\u008e\u008f")
        buf.write("\5\20\t\2\u008f\u0093\7%\2\2\u0090\u0091\7\24\2\2\u0091")
        buf.write("\u0094\58\35\2\u0092\u0094\3\2\2\2\u0093\u0090\3\2\2\2")
        buf.write("\u0093\u0092\3\2\2\2\u0094\25\3\2\2\2\u0095\u0096\5\20")
        buf.write("\t\2\u0096\u0097\7%\2\2\u0097\u0098\7(\2\2\u0098\u0099")
        buf.write("\5\30\r\2\u0099\u009d\7)\2\2\u009a\u009b\7\24\2\2\u009b")
        buf.write("\u009e\58\35\2\u009c\u009e\3\2\2\2\u009d\u009a\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\27\3\2\2\2\u009f\u00a0\7-\2")
        buf.write("\2\u00a0\u00a3\5\32\16\2\u00a1\u00a3\7-\2\2\u00a2\u009f")
        buf.write("\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\31\3\2\2\2\u00a4\u00a5")
        buf.write("\7*\2\2\u00a5\u00a6\7-\2\2\u00a6\u00a9\5\32\16\2\u00a7")
        buf.write("\u00a9\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a9\33\3\2\2\2\u00aa\u00ab\7\7\2\2\u00ab\u00ac\7%\2")
        buf.write("\2\u00ac\u00ad\7\24\2\2\u00ad\u00b6\58\35\2\u00ae\u00af")
        buf.write("\7\b\2\2\u00af\u00b3\7%\2\2\u00b0\u00b1\7\24\2\2\u00b1")
        buf.write("\u00b4\58\35\2\u00b2\u00b4\3\2\2\2\u00b3\u00b0\3\2\2\2")
        buf.write("\u00b3\u00b2\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00aa\3")
        buf.write("\2\2\2\u00b5\u00ae\3\2\2\2\u00b6\35\3\2\2\2\u00b7\u00ba")
        buf.write("\5 \21\2\u00b8\u00ba\5\"\22\2\u00b9\u00b7\3\2\2\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00ba\37\3\2\2\2\u00bb\u00bc\7\t\2\2\u00bc")
        buf.write("\u00bd\7%\2\2\u00bd\u00be\7&\2\2\u00be\u00bf\5$\23\2\u00bf")
        buf.write("\u00c0\7\'\2\2\u00c0\u00c3\5\b\5\2\u00c1\u00c4\5\64\33")
        buf.write("\2\u00c2\u00c4\5.\30\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4!\3\2\2\2\u00c5\u00c6\7\t\2\2\u00c6\u00c7")
        buf.write("\7%\2\2\u00c7\u00c8\7&\2\2\u00c8\u00c9\5$\23\2\u00c9\u00ca")
        buf.write("\7\'\2\2\u00ca\u00cb\5\n\6\2\u00cb#\3\2\2\2\u00cc\u00cd")
        buf.write("\5(\25\2\u00cd\u00ce\5&\24\2\u00ce\u00d1\3\2\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00cc\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1%\3\2\2\2\u00d2\u00d3\7*\2\2\u00d3\u00d4\5(\25\2")
        buf.write("\u00d4\u00d5\5&\24\2\u00d5\u00d8\3\2\2\2\u00d6\u00d8\3")
        buf.write("\2\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\'")
        buf.write("\3\2\2\2\u00d9\u00da\5\20\t\2\u00da\u00db\7%\2\2\u00db")
        buf.write("\u00e3\3\2\2\2\u00dc\u00dd\5\20\t\2\u00dd\u00de\7%\2\2")
        buf.write("\u00de\u00df\7(\2\2\u00df\u00e0\5V,\2\u00e0\u00e1\7)\2")
        buf.write("\2\u00e1\u00e3\3\2\2\2\u00e2\u00d9\3\2\2\2\u00e2\u00dc")
        buf.write("\3\2\2\2\u00e3)\3\2\2\2\u00e4\u00f0\5Z.\2\u00e5\u00f0")
        buf.write("\5`\61\2\u00e6\u00f0\5\16\b\2\u00e7\u00f0\5\64\33\2\u00e8")
        buf.write("\u00e9\5P)\2\u00e9\u00ea\5\n\6\2\u00ea\u00f0\3\2\2\2\u00eb")
        buf.write("\u00f0\5b\62\2\u00ec\u00f0\5.\30\2\u00ed\u00f0\5\60\31")
        buf.write("\2\u00ee\u00f0\5\62\32\2\u00ef\u00e4\3\2\2\2\u00ef\u00e5")
        buf.write("\3\2\2\2\u00ef\u00e6\3\2\2\2\u00ef\u00e7\3\2\2\2\u00ef")
        buf.write("\u00e8\3\2\2\2\u00ef\u00eb\3\2\2\2\u00ef\u00ec\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0+\3\2\2")
        buf.write("\2\u00f1\u00f2\5*\26\2\u00f2\u00f3\5,\27\2\u00f3\u00f6")
        buf.write("\3\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f1\3\2\2\2\u00f5")
        buf.write("\u00f4\3\2\2\2\u00f6-\3\2\2\2\u00f7\u00fa\7\6\2\2\u00f8")
        buf.write("\u00fb\58\35\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\5")
        buf.write("\n\6\2\u00fd/\3\2\2\2\u00fe\u00ff\7\r\2\2\u00ff\u0100")
        buf.write("\5\n\6\2\u0100\61\3\2\2\2\u0101\u0102\7\16\2\2\u0102\u0103")
        buf.write("\5\n\6\2\u0103\63\3\2\2\2\u0104\u0105\7\22\2\2\u0105\u0106")
        buf.write("\5\n\6\2\u0106\u0107\5,\27\2\u0107\u0108\7\23\2\2\u0108")
        buf.write("\u0109\5\n\6\2\u0109\65\3\2\2\2\u010a\u010b\7\63\2\2\u010b")
        buf.write("\u010c\5\n\6\2\u010c\67\3\2\2\2\u010d\u010e\5<\37\2\u010e")
        buf.write("\u010f\7#\2\2\u010f\u0110\5<\37\2\u0110\u0113\3\2\2\2")
        buf.write("\u0111\u0113\5<\37\2\u0112\u010d\3\2\2\2\u0112\u0111\3")
        buf.write("\2\2\2\u01139\3\2\2\2\u0114\u0115\t\4\2\2\u0115;\3\2\2")
        buf.write("\2\u0116\u0117\5> \2\u0117\u0118\5:\36\2\u0118\u0119\5")
        buf.write("> \2\u0119\u011c\3\2\2\2\u011a\u011c\5> \2\u011b\u0116")
        buf.write("\3\2\2\2\u011b\u011a\3\2\2\2\u011c=\3\2\2\2\u011d\u011e")
        buf.write("\b \1\2\u011e\u011f\5@!\2\u011f\u0125\3\2\2\2\u0120\u0121")
        buf.write("\f\4\2\2\u0121\u0122\t\5\2\2\u0122\u0124\5@!\2\u0123\u0120")
        buf.write("\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126?\3\2\2\2\u0127\u0125\3\2\2\2\u0128")
        buf.write("\u0129\b!\1\2\u0129\u012a\5B\"\2\u012a\u0130\3\2\2\2\u012b")
        buf.write("\u012c\f\4\2\2\u012c\u012d\t\6\2\2\u012d\u012f\5B\"\2")
        buf.write("\u012e\u012b\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131A\3\2\2\2\u0132\u0130")
        buf.write("\3\2\2\2\u0133\u0134\b\"\1\2\u0134\u0135\5D#\2\u0135\u013b")
        buf.write("\3\2\2\2\u0136\u0137\f\4\2\2\u0137\u0138\t\7\2\2\u0138")
        buf.write("\u013a\5D#\2\u0139\u0136\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013cC\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013e\u013f\7\32\2\2\u013f\u0142\58\35")
        buf.write("\2\u0140\u0142\5F$\2\u0141\u013e\3\2\2\2\u0141\u0140\3")
        buf.write("\2\2\2\u0142E\3\2\2\2\u0143\u0144\7\26\2\2\u0144\u0147")
        buf.write("\58\35\2\u0145\u0147\5H%\2\u0146\u0143\3\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0147G\3\2\2\2\u0148\u014b\7%\2\2\u0149\u014b")
        buf.write("\5P)\2\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014d\7(\2\2\u014d\u014e\5V,\2\u014e\u014f")
        buf.write("\7)\2\2\u014f\u0152\3\2\2\2\u0150\u0152\5J&\2\u0151\u014a")
        buf.write("\3\2\2\2\u0151\u0150\3\2\2\2\u0152I\3\2\2\2\u0153\u0154")
        buf.write("\7&\2\2\u0154\u0155\58\35\2\u0155\u0156\7\'\2\2\u0156")
        buf.write("\u0159\3\2\2\2\u0157\u0159\5L\'\2\u0158\u0153\3\2\2\2")
        buf.write("\u0158\u0157\3\2\2\2\u0159K\3\2\2\2\u015a\u0162\7-\2\2")
        buf.write("\u015b\u0162\7+\2\2\u015c\u0162\7,\2\2\u015d\u0162\7\65")
        buf.write("\2\2\u015e\u0162\7%\2\2\u015f\u0162\5P)\2\u0160\u0162")
        buf.write("\5N(\2\u0161\u015a\3\2\2\2\u0161\u015b\3\2\2\2\u0161\u015c")
        buf.write("\3\2\2\2\u0161\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0161\u0160\3\2\2\2\u0162M\3\2\2\2\u0163")
        buf.write("\u0164\7(\2\2\u0164\u0165\5V,\2\u0165\u0166\7)\2\2\u0166")
        buf.write("O\3\2\2\2\u0167\u0168\7%\2\2\u0168\u0169\7&\2\2\u0169")
        buf.write("\u016a\5R*\2\u016a\u016b\7\'\2\2\u016bQ\3\2\2\2\u016c")
        buf.write("\u016d\58\35\2\u016d\u016e\5T+\2\u016e\u0171\3\2\2\2\u016f")
        buf.write("\u0171\3\2\2\2\u0170\u016c\3\2\2\2\u0170\u016f\3\2\2\2")
        buf.write("\u0171S\3\2\2\2\u0172\u0173\7*\2\2\u0173\u0174\58\35\2")
        buf.write("\u0174\u0175\5T+\2\u0175\u0178\3\2\2\2\u0176\u0178\3\2")
        buf.write("\2\2\u0177\u0172\3\2\2\2\u0177\u0176\3\2\2\2\u0178U\3")
        buf.write("\2\2\2\u0179\u017a\58\35\2\u017a\u017b\5X-\2\u017bW\3")
        buf.write("\2\2\2\u017c\u017d\7*\2\2\u017d\u017e\58\35\2\u017e\u017f")
        buf.write("\5X-\2\u017f\u0182\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017c")
        buf.write("\3\2\2\2\u0181\u0180\3\2\2\2\u0182Y\3\2\2\2\u0183\u0184")
        buf.write("\7\17\2\2\u0184\u0185\5^\60\2\u0185\u018b\5\\/\2\u0186")
        buf.write("\u0187\7\20\2\2\u0187\u0188\5\b\5\2\u0188\u0189\5*\26")
        buf.write("\2\u0189\u018c\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u0186")
        buf.write("\3\2\2\2\u018b\u018a\3\2\2\2\u018c[\3\2\2\2\u018d\u018e")
        buf.write("\7\21\2\2\u018e\u018f\5^\60\2\u018f\u0190\5\\/\2\u0190")
        buf.write("\u0193\3\2\2\2\u0191\u0193\3\2\2\2\u0192\u018d\3\2\2\2")
        buf.write("\u0192\u0191\3\2\2\2\u0193]\3\2\2\2\u0194\u0195\7&\2\2")
        buf.write("\u0195\u0196\58\35\2\u0196\u0197\7\'\2\2\u0197\u019a\5")
        buf.write("\b\5\2\u0198\u019b\5*\26\2\u0199\u019b\3\2\2\2\u019a\u0198")
        buf.write("\3\2\2\2\u019a\u0199\3\2\2\2\u019b_\3\2\2\2\u019c\u019d")
        buf.write("\7\n\2\2\u019d\u019e\7%\2\2\u019e\u019f\7\13\2\2\u019f")
        buf.write("\u01a0\58\35\2\u01a0\u01a1\7\f\2\2\u01a1\u01a2\58\35\2")
        buf.write("\u01a2\u01a3\5\b\5\2\u01a3\u01a4\5*\26\2\u01a4a\3\2\2")
        buf.write("\2\u01a5\u01ac\7%\2\2\u01a6\u01a7\7%\2\2\u01a7\u01a8\7")
        buf.write("(\2\2\u01a8\u01a9\5V,\2\u01a9\u01aa\7)\2\2\u01aa\u01ac")
        buf.write("\3\2\2\2\u01ab\u01a5\3\2\2\2\u01ab\u01a6\3\2\2\2\u01ac")
        buf.write("\u01ad\3\2\2\2\u01ad\u01ae\7\24\2\2\u01ae\u01af\58\35")
        buf.write("\2\u01af\u01b0\5\n\6\2\u01b0c\3\2\2\2(ltz~\u0086\u008c")
        buf.write("\u0093\u009d\u00a2\u00a8\u00b3\u00b5\u00b9\u00c3\u00d0")
        buf.write("\u00d7\u00e2\u00ef\u00f5\u00fa\u0112\u011b\u0125\u0130")
        buf.write("\u013b\u0141\u0146\u014a\u0151\u0158\u0161\u0170\u0177")
        buf.write("\u0181\u018b\u0192\u019a\u01ab")
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
                     "'false'", "<INVALID>", "'\r\r\n'", "'\r'", "'\r\n'", 
                     "'\n'" ]

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
                      "FALSE_LIT", "REAL_LIT", "NL1", "NL2", "NL3", "NL4", 
                      "WS", "COMMENT_LINE", "UNCLOSE_STRING", "STRING_LIT", 
                      "NEWLINE_STRING", "ILLEGAL_ESCAPE", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_nl_type = 2
    RULE_nl_nullable_list = 3
    RULE_nl_list = 4
    RULE_declaration = 5
    RULE_variable_stat = 6
    RULE_dtype = 7
    RULE_explicit_declare = 8
    RULE_primitive_declare = 9
    RULE_array_declare = 10
    RULE_numlit_list = 11
    RULE_numlit_tail = 12
    RULE_implicit_declare = 13
    RULE_function_stat = 14
    RULE_function_definition = 15
    RULE_function_declaration = 16
    RULE_param_list = 17
    RULE_param_list_tail = 18
    RULE_parameter = 19
    RULE_statement = 20
    RULE_statement_list = 21
    RULE_return_stat = 22
    RULE_break_stat = 23
    RULE_continue_stat = 24
    RULE_block_stat = 25
    RULE_comment = 26
    RULE_expression = 27
    RULE_relation_operation = 28
    RULE_relational_expr = 29
    RULE_logical_expr = 30
    RULE_adding_expr = 31
    RULE_multiplying_expr = 32
    RULE_not_logical = 33
    RULE_sign_expr = 34
    RULE_index_expr = 35
    RULE_parenthesis_expr = 36
    RULE_term = 37
    RULE_array_expr = 38
    RULE_function_expr = 39
    RULE_expression_list = 40
    RULE_expression_list_tail = 41
    RULE_expression_nonempty_list = 42
    RULE_expression_nonempty_tail = 43
    RULE_control_stat = 44
    RULE_elif_stmt_list = 45
    RULE_ifst_component = 46
    RULE_loop_stat = 47
    RULE_assignment = 48

    ruleNames =  [ "program", "decl_list", "nl_type", "nl_nullable_list", 
                   "nl_list", "declaration", "variable_stat", "dtype", "explicit_declare", 
                   "primitive_declare", "array_declare", "numlit_list", 
                   "numlit_tail", "implicit_declare", "function_stat", "function_definition", 
                   "function_declaration", "param_list", "param_list_tail", 
                   "parameter", "statement", "statement_list", "return_stat", 
                   "break_stat", "continue_stat", "block_stat", "comment", 
                   "expression", "relation_operation", "relational_expr", 
                   "logical_expr", "adding_expr", "multiplying_expr", "not_logical", 
                   "sign_expr", "index_expr", "parenthesis_expr", "term", 
                   "array_expr", "function_expr", "expression_list", "expression_list_tail", 
                   "expression_nonempty_list", "expression_nonempty_tail", 
                   "control_stat", "elif_stmt_list", "ifst_component", "loop_stat", 
                   "assignment" ]

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
    REAL_LIT=43
    NL1=44
    NL2=45
    NL3=46
    NL4=47
    WS=48
    COMMENT_LINE=49
    UNCLOSE_STRING=50
    STRING_LIT=51
    NEWLINE_STRING=52
    ILLEGAL_ESCAPE=53
    ERROR_TOKEN=54

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

        def nl_nullable_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_nullable_listContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.nl_nullable_list()
            self.state = 99
            self.decl_list()
            self.state = 100
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(ZCodeParser.DeclarationContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.declaration()
                self.state = 103
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nl_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL1(self):
            return self.getToken(ZCodeParser.NL1, 0)

        def NL3(self):
            return self.getToken(ZCodeParser.NL3, 0)

        def NL4(self):
            return self.getToken(ZCodeParser.NL4, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_nl_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNl_type" ):
                return visitor.visitNl_type(self)
            else:
                return visitor.visitChildren(self)




    def nl_type(self):

        localctx = ZCodeParser.Nl_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nl_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NL1) | (1 << ZCodeParser.NL3) | (1 << ZCodeParser.NL4))) != 0)):
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


    class Nl_nullable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nl_type(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_typeContext,0)


        def nl_nullable_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_nullable_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nl_nullable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNl_nullable_list" ):
                return visitor.visitNl_nullable_list(self)
            else:
                return visitor.visitChildren(self)




    def nl_nullable_list(self):

        localctx = ZCodeParser.Nl_nullable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nl_nullable_list)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NL1, ZCodeParser.NL3, ZCodeParser.NL4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.nl_type()
                self.state = 111
                self.nl_nullable_list()
                pass
            elif token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.BREAK_KEYWORD, ZCodeParser.CONTINUE_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.ELSE_KEYWORD, ZCodeParser.ELIF_KEYWORD, ZCodeParser.BEGIN_KEYWORD, ZCodeParser.END_KEYWORD, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 2)

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


    class Nl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nl_type(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_typeContext,0)


        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNl_list" ):
                return visitor.visitNl_list(self)
            else:
                return visitor.visitChildren(self)




    def nl_list(self):

        localctx = ZCodeParser.Nl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_nl_list)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.nl_type()
                self.state = 117
                self.nl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.nl_type()
                pass


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
        self.enterRule(localctx, 10, self.RULE_declaration)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.variable_stat()
                pass
            elif token in [ZCodeParser.FUNC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.function_stat()
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


    class Variable_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_declare(self):
            return self.getTypedRuleContext(ZCodeParser.Explicit_declareContext,0)


        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


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
        self.enterRule(localctx, 12, self.RULE_variable_stat)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.explicit_declare()
                self.state = 127
                self.nl_list()
                pass
            elif token in [ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.implicit_declare()
                self.state = 130
                self.nl_list()
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
        self.enterRule(localctx, 14, self.RULE_dtype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
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
        self.enterRule(localctx, 16, self.RULE_explicit_declare)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.array_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.primitive_declare()
                pass


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


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

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
        self.enterRule(localctx, 18, self.RULE_primitive_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.dtype()
            self.state = 141
            self.match(ZCodeParser.ID)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN_OP]:
                self.state = 142
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 143
                self.expression()
                pass
            elif token in [ZCodeParser.NL1, ZCodeParser.NL3, ZCodeParser.NL4]:
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

        def numlit_list(self):
            return self.getTypedRuleContext(ZCodeParser.Numlit_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = ZCodeParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.dtype()
            self.state = 148
            self.match(ZCodeParser.ID)
            self.state = 149
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 150
            self.numlit_list()
            self.state = 151
            self.match(ZCodeParser.RIGHT_BRACKET)
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN_OP]:
                self.state = 152
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 153
                self.expression()
                pass
            elif token in [ZCodeParser.NL1, ZCodeParser.NL3, ZCodeParser.NL4]:
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


    class Numlit_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL_LIT(self):
            return self.getToken(ZCodeParser.REAL_LIT, 0)

        def numlit_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Numlit_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlit_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlit_list" ):
                return visitor.visitNumlit_list(self)
            else:
                return visitor.visitChildren(self)




    def numlit_list(self):

        localctx = ZCodeParser.Numlit_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_numlit_list)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(ZCodeParser.REAL_LIT)
                self.state = 158
                self.numlit_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(ZCodeParser.REAL_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numlit_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR_KEYWORD(self):
            return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, 0)

        def REAL_LIT(self):
            return self.getToken(ZCodeParser.REAL_LIT, 0)

        def numlit_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Numlit_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_numlit_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumlit_tail" ):
                return visitor.visitNumlit_tail(self)
            else:
                return visitor.visitChildren(self)




    def numlit_tail(self):

        localctx = ZCodeParser.Numlit_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_numlit_tail)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 163
                self.match(ZCodeParser.REAL_LIT)
                self.state = 164
                self.numlit_tail()
                pass
            elif token in [ZCodeParser.RIGHT_BRACKET]:
                self.enterOuterAlt(localctx, 2)

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


    class Implicit_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_KEYWORD(self):
            return self.getToken(ZCodeParser.VAR_KEYWORD, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

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
        self.enterRule(localctx, 26, self.RULE_implicit_declare)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(ZCodeParser.VAR_KEYWORD)
                self.state = 169
                self.match(ZCodeParser.ID)
                self.state = 170
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 171
                self.expression()
                pass
            elif token in [ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(ZCodeParser.DYNAMIC_KEYWORD)
                self.state = 173
                self.match(ZCodeParser.ID)
                self.state = 177
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN_OP]:
                    self.state = 174
                    self.match(ZCodeParser.ASSIGN_OP)
                    self.state = 175
                    self.expression()
                    pass
                elif token in [ZCodeParser.NL1, ZCodeParser.NL3, ZCodeParser.NL4]:
                    pass
                else:
                    raise NoViableAltException(self)

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


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_stat" ):
                return visitor.visitFunction_stat(self)
            else:
                return visitor.visitChildren(self)




    def function_stat(self):

        localctx = ZCodeParser.Function_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_stat)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.function_declaration()
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

        def nl_nullable_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_nullable_listContext,0)


        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = ZCodeParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ZCodeParser.FUNC_KEYWORD)
            self.state = 186
            self.match(ZCodeParser.ID)
            self.state = 187
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 188
            self.param_list()
            self.state = 189
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 190
            self.nl_nullable_list()
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN_KEYWORD]:
                self.state = 191
                self.block_stat()
                pass
            elif token in [ZCodeParser.RETURN_KEYWORD]:
                self.state = 192
                self.return_stat()
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

        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ZCodeParser.FUNC_KEYWORD)
            self.state = 196
            self.match(ZCodeParser.ID)
            self.state = 197
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 198
            self.param_list()
            self.state = 199
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 200
            self.nl_list()
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

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def param_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_list)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.parameter()
                self.state = 203
                self.param_list_tail()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR_KEYWORD(self):
            return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, 0)

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def param_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list_tail" ):
                return visitor.visitParam_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_list_tail(self):

        localctx = ZCodeParser.Param_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_list_tail)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 209
                self.parameter()
                self.state = 210
                self.param_list_tail()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class ParameterContext(ParserRuleContext):
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

        def expression_nonempty_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_parameter)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.dtype()
                self.state = 216
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.dtype()
                self.state = 219
                self.match(ZCodeParser.ID)
                self.state = 220
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 221
                self.expression_nonempty_list()
                self.state = 222
                self.match(ZCodeParser.RIGHT_BRACKET)
                pass


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


        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def function_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_exprContext,0)


        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ZCodeParser.AssignmentContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statContext,0)


        def break_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statContext,0)


        def continue_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_statement)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.control_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.loop_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.variable_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.block_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.function_expr()
                self.state = 231
                self.nl_list()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 233
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 234
                self.return_stat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 235
                self.break_stat()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 236
                self.continue_stat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement_list)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.BREAK_KEYWORD, ZCodeParser.CONTINUE_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.BEGIN_KEYWORD, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.statement()
                self.state = 240
                self.statement_list()
                pass
            elif token in [ZCodeParser.END_KEYWORD]:
                self.enterOuterAlt(localctx, 2)

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


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_KEYWORD(self):
            return self.getToken(ZCodeParser.RETURN_KEYWORD, 0)

        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stat" ):
                return visitor.visitReturn_stat(self)
            else:
                return visitor.visitChildren(self)




    def return_stat(self):

        localctx = ZCodeParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(ZCodeParser.RETURN_KEYWORD)
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.state = 246
                self.expression()
                pass
            elif token in [ZCodeParser.NL1, ZCodeParser.NL3, ZCodeParser.NL4]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 250
            self.nl_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_KEYWORD(self):
            return self.getToken(ZCodeParser.BREAK_KEYWORD, 0)

        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stat" ):
                return visitor.visitBreak_stat(self)
            else:
                return visitor.visitChildren(self)




    def break_stat(self):

        localctx = ZCodeParser.Break_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_break_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ZCodeParser.BREAK_KEYWORD)
            self.state = 253
            self.nl_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_KEYWORD(self):
            return self.getToken(ZCodeParser.CONTINUE_KEYWORD, 0)

        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stat" ):
                return visitor.visitContinue_stat(self)
            else:
                return visitor.visitChildren(self)




    def continue_stat(self):

        localctx = ZCodeParser.Continue_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continue_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(ZCodeParser.CONTINUE_KEYWORD)
            self.state = 256
            self.nl_list()
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

        def nl_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Nl_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Nl_listContext,i)


        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END_KEYWORD(self):
            return self.getToken(ZCodeParser.END_KEYWORD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stat" ):
                return visitor.visitBlock_stat(self)
            else:
                return visitor.visitChildren(self)




    def block_stat(self):

        localctx = ZCodeParser.Block_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.BEGIN_KEYWORD)
            self.state = 259
            self.nl_list()
            self.state = 260
            self.statement_list()
            self.state = 261
            self.match(ZCodeParser.END_KEYWORD)
            self.state = 262
            self.nl_list()
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

        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_comment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = ZCodeParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(ZCodeParser.COMMENT_LINE)
            self.state = 265
            self.nl_list()
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
        self.enterRule(localctx, 54, self.RULE_expression)
        try:
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.relational_expr()
                self.state = 268
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 269
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
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
        self.enterRule(localctx, 56, self.RULE_relation_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
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
        self.enterRule(localctx, 58, self.RULE_relational_expr)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.logical_expr(0)
                self.state = 277
                self.relation_operation()
                self.state = 278
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.adding_expr(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.multiplying_expr(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.not_logical()
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.not_logical() 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_not_logical)
        try:
            self.state = 319
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(ZCodeParser.NOT_OP)
                self.state = 317
                self.expression()
                pass
            elif token in [ZCodeParser.SUB_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
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
        self.enterRule(localctx, 68, self.RULE_sign_expr)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(ZCodeParser.SUB_OP)
                self.state = 322
                self.expression()
                pass
            elif token in [ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.index_expr()
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

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def expression_nonempty_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def function_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Function_exprContext,0)


        def parenthesis_expr(self):
            return self.getTypedRuleContext(ZCodeParser.Parenthesis_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = ZCodeParser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_index_expr)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 326
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 327
                    self.function_expr()
                    pass


                self.state = 330
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 331
                self.expression_nonempty_list()
                self.state = 332
                self.match(ZCodeParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.parenthesis_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 72, self.RULE_parenthesis_expr)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(ZCodeParser.LEFT_PARENTHESIS)
                self.state = 338
                self.expression()
                self.state = 339
                self.match(ZCodeParser.RIGHT_PARENTHESIS)
                pass
            elif token in [ZCodeParser.ID, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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
        self.enterRule(localctx, 74, self.RULE_term)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(ZCodeParser.REAL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(ZCodeParser.TRUE_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 346
                self.match(ZCodeParser.FALSE_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 347
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 348
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 349
                self.function_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 350
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

        def expression_nonempty_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_expr" ):
                return visitor.visitArray_expr(self)
            else:
                return visitor.visitChildren(self)




    def array_expr(self):

        localctx = ZCodeParser.Array_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 354
            self.expression_nonempty_list()
            self.state = 355
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

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(ZCodeParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_expr" ):
                return visitor.visitFunction_expr(self)
            else:
                return visitor.visitChildren(self)




    def function_expr(self):

        localctx = ZCodeParser.Function_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_function_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ZCodeParser.ID)
            self.state = 358
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 359
            self.expression_list()
            self.state = 360
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def expression_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression_list)
        try:
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.expression()
                self.state = 363
                self.expression_list_tail()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class Expression_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR_KEYWORD(self):
            return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def expression_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list_tail" ):
                return visitor.visitExpression_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def expression_list_tail(self):

        localctx = ZCodeParser.Expression_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression_list_tail)
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 369
                self.expression()
                self.state = 370
                self.expression_list_tail()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 2)

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


    class Expression_nonempty_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def expression_nonempty_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_nonempty_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_nonempty_list" ):
                return visitor.visitExpression_nonempty_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_nonempty_list(self):

        localctx = ZCodeParser.Expression_nonempty_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expression_nonempty_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.expression()
            self.state = 376
            self.expression_nonempty_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_nonempty_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR_KEYWORD(self):
            return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def expression_nonempty_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_nonempty_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_nonempty_tail" ):
                return visitor.visitExpression_nonempty_tail(self)
            else:
                return visitor.visitChildren(self)




    def expression_nonempty_tail(self):

        localctx = ZCodeParser.Expression_nonempty_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expression_nonempty_tail)
        try:
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 379
                self.expression()
                self.state = 380
                self.expression_nonempty_tail()
                pass
            elif token in [ZCodeParser.RIGHT_BRACKET]:
                self.enterOuterAlt(localctx, 2)

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


    class Control_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_KEYWORD(self):
            return self.getToken(ZCodeParser.IF_KEYWORD, 0)

        def ifst_component(self):
            return self.getTypedRuleContext(ZCodeParser.Ifst_componentContext,0)


        def elif_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmt_listContext,0)


        def ELSE_KEYWORD(self):
            return self.getToken(ZCodeParser.ELSE_KEYWORD, 0)

        def nl_nullable_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_nullable_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_control_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_stat" ):
                return visitor.visitControl_stat(self)
            else:
                return visitor.visitChildren(self)




    def control_stat(self):

        localctx = ZCodeParser.Control_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_control_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(ZCodeParser.IF_KEYWORD)
            self.state = 386
            self.ifst_component()
            self.state = 387
            self.elif_stmt_list()
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 388
                self.match(ZCodeParser.ELSE_KEYWORD)
                self.state = 389
                self.nl_nullable_list()
                self.state = 390
                self.statement()
                pass

            elif la_ == 2:
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF_KEYWORD(self):
            return self.getToken(ZCodeParser.ELIF_KEYWORD, 0)

        def ifst_component(self):
            return self.getTypedRuleContext(ZCodeParser.Ifst_componentContext,0)


        def elif_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_stmt_list" ):
                return visitor.visitElif_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_stmt_list(self):

        localctx = ZCodeParser.Elif_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_elif_stmt_list)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(ZCodeParser.ELIF_KEYWORD)
                self.state = 396
                self.ifst_component()
                self.state = 397
                self.elif_stmt_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


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

        def nl_nullable_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_nullable_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifst_component

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfst_component" ):
                return visitor.visitIfst_component(self)
            else:
                return visitor.visitChildren(self)




    def ifst_component(self):

        localctx = ZCodeParser.Ifst_componentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_ifst_component)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 403
            self.expression()
            self.state = 404
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 405
            self.nl_nullable_list()
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 406
                self.statement()
                pass

            elif la_ == 2:
                pass


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

        def nl_nullable_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_nullable_listContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stat" ):
                return visitor.visitLoop_stat(self)
            else:
                return visitor.visitChildren(self)




    def loop_stat(self):

        localctx = ZCodeParser.Loop_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_loop_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(ZCodeParser.FOR_KEYWORD)
            self.state = 411
            self.match(ZCodeParser.ID)
            self.state = 412
            self.match(ZCodeParser.UNTIL_KEYWORD)
            self.state = 413
            self.expression()
            self.state = 414
            self.match(ZCodeParser.BY_KEYWORD)
            self.state = 415
            self.expression()
            self.state = 416
            self.nl_nullable_list()
            self.state = 417
            self.statement()
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

        def ASSIGN_OP(self):
            return self.getToken(ZCodeParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def nl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Nl_listContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LEFT_BRACKET(self):
            return self.getToken(ZCodeParser.LEFT_BRACKET, 0)

        def expression_nonempty_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ZCodeParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 419
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 420
                self.match(ZCodeParser.ID)
                self.state = 421
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 422
                self.expression_nonempty_list()
                self.state = 423
                self.match(ZCodeParser.RIGHT_BRACKET)
                pass


            self.state = 427
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 428
            self.expression()
            self.state = 429
            self.nl_list()
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
        self._predicates[30] = self.logical_expr_sempred
        self._predicates[31] = self.adding_expr_sempred
        self._predicates[32] = self.multiplying_expr_sempred
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
         




