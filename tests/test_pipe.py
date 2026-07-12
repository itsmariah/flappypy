from constantes import ALTURA_CHAO, ALTURA_TELA, GAP_CANO, LARGURA_CANO, LARGURA_TELA, MARGEM_GAP
from pipe import Cano


def test_abertura_tem_o_tamanho_configurado():
    cano = Cano(velocidade=3)
    assert cano.base - cano.topo == GAP_CANO


def test_abertura_respeita_a_margem_da_tela():
    cano = Cano(velocidade=3)
    altura_disponivel = ALTURA_TELA - ALTURA_CHAO
    assert cano.topo >= MARGEM_GAP
    assert cano.base <= altura_disponivel - MARGEM_GAP


def test_cano_nasce_na_borda_direita_da_tela():
    cano = Cano(velocidade=3)
    assert cano.x == LARGURA_TELA


def test_atualizar_move_o_cano_para_a_esquerda():
    cano = Cano(velocidade=3)
    x_inicial = cano.x
    cano.atualizar()
    assert cano.x == x_inicial - 3


def test_fora_da_tela_falso_logo_apos_criar():
    cano = Cano(velocidade=3)
    assert cano.fora_da_tela() is False


def test_fora_da_tela_verdadeiro_apos_passar_da_borda_esquerda():
    cano = Cano(velocidade=3)
    cano.x = -LARGURA_CANO - 1
    assert cano.fora_da_tela() is True


def test_foi_ultrapassado_falso_antes_do_passaro_passar():
    cano = Cano(velocidade=3)
    assert cano.foi_ultrapassado(x_passaro=0) is False


def test_foi_ultrapassado_verdadeiro_uma_unica_vez():
    cano = Cano(velocidade=3)
    cano.x = -LARGURA_CANO - 1  # já ficou pra trás do pássaro

    assert cano.foi_ultrapassado(x_passaro=100) is True
    assert cano.foi_ultrapassado(x_passaro=100) is False


def test_retangulos_ficam_acima_e_abaixo_da_abertura():
    cano = Cano(velocidade=3)
    superior, inferior = cano.obter_retangulos()

    assert superior.top == 0
    assert superior.bottom == cano.topo
    assert inferior.top == cano.base
    assert inferior.bottom == ALTURA_TELA
