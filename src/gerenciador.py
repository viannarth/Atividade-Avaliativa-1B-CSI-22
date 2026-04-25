from src.maquina import MaquinaVendas
from src.interface import Interface
from src.constantes import SENHA_ACESSO_RESTRITO, FormaPagamento, TipoBebida
from src.item import Bebida
from enum import Enum

class Estado(Enum):
    TELA_INICIAL = 0
    ACESSO_RESTRITO_NAO_AUTORIZADO = 1
    ACESSO_RESTRITO_AUTORIZADO = 2
    ESCOLHA_BEBIDA = 3
    FINALIZAR_COMPRA = 4

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
        pass

    def validarAcessoRestrito(self) -> None:
        senha = self._interface.verificarSenha()
        if senha == "":
            self.alterarEstado(Estado.TELA_INICIAL)
        elif senha == SENHA_ACESSO_RESTRITO:
            self.alterarEstado(Estado.ACESSO_RESTRITO_AUTORIZADO)
        else:
            self._interface.senhaInvalida()

    def acessoRestrito(self) -> None:
        input_:int | ValueError = self._interface.opcoesAcessoRestrito()
        if input_ == ValueError:
            self._interface.opcaoInvalida()
            return

        if input_ == 1:
            print("Saldo checado :)")
        elif input_ == 2:
            print("Item estocado :)")
        elif input_ == 3:
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