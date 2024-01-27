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

REAL_LIT: INTPART | INTPART DECPART | INTPART DECPART? EXPPART;
fragment INTPART: [0-9]+;
fragment DECPART: [.][0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;

NL : 'r'?'\n' {self.text = self.text.replace('\r','')};
// NL: '\n';
WS : [ \t\r]+ -> skip ;
COMMENT_LINE: '##' ~[\r\n]* -> skip;

UNCLOSE_STRING: '"' ( ~["\\'\r\n\f] | ('\\' [bfrnt\\']) | ('\'' ["]?) )* {raise UncloseString(self.text[1:])};

STRING_LIT: '"' ( ~["\\'\r\n\f] | ('\\' [bfrnt\\']) | ('\'' ["]?) )* '"' {self.text = self.text[1:-1]};

ILLEGAL_ESCAPE: '"' ( ~["\\'] | ('\'' ["]?) | ('\\' [bfrnt\\']))*? ('\\' ~[bfrnt\\']) {raise IllegalEscape(self.text[1:])};

NEWLINE_STRING: '"' ( ~["\\'\r\n\f] | '\\' [bfrnt\\'] | ('\'' ["]?) )*? [\r\n\f] {raise UncloseString(self.text[1:-1])} ;

ERROR_TOKEN: . {raise ErrorToken(self.text)};

// ----------------------------------------------------------------- PARSER -------------------------------------------------------------------------

declaration
		: variable_stat
		| function_stat ;

variable_stat
		: explicit_declare NL+
		| implicit_declare NL+;

dtype: NUM_KEYWORD | BOOL_KEYWORD | STRING_KEYWORD;

explicit_declare: array_declare
		| primitive_declare;

idlist: ID idlist_tail;
idlist_tail: SEPARATOR_KEYWORD ID idlist_tail | ;

primitive_declare: dtype idlist (ASSIGN_OP expression | );

array_declare: dtype ID LEFT_BRACKET expression_nonempty_list RIGHT_BRACKET (ASSIGN_OP expression | );

implicit_declare: VAR_KEYWORD idlist ASSIGN_OP expression
		| DYNAMIC_KEYWORD idlist (ASSIGN_OP expression |);

		// ----------------------------------------------------------------

function_stat: function_definition
		| function_declaration NL+;

function_definition: FUNC_KEYWORD ID LEFT_PARENTHESIS param_list RIGHT_PARENTHESIS (NL | ) block_stat;
function_declaration: FUNC_KEYWORD ID LEFT_PARENTHESIS param_list RIGHT_PARENTHESIS;
param_list: parameter param_list_tail |;
param_list_tail: SEPARATOR_KEYWORD parameter param_list_tail | ;
parameter : dtype ID 
		  | dtype ID LEFT_BRACKET expression_nonempty_list RIGHT_BRACKET ;

		// ----------------------------------------------------------------

statement_list: statement statement_list_tail | ;
statement_list_tail: statement statement_list_tail | ;

block_stat: BEGIN_KEYWORD NL+ statement_list END_KEYWORD NL+
		| statement ;	// Đảm bảo rằng statement có xuống dòng trong đó

		// ----------------------------------------------------------------

// Đảm bảo rằng các statement này đều có dấu xuống dòng ở cuối dòng
statement: control_stat 
		| loop_stat 
		| variable_stat 
		| function_stat 
		| expression NL+
		| assignment
		| RETURN_KEYWORD (expression | ) NL+
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

index_expr: index_expr LEFT_BRACKET expression_nonempty_list RIGHT_BRACKET
		| parenthesis_expr ;

parenthesis_expr: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
		| term ;

term
		: REAL_LIT 
		| TRUE_LIT | FALSE_LIT
		| STRING_LIT
		| ID
		| function_expr
		| array_expr;

array_expr : LEFT_BRACKET expression_list RIGHT_BRACKET;
function_expr: ID LEFT_PARENTHESIS expression_list RIGHT_PARENTHESIS ;

expression_list: expression expression_list_tail | ;
expression_list_tail: SEPARATOR_KEYWORD expression expression_list_tail | ;

expression_nonempty_list: expression expression_nonempty_tail;
expression_nonempty_tail: SEPARATOR_KEYWORD expression expression_nonempty_tail | ;

	// ---------------------------------------------------------------- CONTROL STATEMENT (MAYBE HAVE ERROR)

control_stat: IF_KEYWORD ifst_component elif_stmt_list (ELSE_KEYWORD NL* block_stat | ) ;

elif_stmt_list: ELIF_KEYWORD ifst_component elif_stmt_list | ;
ifst_component: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS NL* block_stat ;

	// ---------------------------------------------------------------- LOOP STATEMENT

loop_stat: FOR_KEYWORD ID UNTIL_KEYWORD expression BY_KEYWORD expression NL* (loop_body_statement | (BEGIN_KEYWORD NL+ loop_stmt_list END_KEYWORD NL+) );
loop_body_statement
		: statement 
		| BREAK_KEYWORD NL+ 
		| CONTINUE_KEYWORD NL+;

loop_stmt_list: loop_body_statement loop_stmt_list | ;

	// ----------------------------------------------------------------

// Assignment thì expression phía trước ASSIGN_OP không thể là 1 cái array_expr được mà nó phải là 
assignment: <assoc=right> expression ASSIGN_OP expression NL+;