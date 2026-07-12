import random

import pygame

from constantes import (
    COR_PARTICULA,
    FRAMES_SHAKE,
    GRAVIDADE_PARTICULA,
    INTENSIDADE_SHAKE,
    QUANTIDADE_PARTICULAS_PULO,
    TAMANHO_PARTICULA,
    VIDA_PARTICULA,
)


class Particula:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1.5, 1.5)
        self.vy = random.uniform(-2.5, -0.5)
        self.vida = VIDA_PARTICULA

    def atualizar(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVIDADE_PARTICULA
        self.vida -= 1

    def esta_viva(self):
        return self.vida > 0

    def desenhar(self, tela):
        superficie = pygame.Surface((TAMANHO_PARTICULA, TAMANHO_PARTICULA), pygame.SRCALPHA)
        alpha = max(0, min(255, int(255 * self.vida / VIDA_PARTICULA)))
        superficie.fill((*COR_PARTICULA, alpha))
        tela.blit(superficie, (self.x, self.y))


class SistemaParticulas:
    def __init__(self):
        self.particulas = []

    def emitir(self, x, y):
        for _ in range(QUANTIDADE_PARTICULAS_PULO):
            self.particulas.append(Particula(x, y))

    def atualizar(self):
        for particula in self.particulas:
            particula.atualizar()
        self.particulas = [p for p in self.particulas if p.esta_viva()]

    def desenhar(self, tela):
        for particula in self.particulas:
            particula.desenhar(tela)


class Shake:
    def __init__(self):
        self.frames_restantes = 0

    def iniciar(self):
        self.frames_restantes = FRAMES_SHAKE

    def atualizar(self):
        if self.frames_restantes > 0:
            self.frames_restantes -= 1

    def offset(self):
        if self.frames_restantes <= 0:
            return (0, 0)
        return (
            random.randint(-INTENSIDADE_SHAKE, INTENSIDADE_SHAKE),
            random.randint(-INTENSIDADE_SHAKE, INTENSIDADE_SHAKE),
        )
