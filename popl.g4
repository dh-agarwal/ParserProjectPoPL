grammar popl;

//KEYWORD: 'if';
BOOLCOMP: 'and' | 'or';
INT: [0-9]+;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
SPACE: ' ' | '\t';
//NEWLINE: '\n' | '\r\n';
//WHITESPACE: SPACE | NEWLINE;
EMPTYLINE: SPACE* ('\n' | '\r\n')+;
MATHCOMP: '==' | '>=' | '<=' | '>' | '<' | '!=';


start: line;
line: assign line
    | expr line
    | EMPTYLINE line
    | ifblock elifblock* elseblock? line
    | SPACE* EOF;

conditional: (SPACE* MATHCOMP SPACE* | SPACE+ BOOLCOMP SPACE+) expr conditional
    | /* epsilon */;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

ifbody: ('\t' (assign | expr) NEWLINE*)*;
ifstatement: 'if' SPACE+ expr conditional SPACE* ':' EMPTYLINE;
ifblock: ifstatement ifbody;

elifstatement: 'elif' SPACE+ expr conditional SPACE* ':' EMPTYLINE;
elifblock: elifstatement ifbody;

elsestatement: 'else:' EMPTYLINE;
elseblock: elsestatement ifbody;
