import pygame
pygame.init()

from util.constants import (
    COLOR_BACKGROUND, COLOR_BOARD, COLOR_GRID, COLOR_WALL,
    COLOR_PLAYER1, COLOR_PLAYER2, COLOR_VALID_MOVE,
    BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_MARGIN
)

# Additional GUI colors
COLOR_BUTTON = (100, 100, 100)
COLOR_BUTTON_HOVER = (120, 120, 120)
COLOR_TEXT = (255, 255, 255)
COLOR_TEXT_DARK = (51, 51, 51)
COLOR_TEXT_GRAY = (102, 102, 102)

# Fonts
FONT_LARGE = pygame.font.Font(None, 48)
FONT_TITLE = pygame.font.Font(None, 36)
FONT_MEDIUM = pygame.font.Font(None, 24)
FONT_SMALL = pygame.font.Font(None, 18)
FONT_BUTTON = pygame.font.Font(None, 20)

# Screen dimensions
MENU_WIDTH = 600
MENU_HEIGHT = 500

# Animation
AI_DELAY_MS = 500  # Delay before AI move for better UX
