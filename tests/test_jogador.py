import pytest

import jogador as jogador_module
from constantes import LIMITE_NOME
from jogador import Jogador


@pytest.fixture
def caminho_nome(tmp_path, monkeypatch):
    caminho = tmp_path / "jogador.txt"
    monkeypatch.setattr(jogador_module, "CAMINHO_NOME_JOGADOR", caminho)
    return caminho


def test_novo_jogador_comeca_sem_nome(caminho_nome):
    jogador = Jogador()
    assert jogador.tem_nome() is False
    assert jogador.nome == ""


def test_digitar_e_confirmar_salva_o_nome(caminho_nome):
    jogador = Jogador()
    for caractere in "mad":
        jogador.digitar(caractere)

    assert jogador.confirmar() is True
    assert jogador.nome == "mad"
    assert caminho_nome.read_text(encoding="utf-8") == "mad"


def test_confirmar_sem_digitar_nada_nao_salva(caminho_nome):
    jogador = Jogador()
    assert jogador.confirmar() is False
    assert jogador.tem_nome() is False
    assert not caminho_nome.exists()


def test_apagar_remove_o_ultimo_caractere(caminho_nome):
    jogador = Jogador()
    jogador.digitar("a")
    jogador.digitar("b")
    jogador.apagar()
    assert jogador.nome_digitando == "a"


def test_digitar_respeita_o_limite_de_caracteres(caminho_nome):
    jogador = Jogador()
    for _ in range(LIMITE_NOME + 10):
        jogador.digitar("x")
    assert len(jogador.nome_digitando) == LIMITE_NOME


def test_nome_persiste_entre_instancias(caminho_nome):
    primeiro = Jogador()
    for caractere in "ana":
        primeiro.digitar(caractere)
    primeiro.confirmar()

    segundo = Jogador()
    assert segundo.nome == "ana"
    assert segundo.tem_nome() is True


def test_iniciar_edicao_preenche_com_nome_atual(caminho_nome):
    jogador = Jogador()
    for caractere in "ana":
        jogador.digitar(caractere)
    jogador.confirmar()

    jogador.iniciar_edicao()
    assert jogador.nome_digitando == "ana"
