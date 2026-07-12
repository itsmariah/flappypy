import pygame

from constantes import ALTURA_TELA, CAMINHO_FONTE, COR_BRANCO, LARGURA_TELA
from menu import Botao

TAMANHO_FONTE_TITULO_CONFIG = 24
TAMANHO_FONTE_OPCAO_CONFIG = 14


class TelaConfiguracoes:
    def __init__(self):
        self.fonte_titulo = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_TITULO_CONFIG)
        self.fonte_opcao = pygame.font.Font(CAMINHO_FONTE, TAMANHO_FONTE_OPCAO_CONFIG)

        largura_botao = 220
        altura_botao = 32
        x_centro = (LARGURA_TELA - largura_botao) // 2

        self.botao_volume_menos = Botao(self.fonte_opcao, "-", 50, altura_botao)
        self.botao_volume_mais = Botao(self.fonte_opcao, "+", 50, altura_botao)
        self.botao_volume_menos.posicionar(LARGURA_TELA // 2 - 70, 150)
        self.botao_volume_mais.posicionar(LARGURA_TELA // 2 + 20, 150)

        self.botao_nome = Botao(self.fonte_opcao, "Trocar nome", largura_botao, altura_botao)
        self.botao_nome.posicionar(x_centro, 205)

        self.botao_passaro = Botao(self.fonte_opcao, "Trocar passaro", largura_botao, altura_botao)
        self.botao_passaro.posicionar(x_centro, 245)

        self.botao_fundo = Botao(self.fonte_opcao, "Trocar fundo", largura_botao, altura_botao)
        self.botao_fundo.posicionar(x_centro, 285)

        self.botao_cenario = Botao(self.fonte_opcao, "Trocar cenario", largura_botao, altura_botao)
        self.botao_cenario.posicionar(x_centro, 325)

        self.botao_cor = Botao(self.fonte_opcao, "Cor do titulo", largura_botao, altura_botao)
        self.botao_cor.posicionar(x_centro, 365)

        self.botao_zerar = Botao(self.fonte_opcao, "Zerar recorde", largura_botao, altura_botao)
        self.botao_zerar.posicionar(x_centro, 405)

        self.botao_voltar = Botao(self.fonte_opcao, "Voltar", largura_botao, altura_botao)
        self.botao_voltar.posicionar(x_centro, 460)

    def desenhar(self, tela, volume, cor_titulo):
        self._desenhar_texto(tela, "Configuracoes", self.fonte_titulo, 50, cor_titulo)
        self._desenhar_texto(tela, f"Volume: {round(volume * 100)}%", self.fonte_opcao, 115)

        self.botao_volume_menos.desenhar(tela)
        self.botao_volume_mais.desenhar(tela)
        self.botao_nome.desenhar(tela)
        self.botao_passaro.desenhar(tela)
        self.botao_fundo.desenhar(tela)
        self.botao_cenario.desenhar(tela)
        self.botao_cor.desenhar(tela)
        self.botao_zerar.desenhar(tela)
        self.botao_voltar.desenhar(tela)

    def _desenhar_texto(self, tela, texto, fonte, y, cor=COR_BRANCO):
        superficie = fonte.render(texto, True, cor)
        retangulo = superficie.get_rect(centerx=LARGURA_TELA // 2, y=y)
        tela.blit(superficie, retangulo)
