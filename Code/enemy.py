import pygame
import config


class Enemy:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.largura = config.RAQUETE_LARGURA
        self.altura = config.RAQUETE_ALTURA
        self.cor = cor
        self.vel = config.VEL_IA

    def mover(self, bola_y):
        centro_raquete = self.y + self.altura // 2
        if bola_y > centro_raquete and self.y + self.altura < config.ALTURA:
            self.y += self.vel
        elif bola_y < centro_raquete and self.y > 0:
            self.y -= self.vel

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
