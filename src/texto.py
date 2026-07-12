from constantes import COR_BRANCO, COR_SOMBRA_TEXTO, DESLOCAMENTO_SOMBRA_TEXTO


def desenhar_texto(tela, texto, fonte, cor=COR_BRANCO, alpha=None, **posicao):
    sombra = fonte.render(texto, True, COR_SOMBRA_TEXTO)
    if alpha is not None:
        sombra.set_alpha(alpha)
    retangulo_sombra = sombra.get_rect(**posicao)
    retangulo_sombra.x += DESLOCAMENTO_SOMBRA_TEXTO
    retangulo_sombra.y += DESLOCAMENTO_SOMBRA_TEXTO
    tela.blit(sombra, retangulo_sombra)

    superficie = fonte.render(texto, True, cor)
    if alpha is not None:
        superficie.set_alpha(alpha)
    retangulo = superficie.get_rect(**posicao)
    tela.blit(superficie, retangulo)
    return retangulo
