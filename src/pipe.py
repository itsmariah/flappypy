import random

import pygame

from constantes import (
    ALTURA_CHAO,
    ALTURA_TELA,
    CAMINHO_FOLHA_CANOS,
    GAP_CANO,
    LARGURA_CANO,
    LARGURA_TELA,
    MARGEM_GAP,
)

TAMANHO_TILE_ORIGINAL = 32  # tile é quadrado na folha original
AREA_TAMPA_ORIGINAL = (0, 0, TAMANHO_TILE_ORIGINAL, TAMANHO_TILE_ORIGINAL)
AREA_CORPO_ORIGINAL = (0, TAMANHO_TILE_ORIGINAL, TAMANHO_TILE_ORIGINAL, TAMANHO_TILE_ORIGINAL)


class Cano:
    _tampa_original = None
    _corpo_original = None

    def __init__(self, velocidade):
        if Cano._tampa_original is None:
            folha = pygame.image.load(CAMINHO_FOLHA_CANOS).convert_alpha()
            Cano._tampa_original = folha.subsurface(AREA_TAMPA_ORIGINAL)
            Cano._corpo_original = folha.subsurface(AREA_CORPO_ORIGINAL)

        self.velocidade = velocidade
        self.x = LARGURA_TELA
        altura_disponivel = ALTURA_TELA - ALTURA_CHAO
        centro_gap = random.randint(
            MARGEM_GAP + GAP_CANO // 2,
            altura_disponivel - MARGEM_GAP - GAP_CANO // 2,
        )
        self.topo = centro_gap - GAP_CANO // 2
        self.base = centro_gap + GAP_CANO // 2
        self.pontuado = False

        # topo/base não mudam depois de criado, então já preparamos as imagens
        # escaladas uma única vez aqui, em vez de recalcular a cada desenhar().
        self.tampa_inferior = pygame.transform.scale(Cano._tampa_original, (LARGURA_CANO, LARGURA_CANO))
        self.tampa_superior = pygame.transform.flip(self.tampa_inferior, False, True)
        self.corpo_superior = self._escalar_corpo(max(self.topo - LARGURA_CANO, 0))
        self.corpo_inferior = self._escalar_corpo(max((ALTURA_TELA - self.base) - LARGURA_CANO, 0))

    def _escalar_corpo(self, altura):
        return pygame.transform.scale(Cano._corpo_original, (LARGURA_CANO, altura))

    def atualizar(self):
        self.x -= self.velocidade

    def fora_da_tela(self):
        return self.x + LARGURA_CANO < 0

    def foi_ultrapassado(self, x_passaro):
        if not self.pontuado and self.x + LARGURA_CANO < x_passaro:
            self.pontuado = True
            return True
        return False

    def obter_retangulos(self):
        retangulo_superior = pygame.Rect(self.x, 0, LARGURA_CANO, self.topo)
        retangulo_inferior = pygame.Rect(
            self.x, self.base, LARGURA_CANO, ALTURA_TELA - self.base
        )
        return retangulo_superior, retangulo_inferior

    def desenhar(self, tela):
        tela.blit(self.corpo_superior, (self.x, 0))
        tela.blit(self.tampa_superior, (self.x, self.topo - LARGURA_CANO))

        tela.blit(self.tampa_inferior, (self.x, self.base))
        tela.blit(self.corpo_inferior, (self.x, self.base + LARGURA_CANO))
