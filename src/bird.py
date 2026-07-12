import math

import pygame

from constantes import (
    ALTURA_PASSARO,
    AMPLITUDE_FLUTUACAO,
    CAMINHO_FOLHA_PASSARO,
    FORCA_PULO,
    GRAVIDADE,
    INTERVALO_ANIMACAO_PASSARO,
    LARGURA_PASSARO,
    POS_INICIAL_X,
    POS_INICIAL_Y,
    QUADROS_ANIMACAO_PASSARO,
    VELOCIDADE_FLUTUACAO,
)

TAMANHO_FRAME_ORIGINAL = 16  # cada quadro mede 16x16 na folha de sprites original


class Bird:
    _quadros = None

    def __init__(self):
        if Bird._quadros is None:
            Bird._quadros = self._carregar_quadros()

        self.x = POS_INICIAL_X
        self.y = POS_INICIAL_Y
        self.velocidade_y = 0
        self.contador_animacao = 0

    @staticmethod
    def _carregar_quadros():
        folha = pygame.image.load(CAMINHO_FOLHA_PASSARO).convert_alpha()
        quadros = []
        for i in range(QUADROS_ANIMACAO_PASSARO):
            area = (i * TAMANHO_FRAME_ORIGINAL, 0, TAMANHO_FRAME_ORIGINAL, TAMANHO_FRAME_ORIGINAL)
            quadro_original = folha.subsurface(area)
            quadros.append(pygame.transform.scale(quadro_original, (LARGURA_PASSARO, ALTURA_PASSARO)))
        return quadros

    def pular(self):
        self.velocidade_y = FORCA_PULO

    def atualizar(self):
        self.velocidade_y += GRAVIDADE
        self.y += self.velocidade_y
        self.contador_animacao += 1

    def flutuar(self):
        self.contador_animacao += 1
        deslocamento = math.sin(self.contador_animacao * VELOCIDADE_FLUTUACAO) * AMPLITUDE_FLUTUACAO
        self.y = POS_INICIAL_Y + deslocamento

    def pousar(self, y_superficie):
        self.y = y_superficie - ALTURA_PASSARO
        self.velocidade_y = 0

    def obter_retangulo(self):
        return pygame.Rect(self.x, self.y, LARGURA_PASSARO, ALTURA_PASSARO)

    def desenhar(self, tela):
        indice = (self.contador_animacao // INTERVALO_ANIMACAO_PASSARO) % QUADROS_ANIMACAO_PASSARO
        tela.blit(Bird._quadros[indice], (self.x, self.y))
