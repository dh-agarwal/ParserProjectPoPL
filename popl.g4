// Python Parser Project
// By Dhruv Agarwal, Andrew Chang, Ryan Huynh, Adi Pillai, and Ashwin Prayaga

grammar popl;

tokens { INDENT, DEDENT }

// Lexer code
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
BOOLCOMP: 'and' | 'or' | 'in';
MATHCOMP: '==' | '>=' | '<=' | '>' | '<' | '!=';
INT: [0-9]+;
QUOTES: '"' | '\'';
STRING: QUOTES .*? QUOTES;
VAR: [a-zA-Z_][a-zA-Z0-9_]*;
SPACE: ' ' | '\t';
COMMENT:  '#' (~'\n')*;
MULTILINECOMMENT: ('"""' .*? '"""')+ | ('\'\'\'' .*? '\'\'\'')+ ;

start: statement* EOF;

statement: assign NL
    | expr NL
    | COMMENT NL
    | MULTILINECOMMENT NL
    | ifblock elifblock* elseblock?
    | whileblock elseblock?
    | forblock elseblock?
    | funcblock
    | funccall
    | NL;


// Arithmetic operators
expr: expr SPACE* ('*' | '/' | '+' | '-' | '%') SPACE* expr SPACE* COMMENT?
    | INT
    | STRING
    | VAR
    | '(' expr ')';


// Assignment operators
assign: VAR SPACE* ('=' | '+=' | '-=' | '*=' | '/=') SPACE* expr SPACE* COMMENT?;


// Conditional statements
conditional: (SPACE* MATHCOMP SPACE* | SPACE+ BOOLCOMP (SPACE+ | SPACE+ NOT SPACE+)) expr conditional
    | /* epsilon */;
forconditional: VAR SPACE* 'in' SPACE* VAR;

body: statement+ ;

// if, elif, else, while, and for
ifstatement: 'if' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':' SPACE* COMMENT?;
ifblock: ifstatement INDENT body DEDENT;

elifstatement: 'elif' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':' SPACE* COMMENT?;
elifblock: elifstatement INDENT body DEDENT;

elsestatement: 'else' SPACE* ':' SPACE* COMMENT*;
elseblock: elsestatement INDENT body DEDENT;

whilestatement: 'while' SPACE+ (NOT SPACE+)? expr conditional SPACE* ':' SPACE* COMMENT?;
whileblock: whilestatement INDENT body DEDENT;

forstatement: 'for' SPACE+ forconditional SPACE* ':' SPACE* COMMENT?;
forblock: forstatement INDENT body DEDENT;


// Function implementations
args: (SPACE* VAR SPACE* (',' SPACE* VAR SPACE*)*)*;
funcstatement: 'def' SPACE+ VAR SPACE* '(' args ')' SPACE* ':' SPACE* COMMENT?;
funcreturn: 'return' SPACE* expr SPACE* COMMENT?;
funcbody: (statement | funcreturn)+;
funcblock: funcstatement INDENT funcbody DEDENT;


// Function calls
callargs: (SPACE* expr SPACE* (',' SPACE* expr SPACE*)*)*;
funccall: VAR SPACE* '(' callargs ')' SPACE* COMMENT?;


reserved:
     'False' | 'def' | 'if' | 'raise'
    | 'None' | 'del' | 'import' | 'return' | 'True'
    | 'elif' | 'in' | 'try' | 'and' | 'else'
    | 'is'| 'while' | 'as'
    | 'except' | 'lambda' | 'with' | 'assert' 
    | 'finally' | 'nonlocal' | 'yield' | 'break'
    | 'for' | 'not'| 'class' | 'from' | 'or'
    | 'continue' | 'global' | 'pass';