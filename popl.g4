grammar popl;

//KEYWORD: 'if';
NOT: 'not';
BOOLCOMP: 'and' | 'or';
MATHCOMP: '==' | '>=' | '<=' | '>' | '<' | '!=';
INT: [0-9]+;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
SPACE: ' ' | '\t';
//NEWLINE: '\n' | '\r\n';
//WHITESPACE: SPACE | NEWLINE;
EMPTYLINE: SPACE* ('\n' | '\r\n')+;


start: line;
line: assign line
    | expr line
    | EMPTYLINE line
    | ifblock elifblock* elseblock? line
    | SPACE* EOF;

conditional: (SPACE* MATHCOMP SPACE* | SPACE+ BOOLCOMP (SPACE+ | SPACE+ NOT SPACE+)) expr conditional
    | /* epsilon */;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

ifbody: ('\t' (assign | expr) EMPTYLINE*)+;
ifstatement: 'if' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':' EMPTYLINE+;
ifblock: ifstatement ifbody;

elifstatement: 'elif' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':' EMPTYLINE+;
elifblock: elifstatement ifbody;

elsestatement: 'else:' EMPTYLINE+;
elseblock: elsestatement ifbody;
