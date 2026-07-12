import pygame

from constantes import (
    CAMINHO_SOM_FIM_DE_JOGO,
    CAMINHO_SOM_PONTO,
    CAMINHO_SOM_PULO,
    PASSO_VOLUME,
    VOLUME_INICIAL,
)


class Audio:
    _som_pulo = None
    _som_ponto = None
    _som_fim_de_jogo = None

    def __init__(self, volume=VOLUME_INICIAL, mutado=False):
        if Audio._som_pulo is None:
            Audio._som_pulo = pygame.mixer.Sound(CAMINHO_SOM_PULO)
            Audio._som_ponto = pygame.mixer.Sound(CAMINHO_SOM_PONTO)
            Audio._som_fim_de_jogo = pygame.mixer.Sound(CAMINHO_SOM_FIM_DE_JOGO)

        self.volume = volume
        self.mutado = mutado
        self._aplicar_volume()

    def tocar_pulo(self):
        Audio._som_pulo.play()

    def tocar_ponto(self):
        Audio._som_ponto.play()

    def tocar_fim_de_jogo(self):
        Audio._som_fim_de_jogo.play()

    def alternar_mudo(self):
        self.mutado = not self.mutado
        self._aplicar_volume()

    def aumentar_volume(self):
        self.volume = min(1.0, self.volume + PASSO_VOLUME)
        self.mutado = False
        self._aplicar_volume()

    def diminuir_volume(self):
        self.volume = max(0.0, self.volume - PASSO_VOLUME)
        self._aplicar_volume()

    def _aplicar_volume(self):
        volume_efetivo = 0.0 if self.mutado else self.volume
        for som in (Audio._som_pulo, Audio._som_ponto, Audio._som_fim_de_jogo):
            som.set_volume(volume_efetivo)
