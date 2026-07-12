import random

import pygame

from constantes import (
    ALTURA_CHAO,
    ALTURA_TELA,
    ESTILOS_CANO,
    GAP_CANO,
    LARGURA_CANO,
    LARGURA_TELA,
    MARGEM_GAP,
)


class Cano:
    _tampa_por_estilo = {}
    _corpo_por_estilo = {}

    def __init__(self, velocidade, estilo=0):
        if estilo not in Cano._tampa_por_estilo:
            config = ESTILOS_CANO[estilo]
            folha = pygame.image.load(config["folha"]).convert_alpha()
            tampa_original = folha.subsurface(config["area_tampa"])
            corpo_original = folha.subsurface(config["area_corpo"])
            Cano._tampa_por_estilo[estilo] = pygame.transform.scale(
                tampa_original, (LARGURA_CANO, LARGURA_CANO)
            )
            Cano._corpo_por_estilo[estilo] = pygame.transform.scale(
                corpo_original, (LARGURA_CANO, LARGURA_CANO)
            )

        self.tampa_inferior = Cano._tampa_por_estilo[estilo]
        self.tampa_superior = pygame.transform.flip(self.tampa_inferior, False, True)
        self.corpo_tile = Cano._corpo_por_estilo[estilo]

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
        self._desenhar_corpo(tela, 0, max(self.topo - LARGURA_CANO, 0))
        tela.blit(self.tampa_superior, (self.x, self.topo - LARGURA_CANO))

        tela.blit(self.tampa_inferior, (self.x, self.base))
        self._desenhar_corpo(tela, self.base + LARGURA_CANO, ALTURA_TELA)

    def _desenhar_corpo(self, tela, y_inicio, y_fim):
        y = y_inicio
        while y < y_fim:
            altura_restante = y_fim - y
            if altura_restante >= LARGURA_CANO:
                tela.blit(self.corpo_tile, (self.x, y))
            else:
                pedaco = self.corpo_tile.subsurface((0, 0, LARGURA_CANO, altura_restante))
                tela.blit(pedaco, (self.x, y))
            y += LARGURA_CANO
