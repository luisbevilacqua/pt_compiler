grammar PtGrammar;

// PARSER
programa :                      bloco (programa)*;
bloco :                         comando fim_de_instrucao |
                                estrutura_de_controle;
comando :                       declaracao |
                                entrada |
                                saida;
saida :                         imprima abre_parenteses expressao fecha_parenteses;
declaracao :                    tipo atribuicao;
atribuicao :                    identificador operador_atribuicao valor_atribuido;
valor_atribuido :               expressao | 
                                texto;
expressao :                     parenteses_expressao compoe_expressao |
                                valor compoe_expressao;
parenteses_expressao :          abre_parenteses expressao fecha_parenteses;
compoe_expressao :              (operador expressao)*;
texto :                         aspas (qualquer_caractere)* aspas;
estrutura_de_controle :         faca bloco_estrutura_de_controle enquanto condicao |
                                se condicao bloco_estrutura_de_controle se_nao | 
                                enquanto condicao bloco_estrutura_de_controle;
se_nao :                        (senao bloco_estrutura_de_controle)?;
bloco_estrutura_de_controle :   abre_chaves bloco fecha_chaves;
condicao :                      abre_parenteses expressao_booleana fecha_parenteses;
expressao_booleana :            expressao operador_binario expressao;
valor :                         identificador | 
                                numero | 
                                texto;


identificador :                 TEMRINAL_IDENTIFICADOR;
operador_atribuicao :           TERMINAL_OPERADOR_ATRIBUICAO;
abre_parenteses :               TERMINAL_ABRE_PARENTESES;
fecha_parenteses :              TERMINAL_FECHA_PARENTESES;
operador :                      TERMINAL_OPERADOR;
fim_de_instrucao :              TERMINAL_FIM_DE_INSTRUCAO;
aspas :                         TERMINAL_ASPAS;
qualquer_caractere :            TERMINAL_QUALQUER_CARACTERE;
se :                            TERMINAL_SE;
senao :                         TERMINAL_SENAO;
abre_chaves :                   TERMINAL_ABRE_CHAVES;
fecha_chaves :                  TERMINAL_FECHA_CHAVES;
operador_binario :              TERMINAL_OPERADOR_BINARIO;
enquanto :                      TERMINAL_ENQUANTO;
numero :                        TERMINAL_NUMERO;
tipo :                          TERMINAL_TIPO;
entrada:                        TERMINAL_ENTRADA;
imprima:                        TERMINAL_MOSTRE;
faca :                          TERMINAL_FACA;

// LEXER
TERMINAL_NUMERO :               [0-9]+(','[0-9]+)? ;
TERMINAL_ABRE_PARENTESES :      '(';
TERMINAL_FECHA_PARENTESES :     ')';
TERMINAL_ABRE_CHAVES :          '{';
TERMINAL_FECHA_CHAVES :         '}';


TERMINAL_OPERADOR :             ('+'|'-'|'*'|'/');
TERMINAL_FIM_DE_INSTRUCAO :     ';';
TEMRINAL_IDENTIFICADOR :        [a-zA-Z]([a-zA-Z0-9_])*;
TERMINAL_OPERADOR_ATRIBUICAO :  ':=';
TERMINAL_ASPAS :                '"';
TERMINAL_QUALQUER_CARACTERE :   ~["];
TERMINAL_OPERADOR_BINARIO :     ('>'|'<'|'>='|'<='|'<>'|'=');

TERMINAL_TIPO :                 ('numero'|'texto');
TERMINAL_FACA :                 'faca';

TERMINAL_ENQUANTO :             'enquanto';
TERMINAL_SE :                   'se';
TERMINAL_SENAO :                'senao';
TERMINAL_MOSTRE :               'mostre';
TERMINAL_ENTRADA :              'leia';

WS :                            [ \t\r\n]+ -> skip ; 