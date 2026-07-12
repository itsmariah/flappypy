import pygame

from constantes import ALTURA_CHAO, ALTURA_TELA, ESTILOS_CHAO, LARGURA_TELA, LARGURA_TILE_CHAO


class Ground:
    _tile_por_estilo = {}

    def __init__(self, estilo=0):
        if estilo not in Ground._tile_por_estilo:
            config = ESTILOS_CHAO[estilo]
            folha = pygame.image.load(config["folha"]).convert_alpha()
            tile_original = folha.subsurface(config["area_tile"])
            Ground._tile_por_estilo[estilo] = pygame.transform.scale(
                tile_original, (LARGURA_TILE_CHAO, ALTURA_CHAO)
            )
        self.tile = Ground._tile_por_estilo[estilo]

        self.y = ALTURA_TELA - ALTURA_CHAO
        self.x = 0

    def atualizar(self, velocidade):
        self.x -= velocidade
        if self.x <= -LARGURA_TILE_CHAO:
            self.x += LARGURA_TILE_CHAO

    def obter_retangulo(self):
        return pygame.Rect(0, self.y, LARGURA_TELA, ALTURA_CHAO)

    def desenhar(self, tela):
        for x in range(int(self.x), LARGURA_TELA, LARGURA_TILE_CHAO):
            tela.blit(self.tile, (x, self.y))
