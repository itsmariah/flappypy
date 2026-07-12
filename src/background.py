import pygame

from constantes import ALTURA_TELA, CAMINHO_FUNDO, VELOCIDADE_FUNDO


class Fundo:
    _imagem = None

    def __init__(self):
        if Fundo._imagem is None:
            Fundo._imagem = self._carregar_imagem()

        self.largura = Fundo._imagem.get_width()
        self.x = 0

    @staticmethod
    def _carregar_imagem():
        original = pygame.image.load(CAMINHO_FUNDO).convert()
        fator_escala = ALTURA_TELA / original.get_height()
        largura_escalada = round(original.get_width() * fator_escala)
        return pygame.transform.scale(original, (largura_escalada, ALTURA_TELA))

    def atualizar(self):
        self.x -= VELOCIDADE_FUNDO
        if self.x <= -self.largura:
            self.x += self.largura

    def desenhar(self, tela):
        tela.blit(Fundo._imagem, (self.x, 0))
        tela.blit(Fundo._imagem, (self.x + self.largura, 0))
