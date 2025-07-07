import pygame
import config


class Player:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.largura = config.RAQUETE_LARGURA
        self.altura = config.RAQUETE_ALTURA
        self.cor = cor
        self.vel = config.VEL_RAQUETE

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w] and self.y > 0:
            self.y -= self.vel
        if teclas[pygame.K_s] and self.y < config.ALTURA - self.altura:
            self.y += self.vel

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

# commit
