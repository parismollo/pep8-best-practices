from fila_base import FilaBase


class FilaNormal(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def chama_cliente(self, caixa) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}'
