from bird import Bird
from constantes import (
    ALTURA_PASSARO,
    AMPLITUDE_FLUTUACAO,
    FORCA_PULO,
    GRAVIDADE,
    LARGURA_PASSARO,
    POS_INICIAL_X,
    POS_INICIAL_Y,
)


def test_nasce_na_posicao_inicial_parado():
    passaro = Bird()
    assert passaro.x == POS_INICIAL_X
    assert passaro.y == POS_INICIAL_Y
    assert passaro.velocidade_y == 0


def test_pular_define_velocidade_para_cima():
    passaro = Bird()
    passaro.pular()
    assert passaro.velocidade_y == FORCA_PULO


def test_atualizar_aplica_gravidade():
    passaro = Bird()
    y_inicial = passaro.y
    passaro.atualizar()
    assert passaro.velocidade_y == GRAVIDADE
    assert passaro.y == y_inicial + GRAVIDADE


def test_atualizar_acumula_gravidade_a_cada_frame():
    passaro = Bird()
    passaro.atualizar()
    passaro.atualizar()
    assert passaro.velocidade_y == GRAVIDADE * 2


def test_pousar_encosta_o_passaro_na_superficie():
    passaro = Bird()
    passaro.velocidade_y = 10
    passaro.pousar(y_superficie=500)
    assert passaro.y == 500 - ALTURA_PASSARO
    assert passaro.velocidade_y == 0


def test_flutuar_nao_sai_da_amplitude_definida():
    passaro = Bird()
    for _ in range(200):
        passaro.flutuar()
        assert abs(passaro.y - POS_INICIAL_Y) <= AMPLITUDE_FLUTUACAO


def test_obter_retangulo_reflete_posicao_e_tamanho():
    passaro = Bird()
    retangulo = passaro.obter_retangulo()
    assert (retangulo.x, retangulo.y) == (POS_INICIAL_X, POS_INICIAL_Y)
    assert (retangulo.width, retangulo.height) == (LARGURA_PASSARO, ALTURA_PASSARO)
