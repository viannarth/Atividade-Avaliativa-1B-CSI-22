from src.maquina import MaquinaVendas
from src.item import Ingrediente
from src.interface import Interface
from src.constantes import SENHA_ACESSO_RESTRITO, FormaPagamento, TipoBebida, TipoItem, Doses
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
            self.montarBebidaDosada()
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

    def exibirCarrinho(self) -> None:
        valor_total = self._maquina.consultarValorCarrinho()
        bebidas = self._maquina.consultarCarrinho()
        nomes_bebidas: list[str] = []
        quantidades:list[int] = []
        num_dosadas:int = 1
        for bebida in bebidas:
            tipo_bebida = bebida.consultarTipoBebida()
            if tipo_bebida == TipoBebida.LATA:
                nomes_bebidas.append(bebida.consultarNome())
                quantidades.append(self._maquina.consultarItemCarrinho(bebida.consultarNome()))
            else:
                nomes_bebidas.append(f"Bebida Dosada {num_dosadas}")
                quantidades.append(1)
                num_dosadas += 1
        self._interface.exibirCarrinho(valor_total, nomes_bebidas, quantidades)

    def escolhaBebida(self) -> None:
        self.exibirEstoque()

        carrinho_vazio = self._maquina.checarVazio()
        if not carrinho_vazio:
            self.exibirCarrinho()
        
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
        bebida_lata = self._interface.verificarNomeBebidaLata()
        if bebida_lata == "":
            self.alterarEstado(Estado.ESCOLHA_BEBIDA)
            return
        if not self._maquina.verificarBebidaLata(bebida_lata):
            self._interface.opcaoInvalida()
            return
        quantidade = self._interface.verificarQuantidadeBebidaLata()
        if quantidade == ValueError:
            self._interface.opcaoInvalida()
            return
        quantidade_estoque = self._maquina.consultarEstoqueItem(bebida_lata, TipoItem.LATA)
        if quantidade_estoque < quantidade:
            self._interface.opcaoInvalida()
            return
        self._maquina.adicionarBebida(nome_bebida=bebida_lata, num_bebidas=quantidade)
        self.alterarEstado(Estado.ESCOLHA_BEBIDA)

    def montarBebidaDosada(self) -> None:
        self.exibirEstoque()
        estoque_agua:int = self._maquina.consultarEstoqueItem("Agua", TipoItem.INGREDIENTE)
        if estoque_agua < Doses.AGUA.value:
            self._interface.aguaInsuficiente()
            self.alterarEstado(Estado.ESCOLHA_BEBIDA)
            return
        nome_ingrediente = self._interface.escolherIngrediente()
        ingrediente = self._maquina.verificarIngrediente(nome_ingrediente)
        if not ingrediente:
            self._interface.opcaoInvalida()
            return
        dose = self._interface.escolherDose()
        if dose == ValueError:
            self._interface.opcaoInvalida()
            return
        if dose == Doses.CEM:
            dict_dosada:dict[Ingrediente, Doses] = {ingrediente: dose}
        else:
            dict_dosada:dict[Ingrediente, Doses] = {ingrediente: dose}
            nome_segundo_ingrediente = self._interface.escolherSegundoIngrediente()
            segundo_ingrediente = self._maquina.verificarIngrediente(nome_segundo_ingrediente)
            if not segundo_ingrediente:
                self._interface.opcaoInvalida()
                return
            dict_dosada[segundo_ingrediente] = Doses(10 - dose.value)
        bebida_dosada = self._maquina.criarBebidaDosada(dict_dosada)
        self._maquina.adicionarBebida(bebida_dosada=bebida_dosada)
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
        tipo_itens = [item.consultarTipoItem() for item in itens]
        nome_itens = [item.consultarNome() for item in itens]
        quantidades = [self._maquina.consultarEstoqueItem(item.consultarNome(), item.consultarTipoItem()) for item in itens]
        self._interface.exibirEstoque(tipo_itens, nome_itens, quantidades)

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
            self._interface.estadoEspera()
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
        self.exibirCarrinho()
        input_:int | ValueError = self._interface.opcoesFinalizarCompra()
        if input_ == ValueError:
            self._interface.opcaoInvalida()
            return
        
        if input_ == 4:
            self.alterarEstado(Estado.TELA_INICIAL)
            return
        
        forma_pagamento = FormaPagamento(input_)
        self._interface.finalizarCompra(forma_pagamento.value)

        for bebida in self._maquina.consultarCarrinho():
            if bebida.consultarTipoBebida() == TipoBebida.LATA:
                self._interface.dispensarBebidaLata(self._maquina.consultarItemCarrinho(bebida.consultarNome()), bebida.consultarNome())

            if bebida.consultarTipoBebida() == TipoBebida.DOSADA:
                dict_dosada = bebida.consultarIngredientes()
                lista_doses:list[int] = [dict_dosada[ingrediente].value for ingrediente in dict_dosada]
                lista_ingredientes:list[str] = [ingrediente.consultarNome() for ingrediente in dict_dosada]
                self._interface.dispensarIngrediente(lista_doses, lista_ingredientes)

        self._maquina.realizarVenda(forma_pagamento.value)
        self.alterarEstado(Estado.TELA_INICIAL)