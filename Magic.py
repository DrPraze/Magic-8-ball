"""Magic eight ball game"""
import sys
import time
import pygame
from random import choice

class magic:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((480, 490))
        pygame.display.set_caption("Magic 8 ball")
        self.font = pygame.font.SysFont('Helvetica', 35)
        bg = pygame.image.load("magic.jpg")
        self.screen.blit(bg, [0, 0])
        self.draw()
        self.x = 250
        self.y = 365
        self.w = 90
        self.h = 60
        
    def draw(self):
        global WHITE, BLACK, SILVER, DarkGrey, lemon
        lemon = (0, 255, 0)
        DarkGrey = (20, 20, 20)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        SILVER = (192, 192, 192)
        pygame.draw.circle(self.screen, DarkGrey, (230, 200), 135)
        pygame.draw.circle(self.screen, WHITE, (230, 200), 135, 2)
        pygame.draw.circle(self.screen, BLACK, (240, 210), 90)

    def perform(self):
        while True:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    if pos[0] > self.x and pos[0] < self.x + self.w:
                        if pos[1] > self.y and pos[1] < self.y + self.h:
                            pygame.draw.rect(self.screen, WHITE, (250, 365, 90, 40))
                            pygame.draw.rect(self.screen, DarkGrey, (250, 387, 90, 40))
                            pygame.draw.rect(self.screen, BLACK, (250, 365, 90, 60), 2)
                            self.screen.blit(self.font.render('ans', True,  lemon), (265, 370))
                    else:
                        pygame.draw.rect(self.screen, DarkGrey, (250, 365, 90, 40))
                        pygame.draw.rect(self.screen, BLACK, (250, 387, 90, 40))
                        pygame.draw.rect(self.screen, SILVER, (250, 365, 90, 60), 2)
                        self.screen.blit(self.font.render('ans', True,  lemon), (265, 370))
                if event.type == pygame.MOUSEBUTTONDOWN:
                     if pos[0] > self.x and pos[0] < self.x + self.w:
                        if pos[1] > self.y and pos[1] < self.y + self.h:
                            text = ['yes', 'no', 'YES', 'NO', 'hmm', 'never', 'maybe', 'yeah', 'yup', 'nope', 'well...']
                            tell = choice(text)
                            self.screen.blit(self.font.render(f'{tell}', True, WHITE), (205, 176))

            pygame.display.update()
            pygame.display.flip()

if __name__=='__main__':
    AI = magic()
    AI.perform()

