from constantes import VELOCIDADE_CANO_INICIAL, VELOCIDADE_CANO_MAXIMA
from game import calcular_velocidade_cano


def test_velocidade_inicial_com_zero_pontos():
    assert calcular_velocidade_cano(0) == VELOCIDADE_CANO_INICIAL


def test_velocidade_nao_muda_antes_de_completar_um_nivel():
    assert calcular_velocidade_cano(4) == VELOCIDADE_CANO_INICIAL


def test_velocidade_aumenta_a_cada_5_pontos():
    assert calcular_velocidade_cano(5) == VELOCIDADE_CANO_INICIAL + 0.5
    assert calcular_velocidade_cano(10) == VELOCIDADE_CANO_INICIAL + 1.0


def test_velocidade_nao_ultrapassa_o_teto():
    assert calcular_velocidade_cano(1000) == VELOCIDADE_CANO_MAXIMA
