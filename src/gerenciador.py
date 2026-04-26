from src.maquina import MaquinaVendas
from src.item import BebidaDosada
from src.interface import Interface
from src.constantes import SENHA_ACESSO_RESTRITO, FormaPagamento, TipoBebida, TipoItem
from enum import Enum

class Estado(Enum):
    TELA_INICIAL = 0
    ACESSO_RESTRITO_NAO_AUTORIZADO = 1
    ACESSO_RESTRITO_AUTORIZADO = 2
    ESCOLHA_BEBIDA = 3
    ADICIONAR_BEBIDA_LATA = 4
    MONTAR_BEBIDA_DOSADA = 5
    FINALIZAR_COMPRA = 6

class GerenciadorMaquina():
    def __init__(self, maquina:MaquinaVendas) -> None:
        self._maquina:MaquinaVendas = maquina
        self._estado:Estado = Estado.TELA_INICIAL
        self._interface:Interface = Interface()        

    def alterarEstado(self, novo_estado:Estado) -> None:
        self._estado = novo_estado

    def executarEstado(self) -> None:
        if self._estado == Estado.TELA_INICIAL:
            self.telaInicial()
        elif self._estado == Estado.ACESSO_RESTRITO_NAO_AUTORIZADO:
            self.validarAcessoRestrito()
        elif self._estado == Estado.ACESSO_RESTRITO_AUTORIZADO:
            self.acessoRestrito()
        elif self._estado == Estado.ESCOLHA_BEBIDA:
            self.escolhaBebida()
        elif self._estado == Estado.ADICIONAR_BEBIDA_LATA:
            self.adicionarBebidaLata()
        elif self._estado == Estado.MONTAR_BEBIDA_DOSADA:
            self.montarBebidaLata()
        elif self._estado == Estado.FINALIZAR_COMPRA:
            self.finalizarCompra()

    def telaInicial(self) -> None:
        input_:int | ValueError = self._interface.opcoesTelaInicial()
        if input_ == ValueError:
            self._interface.opcaoInvalida()
            return

        if input_ == 1:
            self.alterarEstado(Estado.ESCOLHA_BEBIDA)
        elif input_ == 2:
            self.alterarEstado(Estado.ACESSO_RESTRITO_NAO_AUTORIZADO)
        elif input_ == 3:
            exit()

    def escolhaBebida(self) -> None:
        carrinho_vazio = False
        if self._maquina.consultarValorCarrinho == 0:
            carrinho_vazio = True
        input_:int | ValueError = self._interface.opcoesEscolhaBebida(carrinho_vazio)
        if input_ == ValueError:
            self._interface.opcaoInvalida()
            return
        if carrinho_vazio:
            if input_ == 1:
                self.alterarEstado(Estado.ADICIONAR_BEBIDA_LATA)
            elif input_ == 2:
                self.alterarEstado(Estado.MONTAR_BEBIDA_DOSADA)
            elif input_ == 3:
                self.alterarEstado(Estado.TELA_INICIAL)
        else:
            if input_ == 1:
                self.alterarEstado(Estado.ADICIONAR_BEBIDA_LATA)
            elif input_ == 2:
                self.alterarEstado(Estado.MONTAR_BEBIDA_DOSADA)
            elif input_ == 3:
                self.alterarEstado(Estado.FINALIZAR_COMPRA)
            elif input_ == 4:
                self._maquina.esvaziarCarrinho()
                self.alterarEstado(Estado.TELA_INICIAL)

    def adicionarBebidaLata(self) -> None:
        input_ = self._interface.verificarBebidaLata()
        bebida_lata = self._maquina.verificarBebidaLata(input_[0])
        quantidade_estoque = self._maquina.consultarEstoqueItem(input_[0])
        if input_ == ValueError or not bebida_lata or quantidade_estoque < input_[1]:
            self._interface.opcaoInvalida()
            return
        self._maquina.adicionarBebida(input_[0], input_[1])
        self.alterarEstado(Estado.ESCOLHA_BEBIDA)
        
    def validarAcessoRestrito(self) -> None:
        senha = self._interface.verificarSenha()
        if senha == "":
            self.alterarEstado(Estado.TELA_INICIAL)
        elif senha == SENHA_ACESSO_RESTRITO:
            self.alterarEstado(Estado.ACESSO_RESTRITO_AUTORIZADO)
        else:
            self._interface.senhaInvalida()

    def exibirEstoque(self) -> None:
        itens = self._maquina.consultarEstoqueLista()
        nome_itens = [item.consultarNome() for item in itens]
        quantidades = [self._maquina.consultarEstoqueItem(nome_item) for nome_item in nome_itens]
        self._interface.exibirEstoque(nome_itens, quantidades)

    def acessoRestrito(self) -> None:
        input_:int | ValueError = self._interface.opcoesAcessoRestrito()
        if input_ == ValueError:
            self._interface.opcaoInvalida()
            return

        if input_ == 1:
            saldo_total = self._maquina.consultarSaldo()
            saldo_dosada = self._maquina.consultarSaldoBebida(TipoBebida.DOSADA)
            saldo_lata = self._maquina.consultarSaldoBebida(TipoBebida.LATA)
            self._interface.exibirSaldoMaquina(saldo_total, saldo_dosada, saldo_lata)
        elif input_ == 2:
            self.exibirEstoque()
        elif input_ == 3:
            tupla = self._interface.receberItem()
            if tupla == ValueError:
                self._interface.opcaoInvalida()
                return
            tipo_item:int = tupla[0]
            tipo_item:TipoItem = TipoItem(tipo_item)
            nome_item:str = tupla[1]
            quantidade:int = tupla[2]
            self._maquina.estocarItem(tipo_item, nome_item, quantidade)
            self._interface.itemAdicinado()
        elif input_ == 4:
            self.alterarEstado(Estado.TELA_INICIAL)

    def finalizarCompra(self) -> None:
        input_:int | ValueError = self._interface.opcoesFinalizarCompra()
        if input_ == ValueError:
            self._interface.opcaoInvalida()
            return
        
        if input_ == 4:
            self.alterarEstado(Estado.TELA_INICIAL)
            return
        
        forma_pagamento = FormaPagamento(input_)

        valor_total = MaquinaVendas.consultarValorTotal()
        self._interface.exibirValorTotal(valor_total)
        
        carrinho = self._maquina.consultarCarrinho().copy()

        MaquinaVendas.realizarVenda(forma_pagamento)
        self._interface.finalizarCompra(forma_pagamento)

        for bebida in carrinho:
            if bebida.consultarTipoBebida() == TipoBebida.LATA:
                self._interface.dispensarBebidaLata(carrinho[bebida], bebida.consultarNome())

            else:
                lista_doses:list[int] = [bebida[ingrediente].value for ingrediente in bebida.consultarIngredientes()]
                lista_ingredientes:list[str] = [ingrediente.consultarNome() for ingrediente in bebida.consultarIngredientes()]
                self._interface.dispensarIngrediente(lista_doses, lista_ingredientes)