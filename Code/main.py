import pygame
from game import Game
from menu import Menu
from score_db import salvar_score


def main():
    pygame.init()
    tela = pygame.display.set_mode((800, 500))  # Pode importar de config também
    pygame.display.set_caption("Ping Pong com Menu")
    fonte = pygame.font.SysFont("Arial", 36)

    menu = Menu(tela, fonte)
    escolha = menu.executar()  # Exibe o menu e espera uma ação

    if escolha == "jogar":
        jogo = Game()
        jogo.loop()




if __name__ == "__main__":
    main()
# commit