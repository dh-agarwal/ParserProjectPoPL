grammar popl;

start: EMPTYLINE* (fexpr | assign | /* epsilon */) (EMPTYLINE+ (fexpr | assign))* EMPTYLINE*;
INT: [0-9]+ ;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

fexpr: (expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr) | SPACE*;

VAR: [a-zA-Z_][a-zA-Z0-9_]*;

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

SPACE: ' ' | '\t';
NEWLINE: '\n' | '\r\n' ;
WHITESPACE: SPACE | NEWLINE;
EMPTYLINE: SPACE* NEWLINE;

IF: VAR ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') VAR;