# Generated from PtGrammar.g4 by ANTLR 4.7.2
from antlr4 import *
from StoreProgram import StoreProgram
if __name__ is not None and "." in __name__:
    from .PtGrammarParser import PtGrammarParser
else:
    from PtGrammarParser import PtGrammarParser

# This class defines a complete listener for a parse tree produced by PtGrammarParser.
class PtGrammarListenerC(ParseTreeListener):

    def __init__(self, output_file=None):
        self.content = StoreProgram('c', output_file)

    # Enter a parse tree produced by PtGrammarParser#programa.
    def enterPrograma(self, ctx:PtGrammarParser.ProgramaContext):
        self.content.append("#include <stdio.h>\n")
        self.content.append("#include <string>\n")
        self.content.append("#include <iostream>\n")
        self.content.append("using namespace std;\n")

        self.content.append("int main() {")
        self.content.append("int aux_int;")
        pass

    # Exit a parse tree produced by PtGrammarParser#programa.
    def exitPrograma(self, ctx:PtGrammarParser.ProgramaContext):
        self.content.append("}")
        pass


    # Enter a parse tree produced by PtGrammarParser#bloco.
    def enterBloco(self, ctx:PtGrammarParser.BlocoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#bloco.
    def exitBloco(self, ctx:PtGrammarParser.BlocoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#comando.
    def enterComando(self, ctx:PtGrammarParser.ComandoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#comando.
    def exitComando(self, ctx:PtGrammarParser.ComandoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#declaracao.
    def enterDeclaracao(self, ctx:PtGrammarParser.DeclaracaoContext):
        identifier = ctx.atribuicao().identificador().getText()
        type = ctx.tipo().getText()

        if self.content.already_declared(identifier):
            exc = f'Variável {identifier} declarada múltiplas vezes'
            raise Exception(exc)
        else:
            self.content.add_variable(type, identifier)

    # Exit a parse tree produced by PtGrammarParser#declaracao.
    def exitDeclaracao(self, ctx:PtGrammarParser.DeclaracaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#atribuicao.
    def enterAtribuicao(self, ctx:PtGrammarParser.AtribuicaoContext):
        identifier = ctx.identificador().getText()

        if not self.content.already_declared(identifier):
            exc = f'Variável {identifier} não declarada'
            raise Exception(exc)

    # Exit a parse tree produced by PtGrammarParser#atribuicao.
    def exitAtribuicao(self, ctx:PtGrammarParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#valor_atribuido.
    def enterValor_atribuido(self, ctx:PtGrammarParser.Valor_atribuidoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#valor_atribuido.
    def exitValor_atribuido(self, ctx:PtGrammarParser.Valor_atribuidoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#expressao.
    def enterExpressao(self, ctx:PtGrammarParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#expressao.
    def exitExpressao(self, ctx:PtGrammarParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#parenteses_expressao.
    def enterParenteses_expressao(self, ctx:PtGrammarParser.Parenteses_expressaoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#parenteses_expressao.
    def exitParenteses_expressao(self, ctx:PtGrammarParser.Parenteses_expressaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#compoe_expressao.
    def enterCompoe_expressao(self, ctx:PtGrammarParser.Compoe_expressaoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#compoe_expressao.
    def exitCompoe_expressao(self, ctx:PtGrammarParser.Compoe_expressaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#estrutura_de_controle.
    def enterEstrutura_de_controle(self, ctx:PtGrammarParser.Estrutura_de_controleContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#estrutura_de_controle.
    def exitEstrutura_de_controle(self, ctx:PtGrammarParser.Estrutura_de_controleContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#se_nao.
    def enterSe_nao(self, ctx:PtGrammarParser.Se_naoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#se_nao.
    def exitSe_nao(self, ctx:PtGrammarParser.Se_naoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#bloco_estrutura_de_controle.
    def enterBloco_estrutura_de_controle(self, ctx:PtGrammarParser.Bloco_estrutura_de_controleContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#bloco_estrutura_de_controle.
    def exitBloco_estrutura_de_controle(self, ctx:PtGrammarParser.Bloco_estrutura_de_controleContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#condicao.
    def enterCondicao(self, ctx:PtGrammarParser.CondicaoContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#condicao.
    def exitCondicao(self, ctx:PtGrammarParser.CondicaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#expressao_booleana.
    def enterExpressao_booleana(self, ctx:PtGrammarParser.Expressao_booleanaContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#expressao_booleana.
    def exitExpressao_booleana(self, ctx:PtGrammarParser.Expressao_booleanaContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#valor.
    def enterValor(self, ctx:PtGrammarParser.ValorContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#valor.
    def exitValor(self, ctx:PtGrammarParser.ValorContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#saida.
    def enterSaida(self, ctx:PtGrammarParser.SaidaContext):
        pass

    # Exit a parse tree produced by PtGrammarParser#saida.
    def exitSaida(self, ctx:PtGrammarParser.SaidaContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#numero.
    def enterNumero(self, ctx:PtGrammarParser.NumeroContext):
        number = ctx.getText()
        parsedNumber = number.replace(',', '.')
        self.content.append(f'(float){parsedNumber}')
        pass

    # Exit a parse tree produced by PtGrammarParser#numero.
    def exitNumero(self, ctx:PtGrammarParser.NumeroContext):
        pass

    # Enter a parse tree produced by PtGrammarParser#identificador.
    def enterIdentificador(self, ctx:PtGrammarParser.IdentificadorContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#identificador.
    def exitIdentificador(self, ctx:PtGrammarParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#tipo.
    def enterTipo(self, ctx:PtGrammarParser.TipoContext):
        type = ctx.getText()
        if type == 'texto':
            self.content.append('string ')
        else:
            self.content.append('float ')
        pass

    # Exit a parse tree produced by PtGrammarParser#tipo.
    def exitTipo(self, ctx:PtGrammarParser.TipoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#texto.
    def enterTexto(self, ctx:PtGrammarParser.TextoContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#texto.
    def exitTexto(self, ctx:PtGrammarParser.TextoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#operador_binario.
    def enterOperador_binario(self, ctx:PtGrammarParser.Operador_binarioContext):
        operator = ctx.getText()
        if operator == '=':
            self.content.append('==')
        else:
            self.content.append(operator)

    # Exit a parse tree produced by PtGrammarParser#operador_binario.
    def exitOperador_binario(self, ctx:PtGrammarParser.Operador_binarioContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#operador_aritmetico.
    def enterOperador_aritmetico(self, ctx:PtGrammarParser.Operador_aritmeticoContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#operador_aritmetico.
    def exitOperador_aritmetico(self, ctx:PtGrammarParser.Operador_aritmeticoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#fim_de_instrucao.
    def enterFim_de_instrucao(self, ctx:PtGrammarParser.Fim_de_instrucaoContext):
        self.content.append(";")
        pass

    # Exit a parse tree produced by PtGrammarParser#fim_de_instrucao.
    def exitFim_de_instrucao(self, ctx:PtGrammarParser.Fim_de_instrucaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#operador_atribuicao.
    def enterOperador_atribuicao(self, ctx:PtGrammarParser.Operador_atribuicaoContext):
        self.content.append("=")
        pass

    # Exit a parse tree produced by PtGrammarParser#operador_atribuicao.
    def exitOperador_atribuicao(self, ctx:PtGrammarParser.Operador_atribuicaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#abre_parenteses.
    def enterAbre_parenteses(self, ctx:PtGrammarParser.Abre_parentesesContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#abre_parenteses.
    def exitAbre_parenteses(self, ctx:PtGrammarParser.Abre_parentesesContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#fecha_parenteses.
    def enterFecha_parenteses(self, ctx:PtGrammarParser.Fecha_parentesesContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#fecha_parenteses.
    def exitFecha_parenteses(self, ctx:PtGrammarParser.Fecha_parentesesContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#abre_chaves.
    def enterAbre_chaves(self, ctx:PtGrammarParser.Abre_chavesContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#abre_chaves.
    def exitAbre_chaves(self, ctx:PtGrammarParser.Abre_chavesContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#fecha_chaves.
    def enterFecha_chaves(self, ctx:PtGrammarParser.Fecha_chavesContext):
        self.content.append(ctx.getText())
        pass

    # Exit a parse tree produced by PtGrammarParser#fecha_chaves.
    def exitFecha_chaves(self, ctx:PtGrammarParser.Fecha_chavesContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#faca.
    def enterFaca(self, ctx:PtGrammarParser.FacaContext):
        self.content.append("do")
        pass

    # Exit a parse tree produced by PtGrammarParser#faca.
    def exitFaca(self, ctx:PtGrammarParser.FacaContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#enquanto.
    def enterEnquanto(self, ctx:PtGrammarParser.EnquantoContext):
        self.content.append("while")
        pass

    # Exit a parse tree produced by PtGrammarParser#enquanto.
    def exitEnquanto(self, ctx:PtGrammarParser.EnquantoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#se.
    def enterSe(self, ctx:PtGrammarParser.SeContext):
        self.content.append("if")
        pass

    # Exit a parse tree produced by PtGrammarParser#se.
    def exitSe(self, ctx:PtGrammarParser.SeContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#senao.
    def enterSenao(self, ctx:PtGrammarParser.SenaoContext):
        self.content.append("else")
        pass

    # Exit a parse tree produced by PtGrammarParser#senao.
    def exitSenao(self, ctx:PtGrammarParser.SenaoContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#entrada_de_texto.
    def enterEntrada_de_texto(self, ctx:PtGrammarParser.EntradaContext):
        self.content.append('getchar()')

    # Exit a parse tree produced by PtGrammarParser#entrada_de_texto.
    def exitEntrada_de_texto(self, ctx:PtGrammarParser.EntradaContext):
        pass

    # Enter a parse tree produced by PtGrammarParser#entrada_numerica.
    def enterEntrada_numerica(self, ctx:PtGrammarParser.EntradaContext):
        self.content.append('scanf("%d", &aux_int) ')

    # Exit a parse tree produced by PtGrammarParser#entrada_numerica.
    def exitEntrada_numerica(self, ctx:PtGrammarParser.EntradaContext):
        pass


    # Enter a parse tree produced by PtGrammarParser#imprima.
    def enterImprima(self, ctx:PtGrammarParser.ImprimaContext):
        # import ipdb; ipdb.set_trace()
        self.content.append( "cout <<")
        pass

    # Exit a parse tree produced by PtGrammarParser#imprima.
    def exitImprima(self, ctx:PtGrammarParser.ImprimaContext):
        pass

    def getIdentifierType(self, identifier):
        return 'texto'
