import os

from constantes import CAMINHO_NOME_JOGADOR, LIMITE_NOME


class Jogador:
    def __init__(self):
        self.nome = self._carregar_nome()
        self.nome_digitando = ""

    @staticmethod
    def _carregar_nome():
        if not os.path.exists(CAMINHO_NOME_JOGADOR):
            return ""
        with open(CAMINHO_NOME_JOGADOR, "r", encoding="utf-8") as arquivo:
            return arquivo.read().strip()

    def tem_nome(self):
        return bool(self.nome)

    def iniciar_edicao(self):
        self.nome_digitando = self.nome

    def digitar(self, caractere):
        if caractere.isprintable() and len(self.nome_digitando) < LIMITE_NOME:
            self.nome_digitando += caractere

    def apagar(self):
        self.nome_digitando = self.nome_digitando[:-1]

    def confirmar(self):
        if not self.nome_digitando:
            return False
        self.nome = self.nome_digitando
        self._salvar_nome()
        return True

    def _salvar_nome(self):
        os.makedirs(os.path.dirname(CAMINHO_NOME_JOGADOR), exist_ok=True)
        with open(CAMINHO_NOME_JOGADOR, "w", encoding="utf-8") as arquivo:
            arquivo.write(self.nome)
