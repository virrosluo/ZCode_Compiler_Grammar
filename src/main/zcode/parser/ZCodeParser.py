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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u01e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\7\2^\n\2\f\2\16\2a\13\2\3\2\7\2d\n\2\f\2\16\2g\13\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3m\n\3\3\4\3\4\6\4q\n\4\r\4\16\4r\3")
        buf.write("\4\3\4\6\4w\n\4\r\4\16\4x\5\4{\n\4\3\5\3\5\3\6\3\6\5\6")
        buf.write("\u0081\n\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\5\b\u008a\n\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\5\t\u0091\n\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u009b\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00a7\n\13\5\13\u00a9\n\13\3")
        buf.write("\f\3\f\3\f\6\f\u00ae\n\f\r\f\16\f\u00af\5\f\u00b2\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00bb\n\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00c9")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00d0\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00db\n\21")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00e1\n\22\3\23\3\23\3\23\3")
        buf.write("\23\5\23\u00e7\n\23\3\24\3\24\6\24\u00eb\n\24\r\24\16")
        buf.write("\24\u00ec\3\24\3\24\3\24\6\24\u00f2\n\24\r\24\16\24\u00f3")
        buf.write("\3\24\5\24\u00f7\n\24\3\25\3\25\3\25\3\25\3\25\3\25\6")
        buf.write("\25\u00ff\n\25\r\25\16\25\u0100\3\25\3\25\3\25\3\25\5")
        buf.write("\25\u0107\n\25\3\25\6\25\u010a\n\25\r\25\16\25\u010b\3")
        buf.write("\25\5\25\u010f\n\25\3\26\3\26\6\26\u0113\n\26\r\26\16")
        buf.write("\26\u0114\3\27\3\27\3\27\3\27\3\27\5\27\u011c\n\27\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0125\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\7\32\u012d\n\32\f\32\16\32\u0130")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0138\n\33\f")
        buf.write("\33\16\33\u013b\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7")
        buf.write("\34\u0143\n\34\f\34\16\34\u0146\13\34\3\35\3\35\3\35\5")
        buf.write("\35\u014b\n\35\3\36\3\36\3\36\5\36\u0150\n\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u015a\n\37\f\37\16")
        buf.write("\37\u015d\13\37\3 \3 \3 \3 \3 \5 \u0164\n \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\5!\u016d\n!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\5$\u017c\n$\3%\3%\3%\3%\3%\5%\u0183\n%\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u018d\n\'\3(\3(\3(\3(")
        buf.write("\3(\7(\u0194\n(\f(\16(\u0197\13(\3(\3(\5(\u019b\n(\3)")
        buf.write("\3)\3)\3)\3)\5)\u01a2\n)\3*\3*\3*\3*\7*\u01a8\n*\f*\16")
        buf.write("*\u01ab\13*\3*\3*\3+\3+\3+\3+\3+\3+\3+\7+\u01b6\n+\f+")
        buf.write("\16+\u01b9\13+\3+\3+\3+\6+\u01be\n+\r+\16+\u01bf\3+\3")
        buf.write("+\3+\6+\u01c5\n+\r+\16+\u01c6\5+\u01c9\n+\3,\3,\3,\6,")
        buf.write("\u01ce\n,\r,\16,\u01cf\3,\3,\6,\u01d4\n,\r,\16,\u01d5")
        buf.write("\5,\u01d8\n,\3-\3-\3-\3-\5-\u01de\n-\3.\3.\3.\3.\6.\u01e4")
        buf.write("\n.\r.\16.\u01e5\3.\2\6\62\64\66</\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\2\7\3\2\3\5\4\2\35\"$$\3\2\33\34\3\2\25\26\3\2\27")
        buf.write("\31\2\u01fc\2_\3\2\2\2\4l\3\2\2\2\6z\3\2\2\2\b|\3\2\2")
        buf.write("\2\n\u0080\3\2\2\2\f\u0082\3\2\2\2\16\u0089\3\2\2\2\20")
        buf.write("\u008b\3\2\2\2\22\u0092\3\2\2\2\24\u00a8\3\2\2\2\26\u00b1")
        buf.write("\3\2\2\2\30\u00b3\3\2\2\2\32\u00be\3\2\2\2\34\u00c8\3")
        buf.write("\2\2\2\36\u00cf\3\2\2\2 \u00da\3\2\2\2\"\u00e0\3\2\2\2")
        buf.write("$\u00e6\3\2\2\2&\u00f6\3\2\2\2(\u010e\3\2\2\2*\u0110\3")
        buf.write("\2\2\2,\u011b\3\2\2\2.\u011d\3\2\2\2\60\u0124\3\2\2\2")
        buf.write("\62\u0126\3\2\2\2\64\u0131\3\2\2\2\66\u013c\3\2\2\28\u014a")
        buf.write("\3\2\2\2:\u014f\3\2\2\2<\u0151\3\2\2\2>\u0163\3\2\2\2")
        buf.write("@\u016c\3\2\2\2B\u016e\3\2\2\2D\u0172\3\2\2\2F\u017b\3")
        buf.write("\2\2\2H\u0182\3\2\2\2J\u0184\3\2\2\2L\u018c\3\2\2\2N\u018e")
        buf.write("\3\2\2\2P\u01a1\3\2\2\2R\u01a3\3\2\2\2T\u01ae\3\2\2\2")
        buf.write("V\u01d7\3\2\2\2X\u01dd\3\2\2\2Z\u01df\3\2\2\2\\^\7.\2")
        buf.write("\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`e\3\2\2\2")
        buf.write("a_\3\2\2\2bd\5\4\3\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3")
        buf.write("\2\2\2fh\3\2\2\2ge\3\2\2\2hi\7\2\2\3i\3\3\2\2\2jm\5\6")
        buf.write("\4\2km\5\26\f\2lj\3\2\2\2lk\3\2\2\2m\5\3\2\2\2np\5\n\6")
        buf.write("\2oq\7.\2\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3\2\2\2s{")
        buf.write("\3\2\2\2tv\5\24\13\2uw\7.\2\2vu\3\2\2\2wx\3\2\2\2xv\3")
        buf.write("\2\2\2xy\3\2\2\2y{\3\2\2\2zn\3\2\2\2zt\3\2\2\2{\7\3\2")
        buf.write("\2\2|}\t\2\2\2}\t\3\2\2\2~\u0081\5\22\n\2\177\u0081\5")
        buf.write("\20\t\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\13\3\2")
        buf.write("\2\2\u0082\u0083\7%\2\2\u0083\u0084\5\16\b\2\u0084\r\3")
        buf.write("\2\2\2\u0085\u0086\7*\2\2\u0086\u0087\7%\2\2\u0087\u008a")
        buf.write("\5\16\b\2\u0088\u008a\3\2\2\2\u0089\u0085\3\2\2\2\u0089")
        buf.write("\u0088\3\2\2\2\u008a\17\3\2\2\2\u008b\u008c\5\b\5\2\u008c")
        buf.write("\u0090\5\f\7\2\u008d\u008e\7\24\2\2\u008e\u0091\5,\27")
        buf.write("\2\u008f\u0091\3\2\2\2\u0090\u008d\3\2\2\2\u0090\u008f")
        buf.write("\3\2\2\2\u0091\21\3\2\2\2\u0092\u0093\5\b\5\2\u0093\u0094")
        buf.write("\7%\2\2\u0094\u0095\7(\2\2\u0095\u0096\5J&\2\u0096\u009a")
        buf.write("\7)\2\2\u0097\u0098\7\24\2\2\u0098\u009b\5,\27\2\u0099")
        buf.write("\u009b\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0099\3\2\2\2")
        buf.write("\u009b\23\3\2\2\2\u009c\u009d\7\7\2\2\u009d\u009e\5\f")
        buf.write("\7\2\u009e\u009f\7\24\2\2\u009f\u00a0\5,\27\2\u00a0\u00a9")
        buf.write("\3\2\2\2\u00a1\u00a2\7\b\2\2\u00a2\u00a6\5\f\7\2\u00a3")
        buf.write("\u00a4\7\24\2\2\u00a4\u00a7\5,\27\2\u00a5\u00a7\3\2\2")
        buf.write("\2\u00a6\u00a3\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a9")
        buf.write("\3\2\2\2\u00a8\u009c\3\2\2\2\u00a8\u00a1\3\2\2\2\u00a9")
        buf.write("\25\3\2\2\2\u00aa\u00b2\5\30\r\2\u00ab\u00ad\5\32\16\2")
        buf.write("\u00ac\u00ae\7.\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00af\3")
        buf.write("\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2")
        buf.write("\3\2\2\2\u00b1\u00aa\3\2\2\2\u00b1\u00ab\3\2\2\2\u00b2")
        buf.write("\27\3\2\2\2\u00b3\u00b4\7\t\2\2\u00b4\u00b5\7%\2\2\u00b5")
        buf.write("\u00b6\7&\2\2\u00b6\u00b7\5\34\17\2\u00b7\u00ba\7\'\2")
        buf.write("\2\u00b8\u00bb\7.\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\5&\24\2\u00bd\31\3\2\2\2\u00be\u00bf\7\t\2\2\u00bf")
        buf.write("\u00c0\7%\2\2\u00c0\u00c1\7&\2\2\u00c1\u00c2\5\34\17\2")
        buf.write("\u00c2\u00c3\7\'\2\2\u00c3\33\3\2\2\2\u00c4\u00c5\5 \21")
        buf.write("\2\u00c5\u00c6\5\36\20\2\u00c6\u00c9\3\2\2\2\u00c7\u00c9")
        buf.write("\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\35\3\2\2\2\u00ca\u00cb\7*\2\2\u00cb\u00cc\5 \21\2\u00cc")
        buf.write("\u00cd\5\36\20\2\u00cd\u00d0\3\2\2\2\u00ce\u00d0\3\2\2")
        buf.write("\2\u00cf\u00ca\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\37\3")
        buf.write("\2\2\2\u00d1\u00d2\5\b\5\2\u00d2\u00d3\7%\2\2\u00d3\u00db")
        buf.write("\3\2\2\2\u00d4\u00d5\5\b\5\2\u00d5\u00d6\7%\2\2\u00d6")
        buf.write("\u00d7\7(\2\2\u00d7\u00d8\5J&\2\u00d8\u00d9\7)\2\2\u00d9")
        buf.write("\u00db\3\2\2\2\u00da\u00d1\3\2\2\2\u00da\u00d4\3\2\2\2")
        buf.write("\u00db!\3\2\2\2\u00dc\u00dd\5(\25\2\u00dd\u00de\5$\23")
        buf.write("\2\u00de\u00e1\3\2\2\2\u00df\u00e1\3\2\2\2\u00e0\u00dc")
        buf.write("\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1#\3\2\2\2\u00e2\u00e3")
        buf.write("\5(\25\2\u00e3\u00e4\5$\23\2\u00e4\u00e7\3\2\2\2\u00e5")
        buf.write("\u00e7\3\2\2\2\u00e6\u00e2\3\2\2\2\u00e6\u00e5\3\2\2\2")
        buf.write("\u00e7%\3\2\2\2\u00e8\u00ea\7\22\2\2\u00e9\u00eb\7.\2")
        buf.write("\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\u00ef\5\"\22\2\u00ef\u00f1\7\23\2\2\u00f0\u00f2\7.\2")
        buf.write("\2\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5")
        buf.write("\u00f7\5(\25\2\u00f6\u00e8\3\2\2\2\u00f6\u00f5\3\2\2\2")
        buf.write("\u00f7\'\3\2\2\2\u00f8\u010f\5N(\2\u00f9\u010f\5T+\2\u00fa")
        buf.write("\u010f\5\6\4\2\u00fb\u010f\5\26\f\2\u00fc\u00fe\5,\27")
        buf.write("\2\u00fd\u00ff\7.\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u010f\3\2\2\2\u0102\u010f\5Z.\2\u0103\u0106\7\6\2\2\u0104")
        buf.write("\u0107\5,\27\2\u0105\u0107\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0105\3\2\2\2\u0107\u0109\3\2\2\2\u0108\u010a\7")
        buf.write(".\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010f\3\2\2\2\u010d")
        buf.write("\u010f\5*\26\2\u010e\u00f8\3\2\2\2\u010e\u00f9\3\2\2\2")
        buf.write("\u010e\u00fa\3\2\2\2\u010e\u00fb\3\2\2\2\u010e\u00fc\3")
        buf.write("\2\2\2\u010e\u0102\3\2\2\2\u010e\u0103\3\2\2\2\u010e\u010d")
        buf.write("\3\2\2\2\u010f)\3\2\2\2\u0110\u0112\7\60\2\2\u0111\u0113")
        buf.write("\7.\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115+\3\2\2\2\u0116")
        buf.write("\u0117\5\60\31\2\u0117\u0118\7#\2\2\u0118\u0119\5\60\31")
        buf.write("\2\u0119\u011c\3\2\2\2\u011a\u011c\5\60\31\2\u011b\u0116")
        buf.write("\3\2\2\2\u011b\u011a\3\2\2\2\u011c-\3\2\2\2\u011d\u011e")
        buf.write("\t\3\2\2\u011e/\3\2\2\2\u011f\u0120\5\62\32\2\u0120\u0121")
        buf.write("\5.\30\2\u0121\u0122\5\62\32\2\u0122\u0125\3\2\2\2\u0123")
        buf.write("\u0125\5\62\32\2\u0124\u011f\3\2\2\2\u0124\u0123\3\2\2")
        buf.write("\2\u0125\61\3\2\2\2\u0126\u0127\b\32\1\2\u0127\u0128\5")
        buf.write("\64\33\2\u0128\u012e\3\2\2\2\u0129\u012a\f\4\2\2\u012a")
        buf.write("\u012b\t\4\2\2\u012b\u012d\5\64\33\2\u012c\u0129\3\2\2")
        buf.write("\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012f\63\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0132")
        buf.write("\b\33\1\2\u0132\u0133\5\66\34\2\u0133\u0139\3\2\2\2\u0134")
        buf.write("\u0135\f\4\2\2\u0135\u0136\t\5\2\2\u0136\u0138\5\66\34")
        buf.write("\2\u0137\u0134\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137")
        buf.write("\3\2\2\2\u0139\u013a\3\2\2\2\u013a\65\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013c\u013d\b\34\1\2\u013d\u013e\58\35\2\u013e")
        buf.write("\u0144\3\2\2\2\u013f\u0140\f\4\2\2\u0140\u0141\t\6\2\2")
        buf.write("\u0141\u0143\58\35\2\u0142\u013f\3\2\2\2\u0143\u0146\3")
        buf.write("\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3\2\2\2\u0145\67")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0147\u0148\7\32\2\2\u0148")
        buf.write("\u014b\5,\27\2\u0149\u014b\5:\36\2\u014a\u0147\3\2\2\2")
        buf.write("\u014a\u0149\3\2\2\2\u014b9\3\2\2\2\u014c\u014d\7\26\2")
        buf.write("\2\u014d\u0150\5,\27\2\u014e\u0150\5<\37\2\u014f\u014c")
        buf.write("\3\2\2\2\u014f\u014e\3\2\2\2\u0150;\3\2\2\2\u0151\u0152")
        buf.write("\b\37\1\2\u0152\u0153\5> \2\u0153\u015b\3\2\2\2\u0154")
        buf.write("\u0155\f\4\2\2\u0155\u0156\7(\2\2\u0156\u0157\5J&\2\u0157")
        buf.write("\u0158\7)\2\2\u0158\u015a\3\2\2\2\u0159\u0154\3\2\2\2")
        buf.write("\u015a\u015d\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c\3")
        buf.write("\2\2\2\u015c=\3\2\2\2\u015d\u015b\3\2\2\2\u015e\u015f")
        buf.write("\7&\2\2\u015f\u0160\5,\27\2\u0160\u0161\7\'\2\2\u0161")
        buf.write("\u0164\3\2\2\2\u0162\u0164\5@!\2\u0163\u015e\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164?\3\2\2\2\u0165\u016d\7-\2\2\u0166")
        buf.write("\u016d\7+\2\2\u0167\u016d\7,\2\2\u0168\u016d\7\62\2\2")
        buf.write("\u0169\u016d\7%\2\2\u016a\u016d\5D#\2\u016b\u016d\5B\"")
        buf.write("\2\u016c\u0165\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0167")
        buf.write("\3\2\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016dA\3\2\2\2\u016e")
        buf.write("\u016f\7(\2\2\u016f\u0170\5F$\2\u0170\u0171\7)\2\2\u0171")
        buf.write("C\3\2\2\2\u0172\u0173\7%\2\2\u0173\u0174\7&\2\2\u0174")
        buf.write("\u0175\5F$\2\u0175\u0176\7\'\2\2\u0176E\3\2\2\2\u0177")
        buf.write("\u0178\5,\27\2\u0178\u0179\5H%\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u017c\3\2\2\2\u017b\u0177\3\2\2\2\u017b\u017a\3\2\2\2")
        buf.write("\u017cG\3\2\2\2\u017d\u017e\7*\2\2\u017e\u017f\5,\27\2")
        buf.write("\u017f\u0180\5H%\2\u0180\u0183\3\2\2\2\u0181\u0183\3\2")
        buf.write("\2\2\u0182\u017d\3\2\2\2\u0182\u0181\3\2\2\2\u0183I\3")
        buf.write("\2\2\2\u0184\u0185\5,\27\2\u0185\u0186\5L\'\2\u0186K\3")
        buf.write("\2\2\2\u0187\u0188\7*\2\2\u0188\u0189\5,\27\2\u0189\u018a")
        buf.write("\5L\'\2\u018a\u018d\3\2\2\2\u018b\u018d\3\2\2\2\u018c")
        buf.write("\u0187\3\2\2\2\u018c\u018b\3\2\2\2\u018dM\3\2\2\2\u018e")
        buf.write("\u018f\7\17\2\2\u018f\u0190\5R*\2\u0190\u019a\5P)\2\u0191")
        buf.write("\u0195\7\20\2\2\u0192\u0194\7.\2\2\u0193\u0192\3\2\2\2")
        buf.write("\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3")
        buf.write("\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019b")
        buf.write("\5&\24\2\u0199\u019b\3\2\2\2\u019a\u0191\3\2\2\2\u019a")
        buf.write("\u0199\3\2\2\2\u019bO\3\2\2\2\u019c\u019d\7\21\2\2\u019d")
        buf.write("\u019e\5R*\2\u019e\u019f\5P)\2\u019f\u01a2\3\2\2\2\u01a0")
        buf.write("\u01a2\3\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u01a0\3\2\2\2")
        buf.write("\u01a2Q\3\2\2\2\u01a3\u01a4\7&\2\2\u01a4\u01a5\5,\27\2")
        buf.write("\u01a5\u01a9\7\'\2\2\u01a6\u01a8\7.\2\2\u01a7\u01a6\3")
        buf.write("\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\5&\24\2\u01adS\3\2\2\2\u01ae\u01af\7\n\2\2\u01af")
        buf.write("\u01b0\7%\2\2\u01b0\u01b1\7\13\2\2\u01b1\u01b2\5,\27\2")
        buf.write("\u01b2\u01b3\7\f\2\2\u01b3\u01b7\5,\27\2\u01b4\u01b6\7")
        buf.write(".\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5")
        buf.write("\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01c8\3\2\2\2\u01b9")
        buf.write("\u01b7\3\2\2\2\u01ba\u01c9\5V,\2\u01bb\u01bd\7\22\2\2")
        buf.write("\u01bc\u01be\7.\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3")
        buf.write("\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1")
        buf.write("\3\2\2\2\u01c1\u01c2\5X-\2\u01c2\u01c4\7\23\2\2\u01c3")
        buf.write("\u01c5\7.\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3")
        buf.write("\2\2\2\u01c8\u01ba\3\2\2\2\u01c8\u01bb\3\2\2\2\u01c9U")
        buf.write("\3\2\2\2\u01ca\u01d8\5(\25\2\u01cb\u01cd\7\r\2\2\u01cc")
        buf.write("\u01ce\7.\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d8\3")
        buf.write("\2\2\2\u01d1\u01d3\7\16\2\2\u01d2\u01d4\7.\2\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6\u01d8\3\2\2\2\u01d7\u01ca\3\2\2\2")
        buf.write("\u01d7\u01cb\3\2\2\2\u01d7\u01d1\3\2\2\2\u01d8W\3\2\2")
        buf.write("\2\u01d9\u01da\5V,\2\u01da\u01db\5X-\2\u01db\u01de\3\2")
        buf.write("\2\2\u01dc\u01de\3\2\2\2\u01dd\u01d9\3\2\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01deY\3\2\2\2\u01df\u01e0\5,\27\2\u01e0\u01e1")
        buf.write("\7\24\2\2\u01e1\u01e3\5,\27\2\u01e2\u01e4\7.\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6[\3\2\2\28_elrxz\u0080\u0089")
        buf.write("\u0090\u009a\u00a6\u00a8\u00af\u00b1\u00ba\u00c8\u00cf")
        buf.write("\u00da\u00e0\u00e6\u00ec\u00f3\u00f6\u0100\u0106\u010b")
        buf.write("\u010e\u0114\u011b\u0124\u012e\u0139\u0144\u014a\u014f")
        buf.write("\u015b\u0163\u016c\u017b\u0182\u018c\u0195\u019a\u01a1")
        buf.write("\u01a9\u01b7\u01bf\u01c6\u01c8\u01cf\u01d5\u01d7\u01dd")
        buf.write("\u01e5")
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
                      "FALSE_LIT", "REAL_LIT", "NL", "WS", "COMMENT_LINE", 
                      "UNCLOSE_STRING", "STRING_LIT", "ILLEGAL_ESCAPE", 
                      "NEWLINE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_variable_stat = 2
    RULE_dtype = 3
    RULE_explicit_declare = 4
    RULE_idlist = 5
    RULE_idlist_tail = 6
    RULE_primitive_declare = 7
    RULE_array_declare = 8
    RULE_implicit_declare = 9
    RULE_function_stat = 10
    RULE_function_definition = 11
    RULE_function_declaration = 12
    RULE_param_list = 13
    RULE_param_list_tail = 14
    RULE_parameter = 15
    RULE_statement_list = 16
    RULE_statement_list_tail = 17
    RULE_block_stat = 18
    RULE_statement = 19
    RULE_comment = 20
    RULE_expression = 21
    RULE_relation_operation = 22
    RULE_relational_expr = 23
    RULE_logical_expr = 24
    RULE_adding_expr = 25
    RULE_multiplying_expr = 26
    RULE_not_logical = 27
    RULE_sign_expr = 28
    RULE_index_expr = 29
    RULE_parenthesis_expr = 30
    RULE_term = 31
    RULE_array_expr = 32
    RULE_function_expr = 33
    RULE_expression_list = 34
    RULE_expression_list_tail = 35
    RULE_expression_nonempty_list = 36
    RULE_expression_nonempty_tail = 37
    RULE_control_stat = 38
    RULE_elif_stmt_list = 39
    RULE_ifst_component = 40
    RULE_loop_stat = 41
    RULE_loop_body_statement = 42
    RULE_loop_stmt_list = 43
    RULE_assignment = 44

    ruleNames =  [ "program", "declaration", "variable_stat", "dtype", "explicit_declare", 
                   "idlist", "idlist_tail", "primitive_declare", "array_declare", 
                   "implicit_declare", "function_stat", "function_definition", 
                   "function_declaration", "param_list", "param_list_tail", 
                   "parameter", "statement_list", "statement_list_tail", 
                   "block_stat", "statement", "comment", "expression", "relation_operation", 
                   "relational_expr", "logical_expr", "adding_expr", "multiplying_expr", 
                   "not_logical", "sign_expr", "index_expr", "parenthesis_expr", 
                   "term", "array_expr", "function_expr", "expression_list", 
                   "expression_list_tail", "expression_nonempty_list", "expression_nonempty_tail", 
                   "control_stat", "elif_stmt_list", "ifst_component", "loop_stat", 
                   "loop_body_statement", "loop_stmt_list", "assignment" ]

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
    NL=44
    WS=45
    COMMENT_LINE=46
    UNCLOSE_STRING=47
    STRING_LIT=48
    ILLEGAL_ESCAPE=49
    NEWLINE_STRING=50
    ERROR_TOKEN=51

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
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 90
                self.match(ZCodeParser.NL)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUM_KEYWORD) | (1 << ZCodeParser.BOOL_KEYWORD) | (1 << ZCodeParser.STRING_KEYWORD) | (1 << ZCodeParser.VAR_KEYWORD) | (1 << ZCodeParser.DYNAMIC_KEYWORD) | (1 << ZCodeParser.FUNC_KEYWORD))) != 0):
                self.state = 96
                self.declaration()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
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
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.variable_stat()
                pass
            elif token in [ZCodeParser.FUNC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
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
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.explicit_declare()
                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 109
                    self.match(ZCodeParser.NL)
                    self.state = 112 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            elif token in [ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.implicit_declare()
                self.state = 116 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 115
                    self.match(ZCodeParser.NL)
                    self.state = 118 
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
            self.state = 122
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
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.array_declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
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

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def idlist_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Idlist_tailContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(ZCodeParser.ID)
            self.state = 129
            self.idlist_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idlist_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEPARATOR_KEYWORD(self):
            return self.getToken(ZCodeParser.SEPARATOR_KEYWORD, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def idlist_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Idlist_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_idlist_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist_tail" ):
                return visitor.visitIdlist_tail(self)
            else:
                return visitor.visitChildren(self)




    def idlist_tail(self):

        localctx = ZCodeParser.Idlist_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_idlist_tail)
        try:
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 132
                self.match(ZCodeParser.ID)
                self.state = 133
                self.idlist_tail()
                pass
            elif token in [ZCodeParser.ASSIGN_OP, ZCodeParser.NL]:
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
        self.enterRule(localctx, 14, self.RULE_primitive_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.dtype()
            self.state = 138
            self.idlist()
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN_OP]:
                self.state = 139
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 140
                self.expression()
                pass
            elif token in [ZCodeParser.NL]:
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

        def expression_nonempty_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_listContext,0)


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
        self.enterRule(localctx, 16, self.RULE_array_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.dtype()
            self.state = 145
            self.match(ZCodeParser.ID)
            self.state = 146
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 147
            self.expression_nonempty_list()
            self.state = 148
            self.match(ZCodeParser.RIGHT_BRACKET)
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ASSIGN_OP]:
                self.state = 149
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 150
                self.expression()
                pass
            elif token in [ZCodeParser.NL]:
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
        self.enterRule(localctx, 18, self.RULE_implicit_declare)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.VAR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(ZCodeParser.VAR_KEYWORD)
                self.state = 155
                self.idlist()
                self.state = 156
                self.match(ZCodeParser.ASSIGN_OP)
                self.state = 157
                self.expression()
                pass
            elif token in [ZCodeParser.DYNAMIC_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(ZCodeParser.DYNAMIC_KEYWORD)
                self.state = 160
                self.idlist()
                self.state = 164
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.ASSIGN_OP]:
                    self.state = 161
                    self.match(ZCodeParser.ASSIGN_OP)
                    self.state = 162
                    self.expression()
                    pass
                elif token in [ZCodeParser.NL]:
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
        self.enterRule(localctx, 20, self.RULE_function_stat)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.function_definition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.function_declaration()
                self.state = 171 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 170
                    self.match(ZCodeParser.NL)
                    self.state = 173 
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


        def NL(self):
            return self.getToken(ZCodeParser.NL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_function_definition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = ZCodeParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_definition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ZCodeParser.FUNC_KEYWORD)
            self.state = 178
            self.match(ZCodeParser.ID)
            self.state = 179
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 180
            self.param_list()
            self.state = 181
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NL]:
                self.state = 182
                self.match(ZCodeParser.NL)
                pass
            elif token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.BEGIN_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 186
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
        self.enterRule(localctx, 24, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.FUNC_KEYWORD)
            self.state = 189
            self.match(ZCodeParser.ID)
            self.state = 190
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 191
            self.param_list()
            self.state = 192
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
        self.enterRule(localctx, 26, self.RULE_param_list)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.parameter()
                self.state = 195
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
        self.enterRule(localctx, 28, self.RULE_param_list_tail)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 201
                self.parameter()
                self.state = 202
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
        self.enterRule(localctx, 30, self.RULE_parameter)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.dtype()
                self.state = 208
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.dtype()
                self.state = 211
                self.match(ZCodeParser.ID)
                self.state = 212
                self.match(ZCodeParser.LEFT_BRACKET)
                self.state = 213
                self.expression_nonempty_list()
                self.state = 214
                self.match(ZCodeParser.RIGHT_BRACKET)
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


        def statement_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_statement_list)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.statement()
                self.state = 219
                self.statement_list_tail()
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


    class Statement_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def statement_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list_tail" ):
                return visitor.visitStatement_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def statement_list_tail(self):

        localctx = ZCodeParser.Statement_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_statement_list_tail)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.statement()
                self.state = 225
                self.statement_list_tail()
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


    class Block_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_KEYWORD(self):
            return self.getToken(ZCodeParser.BEGIN_KEYWORD, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def END_KEYWORD(self):
            return self.getToken(ZCodeParser.END_KEYWORD, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stat" ):
                return visitor.visitBlock_stat(self)
            else:
                return visitor.visitChildren(self)




    def block_stat(self):

        localctx = ZCodeParser.Block_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block_stat)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.BEGIN_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(ZCodeParser.BEGIN_KEYWORD)
                self.state = 232 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 231
                    self.match(ZCodeParser.NL)
                    self.state = 234 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                self.state = 236
                self.statement_list()
                self.state = 237
                self.match(ZCodeParser.END_KEYWORD)
                self.state = 239 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 238
                    self.match(ZCodeParser.NL)
                    self.state = 241 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            elif token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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
        self.enterRule(localctx, 38, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.control_stat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.loop_stat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.variable_stat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.function_stat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 250
                self.expression()
                self.state = 252 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 251
                    self.match(ZCodeParser.NL)
                    self.state = 254 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 256
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 257
                self.match(ZCodeParser.RETURN_KEYWORD)
                self.state = 260
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                    self.state = 258
                    self.expression()
                    pass
                elif token in [ZCodeParser.NL]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 263 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 262
                    self.match(ZCodeParser.NL)
                    self.state = 265 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 267
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
        self.enterRule(localctx, 40, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.COMMENT_LINE)
            self.state = 272 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 271
                self.match(ZCodeParser.NL)
                self.state = 274 
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
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.relational_expr()
                self.state = 277
                self.match(ZCodeParser.CONCAT_OP)
                self.state = 278
                self.relational_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
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
        self.enterRule(localctx, 44, self.RULE_relation_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
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
        self.enterRule(localctx, 46, self.RULE_relational_expr)
        try:
            self.state = 290
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.logical_expr(0)
                self.state = 286
                self.relation_operation()
                self.state = 287
                self.logical_expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_logical_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.adding_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 300
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expr)
                    self.state = 295
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 296
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND_OP or _la==ZCodeParser.OR_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 297
                    self.adding_expr(0) 
                self.state = 302
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_adding_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.multiplying_expr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 311
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_expr)
                    self.state = 306
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 307
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.ADD_OP or _la==ZCodeParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 308
                    self.multiplying_expr(0) 
                self.state = 313
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_multiplying_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.not_logical()
            self._ctx.stop = self._input.LT(-1)
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_expr)
                    self.state = 317
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 318
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL_OP) | (1 << ZCodeParser.DIV_OP) | (1 << ZCodeParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 319
                    self.not_logical() 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_not_logical)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(ZCodeParser.NOT_OP)
                self.state = 326
                self.expression()
                pass
            elif token in [ZCodeParser.SUB_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
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
        self.enterRule(localctx, 56, self.RULE_sign_expr)
        try:
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(ZCodeParser.SUB_OP)
                self.state = 331
                self.expression()
                pass
            elif token in [ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
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

        def expression_nonempty_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_nonempty_listContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(ZCodeParser.RIGHT_BRACKET, 0)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_index_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.parenthesis_expr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Index_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_expr)
                    self.state = 338
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 339
                    self.match(ZCodeParser.LEFT_BRACKET)
                    self.state = 340
                    self.expression_nonempty_list()
                    self.state = 341
                    self.match(ZCodeParser.RIGHT_BRACKET) 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

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
        self.enterRule(localctx, 60, self.RULE_parenthesis_expr)
        try:
            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LEFT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(ZCodeParser.LEFT_PARENTHESIS)
                self.state = 349
                self.expression()
                self.state = 350
                self.match(ZCodeParser.RIGHT_PARENTHESIS)
                pass
            elif token in [ZCodeParser.ID, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
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
        self.enterRule(localctx, 62, self.RULE_term)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(ZCodeParser.REAL_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(ZCodeParser.TRUE_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.match(ZCodeParser.FALSE_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 358
                self.match(ZCodeParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 359
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 360
                self.function_expr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 361
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

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


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
        self.enterRule(localctx, 64, self.RULE_array_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(ZCodeParser.LEFT_BRACKET)
            self.state = 365
            self.expression_list()
            self.state = 366
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
        self.enterRule(localctx, 66, self.RULE_function_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(ZCodeParser.ID)
            self.state = 369
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 370
            self.expression_list()
            self.state = 371
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
        self.enterRule(localctx, 68, self.RULE_expression_list)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.expression()
                self.state = 374
                self.expression_list_tail()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS, ZCodeParser.RIGHT_BRACKET]:
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
        self.enterRule(localctx, 70, self.RULE_expression_list_tail)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 380
                self.expression()
                self.state = 381
                self.expression_list_tail()
                pass
            elif token in [ZCodeParser.RIGHT_PARENTHESIS, ZCodeParser.RIGHT_BRACKET]:
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
        self.enterRule(localctx, 72, self.RULE_expression_nonempty_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expression()
            self.state = 387
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
        self.enterRule(localctx, 74, self.RULE_expression_nonempty_tail)
        try:
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEPARATOR_KEYWORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.match(ZCodeParser.SEPARATOR_KEYWORD)
                self.state = 390
                self.expression()
                self.state = 391
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

        def block_stat(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_control_stat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControl_stat" ):
                return visitor.visitControl_stat(self)
            else:
                return visitor.visitChildren(self)




    def control_stat(self):

        localctx = ZCodeParser.Control_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_control_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(ZCodeParser.IF_KEYWORD)
            self.state = 397
            self.ifst_component()
            self.state = 398
            self.elif_stmt_list()
            self.state = 408
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.state = 399
                self.match(ZCodeParser.ELSE_KEYWORD)
                self.state = 403
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZCodeParser.NL:
                    self.state = 400
                    self.match(ZCodeParser.NL)
                    self.state = 405
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 406
                self.block_stat()
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
        self.enterRule(localctx, 78, self.RULE_elif_stmt_list)
        try:
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.match(ZCodeParser.ELIF_KEYWORD)
                self.state = 411
                self.ifst_component()
                self.state = 412
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
        self.enterRule(localctx, 80, self.RULE_ifst_component)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(ZCodeParser.LEFT_PARENTHESIS)
            self.state = 418
            self.expression()
            self.state = 419
            self.match(ZCodeParser.RIGHT_PARENTHESIS)
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 420
                self.match(ZCodeParser.NL)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 426
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

        def loop_body_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_body_statementContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NL)
            else:
                return self.getToken(ZCodeParser.NL, i)

        def BEGIN_KEYWORD(self):
            return self.getToken(ZCodeParser.BEGIN_KEYWORD, 0)

        def loop_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_stmt_listContext,0)


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
        self.enterRule(localctx, 82, self.RULE_loop_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(ZCodeParser.FOR_KEYWORD)
            self.state = 429
            self.match(ZCodeParser.ID)
            self.state = 430
            self.match(ZCodeParser.UNTIL_KEYWORD)
            self.state = 431
            self.expression()
            self.state = 432
            self.match(ZCodeParser.BY_KEYWORD)
            self.state = 433
            self.expression()
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NL:
                self.state = 434
                self.match(ZCodeParser.NL)
                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 454
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.BREAK_KEYWORD, ZCodeParser.CONTINUE_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                self.state = 440
                self.loop_body_statement()
                pass
            elif token in [ZCodeParser.BEGIN_KEYWORD]:
                self.state = 441
                self.match(ZCodeParser.BEGIN_KEYWORD)
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

                self.state = 447
                self.loop_stmt_list()
                self.state = 448
                self.match(ZCodeParser.END_KEYWORD)
                self.state = 450 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 449
                    self.match(ZCodeParser.NL)
                    self.state = 452 
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
        self.enterRule(localctx, 84, self.RULE_loop_body_statement)
        self._la = 0 # Token type
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.statement()
                pass
            elif token in [ZCodeParser.BREAK_KEYWORD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.match(ZCodeParser.BREAK_KEYWORD)
                self.state = 459 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 458
                    self.match(ZCodeParser.NL)
                    self.state = 461 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.NL):
                        break

                pass
            elif token in [ZCodeParser.CONTINUE_KEYWORD]:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.match(ZCodeParser.CONTINUE_KEYWORD)
                self.state = 465 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 464
                    self.match(ZCodeParser.NL)
                    self.state = 467 
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


    class Loop_stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop_body_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_body_statementContext,0)


        def loop_stmt_list(self):
            return self.getTypedRuleContext(ZCodeParser.Loop_stmt_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_loop_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_stmt_list" ):
                return visitor.visitLoop_stmt_list(self)
            else:
                return visitor.visitChildren(self)




    def loop_stmt_list(self):

        localctx = ZCodeParser.Loop_stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_loop_stmt_list)
        try:
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUM_KEYWORD, ZCodeParser.BOOL_KEYWORD, ZCodeParser.STRING_KEYWORD, ZCodeParser.RETURN_KEYWORD, ZCodeParser.VAR_KEYWORD, ZCodeParser.DYNAMIC_KEYWORD, ZCodeParser.FUNC_KEYWORD, ZCodeParser.FOR_KEYWORD, ZCodeParser.BREAK_KEYWORD, ZCodeParser.CONTINUE_KEYWORD, ZCodeParser.IF_KEYWORD, ZCodeParser.SUB_OP, ZCodeParser.NOT_OP, ZCodeParser.ID, ZCodeParser.LEFT_PARENTHESIS, ZCodeParser.LEFT_BRACKET, ZCodeParser.TRUE_LIT, ZCodeParser.FALSE_LIT, ZCodeParser.REAL_LIT, ZCodeParser.COMMENT_LINE, ZCodeParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.loop_body_statement()
                self.state = 472
                self.loop_stmt_list()
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
        self.enterRule(localctx, 88, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.expression()
            self.state = 478
            self.match(ZCodeParser.ASSIGN_OP)
            self.state = 479
            self.expression()
            self.state = 481 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 480
                self.match(ZCodeParser.NL)
                self.state = 483 
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.logical_expr_sempred
        self._predicates[25] = self.adding_expr_sempred
        self._predicates[26] = self.multiplying_expr_sempred
        self._predicates[29] = self.index_expr_sempred
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
         




