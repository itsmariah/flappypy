import pygame

from bird import Bird
from collision import colidiu
from constantes import (
    ALTURA_TELA,
    COR_CEU,
    ESTADO_GAME_OVER,
    ESTADO_JOGANDO,
    ESTADO_MENU,
    FPS,
    INTERVALO_CANOS,
    LARGURA_TELA,
    TITULO,
)
from ground import Ground
from menu import Menu
from pipe import Cano
from score import Placar


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption(TITULO)
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.menu = Menu()
        self.chao = Ground()
        self.estado = ESTADO_MENU
        self._reiniciar()

    def _reiniciar(self):
        self.passaro = Bird()
        self.canos = []
        self.frames_desde_ultimo_cano = INTERVALO_CANOS
        self.placar = Placar()

    def executar(self):
        while self.rodando:
            self._processar_eventos()
            self._atualizar()
            self._desenhar()
            self.relogio.tick(FPS)

        pygame.quit()

    def _processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                self._processar_espaco()

    def _processar_espaco(self):
        if self.estado == ESTADO_JOGANDO:
            self.passaro.pular()
        elif self.estado == ESTADO_MENU:
            self.estado = ESTADO_JOGANDO
        elif self.estado == ESTADO_GAME_OVER:
            self._reiniciar()
            self.estado = ESTADO_JOGANDO

    def _atualizar(self):
        if self.estado != ESTADO_JOGANDO:
            return

        self.passaro.atualizar()
        if colidiu(self.passaro.obter_retangulo(), self.chao.obter_retangulo()):
            self.passaro.pousar(self.chao.y)
            self.estado = ESTADO_GAME_OVER
        self._atualizar_canos()

    def _atualizar_canos(self):
        self.frames_desde_ultimo_cano += 1
        if self.frames_desde_ultimo_cano >= INTERVALO_CANOS:
            self.canos.append(Cano())
            self.frames_desde_ultimo_cano = 0

        retangulo_passaro = self.passaro.obter_retangulo()
        for cano in self.canos:
            cano.atualizar()
            superior, inferior = cano.obter_retangulos()
            if colidiu(retangulo_passaro, superior) or colidiu(retangulo_passaro, inferior):
                self.estado = ESTADO_GAME_OVER
            elif cano.foi_ultrapassado(self.passaro.x):
                self.placar.incrementar()

        self.canos = [cano for cano in self.canos if not cano.fora_da_tela()]

    def _desenhar(self):
        self.tela.fill(COR_CEU)
        for cano in self.canos:
            cano.desenhar(self.tela)
        self.passaro.desenhar(self.tela)
        self.chao.desenhar(self.tela)
        self.placar.desenhar(self.tela)

        if self.estado == ESTADO_MENU:
            self.menu.desenhar_tela_inicial(self.tela)
        elif self.estado == ESTADO_GAME_OVER:
            self.menu.desenhar_tela_fim(self.tela, self.placar.pontos)

        pygame.display.flip()
