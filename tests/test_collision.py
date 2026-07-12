import pygame

from collision import colidiu


def test_colidiu_quando_retangulos_se_sobrepoem():
    a = pygame.Rect(0, 0, 10, 10)
    b = pygame.Rect(5, 5, 10, 10)
    assert colidiu(a, b) is True


def test_nao_colidiu_quando_retangulos_estao_distantes():
    a = pygame.Rect(0, 0, 10, 10)
    b = pygame.Rect(50, 50, 10, 10)
    assert colidiu(a, b) is False


def test_nao_colidiu_quando_retangulos_apenas_se_tocam_na_borda():
    a = pygame.Rect(0, 0, 10, 10)
    b = pygame.Rect(10, 0, 10, 10)
    assert colidiu(a, b) is False
