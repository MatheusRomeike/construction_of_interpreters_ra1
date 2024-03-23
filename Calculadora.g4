grammar Calculadora;

start: line (ENTER line)*;

line: expression;

expression: NUMBER | '(' expression expression SYMBOL ')' | res | mem;

res: '(' expression 'RES' ')';
mem: '(' expression MEM ')' | MEM | '(' MEM ')';

SYMBOL: SUM | SUBTRACTION | MULTIPLY | DIVISION | INTEGER_DIVISION | MODULO | POTENTIATION;
SUM: '+';
SUBTRACTION: '-';
MULTIPLY: '*';
DIVISION: '|';
INTEGER_DIVISION: '/';
MODULO: '%';
POTENTIATION: '^';
ENTER: '\n';
RES: 'RES';
MEM: 'MEM';
NUMBER: '-'?INTEGER+('.'INTEGER+)?;
INTEGER: [0-9];

WS : [ \t\r]+ -> skip;