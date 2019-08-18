grammar number_grammar;

r : NUMERO+ ;
number : NUMERO+;

WS : [ \t\r\n]+ -> skip ; 
NUMERO : [0-9]+(','[0-9]+)? ;

expression : bracket_expression compose_expression | terminal_number compose_expression
bracket_expression : open_bracket expression close_bracket;
compose_expression : (operator expression)*;
number : TERMINAL_NUMBER;
open_bracket : TERMINAL_OPEN_BRACKET;
close_bracket : TERMINAL_CLOSE_BRACKET;
Operators : TERMINAL_OPERATORS;
TERMINAL_NUMBER : [0-9]+(','[0-9]+)? ;
TERMINAL_OPEN_BRACKET : '(';
TERMINAL_CLOSE_BRACKET : ')';
TERMINAL_OPERATORS : [+-*/];

Expr -> Bracket_expressions Compose_expr | Number Compose_expr.
Compose_expr -> Operators Expr | .
Bracket_expressions -> Open_brack Expr Close_brack.
Number -> number.
Operators -> Add_operators | Prod_operators.
Add_operators -> plus | minus.
Prod_operators -> times | divided.
Open_brack -> open_bracket.
Close_brack -> close_bracket.