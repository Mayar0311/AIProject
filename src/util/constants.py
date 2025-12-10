# Board dimensions
BOARD_SIZE = 9
CELL_SIZE = 60
WALL_THICKNESS = 10
WALL_LENGTH = 2

# Window dimensions
SIDEBAR_WIDTH = 250
WINDOW_WIDTH = BOARD_SIZE * CELL_SIZE + WALL_THICKNESS * (BOARD_SIZE + 1) + SIDEBAR_WIDTH
WINDOW_HEIGHT = BOARD_SIZE * CELL_SIZE + WALL_THICKNESS * (BOARD_SIZE + 1) + 100

# Game rules
WALLS_PER_PLAYER = 10
MIN_PLAYERS = 2
MAX_PLAYERS = 2

# Colors (RGB tuples)
COLOR_BACKGROUND = (240, 240, 240)
COLOR_BOARD = (255, 255, 255)
COLOR_GRID = (200, 200, 200)
COLOR_WALL = (139, 69, 19)
COLOR_WALL_PREVIEW = (139, 69, 19, 128)  # With alpha
COLOR_PLAYER1 = (255, 50, 50)
COLOR_PLAYER2 = (50, 50, 255)
COLOR_VALID_MOVE = (144, 238, 144, 102)  # With alpha

# Player starting positions (x, y)
PLAYER_STARTS = [
    (4, 0),  # Player 1 starts at top center
    (4, 8)   # Player 2 starts at bottom center
]

# Player goal rows
PLAYER_GOALS = [
    8,  # Player 1 aims for bottom row
    0   # Player 2 aims for top row
]

# Save directory
SAVE_DIR = "saves"

# UI
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 40
BUTTON_MARGIN = 10