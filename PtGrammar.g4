grammar PtGrammar;

// PARSER
programa :                      (bloco)* EOF;
bloco :                         comando fim_de_instrucao |
                                estrutura_de_controle;
comando :                       declaracao |
                                entrada |
                                saida |
                                atribuicao;
saida :                         imprima abre_parenteses expressao fecha_parenteses;
declaracao :                    tipo atribuicao;
atribuicao :                    identificador operador_atribuicao valor_atribuido;
valor_atribuido :               expressao |
                                texto;
expressao :                     parenteses_expressao compoe_expressao |
                                valor compoe_expressao;
parenteses_expressao :          abre_parenteses expressao fecha_parenteses;
compoe_expressao :              (operador expressao)*;
estrutura_de_controle :         faca bloco_estrutura_de_controle enquanto condicao |
                                se condicao bloco_estrutura_de_controle se_nao |
                                enquanto condicao bloco_estrutura_de_controle;
se_nao :                        (senao bloco_estrutura_de_controle)?;
bloco_estrutura_de_controle :   abre_chaves (bloco)* fecha_chaves;
condicao :                      abre_parenteses expressao_booleana fecha_parenteses;
expressao_booleana :            expressao operador_binario expressao;
texto :                         terminal_texto;
valor :                         identificador |
                                numero |
                                texto;


identificador :                 TERMINAL_IDENTIFICADOR;
operador_atribuicao :           terminal_operador_atribuicao;
abre_parenteses :               terminal_abre_parenteses;
fecha_parenteses :              terminal_fecha_parenteses;
operador :                      terminal_operador;
fim_de_instrucao :              terminal_fim_de_instrucao;
se :                            terminal_se;
senao :                         terminal_senao;
abre_chaves :                   terminal_abre_chaves;
fecha_chaves :                  terminal_fecha_chaves;
operador_binario :              terminal_operador_binario;
enquanto :                      terminal_enquanto;
numero :                        TERMINAL_NUMERO;
tipo :                          terminal_tipo;
entrada:                        terminal_entrada;
imprima:                        terminal_mostre;
faca :                          terminal_faca;

// LEXER
TERMINAL_NUMERO :               [0-9]+(','[0-9]+)? ;
terminal_abre_parenteses :      '(';
terminal_fecha_parenteses :     ')';
terminal_abre_chaves :          '{';
terminal_fecha_chaves :         '}';

terminal_texto :                '"' ~'"'* '"';
terminal_operador :             ('+'|'-'|'*'|'/');
terminal_fim_de_instrucao :     '.';
TERMINAL_IDENTIFICADOR :        [a-zA-Z]([a-zA-Z0-9_])*;
terminal_operador_atribuicao :  ':=';
terminal_operador_binario :     ('>'|'<'|'>='|'<='|'<>'|'=');

terminal_tipo :                 ('número'|'texto');
terminal_faca :                 'faça';

terminal_enquanto :             'enquanto';
terminal_se :                   'se';
terminal_senao :                'senão';
terminal_mostre :               'mostre';
terminal_entrada :              'leia';

WHITESPACE :                    [ \t] -> skip;
NEWLINE :                       '\r'? '\n' -> skip;