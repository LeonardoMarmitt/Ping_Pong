# menu.py
# Tela de menu inicial com opções "Jogar" e "Ver Scores"

import pygame
from config import LARGURA, ALTURA, BRANCO, AZUL_MESA, AMARELO
from score_db import carregar_scores

pygame.mixer.init()
pygame.mixer.music.load("assets/pixel-fight-8-bit-arcade-music-background-music-for-video-208775.mp3")
pygame.mixer.music.play(-1)  # -1 para tocar em loop


class Menu:
    def __init__(self, tela, fonte):
        self.tela = tela
        self.fonte = fonte
        self.opcao_selecionada = 0  # 0 = Jogar, 1 = Ver Scores
        self.fundo = pygame.image.load("assets/table-tennis-4291378_1280.jpg")

    def desenhar_menu(self):
        # E desenha no início de cada frame
        self.tela.blit(self.fundo, (0, 0))

        titulo = self.fonte.render("PING PONG", True, BRANCO)
        self.tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 50))

        opcoes = ["Jogar", "Ver Scores"]

        for i, texto in enumerate(opcoes):
            cor = AMARELO if i == self.opcao_selecionada else BRANCO
            opcao = self.fonte.render(texto, True, cor)
            self.tela.blit(opcao, (LARGURA // 2 - opcao.get_width() // 2, 150 + i * 60))

        pygame.display.update()

    def mostrar_scores(self):
        scores = carregar_scores()
        self.tela.fill(AZUL_MESA)

        titulo = self.fonte.render("SCORES", True, BRANCO)
        self.tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 40))

        for i, item in enumerate(scores[-10:]):
            texto = f"{item['nome']}: {item['pontuacao']}"
            linha = self.fonte.render(texto, True, BRANCO)
            self.tela.blit(linha, (LARGURA // 2 - linha.get_width() // 2, 100 + i * 40))

        pygame.display.update()

        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        esperando = False

    def executar(self):
        selecionando = True
        while selecionando:
            self.desenhar_menu()
            mouse_pos = pygame.mouse.get_pos()
            opcoes = ["Jogar", "Ver Scores"]
            opcao_rects = []

            for i, texto in enumerate(opcoes):
                opcao = self.fonte.render(texto, True, BRANCO)
                rect = opcao.get_rect(center=(LARGURA // 2, 150 + i * 60))
                opcao_rects.append(rect)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    for i, rect in enumerate(opcao_rects):
                        if rect.collidepoint(mouse_pos):
                            if i == 0:
                                return "jogar"
                            else:
                                self.mostrar_scores()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        self.opcao_selecionada = (self.opcao_selecionada - 1) % 2
                    elif evento.key == pygame.K_DOWN:
                        self.opcao_selecionada = (self.opcao_selecionada + 1) % 2
                    elif evento.key == pygame.K_RETURN:
                        if self.opcao_selecionada == 0:
                            return "jogar"
                        elif self.opcao_selecionada == 1:
                            self.mostrar_scores()
# commit