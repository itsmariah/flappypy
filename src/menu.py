import math

import pygame

from constantes import (
    ALTURA_TELA,
    AMPLITUDE_PULSO,
    CAMINHO_FONTE,
    COR_BRANCO,
    LARGURA_TELA,
    TAMANHO_FONTE_PLACAR,
    VELOCIDADE_PULSO,
)
from texto import desenhar_texto

TAMANHO_ICONE_LAPIS = 14
COR_PONTA_LAPIS = (255, 210, 120)
PONTOS_CORPO_LAPIS = [(1, 12), (3, 12), (13, 2), (11, 0)]
PONTOS_PONTA_LAPIS = [(1, 12), (3, 12), (1, 10)]

CORES_TITULO = [
    COR_BRANCO,
    (255, 215, 0),  # amarelo
    (255, 99, 71),  # coral
    (100, 220, 255),  # ciano
    (140, 255, 140),  # verde
]

TAMANHO_ICONE = 18
COR_FUNDO_ICONE = (30, 30, 30)
COR_ALERTA = (255, 90, 90)
COR_CONTORNO_ICONE = (0, 0, 0)
CORPO_ALTOFALANTE = [(2, 6), (6, 6), (11, 1), (11, 17), (6, 12), (2, 12)]


def gerar_engrenagem(centro, raio_externo, raio_interno, dentes):
    pontos = []
    total = dentes * 2
    for i in range(total):
        angulo = (2 * math.pi / total) * i
        raio = raio_externo if i % 2 == 0 else raio_interno
        x = centro[0] + raio * math.cos(angulo)
        y = centro[1] + raio * math.sin(angulo)
        pontos.append((x, y))
    return pontos


class Botao:
    def __init__(self, fonte, texto, largura, altura, cor=COR_BRANCO):
        self.fonte = fonte
        self.texto = texto
        self.cor = cor
        self.rect = pygame.Rect(0, 0, largura, altura)

    def posicionar(self, x, y):
        self.rect.topleft = (x, y)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect, width=2)
        desenhar_texto(tela, self.texto, self.fonte, self.cor, center=self.rect.center)

    def foi_clicado(self, pos):
        return self.rect.collidepoint(pos)


class Menu:
    def __init__(self, indice_cor_titulo=0):
        self.fonte_titulo = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_PLACAR)
        self.fonte_instrucao = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_PLACAR // 2)
        self.retangulo_nome = None
        self.retangulo_recorde = None
        self.retangulo_titulo = None
        self.indice_cor_titulo = indice_cor_titulo
        self.contador_pulso = 0
        self.botao_menu = Botao(self.fonte_instrucao, "Menu", 150, 36)
        self.botao_reiniciar = Botao(self.fonte_instrucao, "Reiniciar", 150, 36)
        self.botao_continuar = Botao(self.fonte_instrucao, "Continuar", 150, 36)
        self.retangulo_mudo = pygame.Rect(10, 34, TAMANHO_ICONE, TAMANHO_ICONE)
        self.retangulo_config = pygame.Rect(10, 34 + TAMANHO_ICONE + 6, TAMANHO_ICONE, TAMANHO_ICONE)

    def atualizar(self):
        self.contador_pulso += 1

    def desenhar_tela_nome(self, tela, nome_digitando):
        self._desenhar_texto(tela, "Qual seu nome?", self.fonte_instrucao, ALTURA_TELA // 2 - 40)
        self._desenhar_texto(tela, nome_digitando + "_", self.fonte_titulo, ALTURA_TELA // 2)
        self._desenhar_texto(
            tela, "Aperte Enter para confirmar", self.fonte_instrucao, ALTURA_TELA // 2 + 50
        )

    def desenhar_tela_inicial(self, tela, nome, recorde, audio_mutado):
        self._desenhar_titulo(tela)
        self._desenhar_dica_espaco(tela)
        self._desenhar_canto(tela, nome, "topleft")
        self._desenhar_icone_lapis(tela)
        self._desenhar_canto(tela, f"Recorde: {recorde}", "topright")
        self._desenhar_icone_mudo(tela, audio_mutado)
        self._desenhar_icone_config(tela)

    def desenhar_tela_fim(self, tela, pontos, recorde):
        self._desenhar_texto(tela, "Game Over", self.fonte_titulo, ALTURA_TELA // 2 - 60, COR_ALERTA)
        self._desenhar_texto(
            tela, f"Pontuação: {pontos}", self.fonte_instrucao, ALTURA_TELA // 2 - 10
        )
        self._desenhar_texto(
            tela, f"Recorde: {recorde}", self.fonte_instrucao, ALTURA_TELA // 2 + 25
        )

        espaco = 20
        largura_total = self.botao_menu.rect.width + espaco + self.botao_reiniciar.rect.width
        x_inicial = (LARGURA_TELA - largura_total) // 2
        y_botoes = ALTURA_TELA // 2 + 80
        self.botao_menu.posicionar(x_inicial, y_botoes)
        self.botao_reiniciar.posicionar(x_inicial + self.botao_menu.rect.width + espaco, y_botoes)
        self.botao_menu.desenhar(tela)
        self.botao_reiniciar.desenhar(tela)

    def desenhar_tela_pausa(self, tela):
        self._desenhar_texto(tela, "Pausado", self.fonte_titulo, ALTURA_TELA // 2 - 60)

        espaco = 20
        largura_total = self.botao_continuar.rect.width + espaco + self.botao_menu.rect.width
        x_inicial = (LARGURA_TELA - largura_total) // 2
        y_botoes = ALTURA_TELA // 2
        self.botao_continuar.posicionar(x_inicial, y_botoes)
        self.botao_menu.posicionar(x_inicial + self.botao_continuar.rect.width + espaco, y_botoes)
        self.botao_continuar.desenhar(tela)
        self.botao_menu.desenhar(tela)

    def _desenhar_texto(self, tela, texto, fonte, y, cor=COR_BRANCO):
        desenhar_texto(tela, texto, fonte, cor, centerx=LARGURA_TELA // 2, y=y)

    def _desenhar_canto(self, tela, texto, canto):
        margem = 10
        if canto == "topleft":
            self.retangulo_nome = desenhar_texto(
                tela, texto, self.fonte_instrucao, topleft=(margem, margem)
            )
        else:
            self.retangulo_recorde = desenhar_texto(
                tela, texto, self.fonte_instrucao, topright=(LARGURA_TELA - margem, margem)
            )

    def _desenhar_icone_lapis(self, tela, espaco=4):
        x = self.retangulo_nome.right + espaco
        y = self.retangulo_nome.centery - TAMANHO_ICONE_LAPIS // 2
        corpo = [(x + px, y + py) for px, py in PONTOS_CORPO_LAPIS]
        ponta = [(x + px, y + py) for px, py in PONTOS_PONTA_LAPIS]
        pygame.draw.polygon(tela, COR_BRANCO, corpo)
        pygame.draw.polygon(tela, COR_PONTA_LAPIS, ponta)
        self.retangulo_nome.width += espaco + TAMANHO_ICONE_LAPIS

    def nome_foi_clicado(self, pos):
        return self.retangulo_nome is not None and self.retangulo_nome.collidepoint(pos)

    def recorde_foi_clicado(self, pos):
        return self.retangulo_recorde is not None and self.retangulo_recorde.collidepoint(pos)

    def _desenhar_titulo(self, tela):
        cor = CORES_TITULO[self.indice_cor_titulo]
        self.retangulo_titulo = desenhar_texto(
            tela, "Flappy Py", self.fonte_titulo, cor, centerx=LARGURA_TELA // 2, y=ALTURA_TELA // 2 - 40
        )

    def titulo_foi_clicado(self, pos):
        return self.retangulo_titulo is not None and self.retangulo_titulo.collidepoint(pos)

    def ciclar_cor_titulo(self):
        self.indice_cor_titulo = (self.indice_cor_titulo + 1) % len(CORES_TITULO)

    def cor_titulo_atual(self):
        return CORES_TITULO[self.indice_cor_titulo]

    def _desenhar_icone_mudo(self, tela, mutado):
        pygame.draw.rect(tela, COR_FUNDO_ICONE, self.retangulo_mudo)
        x, y = self.retangulo_mudo.topleft
        corpo = [(x + px, y + py) for px, py in CORPO_ALTOFALANTE]
        pygame.draw.polygon(tela, COR_BRANCO, corpo)
        pygame.draw.polygon(tela, COR_CONTORNO_ICONE, corpo, width=1)
        if mutado:
            pygame.draw.line(tela, COR_ALERTA, (x + 13, y + 3), (x + 17, y + 15), 2)
            pygame.draw.line(tela, COR_ALERTA, (x + 17, y + 3), (x + 13, y + 15), 2)
        else:
            pygame.draw.line(tela, COR_BRANCO, (x + 13, y + 5), (x + 16, y + 9), 2)
            pygame.draw.line(tela, COR_BRANCO, (x + 13, y + 13), (x + 16, y + 9), 2)

    def mudo_foi_clicado(self, pos):
        return self.retangulo_mudo.collidepoint(pos)

    def _desenhar_icone_config(self, tela):
        pygame.draw.rect(tela, COR_FUNDO_ICONE, self.retangulo_config)
        centro = self.retangulo_config.center
        pontos = gerar_engrenagem(centro, 8, 6.5, 8)
        pygame.draw.polygon(tela, COR_BRANCO, pontos)
        pygame.draw.polygon(tela, COR_CONTORNO_ICONE, pontos, width=1)
        pygame.draw.circle(tela, COR_FUNDO_ICONE, centro, 3)

    def config_foi_clicado(self, pos):
        return self.retangulo_config.collidepoint(pos)

    def _desenhar_dica_espaco(self, tela):
        alpha = 195 + math.sin(self.contador_pulso * VELOCIDADE_PULSO) * AMPLITUDE_PULSO
        desenhar_texto(
            tela,
            "<espaço>",
            self.fonte_instrucao,
            alpha=int(alpha),
            centerx=LARGURA_TELA // 2,
            y=ALTURA_TELA // 2 + 20,
        )
