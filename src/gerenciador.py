from src.maquina import MaquinaVendas
from src.interface import Interface
from enum import Enum

SENHA_ACESSO_RESTRITO = "1000000390"

class Estado(Enum):
    TELA_INICIAL = 0
    ACESSO_RESTRITO = 1
    ESCOLHA_BEBIDA = 2
    FINALIZAR_COMPRA = 3

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
        elif self._estado == Estado.ACESSO_RESTRITO:
            self.acessoRestrito()
        elif self._estado == Estado.ESCOLHA_BEBIDA:
            self.escolhaBebida()
        elif self._estado == Estado.FINALIZAR_COMPRA:
            self.finalizarCompra()

    def telaInicial(self) -> None:
        input_:int | ValueError = self._interface.opcoesTelaInicial()
        if input_ == ValueError:
            print("Digite uma opção válida.")
            return

        if input_ == 1:
            self.alterarEstado(Estado.ESCOLHA_BEBIDA)
        elif input_ == 2:
            self.alterarEstado(Estado.ACESSO_RESTRITO)
        elif input_ == 3:
            exit()

    def escolhaBebida(self) -> None:
        pass

    def acessoRestrito(self) -> None:
        pass

    def finalizarCompra(self) -> None:
        pass
    