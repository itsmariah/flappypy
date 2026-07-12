import json
import os

from constantes import CAMINHO_PREFERENCIAS, VOLUME_INICIAL

PADRAO = {
    "estilo_fundo": 0,
    "estilo_cenario": 0,
    "estilo_passaro": 0,
    "indice_cor_titulo": 0,
    "volume": VOLUME_INICIAL,
    "mutado": False,
}


class Preferencias:
    def __init__(self):
        dados = self._carregar()
        for chave, padrao in PADRAO.items():
            setattr(self, chave, dados.get(chave, padrao))

    def salvar(self, **valores):
        for chave, valor in valores.items():
            setattr(self, chave, valor)
        os.makedirs(os.path.dirname(CAMINHO_PREFERENCIAS), exist_ok=True)
        with open(CAMINHO_PREFERENCIAS, "w", encoding="utf-8") as arquivo:
            json.dump({chave: getattr(self, chave) for chave in PADRAO}, arquivo)

    @staticmethod
    def _carregar():
        if not os.path.exists(CAMINHO_PREFERENCIAS):
            return {}
        with open(CAMINHO_PREFERENCIAS, "r", encoding="utf-8") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                return {}
