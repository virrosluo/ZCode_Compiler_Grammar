grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: NL* declaration* EOF;

NUM_KEYWORD: 'number';
BOOL_KEYWORD: 'bool';
STRING_KEYWORD: 'string';

RETURN_KEYWORD: 'return';

VAR_KEYWORD: 'var';
DYNAMIC_KEYWORD: 'dynamic';
FUNC_KEYWORD: 'func';

FOR_KEYWORD: 'for';
UNTIL_KEYWORD: 'until';
BY_KEYWORD: 'by';

BREAK_KEYWORD: 'break';
CONTINUE_KEYWORD: 'continue';

IF_KEYWORD: 'if';
ELSE_KEYWORD: 'else';
ELIF_KEYWORD: 'elif';

BEGIN_KEYWORD: 'begin';
END_KEYWORD: 'end';

ASSIGN_OP: '<-';
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
NOT_OP: 'not';
AND_OP: 'and';
OR_OP: 'or';
EQUAL_OP: '=';
INEQUAL_OP: '!=';
LESS_OP: '<';
LESSEQUAL_OP: '<=';
LARGE_OP: '>';
LARGEEQUAL_OP: '>=';
CONCAT_OP: '...';
EQUAL_STR_OP: '==';


ID : [a-zA-Z_]+[a-zA-Z0-9_]*;

LEFT_PARENTHESIS : '(';
RIGHT_PARENTHESIS : ')';

LEFT_BRACKET: '[';
RIGHT_BRACKET: ']';

SEPARATOR_KEYWORD: ',';

TRUE_LIT: 'true';
FALSE_LIT: 'false';

INT_LIT: INTPART;

REAL_LIT: INTPART DECPART | INTPART DECPART? EXPPART;
fragment INTPART: [0-9]+;
fragment DECPART: [.][0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;

STRING_LIT: '"' (~[\\'\r\n\f] | ('\\' [bfrnt\\']) | ('\'"'))*? '"' {self.text = self.text[1:-1]};
// * -> Greedy:  /* */ -> If exists another */ => It also will take to the last */
// *? -> Non-Greedy: It will take least character that satisfy the regex. In comment command -> /* */ If in command, it see another */ => The second */ will not be taken

NL : 'r'?'\n' {self.text = self.text.replace('\r','')};
// NL: '\n';
WS : [ \t\r]+ -> skip ; // skip spaces, tabs
COMMENT_LINE: '##' ~[\r\n]* -> skip;

NEWLINE_STRING: '"' ( ~["\\'\r\n\f] | '\\' [bfrnt\\'] | ('\'"') )*? [\r\n\f] {raise UncloseString(self.text[1:-1])} ;

UNCLOSE_STRING: '"' ( ~["\\'\r\n\f] | ('\\' [bfrnt\\']) | ('\'"') )* {raise UncloseString(self.text[1:])};

ILLEGAL_ESCAPE: '"' ( ~["\\'] | ('\'"') | ('\\' [bfrnt\\']))*? ('\\' ~[bfrnt\\'] | '\'' ~["]) {raise IllegalEscape(self.text[1:])};

ERROR_TOKEN: . {raise ErrorToken(self.text)};


// ----------------------------------------------------------------- PARSER -------------------------------------------------------------------------

declaration
		: variable_stat
		| block_stat 
		| function_stat ;

variable_stat
		: explicit_declare NL+
		| implicit_declare NL+;

dtype: NUM_KEYWORD | BOOL_KEYWORD | STRING_KEYWORD;

explicit_declare: array_declare
		| primitive_declare;

idlist: ID (SEPARATOR_KEYWORD ID)*;

primitive_declare: dtype idlist (ASSIGN_OP expression)?;

array_declare: dtype ID LEFT_BRACKET expression (SEPARATOR_KEYWORD expression)* RIGHT_BRACKET (ASSIGN_OP expression)?;

implicit_declare: VAR_KEYWORD idlist ASSIGN_OP expression
		| DYNAMIC_KEYWORD idlist (ASSIGN_OP expression)? ;

		// ----------------------------------------------------------------

function_stat: function_definition
		| function_declaration NL+;

function_definition: FUNC_KEYWORD ID LEFT_PARENTHESIS param_list RIGHT_PARENTHESIS NL* block_stat;
function_declaration: FUNC_KEYWORD ID LEFT_PARENTHESIS param_list RIGHT_PARENTHESIS;
param_list: (parameter (SEPARATOR_KEYWORD parameter)*)?;
parameter: (NUM_KEYWORD | STRING_KEYWORD | BOOL_KEYWORD) ID;

		// ----------------------------------------------------------------

block_stat: BEGIN_KEYWORD NL statement* END_KEYWORD NL+
		| statement ;	// Đảm bảo rằng statement có xuống dòng trong đó

		// ----------------------------------------------------------------

// Đảm bảo rằng các statement này đều có dấu xuống dòng ở cuối dòng
statement: control_stat 
		| loop_stat 
		| variable_stat 
		| function_stat 
		| expression NL+
		| assignment
		| (RETURN_KEYWORD expression? NL+)
		| comment ;

	// ---------------------------------------------------------------- COMMENT_LINE_STRUCTURE
comment: COMMENT_LINE NL+;
		
	// ---------------------------------------------------------------- EXPRESSION

// Concat operator
expression
		: relational_expr CONCAT_OP relational_expr
		| relational_expr ;

relation_operation: EQUAL_OP | EQUAL_STR_OP | INEQUAL_OP | LESS_OP | LARGE_OP | LESSEQUAL_OP | LARGEEQUAL_OP;
relational_expr: logical_expr relation_operation logical_expr
		| logical_expr;

logical_expr: logical_expr (AND_OP | OR_OP) adding_expr
		| adding_expr;

adding_expr: adding_expr (ADD_OP | SUB_OP) multiplying_expr
		| multiplying_expr ;
multiplying_expr: multiplying_expr (MUL_OP | DIV_OP | MOD_OP) not_logical
		| not_logical ;

not_logical: NOT_OP expression
		| sign_expr ;

sign_expr: SUB_OP expression
		| index_expr;

index_expr: index_expr LEFT_BRACKET expression (SEPARATOR_KEYWORD expression)* RIGHT_BRACKET
		| parenthesis_expr ;

parenthesis_expr: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
		| term ;

term
		: REAL_LIT 
		| INT_LIT 
		| TRUE_LIT | FALSE_LIT
		| STRING_LIT
		| ID
		| function_expr
		| array_expr;

array_expr : LEFT_BRACKET (expression (SEPARATOR_KEYWORD expression)*)? RIGHT_BRACKET;

function_expr: ID LEFT_PARENTHESIS (expression (SEPARATOR_KEYWORD expression)*)? RIGHT_PARENTHESIS ;

	// ---------------------------------------------------------------- CONTROL STATEMENT (MAYBE HAVE ERROR)

ifst_component: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS NL* block_stat
		| expression NL* block_stat;
control_stat: IF_KEYWORD ifst_component (ELIF_KEYWORD ifst_component)* (ELSE_KEYWORD block_stat)? ;

	// ---------------------------------------------------------------- LOOP STATEMENT

loop_stat: FOR_KEYWORD ID UNTIL_KEYWORD expression BY_KEYWORD expression NL* (loop_body_statement | (BEGIN_KEYWORD NL loop_body_statement* END_KEYWORD NL+) );
loop_body_statement
		: statement 
		| BREAK_KEYWORD NL+ 
		| CONTINUE_KEYWORD NL+;

	// ----------------------------------------------------------------

// Assignment thì expression phía trước ASSIGN_OP không thể là 1 cái array_expr được mà nó phải là 
assignment: <assoc=right> expression ASSIGN_OP expression NL+;
lhs: index_variable;

index_variable: index_variable LEFT_BRACKET expression (SEPARATOR_KEYWORD expression)* RIGHT_BRACKET
		| parenthesis_variable ;

parenthesis_variable: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
		| lhs_variable ;

lhs_variable: ID | function_expr;