grammar PtGrammar;

// PARSER
programa :                      (bloco)* EOF;
bloco :                         comando fim_de_instrucao |
                                estrutura_de_controle;
comando :                       declaracao |
                                saida |
                                atribuicao;
declaracao :                    tipo atribuicao;
atribuicao :                    identificador operador_atribuicao valor_atribuido;
valor_atribuido :               expressao |
                                texto |
                                entrada;
expressao :                     parenteses_expressao compoe_expressao |
                                valor compoe_expressao;
parenteses_expressao :          abre_parenteses expressao fecha_parenteses;
compoe_expressao :              (operador_aritmetico expressao)*;
estrutura_de_controle :         faca bloco_estrutura_de_controle enquanto condicao fim_de_instrucao |
                                se condicao bloco_estrutura_de_controle (se_nao)? |
                                enquanto condicao bloco_estrutura_de_controle;
se_nao :                        senao bloco_estrutura_de_controle;
bloco_estrutura_de_controle :   abre_chaves (bloco)* fecha_chaves;
condicao :                      abre_parenteses expressao_booleana fecha_parenteses;
expressao_booleana :            expressao operador_binario expressao;
valor :                         identificador |
                                numero |
                                texto;
saida :                         imprima abre_parenteses expressao fecha_parenteses;
entrada:                        entrada_de_texto | entrada_numerica;

// LEXER
numero :                        TERMINAL_NUMERO;
identificador :                 TERMINAL_IDENTIFICADOR;
texto :                         TERMINAL_TEXTO;
tipo :                          ('número'|'texto');
operador_binario :              ('>'|'<'|'>='|'<='|'<>'|'=');
operador_aritmetico :           ('+'|'-'|'*'|'/');
fim_de_instrucao :              '.';
operador_atribuicao :           ':=';
abre_parenteses :               '(';
fecha_parenteses :              ')';
abre_chaves :                   '{';
fecha_chaves :                  '}';
faca :                          'faça';
enquanto :                      'enquanto';
se :                            'se';
senao :                         'senão';
entrada_de_texto :              'leia_texto';
entrada_numerica :              'leia_número';
imprima:                        'mostre';

TERMINAL_NUMERO :               [0-9]+(','[0-9]+)? ;
TERMINAL_IDENTIFICADOR :        [a-zA-Z]([a-zA-Z0-9_])*;
TERMINAL_TEXTO :                '"' ~'"'* '"';
WHITESPACE :                    [ \t] -> skip;
NEWLINE :                       '\r'? '\n' -> skip;
