import pygame
from config import LARGURA, ALTURA, AZUL_MESA, BRANCO
from score_db import salvar_score


def pedir_nome_e_salvar(tela, fonte, score_final):
    nome = ""
    ativo = True

    while ativo:
        tela.fill(AZUL_MESA)

        titulo = fonte.render("Fim de Jogo!", True, BRANCO)
        texto = fonte.render("Digite seu nome:", True, BRANCO)
        nome_render = fonte.render(nome + "|", True, BRANCO)

        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 80))
        tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 160))
        tela.blit(nome_render, (LARGURA // 2 - nome_render.get_width() // 2, 220))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nome != "":
                    salvar_score(nome, score_final)
                    ativo = False  # Sai da tela após salvar
                elif evento.key == pygame.K_BACKSPACE:
                    nome = nome[:-1]  # Remove último caractere
                else:
                    if len(nome) < 12:  # Limite opcional de caracteres
                        nome += evento.unicode
