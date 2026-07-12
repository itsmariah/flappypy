import pygame

from constantes import CAMINHO_SOM_FIM_DE_JOGO, CAMINHO_SOM_PONTO, CAMINHO_SOM_PULO


class Audio:
    _som_pulo = None
    _som_ponto = None
    _som_fim_de_jogo = None

    def __init__(self):
        if Audio._som_pulo is None:
            Audio._som_pulo = pygame.mixer.Sound(CAMINHO_SOM_PULO)
            Audio._som_ponto = pygame.mixer.Sound(CAMINHO_SOM_PONTO)
            Audio._som_fim_de_jogo = pygame.mixer.Sound(CAMINHO_SOM_FIM_DE_JOGO)

    def tocar_pulo(self):
        Audio._som_pulo.play()

    def tocar_ponto(self):
        Audio._som_ponto.play()

    def tocar_fim_de_jogo(self):
        Audio._som_fim_de_jogo.play()
