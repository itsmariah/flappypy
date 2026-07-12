# Flappy Py

![Python](https://img.shields.io/badge/python-3.13-blue)
![Pygame](https://img.shields.io/badge/pygame-2.6.1-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Um clone do clássico *Flappy Bird* feito em Python com [Pygame](https://www.pygame.org/), construído do zero como projeto de estudo de arquitetura de software aplicada a jogos.

<p align="center">
  <img src="docs/screenshot-menu.png" width="30%" alt="Tela inicial" />
  <img src="docs/screenshot-jogando.png" width="30%" alt="Jogo em andamento" />
  <img src="docs/screenshot-gameover.png" width="30%" alt="Tela de game over" />
</p>

## Sobre o projeto

Este projeto não teve como objetivo só "fazer o jogo funcionar", mas praticar arquitetura de software: separação de responsabilidades, encapsulamento e código legível, evitando complexidade desnecessária a cada etapa. Cada funcionalidade foi construída incrementalmente — física do pássaro, colisão, canos, pontuação, estados de jogo (menu/jogando/game over) e, por fim, arte de verdade no lugar de formas geométricas.

## Funcionalidades

- Física de queda livre e pulo do pássaro (gravidade + impulso)
- Geração procedural de canos em intervalos regulares, com abertura em posição aleatória
- Detecção de colisão (pássaro × chão, pássaro × canos)
- Pontuação: soma um ponto a cada par de canos ultrapassado
- Máquina de estados simples: **menu inicial → jogando → game over → reiniciar**
- Pássaro com animação de bater asas (sprite sheet), canos e chão com sprites reais (não são retângulos coloridos)

## Arquitetura

O projeto segue separação de responsabilidades: cada módulo cuida de uma única coisa, e o `Game` apenas orquestra — sem conhecer os detalhes internos de cada entidade.

| Módulo | Responsabilidade |
|---|---|
| `main.py` | Ponto de entrada — cria e roda o `Game` |
| `game.py` | Orquestra o loop principal, os estados do jogo e a interação entre entidades |
| `constantes.py` | Toda a configuração do jogo (tamanhos, velocidades, cores, caminhos de assets) num só lugar |
| `bird.py` | Física, animação e desenho do pássaro |
| `background.py` | Rolagem contínua (parallax) do céu |
| `pipe.py` | Geração, movimento, desenho e detecção de "ultrapassado" de cada par de canos |
| `ground.py` | Posição e desenho (tiled) do chão |
| `collision.py` | Função genérica de colisão entre retângulos, reaproveitada para chão e canos |
| `audio.py` | Carregamento e reprodução dos efeitos sonoros |
| `score.py` | Contagem e exibição da pontuação |
| `menu.py` | Telas de texto (inicial e game over) |

**Decisões de design que valem destacar:**
- Cada entidade encapsula o próprio estado e comportamento (`Bird.pousar()`, `Cano.foi_ultrapassado()`) — o `Game` nunca lê ou altera atributos internos diretamente, só chama métodos.
- `collision.colidiu()` é uma função pura e genérica (dois retângulos → booleano), reaproveitada sem alteração tanto para o chão quanto para os canos.
- Sprites são carregados uma única vez (cache em atributo de classe) e recortados de sprite sheets via `Surface.subsurface()`, em vez de um arquivo de imagem por elemento.
- Estados do jogo (`ESTADO_MENU`, `ESTADO_JOGANDO`, `ESTADO_GAME_OVER`) são simples constantes de string, não um padrão *State* completo — decisão deliberada para manter a complexidade proporcional ao tamanho do projeto.

## Tecnologias

- [Python 3.13](https://www.python.org/)
- [Pygame 2.6.1](https://www.pygame.org/)

## Como executar

```bash
# 1. Crie e ative um ambiente virtual
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # Linux/macOS

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Rode o jogo
python src/main.py
```

**Controles:** barra de espaço para pular / começar / reiniciar.

## Estrutura de pastas

```
flappypy/
├── assets/
│   ├── images/       # sprites (pássaro, canos, tiles, backgrounds)
│   └── sounds/        # reservado para efeitos sonoros (ainda não usado)
├── docs/               # screenshots usados neste README
├── src/                # código-fonte
└── requirements.txt
```

## Roadmap

- [x] Fundo com parallax scrolling
- [x] Efeitos sonoros (pulo, colisão, ponto)
- [ ] Recorde persistente entre execuções
- [ ] Ajuste fino de física (gravidade/impulso) para uma sensação de jogo mais suave

## Créditos

Os sprites (pássaro, canos e tiles de chão) são do pacote [Flappy Bird Assets](https://megacrash.itch.io/flappy-bird-assets), por **megacrash** (itch.io). Direitos de uso sujeitos aos termos da página original — consulte antes de reutilizar este repositório para outros fins.

Os efeitos sonoros (pulo, ponto e game over) vieram do [Pixabay](https://pixabay.com), sob a licença da própria plataforma.

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais detalhes. A licença cobre o código-fonte deste repositório; os assets de terceiros seguem sua própria licença (veja Créditos acima).

## Autor

**itsmariah**
