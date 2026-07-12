import pygame

from constantes import CAMINHO_FONTE, FRAMES_CONFIRMACAO, LARGURA_TELA
from menu import COR_ALERTA, Botao
from texto import desenhar_texto

TAMANHO_FONTE_TITULO_CONFIG = 24
TAMANHO_FONTE_OPCAO_CONFIG = 14
TEXTO_ZERAR_PADRAO = "Zerar recorde"
TEXTO_ZERAR_CONFIRMACAO = "Confirmar?"


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

        self.botao_zerar = Botao(
            self.fonte_opcao, TEXTO_ZERAR_PADRAO, largura_botao, altura_botao, cor=COR_ALERTA
        )
        self.botao_zerar.posicionar(x_centro, 405)

        self.botao_voltar = Botao(self.fonte_opcao, "Voltar", largura_botao, altura_botao)
        self.botao_voltar.posicionar(x_centro, 460)

        self.confirmando_zerar = False
        self.frames_confirmacao = 0

    def atualizar(self):
        if self.confirmando_zerar:
            self.frames_confirmacao -= 1
            if self.frames_confirmacao <= 0:
                self.cancelar_confirmacao_zerar()

    def solicitar_zerar(self):
        """Primeiro clique arma a confirmação; segundo clique (dentro do prazo) efetiva o reset."""
        if self.confirmando_zerar:
            self.cancelar_confirmacao_zerar()
            return True
        self.confirmando_zerar = True
        self.frames_confirmacao = FRAMES_CONFIRMACAO
        self.botao_zerar.texto = TEXTO_ZERAR_CONFIRMACAO
        return False

    def cancelar_confirmacao_zerar(self):
        self.confirmando_zerar = False
        self.botao_zerar.texto = TEXTO_ZERAR_PADRAO

    def desenhar(self, tela, volume, cor_titulo):
        desenhar_texto(tela, "Configuracoes", self.fonte_titulo, cor_titulo, centerx=LARGURA_TELA // 2, y=50)
        desenhar_texto(
            tela, f"Volume: {round(volume * 100)}%", self.fonte_opcao, centerx=LARGURA_TELA // 2, y=115
        )

        self.botao_volume_menos.desenhar(tela)
        self.botao_volume_mais.desenhar(tela)
        self.botao_nome.desenhar(tela)
        self.botao_passaro.desenhar(tela)
        self.botao_fundo.desenhar(tela)
        self.botao_cenario.desenhar(tela)
        self.botao_cor.desenhar(tela)
        self.botao_zerar.desenhar(tela)
        self.botao_voltar.desenhar(tela)
