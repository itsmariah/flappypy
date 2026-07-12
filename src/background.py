import pygame

from constantes import ALTURA_TELA, CAMINHOS_FUNDO, VELOCIDADE_FUNDO


class Fundo:
    _imagens_por_estilo = {}

    def __init__(self, estilo=0):
        if estilo not in Fundo._imagens_por_estilo:
            Fundo._imagens_por_estilo[estilo] = self._carregar_imagem(estilo)
        self.imagem = Fundo._imagens_por_estilo[estilo]

        self.largura = self.imagem.get_width()
        self.x = 0

    @staticmethod
    def _carregar_imagem(estilo):
        original = pygame.image.load(CAMINHOS_FUNDO[estilo]).convert()
        fator_escala = ALTURA_TELA / original.get_height()
        largura_escalada = round(original.get_width() * fator_escala)
        return pygame.transform.scale(original, (largura_escalada, ALTURA_TELA))

    def atualizar(self):
        self.x -= VELOCIDADE_FUNDO
        if self.x <= -self.largura:
            self.x += self.largura

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, 0))
        tela.blit(self.imagem, (self.x + self.largura, 0))
