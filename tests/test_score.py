import pytest

import score as score_module
from score import Placar


@pytest.fixture
def caminho_recordes(tmp_path, monkeypatch):
    caminho = tmp_path / "recordes.json"
    monkeypatch.setattr(score_module, "CAMINHO_RECORDES", caminho)
    return caminho


def test_placar_novo_comeca_zerado(caminho_recordes):
    placar = Placar("mad")
    assert placar.pontos == 0
    assert placar.recorde == 0


def test_incrementar_aumenta_pontos(caminho_recordes):
    placar = Placar("mad")
    placar.incrementar()
    placar.incrementar()
    assert placar.pontos == 2


def test_incrementar_atualiza_recorde_quando_supera(caminho_recordes):
    placar = Placar("mad")
    placar.incrementar()
    assert placar.recorde == 1


def test_recorde_nao_diminui_numa_partida_pior(caminho_recordes):
    primeiro = Placar("mad")
    for _ in range(5):
        primeiro.incrementar()

    segundo = Placar("mad")
    segundo.incrementar()
    assert segundo.recorde == 5


def test_recorde_e_especifico_por_jogador(caminho_recordes):
    placar_mad = Placar("mad")
    for _ in range(3):
        placar_mad.incrementar()

    placar_lulu = Placar("lulu")
    assert placar_lulu.recorde == 0


def test_zerar_recorde(caminho_recordes):
    placar = Placar("mad")
    for _ in range(3):
        placar.incrementar()

    placar.zerar_recorde()
    assert placar.recorde == 0

    recarregado = Placar("mad")
    assert recarregado.recorde == 0
