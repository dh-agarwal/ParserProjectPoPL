grammar popl;
hi : 'hello' ID ;
ID : [a-z]+ ;
WS : [ \t\r\n]+ -> skip ;