import pygame

from constantes import COR_BRANCO, TAMANHO_FONTE_PLACAR


class Placar:
    def __init__(self):
        self.pontos = 0
        self.fonte = pygame.font.SysFont(None, TAMANHO_FONTE_PLACAR)

    def incrementar(self):
        self.pontos += 1

    def desenhar(self, tela):
        texto = self.fonte.render(str(self.pontos), True, COR_BRANCO)
        posicao = texto.get_rect(centerx=tela.get_width() // 2, y=20)
        tela.blit(texto, posicao)
