import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion: 
    #Overall class to manage game assest and behavior.
    def __init__(self) -> None:
        #initiates the game and creates game resources
        pygame.init()
        self.clock : pygame.time.Clock = pygame.time.Clock()
        self.settings : Settings = Settings()

        self.screen : pygame.display = pygame.display.set_mode((self.settings.screenWidth,self.settings.screenHeight))
        pygame.display.set_caption("Alien Invasion")

        self.ship : Ship = Ship(self)

    def run_game(self) -> None:
        #starts the main loop
        while True:
            #waits for keyboard activity
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #set the background color each loop
            self.screen.fill(self.settings.backgroundColor)

            #create a visual of the ship
            self.ship.blitme()
            
            #makes the most recent screen visible
            pygame.display.flip()

            #set the refresh rate, unit: frames per second
            self.clock.tick(60)


if __name__ == "__main__":
    #creates an instance of the game and runs it. 
    ai : AlienInvasion = AlienInvasion()
    ai.run_game()