grammar popl;

start: (expr NEWLINE)* ;
INT: [0-9]+ ;

expr: expr ('*' | '/' | '+' | '-' | '%') expr
    | INT
    | '(' expr ')';

VAR: [a-zA-Z0-9]+;

assign: VAR ('=' | '+=' | '-=' | '*=' | '/=') expr;
NEWLINE: [\n]+
    | [\r][\n]+ ;

IF: VAR ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') VAR;