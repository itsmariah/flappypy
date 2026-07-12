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
CAMINHOS_FUNDO = [
    os.path.join(PASTA_IMAGENS, "backgrounds", f"Background{i}.png") for i in range(1, 10)
]
VELOCIDADE_FUNDO = 1

# Pássaro
CAMINHOS_FOLHA_PASSARO = [
    os.path.join(PASTA_IMAGENS, "player", "StyleBird1", "Bird1-1.png"),
    os.path.join(PASTA_IMAGENS, "player", "StyleBird2", "Bird2-1.png"),
]
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
LARGURA_TILE_CHAO = 32
ALTURA_CHAO = 50

# Canos
LARGURA_CANO = 64
GAP_CANO = 150
VELOCIDADE_CANO_INICIAL = 3
VELOCIDADE_CANO_MAXIMA = 7
INCREMENTO_VELOCIDADE_CANO = 0.5
PONTOS_POR_NIVEL = 5
INTERVALO_CANOS = 90
MARGEM_GAP = 50

# Estilos de cenário (cano + chão), pareados pela mesma pasta "Style N"
# area_tampa == area_corpo quando o estilo não tem um bico destacado (textura uniforme)
_PASTA_TILES = os.path.join(PASTA_IMAGENS, "tiles")
ESTILOS_CANO = [
    {
        "folha": os.path.join(_PASTA_TILES, "Style 1", "PipeStyle1.png"),
        "area_tampa": (0, 0, 32, 32),
        "area_corpo": (0, 32, 32, 32),
    },
    {
        "folha": os.path.join(_PASTA_TILES, "Style 2", "PipeStyle2.png"),
        "area_tampa": (0, 0, 32, 32),
        "area_corpo": (0, 0, 32, 32),
    },
    {
        "folha": os.path.join(_PASTA_TILES, "Style 3", "PipeStyle3.png"),
        "area_tampa": (0, 0, 32, 32),
        "area_corpo": (0, 0, 32, 32),
    },
]
ESTILOS_CHAO = [
    {"folha": os.path.join(_PASTA_TILES, "Style 1", "SimpleStyle1.png"), "area_tile": (0, 80, 16, 32)},
    {"folha": os.path.join(_PASTA_TILES, "Style 2", "SimpleStyle2.png"), "area_tile": (0, 48, 16, 32)},
    {"folha": os.path.join(_PASTA_TILES, "Style 3", "SimpleStyle3.png"), "area_tile": (0, 48, 16, 32)},
]

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
ESTADO_PAUSADO = "pausado"

# Jogador
CAMINHO_NOME_JOGADOR = os.path.join(_PASTA_RAIZ, "data", "jogador.txt")
LIMITE_NOME = 12

# Sons
CAMINHO_SOM_PULO = os.path.join(PASTA_SONS, "wing_flap.mp3")
CAMINHO_SOM_PONTO = os.path.join(PASTA_SONS, "coin.wav")  # coin.mp3 tinha ~185ms de silêncio no início
CAMINHO_SOM_FIM_DE_JOGO = os.path.join(PASTA_SONS, "game_over_arcade.mp3")
VOLUME_INICIAL = 0.7
PASSO_VOLUME = 0.1

# Efeitos (juice)
COR_PARTICULA = (255, 230, 120)
TAMANHO_PARTICULA = 3
QUANTIDADE_PARTICULAS_PULO = 6
VIDA_PARTICULA = 18
GRAVIDADE_PARTICULA = 0.15

FRAMES_SHAKE = 12
INTENSIDADE_SHAKE = 6
