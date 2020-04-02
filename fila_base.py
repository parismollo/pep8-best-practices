import abc
from typing import List

from constantes import TAMANHO_PADRAO_MAX, TAMANHO_PADRAO_MIN, KEY_WORD


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAX:
            self.codigo = TAMANHO_PADRAO_MIN
        else:
            self.codigo += 1

    def insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.insere_cliente()

    def apaga_dados(self, senha: str) -> str:
        if senha == KEY_WORD:
            self.clientes_atendidos = []
            print('Dados apagados')
        else:
            print('Acesso negado!')

    @abc.abstractmethod
    def chama_cliente(self, caixa: int) -> str:
        ...
