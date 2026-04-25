from src.gerenciador import GerenciadorMaquina
from src.maquina import MaquinaVendas

#TODO: create a .env file for allow private access

maquina = MaquinaVendas()
gerenciador = GerenciadorMaquina(maquina)

while(True):
    gerenciador.executarEstado()
