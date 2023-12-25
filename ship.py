import pygame

class Ship:
    #class to manage the behavior of the ship
    def __init__(self, ai_game) -> None:
        #initialize the ship and set it to starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the image of the ship
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        #draw in the ship at its current location
        self.screen.blit(self.image, self.rect)

