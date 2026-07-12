import os

_PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_IMAGENS = os.path.join(_PASTA_RAIZ, "assets", "images")
PASTA_SONS = os.path.join(_PASTA_RAIZ, "assets", "sounds")

# Janela
LARGURA_TELA = 400
ALTURA_TELA = 600
TITULO = "Flappy Py"

# Loop principal
FPS = 60

# Cores (RGB)
COR_BRANCO = (255, 255, 255)

# Fundo
CAMINHO_FUNDO = os.path.join(PASTA_IMAGENS, "backgrounds", "Background1.png")
VELOCIDADE_FUNDO = 1

# Pássaro
CAMINHO_FOLHA_PASSARO = os.path.join(PASTA_IMAGENS, "player", "StyleBird1", "Bird1-1.png")
LARGURA_PASSARO = 32
ALTURA_PASSARO = 32
QUADROS_ANIMACAO_PASSARO = 4
INTERVALO_ANIMACAO_PASSARO = 5
POS_INICIAL_X = 60
POS_INICIAL_Y = ALTURA_TELA // 2
GRAVIDADE = 0.35
FORCA_PULO = -7
AMPLITUDE_FLUTUACAO = 10
VELOCIDADE_FLUTUACAO = 0.05

# Chão
CAMINHO_FOLHA_CHAO = os.path.join(PASTA_IMAGENS, "tiles", "Style 1", "SimpleStyle1.png")
LARGURA_TILE_CHAO = 32
ALTURA_CHAO = 50

# Canos
CAMINHO_FOLHA_CANOS = os.path.join(PASTA_IMAGENS, "tiles", "Style 1", "PipeStyle1.png")
LARGURA_CANO = 64
GAP_CANO = 150
VELOCIDADE_CANO_INICIAL = 3
VELOCIDADE_CANO_MAXIMA = 7
INCREMENTO_VELOCIDADE_CANO = 0.5
PONTOS_POR_NIVEL = 5
INTERVALO_CANOS = 90
MARGEM_GAP = 50

# Fonte
CAMINHO_FONTE = os.path.join(_PASTA_RAIZ, "assets", "fonts", "PressStart2P-Regular.ttf")
AMPLITUDE_PULSO = 60
VELOCIDADE_PULSO = 0.08

# Placar
TAMANHO_FONTE_PLACAR = 28
CAMINHO_RECORDES = os.path.join(_PASTA_RAIZ, "data", "recordes.json")

# Estados do jogo
ESTADO_NOME = "nome"
ESTADO_MENU = "menu"
ESTADO_JOGANDO = "jogando"
ESTADO_GAME_OVER = "game_over"
ESTADO_CONFIG = "config"

# Jogador
CAMINHO_NOME_JOGADOR = os.path.join(_PASTA_RAIZ, "data", "jogador.txt")
LIMITE_NOME = 12

# Sons
CAMINHO_SOM_PULO = os.path.join(PASTA_SONS, "wing_flap.mp3")
CAMINHO_SOM_PONTO = os.path.join(PASTA_SONS, "coin.wav")  # coin.mp3 tinha ~185ms de silêncio no início
CAMINHO_SOM_FIM_DE_JOGO = os.path.join(PASTA_SONS, "game_over_arcade.mp3")
VOLUME_INICIAL = 0.7
PASSO_VOLUME = 0.1
