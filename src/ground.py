import pygame

from constantes import (
    ALTURA_CHAO,
    ALTURA_TELA,
    CAMINHO_FOLHA_CHAO,
    LARGURA_TELA,
    LARGURA_TILE_CHAO,
    VELOCIDADE_CANO,
)

AREA_TILE_ORIGINAL = (0, 80, 16, 32)  # grama + terra, sem decorações, na folha original


class Ground:
    _tile = None

    def __init__(self):
        if Ground._tile is None:
            folha = pygame.image.load(CAMINHO_FOLHA_CHAO).convert_alpha()
            tile_original = folha.subsurface(AREA_TILE_ORIGINAL)
            Ground._tile = pygame.transform.scale(tile_original, (LARGURA_TILE_CHAO, ALTURA_CHAO))

        self.y = ALTURA_TELA - ALTURA_CHAO
        self.x = 0

    def atualizar(self):
        self.x -= VELOCIDADE_CANO
        if self.x <= -LARGURA_TILE_CHAO:
            self.x += LARGURA_TILE_CHAO

    def obter_retangulo(self):
        return pygame.Rect(0, self.y, LARGURA_TELA, ALTURA_CHAO)

    def desenhar(self, tela):
        for x in range(self.x, LARGURA_TELA, LARGURA_TILE_CHAO):
            tela.blit(Ground._tile, (x, self.y))
