import pygame

from constantes import ALTURA_TELA, CAMINHO_FONTE, COR_BRANCO, LARGURA_TELA
from menu import Botao

TAMANHO_FONTE_TITULO_RANKING = 24
TAMANHO_FONTE_ITEM_RANKING = 14
MAX_ITENS_RANKING = 8
ESPACO_ENTRE_ITENS = 30


class TelaRanking:
    def __init__(self):
        self.fonte_titulo = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_TITULO_RANKING)
        self.fonte_item = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_ITEM_RANKING)

        self.botao_voltar = Botao(self.fonte_item, "Voltar", 220, 32)
        self.botao_voltar.posicionar((LARGURA_TELA - 220) // 2, ALTURA_TELA - 100)

    def desenhar(self, tela, ranking):
        self._desenhar_texto(tela, "Ranking", self.fonte_titulo, 50)

        if not ranking:
            self._desenhar_texto(tela, "Ninguem jogou ainda", self.fonte_item, 150)
        else:
            y = 110
            for posicao, (nome, pontos) in enumerate(ranking[:MAX_ITENS_RANKING], start=1):
                self._desenhar_texto(tela, f"{posicao}. {nome} - {pontos}", self.fonte_item, y)
                y += ESPACO_ENTRE_ITENS

        self.botao_voltar.desenhar(tela)

    def _desenhar_texto(self, tela, texto, fonte, y):
        superficie = fonte.render(texto, True, COR_BRANCO)
        retangulo = superficie.get_rect(centerx=LARGURA_TELA // 2, y=y)
        tela.blit(superficie, retangulo)
