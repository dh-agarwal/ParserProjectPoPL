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

NL: ('\r'? '\n' '\t'*);

INT: [0-9]+;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
SPACE: ' ';
WHITESPACE: SPACE | NL;
EMPTYLINE: SPACE* NL+;

start: statement+ EOF;

statement: assign NL
    | ifblock ;

ifline: assign
    | expr
    | EMPTYLINE
    | ifblock elifblock*
    | SPACE* EOF;

expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr
    | INT
    | VAR
    | '(' expr ')';

assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr;

ifbody: statement+;
ifstatement: 'if' SPACE* (VAR | INT) SPACE* ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') SPACE* (VAR | INT) SPACE* ':';
ifblock: ifstatement INDENT ifbody DEDENT ;

elifstatement: 'if' | SPACE* (VAR | INT) SPACE* ('==' | '>=' | '<=' | '>' | '<' | '!=' | 'and' | 'or' | 'not') SPACE* (VAR | INT) SPACE* ':' NL;
elifblock: elifstatement ifbody;

elsestatement: 'else:' NL;
elseblock: elsestatement ifbody;