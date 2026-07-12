import os

_PASTA_RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_IMAGENS = os.path.join(_PASTA_RAIZ, "assets", "images")

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
GRAVIDADE = 0.5
FORCA_PULO = -8

# Chão
CAMINHO_FOLHA_CHAO = os.path.join(PASTA_IMAGENS, "tiles", "Style 1", "SimpleStyle1.png")
LARGURA_TILE_CHAO = 32
ALTURA_CHAO = 50

# Canos
CAMINHO_FOLHA_CANOS = os.path.join(PASTA_IMAGENS, "tiles", "Style 1", "PipeStyle1.png")
LARGURA_CANO = 64
GAP_CANO = 150
VELOCIDADE_CANO = 3
INTERVALO_CANOS = 90
MARGEM_GAP = 50

# Placar
TAMANHO_FONTE_PLACAR = 48

# Estados do jogo
ESTADO_MENU = "menu"
ESTADO_JOGANDO = "jogando"
ESTADO_GAME_OVER = "game_over"
