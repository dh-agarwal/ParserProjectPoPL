grammar popl;

start: (expr NEWLINE)* 
    | (assign NEWLINE)* ;
INT: [0-9]+ ;

expr: expr ('*' | '/' | '+' | '-' | '%') expr
    | INT
    | VAR
    | '(' expr ')';

VAR: [a-zA-Z_][a-zA-Z0-9_]*;

assign: VAR ('=' | '+=' | '-=' | '*=' | '/=') expr;
NEWLINE: [\n]+
    | [\r][\n]+ ;

IF: VAR ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') VAR;