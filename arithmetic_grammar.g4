grammar arithmetic_grammar;

program : expression+ ;
expression : expr_soma;
expr_soma : expr_mult compoe_soma | ABRE_PAR expr_soma FECHA_PAR;
compoe_soma : (type_OP_ADD expr_mult compoe_soma)*;
expr_mult : NUMERO compoe_mult;
compoe_mult : (type_OP_MUL NUMERO)*;
type_OP_ADD : OP_ADD | OP_SUB;
type_OP_MUL : OP_MUL | OP_DIV;
NUMERO : [0–9]+(','[0-9])+? ;
OP_ADD : [+];
OP_SUB : [-];
OP_MUL : [*];
OP_DIV : [/];
ABRE_PAR : '(';
FECHA_PAR : ')';
VAZIO : [ \n\t]+ -> skip;
