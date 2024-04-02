//Gabriel Barros, Guilherme Ramos, Matheus Romeike
grammar Calculadora;

//start is the initial rule
start: line (ENTER line)*;


//line is the rule that represents a line of the input
line: expression;

//expression is the rule that represents an expression, it can be a number, a result, a memory or a operation
expression: NUMBER | '(' expression expression SYMBOL ')' | res | mem;

//res is the rule that represents the result of the N line of the input
res: '(' expression 'RES' ')';
//mem is the rule that represents the memory, it can be a number or a memory. number set the memory to the number, memory get the memory value
mem: '(' expression MEM ')' | MEM | '(' MEM ')';

//tokens
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

//skip whitespaces
WS : [ \t\r]+ -> skip;