grammar popl;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from poplParser import poplParser
}
@lexer::members {
class poplDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: poplLexer = lexer

    def pull_token(self):
        return super(poplLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.poplDenter(self, self.NL, poplParser.INDENT, poplParser.DEDENT, False)
    return self.denter.next_token()
}

NL: ((' ' | '\t')* '\r'? '\n' '\t'*);

NOT: 'not';
BOOLCOMP: 'and' | 'or';
MATHCOMP: '==' | '>=' | '<=' | '>' | '<' | '!=';
INT: [0-9]+;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
SPACE: ' ' | '\t';
EMPTYLINE: SPACE* NL+;

// start: line;
// line: assign line
//     | expr line
//     | EMPTYLINE line
//     | ifblock elifblock* elseblock? line
//     | SPACE* EOF;

start: statement+ EOF;

statement: assign SPACE* NL
    | expr SPACE* NL
    | ifblock elifblock* elseblock?;

conditional: (SPACE* MATHCOMP SPACE* | SPACE+ BOOLCOMP (SPACE+ | SPACE+ NOT SPACE+)) expr conditional
    | /* epsilon */;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

body: statement+;
ifstatement: 'if' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':';
ifblock: ifstatement INDENT body DEDENT;

elifstatement: 'elif' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':';
elifblock: elifstatement INDENT body DEDENT;

elsestatement: 'else' SPACE* ':';
elseblock: elsestatement INDENT body DEDENT;

// look into WS