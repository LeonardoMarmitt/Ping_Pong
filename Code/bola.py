import pygame
import config


class Bola:
    def __init__(self):
        self.x = config.LARGURA // 2
        self.y = config.ALTURA // 2
        self.raio = config.BOLA_RAIO
        self.vel_x = config.VEL_BOLA_X
        self.vel_y = config.VEL_BOLA_Y

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y - self.raio <= 0 or self.y + self.raio >= config.ALTURA:
            self.vel_y *= -1

    def desenhar(self, tela):
        pygame.draw.circle(tela, config.BRANCO, (self.x, self.y), self.raio)

    def get_rect(self):
        return pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)

    def resetar(self):
        self.x = config.LARGURA // 2
        self.y = config.ALTURA // 2
        self.vel_x *= -1
