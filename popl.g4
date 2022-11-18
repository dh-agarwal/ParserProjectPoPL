grammar popl;

start: line;

line: assign line
    | expr line
    | NEWLINE line
    | EMPTYLINE line
    | SPACE* EOF;

INT: [0-9]+ ;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

VAR: [a-zA-Z_][a-zA-Z0-9_]*;

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

SPACE: ' ' | '\t';
NEWLINE: '\n' | '\r\n';
WHITESPACE: SPACE | NEWLINE;
EMPTYLINE: SPACE* NEWLINE+;

IF: VAR ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') VAR;