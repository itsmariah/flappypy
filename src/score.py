import os

import pygame

from constantes import CAMINHO_FONTE, CAMINHO_RECORDE, COR_BRANCO, TAMANHO_FONTE_PLACAR


class Placar:
    def __init__(self):
        self.pontos = 0
        self.recorde = self._carregar_recorde()
        self.fonte = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_PLACAR)

    def incrementar(self):
        self.pontos += 1
        if self.pontos > self.recorde:
            self.recorde = self.pontos
            self._salvar_recorde()

    def zerar_recorde(self):
        self.recorde = 0
        self._salvar_recorde()

    @staticmethod
    def _carregar_recorde():
        if not os.path.exists(CAMINHO_RECORDE):
            return 0
        with open(CAMINHO_RECORDE, "r") as arquivo:
            conteudo = arquivo.read().strip()
            return int(conteudo) if conteudo.isdigit() else 0

    def _salvar_recorde(self):
        os.makedirs(os.path.dirname(CAMINHO_RECORDE), exist_ok=True)
        with open(CAMINHO_RECORDE, "w") as arquivo:
            arquivo.write(str(self.recorde))

    def desenhar(self, tela):
        texto = self.fonte.render(str(self.pontos), True, COR_BRANCO)
        posicao = texto.get_rect(centerx=tela.get_width() // 2, y=20)
        tela.blit(texto, posicao)
