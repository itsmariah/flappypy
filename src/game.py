import pygame

from audio import Audio
from background import Fundo
from bird import Bird
from collision import colidiu
from configuracoes import TelaConfiguracoes
from constantes import (
    ALTURA_PASSARO,
    ALTURA_TELA,
    CAMINHOS_FOLHA_PASSARO,
    CAMINHOS_FUNDO,
    ESTADO_CONFIG,
    ESTADO_GAME_OVER,
    ESTADO_JOGANDO,
    ESTADO_MENU,
    ESTADO_NOME,
    ESTILOS_CANO,
    FPS,
    INCREMENTO_VELOCIDADE_CANO,
    INTERVALO_CANOS,
    LARGURA_TELA,
    PONTOS_POR_NIVEL,
    TITULO,
    VELOCIDADE_CANO_INICIAL,
    VELOCIDADE_CANO_MAXIMA,
)
from efeitos import Shake, SistemaParticulas
from ground import Ground
from jogador import Jogador
from menu import Menu
from pipe import Cano
from score import Placar


def calcular_velocidade_cano(pontos):
    nivel = pontos // PONTOS_POR_NIVEL
    velocidade = VELOCIDADE_CANO_INICIAL + nivel * INCREMENTO_VELOCIDADE_CANO
    return min(velocidade, VELOCIDADE_CANO_MAXIMA)


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.cena = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        pygame.display.set_caption(TITULO)
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.menu = Menu()
        self.tela_config = TelaConfiguracoes()
        self.audio = Audio()
        self.estilo_fundo = 0
        self.fundo = Fundo(self.estilo_fundo)
        self.estilo_cenario = 0
        self.chao = Ground(self.estilo_cenario)
        self.jogador = Jogador()
        self.estilo_passaro = 0
        self.particulas = SistemaParticulas()
        self.shake = Shake()
        self.estado = ESTADO_MENU if self.jogador.tem_nome() else ESTADO_NOME
        self.origem_estado_nome = ESTADO_MENU
        self._reiniciar()

    def _reiniciar(self):
        self.passaro = Bird(self.estilo_passaro)
        self.canos = []
        self.frames_desde_ultimo_cano = INTERVALO_CANOS
        self.placar = Placar(self.jogador.nome)

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
            elif self.estado == ESTADO_NOME:
                self._processar_evento_nome(evento)
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                self._processar_espaco()
            elif evento.type == pygame.MOUSEBUTTONDOWN and self.estado == ESTADO_MENU:
                self._processar_clique_menu(evento.pos)
            elif evento.type == pygame.MOUSEBUTTONDOWN and self.estado == ESTADO_GAME_OVER:
                self._processar_clique_game_over(evento.pos)
            elif evento.type == pygame.MOUSEBUTTONDOWN and self.estado == ESTADO_CONFIG:
                self._processar_clique_config(evento.pos)

    def _processar_clique_menu(self, pos):
        if self.menu.nome_foi_clicado(pos):
            self.jogador.iniciar_edicao()
            self.origem_estado_nome = ESTADO_MENU
            self.estado = ESTADO_NOME
        elif self.menu.titulo_foi_clicado(pos):
            self.menu.ciclar_cor_titulo()
        elif self.menu.mudo_foi_clicado(pos):
            self.audio.alternar_mudo()
        elif self.menu.config_foi_clicado(pos):
            self.estado = ESTADO_CONFIG

    def _processar_clique_config(self, pos):
        if self.tela_config.botao_voltar.foi_clicado(pos):
            self.estado = ESTADO_MENU
        elif self.tela_config.botao_volume_menos.foi_clicado(pos):
            self.audio.diminuir_volume()
        elif self.tela_config.botao_volume_mais.foi_clicado(pos):
            self.audio.aumentar_volume()
        elif self.tela_config.botao_nome.foi_clicado(pos):
            self.jogador.iniciar_edicao()
            self.origem_estado_nome = ESTADO_CONFIG
            self.estado = ESTADO_NOME
        elif self.tela_config.botao_passaro.foi_clicado(pos):
            self.estilo_passaro = (self.estilo_passaro + 1) % len(CAMINHOS_FOLHA_PASSARO)
            self._reiniciar()
        elif self.tela_config.botao_fundo.foi_clicado(pos):
            self.estilo_fundo = (self.estilo_fundo + 1) % len(CAMINHOS_FUNDO)
            self.fundo = Fundo(self.estilo_fundo)
        elif self.tela_config.botao_cenario.foi_clicado(pos):
            self.estilo_cenario = (self.estilo_cenario + 1) % len(ESTILOS_CANO)
            self.chao = Ground(self.estilo_cenario)
        elif self.tela_config.botao_cor.foi_clicado(pos):
            self.menu.ciclar_cor_titulo()
        elif self.tela_config.botao_zerar.foi_clicado(pos):
            self.placar.zerar_recorde()

    def _processar_clique_game_over(self, pos):
        if self.menu.botao_reiniciar.foi_clicado(pos):
            self._reiniciar()
            self.estado = ESTADO_JOGANDO
        elif self.menu.botao_menu.foi_clicado(pos):
            self._reiniciar()
            self.estado = ESTADO_MENU

    def _processar_evento_nome(self, evento):
        if evento.type != pygame.KEYDOWN:
            return
        if evento.key == pygame.K_RETURN:
            if self.jogador.confirmar():
                self._reiniciar()
                self.estado = self.origem_estado_nome
        elif evento.key == pygame.K_BACKSPACE:
            self.jogador.apagar()
        elif evento.unicode:
            self.jogador.digitar(evento.unicode)

    def _processar_espaco(self):
        self.audio.tocar_pulo()
        if self.estado == ESTADO_JOGANDO:
            self.passaro.pular()
            self.particulas.emitir(self.passaro.x, self.passaro.y + ALTURA_PASSARO // 2)
        elif self.estado == ESTADO_MENU:
            self.estado = ESTADO_JOGANDO
        elif self.estado == ESTADO_GAME_OVER:
            self._reiniciar()
            self.estado = ESTADO_JOGANDO

    def _atualizar(self):
        self.shake.atualizar()
        self.particulas.atualizar()

        if self.estado == ESTADO_MENU:
            self.passaro.flutuar()
            self.menu.atualizar()
            return
        if self.estado != ESTADO_JOGANDO:
            return

        velocidade_atual = calcular_velocidade_cano(self.placar.pontos)
        self.fundo.atualizar()
        self.chao.atualizar(velocidade_atual)
        self.passaro.atualizar()
        if colidiu(self.passaro.obter_retangulo(), self.chao.obter_retangulo()):
            self.passaro.pousar(self.chao.y)
            self.estado = ESTADO_GAME_OVER
            self.audio.tocar_fim_de_jogo()
            self.shake.iniciar()
        self._atualizar_canos(velocidade_atual)

    def _atualizar_canos(self, velocidade_atual):
        self.frames_desde_ultimo_cano += 1
        if self.frames_desde_ultimo_cano >= INTERVALO_CANOS:
            self.canos.append(Cano(velocidade_atual, self.estilo_cenario))
            self.frames_desde_ultimo_cano = 0

        retangulo_passaro = self.passaro.obter_retangulo()
        for cano in self.canos:
            cano.atualizar()
            superior, inferior = cano.obter_retangulos()
            if colidiu(retangulo_passaro, superior) or colidiu(retangulo_passaro, inferior):
                self.estado = ESTADO_GAME_OVER
                self.audio.tocar_fim_de_jogo()
                self.shake.iniciar()
            elif cano.foi_ultrapassado(self.passaro.x):
                self.placar.incrementar()
                self.audio.tocar_ponto()

        self.canos = [cano for cano in self.canos if not cano.fora_da_tela()]

    def _desenhar(self):
        self.fundo.desenhar(self.cena)
        for cano in self.canos:
            cano.desenhar(self.cena)
        self.passaro.desenhar(self.cena)
        self.particulas.desenhar(self.cena)
        self.chao.desenhar(self.cena)

        if self.estado in (ESTADO_JOGANDO, ESTADO_GAME_OVER):
            self.placar.desenhar(self.cena)

        if self.estado == ESTADO_NOME:
            self.menu.desenhar_tela_nome(self.cena, self.jogador.nome_digitando)
        elif self.estado == ESTADO_MENU:
            self.menu.desenhar_tela_inicial(
                self.cena, self.jogador.nome, self.placar.recorde, self.audio.mutado
            )
        elif self.estado == ESTADO_GAME_OVER:
            self.menu.desenhar_tela_fim(self.cena, self.placar.pontos, self.placar.recorde)
        elif self.estado == ESTADO_CONFIG:
            self.tela_config.desenhar(self.cena, self.audio.volume, self.menu.cor_titulo_atual())

        self.tela.fill((0, 0, 0))
        self.tela.blit(self.cena, self.shake.offset())
        pygame.display.flip()
