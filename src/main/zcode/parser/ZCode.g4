// 2153379
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: nl_nullable_list decl_list EOF;
decl_list: declaration decl_list | declaration;

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

// nullable list of newlines
nl_nullable_list: NL nl_nullable_list |;

// not null list of newlines
nl_list: NL nl_list | NL;

declaration
		: variable_stat
		| function_stat ;

variable_stat
		: explicit_declare nl_list
		| implicit_declare nl_list;

dtype: NUM_KEYWORD | BOOL_KEYWORD | STRING_KEYWORD;

explicit_declare: array_declare
		| primitive_declare;

primitive_declare: dtype ID (ASSIGN_OP expression | );

array_declare: dtype ID LEFT_BRACKET expression_nonempty_list RIGHT_BRACKET (ASSIGN_OP LEFT_BRACKET array_lit_list RIGHT_BRACKET | );
array_lit_list: array_lit array_lit_tail | ;
array_lit_tail: SEPARATOR_KEYWORD array_lit array_lit_tail | ;
array_lit: LEFT_BRACKET array_lit_list RIGHT_BRACKET 
		| expression_list;

implicit_declare: VAR_KEYWORD ID ASSIGN_OP expression
		| DYNAMIC_KEYWORD ID (ASSIGN_OP expression | );

		// ----------------------------------------------------------------

function_stat: function_definition
		| function_declaration ;

function_definition: FUNC_KEYWORD ID LEFT_PARENTHESIS param_list RIGHT_PARENTHESIS nl_nullable_list (block_stat | return_stat);
function_declaration: FUNC_KEYWORD ID LEFT_PARENTHESIS param_list RIGHT_PARENTHESIS nl_list;

param_list: parameter param_list_tail |;
param_list_tail: SEPARATOR_KEYWORD parameter param_list_tail | ;
parameter 
		: dtype ID 
		| dtype ID LEFT_BRACKET expression_nonempty_list RIGHT_BRACKET ;


		// ----------------------------------------------------------------

// Đảm bảo rằng các statement này đều có dấu xuống dòng ở cuối dòng
statement: control_stat 
		| loop_stat
		| variable_stat
		| function_stat
		| block_stat
		| expression nl_list
		| assignment
		| return_stat
		| break_stat
		| continue_stat;

		// ----------------------------------------------------------------

statement_list: statement statement_list | ;

	// ---------------------------------------------------------------- RETURN BREAK CONTINUE STATEMENT
return_stat: RETURN_KEYWORD (expression | ) nl_list ;
break_stat: BREAK_KEYWORD nl_list ;
continue_stat: CONTINUE_KEYWORD nl_list ;
block_stat: BEGIN_KEYWORD nl_list statement_list END_KEYWORD nl_list;

	// ---------------------------------------------------------------- COMMENT_LINE_STRUCTURE
comment: COMMENT_LINE nl_list;
		
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

index_expr: parenthesis_expr LEFT_BRACKET expression_nonempty_list RIGHT_BRACKET
		| parenthesis_expr ;

parenthesis_expr: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
		| term ;

term
		: REAL_LIT 
		| TRUE_LIT | FALSE_LIT
		| STRING_LIT
		| ID
		| function_expr ;

function_expr: ID LEFT_PARENTHESIS expression_list RIGHT_PARENTHESIS ;

expression_list: expression expression_list_tail | ;
expression_list_tail: SEPARATOR_KEYWORD expression expression_list_tail | ;

expression_nonempty_list: expression expression_nonempty_tail;
expression_nonempty_tail: SEPARATOR_KEYWORD expression expression_nonempty_tail | ;

	// ---------------------------------------------------------------- CONTROL STATEMENT (MAYBE HAVE ERROR)

control_stat: IF_KEYWORD ifst_component elif_stmt_list (ELSE_KEYWORD nl_nullable_list statement | ) ;

elif_stmt_list: ELIF_KEYWORD ifst_component elif_stmt_list | ;
ifst_component: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS nl_nullable_list statement ;

	// ---------------------------------------------------------------- LOOP STATEMENT

loop_stat: FOR_KEYWORD ID UNTIL_KEYWORD expression BY_KEYWORD expression nl_nullable_list statement ;

	// ----------------------------------------------------------------

// Assignment thì expression phía trước ASSIGN_OP không thể là 1 cái array_expr được mà nó phải là 
assignment: <assoc=right> expression ASSIGN_OP expression nl_list;