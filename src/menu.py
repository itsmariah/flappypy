import pygame

from constantes import ALTURA_TELA, COR_BRANCO, LARGURA_TELA, TAMANHO_FONTE_PLACAR


class Menu:
    def __init__(self):
        self.fonte_titulo = pygame.font.SysFont(None, TAMANHO_FONTE_PLACAR)
        self.fonte_instrucao = pygame.font.SysFont(None, TAMANHO_FONTE_PLACAR // 2)

    def desenhar_tela_inicial(self, tela, recorde):
        self._desenhar_texto(tela, "Flappy Py", self.fonte_titulo, ALTURA_TELA // 2 - 40)
        self._desenhar_texto(tela, f"Recorde: {recorde}", self.fonte_instrucao, ALTURA_TELA // 2)
        self._desenhar_texto(
            tela, "Aperte espaço para começar", self.fonte_instrucao, ALTURA_TELA // 2 + 35
        )

    def desenhar_tela_fim(self, tela, pontos, recorde):
        self._desenhar_texto(tela, "Game Over", self.fonte_titulo, ALTURA_TELA // 2 - 40)
        self._desenhar_texto(
            tela, f"Pontuação: {pontos}", self.fonte_instrucao, ALTURA_TELA // 2
        )
        self._desenhar_texto(
            tela, f"Recorde: {recorde}", self.fonte_instrucao, ALTURA_TELA // 2 + 30
        )
        self._desenhar_texto(
            tela, "Aperte espaço para reiniciar", self.fonte_instrucao, ALTURA_TELA // 2 + 70
        )

    def _desenhar_texto(self, tela, texto, fonte, y):
        superficie = fonte.render(texto, True, COR_BRANCO)
        retangulo = superficie.get_rect(centerx=LARGURA_TELA // 2, y=y)
        tela.blit(superficie, retangulo)
