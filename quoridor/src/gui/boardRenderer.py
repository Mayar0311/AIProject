import pygame
from util.constants import (
    BOARD_SIZE, CELL_SIZE, WALL_THICKNESS,
    COLOR_BACKGROUND, COLOR_BOARD, COLOR_GRID, COLOR_WALL, COLOR_VALID_MOVE
)


class BoardRenderer:
    
    def __init__(self, surface):
        self.surface = surface
        self.wall_preview = None
        self.show_valid_moves = False
    
    def render(self, game_state):
        self.draw_board()
        self.draw_walls(game_state.board)
        
        if self.show_valid_moves and not game_state.get_current_player().is_ai:
            self.highlight_valid_moves(game_state.get_valid_moves())
        
        if self.wall_preview:
            self.draw_wall_preview(self.wall_preview[0], self.wall_preview[1], self.wall_preview[2])
        
        self.draw_pawns(game_state.players)
    
    def draw_board(self):
        # Background
        self.surface.fill(COLOR_BACKGROUND)
        
        # Board background
        board_size = BOARD_SIZE * CELL_SIZE + (BOARD_SIZE + 1) * WALL_THICKNESS
        pygame.draw.rect(self.surface, COLOR_BOARD, (0, 0, board_size, board_size))
        
        # Grid lines
        for i in range(BOARD_SIZE + 1):
            pos = i * (CELL_SIZE + WALL_THICKNESS)
            # Vertical lines
            pygame.draw.rect(self.surface, COLOR_GRID,
                           (pos, 0, WALL_THICKNESS, board_size))
            # Horizontal lines
            pygame.draw.rect(self.surface, COLOR_GRID,
                           (0, pos, board_size, WALL_THICKNESS))
    
    def draw_pawns(self, players):
        for player in players:
            pixel_x = player.x * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS + CELL_SIZE // 2
            pixel_y = player.y * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS + CELL_SIZE // 2
            radius = CELL_SIZE // 3
            
            # Fill
            pygame.draw.circle(self.surface, player.color, (pixel_x, pixel_y), radius)
            
            # Outline
            pygame.draw.circle(self.surface, (0, 0, 0), (pixel_x, pixel_y), radius, 2)
    
    def draw_walls(self, board):
        # Horizontal walls
        for y in range(BOARD_SIZE - 1):
            for x in range(BOARD_SIZE - 1):
                if board.horizontal_walls[y][x]:
                    pixel_x = x * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
                    pixel_y = (y + 1) * (CELL_SIZE + WALL_THICKNESS)
                    width = 2 * CELL_SIZE + WALL_THICKNESS
                    pygame.draw.rect(self.surface, COLOR_WALL,
                                   (pixel_x, pixel_y, width, WALL_THICKNESS))
        
        # Vertical walls
        for y in range(BOARD_SIZE - 1):
            for x in range(BOARD_SIZE - 1):
                if board.vertical_walls[y][x]:
                    pixel_x = (x + 1) * (CELL_SIZE + WALL_THICKNESS)
                    pixel_y = y * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
                    height = 2 * CELL_SIZE + WALL_THICKNESS
                    pygame.draw.rect(self.surface, COLOR_WALL,
                                   (pixel_x, pixel_y, WALL_THICKNESS, height))
    
    def draw_wall_preview(self, x, y, is_horizontal):
        # Create semi-transparent surface
        preview_color = (*COLOR_WALL, 128)
        
        if is_horizontal:
            pixel_x = x * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
            pixel_y = (y + 1) * (CELL_SIZE + WALL_THICKNESS)
            width = 2 * CELL_SIZE + WALL_THICKNESS
            
            # Draw with alpha
            s = pygame.Surface((width, WALL_THICKNESS), pygame.SRCALPHA)
            s.fill(preview_color)
            self.surface.blit(s, (pixel_x, pixel_y))
        else:
            pixel_x = (x + 1) * (CELL_SIZE + WALL_THICKNESS)
            pixel_y = y * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
            height = 2 * CELL_SIZE + WALL_THICKNESS
            
            # Draw with alpha
            s = pygame.Surface((WALL_THICKNESS, height), pygame.SRCALPHA)
            s.fill(preview_color)
            self.surface.blit(s, (pixel_x, pixel_y))
    
    def highlight_valid_moves(self, valid_moves):
        highlight_color = (*COLOR_VALID_MOVE[:3], 102)
        
        for pos in valid_moves:
            pixel_x = pos.x * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
            pixel_y = pos.y * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
            
            # Draw with alpha
            s = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            s.fill(highlight_color)
            self.surface.blit(s, (pixel_x, pixel_y))
    
    def set_wall_preview(self, preview):
        self.wall_preview = preview
    
    def toggle_valid_moves(self):
        self.show_valid_moves = not self.show_valid_moves
