

import pygame
import config
from player import Player
from enemy import Enemy
from bola import Bola


class Game:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((config.LARGURA, config.ALTURA))
        pygame.display.set_caption("Ping Pong Modular")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont("Arial", 36)

        self.jogador = Player(40, config.ALTURA // 2 - 50, config.VERDE)
        self.inimigo = Enemy(config.LARGURA - 60, config.ALTURA // 2 - 50, config.VERMELHO)
        self.bola = Bola()

        self.pontos_jogador = 0
        self.pontos_ia = 0
        self.rodando = True

    def desenhar_fundo(self):
        self.tela.fill(config.AZUL_MESA)
        pygame.draw.line(self.tela, config.BRANCO, (0, 0), (0, config.ALTURA), 10)
        pygame.draw.line(self.tela, config.BRANCO, (config.LARGURA - 1, 0), (config.LARGURA - 1, config.ALTURA), 10)
        for i in range(0, config.ALTURA, 30):
            pygame.draw.rect(self.tela, config.BRANCO, (config.LARGURA // 2 - 5, i, 10, 20))

    def desenhar_placar(self):
        texto = self.fonte.render(f"{self.pontos_jogador}   {self.pontos_ia}", True, config.BRANCO)
        self.tela.blit(texto, (config.LARGURA // 2 - 28, 20))

    def checar_colisoes(self):
        if self.bola.get_rect().colliderect(self.jogador.get_rect()):
            self.bola.vel_x *= -1
        if self.bola.get_rect().colliderect(self.inimigo.get_rect()):
            self.bola.vel_x *= -1

    def checar_ponto(self):
        if self.bola.x < 0:
            self.pontos_ia += 1
            self.bola.resetar()
        elif self.bola.x > config.LARGURA:
            self.pontos_jogador += 1
            self.bola.resetar()

    def atualizar_tela(self):
        self.desenhar_fundo()
        self.jogador.desenhar(self.tela)
        self.inimigo.desenhar(self.tela)
        self.bola.desenhar(self.tela)
        self.desenhar_placar()
        pygame.display.update()

    def loop(self):
        while self.rodando:
            self.clock.tick(config.FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.rodando = False

            self.jogador.mover()
            self.inimigo.mover(self.bola.y)
            self.bola.mover()
            self.checar_colisoes()
            self.checar_ponto()
            self.atualizar_tela()

        pygame.quit()
