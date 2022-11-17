grammar popl;

start: (expr NEWLINE)* ;

expr: expr ('*' | '/' | '+' | '-' | '%') expr
    | INT
    | '(' expr ')';

VAR: [a-zA-Z0-9]+;

assign: VAR ('=' | '+=' | '-=' | '*=' | '/=') expr;
NEWLINE: [\n]+ ;
INT: [0-9]+ ;

if: VAR ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') VAR;