import json
import os

import pygame

from constantes import CAMINHO_FONTE, CAMINHO_RECORDES, COR_BRANCO, TAMANHO_FONTE_PLACAR


class Placar:
    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
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
    def obter_ranking():
        recordes = Placar._carregar_todos_recordes()
        return sorted(recordes.items(), key=lambda item: item[1], reverse=True)

    def _carregar_recorde(self):
        recordes = self._carregar_todos_recordes()
        return recordes.get(self.nome_jogador, 0)

    def _salvar_recorde(self):
        recordes = self._carregar_todos_recordes()
        recordes[self.nome_jogador] = self.recorde
        os.makedirs(os.path.dirname(CAMINHO_RECORDES), exist_ok=True)
        with open(CAMINHO_RECORDES, "w", encoding="utf-8") as arquivo:
            json.dump(recordes, arquivo)

    @staticmethod
    def _carregar_todos_recordes():
        if not os.path.exists(CAMINHO_RECORDES):
            return {}
        with open(CAMINHO_RECORDES, "r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}

    def desenhar(self, tela):
        texto = self.fonte.render(str(self.pontos), True, COR_BRANCO)
        posicao = texto.get_rect(centerx=tela.get_width() // 2, y=20)
        tela.blit(texto, posicao)
