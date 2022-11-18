grammar popl;

start: line;

line: assign line
    | expr line
    | NEWLINE line
    | EMPTYLINE line
    | ifblock line
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

ifbody: ('\t' (assign | expr) NEWLINE*)*;
ifstatement: 'if' SPACE* (VAR | INT) SPACE* ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') SPACE* (VAR | INT) SPACE* ':' NEWLINE;
ifblock: ifstatement ifbody;