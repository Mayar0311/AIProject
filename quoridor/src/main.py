import pygame
import sys

from gui.menuScreen import MenuScreen
from gui.gameScreen import GameScreen
from gui.constants import MENU_WIDTH, MENU_HEIGHT
from util.constants import WINDOW_WIDTH, WINDOW_HEIGHT


def main():
    """Main application entry point."""
    pygame.init()
    
    # Create window
    screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
    pygame.display.set_caption("Quoridor")
    
    running = True
    
    while running:
        # Show menu
        menu = MenuScreen(screen)
        mode, difficulty = menu.run()
        
        if mode is None:
            # User closed window
            running = False
            break
        
        # Resize window for game
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        # Run game
        game = GameScreen(screen, mode, difficulty)
        continue_playing = game.run()
        
        if not continue_playing:
            # User closed window
            running = False
            break
        
        # Resize window back to menu
        screen = pygame.display.set_mode((MENU_WIDTH, MENU_HEIGHT))
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
