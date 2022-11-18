grammar popl;

INT: [0-9]+;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
SPACE: ' ' | '\t';
NEWLINE: '\n' | '\r\n';
WHITESPACE: SPACE | NEWLINE;
EMPTYLINE: SPACE* NEWLINE+;

start: line;

line: assign line
    | expr line
    | NEWLINE line // come back to this
    | EMPTYLINE line
    | SPACE* EOF;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;


IF: VAR ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') VAR;