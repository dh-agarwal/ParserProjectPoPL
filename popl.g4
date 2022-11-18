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
    | ifblock elifblock* elseblock? line
    | SPACE* EOF;

ifline: assign
    | expr
    | EMPTYLINE
    | ifblock elifblock* elseblock?
    | SPACE* EOF;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

ifbody: ('\t' (ifline) NEWLINE*)*;
ifstatement: 'if' | SPACE* (VAR | INT) SPACE* ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') SPACE* (VAR | INT) SPACE* ':' NEWLINE;
ifblock: ifstatement ifbody;

elifstatement: 'elif' | SPACE* (VAR | INT) SPACE* ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') SPACE* (VAR | INT) SPACE* ':' NEWLINE;
elifblock: elifstatement ifbody;

elsestatement: 'else:' NEWLINE;
elseblock: elsestatement ifbody;