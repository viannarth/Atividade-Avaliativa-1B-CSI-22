from src.gerenciador import GerenciadorMaquina
from src.maquina import MaquinaVendas

maquina = MaquinaVendas()
gerenciador = GerenciadorMaquina(maquina)

while(True):
    gerenciador.executarEstado()
