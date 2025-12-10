import pygame
import time

from game.gameState import GameState
from game.pathFinding import Position
from gui.boardRenderer import BoardRenderer
from gui.constants import (
    COLOR_BACKGROUND, COLOR_BUTTON, COLOR_BUTTON_HOVER, COLOR_TEXT,
    COLOR_TEXT_DARK, COLOR_TEXT_GRAY, COLOR_PLAYER1, COLOR_PLAYER2,
    FONT_TITLE, FONT_MEDIUM, FONT_SMALL, FONT_BUTTON,
    AI_DELAY_MS, BUTTON_WIDTH, BUTTON_HEIGHT
)
from util.constants import (
    BOARD_SIZE, CELL_SIZE, WALL_THICKNESS, SIDEBAR_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT
)
from ai.easy_ai import EasyAI
from ai.medium_ai import MediumAI
from ai.hard_ai import HardAI

class GameScreen:
    
    def __init__(self, screen, mode, difficulty):
        self.screen = screen
        self.game_state = GameState(mode, difficulty)
        
        board_size = BOARD_SIZE * CELL_SIZE + (BOARD_SIZE + 1) * WALL_THICKNESS
        self.board_surface = pygame.Surface((board_size, board_size))
        self.renderer = BoardRenderer(self.board_surface)
        
        # AI player
        self.ai_player = None
        if mode == "human_vs_ai":
            if difficulty == "easy":
                self.ai_player = EasyAI(1)
            elif difficulty == "medium":
                self.ai_player = MediumAI(1)
            elif difficulty == "hard":
                self.ai_player = HardAI(1)
        
        # UI state
        self.return_to_menu = False
        self.ai_thinking = False
        self.ai_move_time = 0
        
        # Create buttons
        self.buttons = self._create_buttons()
    
    def _create_buttons(self):
        buttons = []
        button_x = BOARD_SIZE * CELL_SIZE + (BOARD_SIZE + 1) * WALL_THICKNESS + 25
        start_y = 350
        spacing = BUTTON_HEIGHT + 10
        
        class GameButton:
            def __init__(self, x, y, width, height, text, callback):
                self.rect = pygame.Rect(x, y, width, height)
                self.text = text
                self.callback = callback
                self.hovered = False
            
            def draw(self, surface, font):
                color = COLOR_BUTTON_HOVER if self.hovered else COLOR_BUTTON
                pygame.draw.rect(surface, color, self.rect, border_radius=5)
                text_surf = font.render(self.text, True, COLOR_TEXT)
                text_rect = text_surf.get_rect(center=self.rect.center)
                surface.blit(text_surf, text_rect)
            
            def handle_event(self, event):
                if event.type == pygame.MOUSEMOTION:
                    self.hovered = self.rect.collidepoint(event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.hovered:
                        self.callback()
                        return True
                return False
        
        buttons.append(GameButton(button_x, start_y, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Reset (R)", self.handle_reset))
        buttons.append(GameButton(button_x, start_y + spacing, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Undo (U)", self.handle_undo))
        buttons.append(GameButton(button_x, start_y + spacing * 2, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Redo (Y)", self.handle_redo))
        buttons.append(GameButton(button_x, start_y + spacing * 3, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Save (S)", self.handle_save))
        buttons.append(GameButton(button_x, start_y + spacing * 4, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Load (L)", self.handle_load))
        buttons.append(GameButton(button_x, start_y + spacing * 5, BUTTON_WIDTH, BUTTON_HEIGHT,
                                 "Main Menu", self.handle_menu))
        
        return buttons
    
    def handle_mouse_click(self, pos):
        if self.game_state.winner is not None:
            return
        
        if self.game_state.get_current_player().is_ai:
            return
        
        # Try to get cell position
        cell_pos = self._get_cell_from_mouse(pos)
        if cell_pos:
            self.game_state.move_pawn(cell_pos[0], cell_pos[1])
            return
        
        # Try to get wall position
        wall_pos = self._get_wall_from_mouse(pos)
        if wall_pos:
            self.game_state.place_wall(wall_pos[0], wall_pos[1], wall_pos[2])
    
    def handle_mouse_move(self, pos):
        wall_pos = self._get_wall_from_mouse(pos)
        self.renderer.set_wall_preview(wall_pos)
    
    def _get_cell_from_mouse(self, pos):
        mx, my = pos
        
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                cell_x = x * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
                cell_y = y * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
                
                if (cell_x <= mx < cell_x + CELL_SIZE and
                    cell_y <= my < cell_y + CELL_SIZE):
                    return (x, y)
        
        return None
    
    def _get_wall_from_mouse(self, pos):
        mx, my = pos
        threshold = WALL_THICKNESS + 5
        
        for y in range(BOARD_SIZE - 1):
            for x in range(BOARD_SIZE - 1):
                # Check horizontal wall
                h_x = x * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
                h_y = (y + 1) * (CELL_SIZE + WALL_THICKNESS)
                h_width = 2 * CELL_SIZE + WALL_THICKNESS
                
                if (h_x <= mx < h_x + h_width and
                    h_y - threshold <= my < h_y + WALL_THICKNESS + threshold):
                    return (x, y, True)
                
                # Check vertical wall
                v_x = (x + 1) * (CELL_SIZE + WALL_THICKNESS)
                v_y = y * (CELL_SIZE + WALL_THICKNESS) + WALL_THICKNESS
                v_height = 2 * CELL_SIZE + WALL_THICKNESS
                
                if (v_x - threshold <= mx < v_x + WALL_THICKNESS + threshold and
                    v_y <= my < v_y + v_height):
                    return (x, y, False)
        
        return None
    
    def handle_reset(self):
        self.game_state.reset_game()
    
    def handle_undo(self):
        self.game_state.undo()
    
    def handle_redo(self):
        self.game_state.redo()
    
    def handle_save(self):
        self.game_state.save_game()
    
    def handle_load(self):
        self.game_state.load_game()
    
    def handle_menu(self):
        self.return_to_menu = True
    
    def handle_key_press(self, key):
        if key == pygame.K_r:
            self.handle_reset()
        elif key == pygame.K_u:
            self.handle_undo()
        elif key == pygame.K_y:
            self.handle_redo()
        elif key == pygame.K_s:
            self.handle_save()
        elif key == pygame.K_l:
            self.handle_load()
        elif key == pygame.K_h:
            self.renderer.toggle_valid_moves()
    
    def process_ai_turn(self):
        if self.game_state.winner is not None:
            return
        
        current_player = self.game_state.get_current_player()
        if not current_player.is_ai:
            return
        
        if not self.ai_thinking:
            self.ai_thinking = True
            self.ai_move_time = pygame.time.get_ticks()
            return
        
        # Wait for delay
        if pygame.time.get_ticks() - self.ai_move_time < AI_DELAY_MS:
            return
        
        # Get and execute AI move
        ai_move = self.ai_player.get_move(self.game_state)
        if ai_move:
            if ai_move.type.value == "pawn":
                self.game_state.move_pawn(ai_move.x, ai_move.y)
            else:
                self.game_state.place_wall(ai_move.x, ai_move.y, ai_move.is_horizontal)
        
        self.ai_thinking = False
    
    def handle_event(self, event):
        # Check buttons first
        for button in self.buttons:
            if button.handle_event(event):
                return
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_click(event.pos)
        elif event.type == pygame.MOUSEMOTION:
            self.handle_mouse_move(event.pos)
        elif event.type == pygame.KEYDOWN:
            self.handle_key_press(event.key)
    
    def draw(self):
        self.screen.fill(COLOR_BACKGROUND)
        
        # Draw board
        self.renderer.render(self.game_state)
        self.screen.blit(self.board_surface, (0, 0))
        
        # Draw sidebar
        sidebar_x = BOARD_SIZE * CELL_SIZE + (BOARD_SIZE + 1) * WALL_THICKNESS
        
        # Title
        title = FONT_TITLE.render("QUORIDOR", True, COLOR_TEXT_DARK)
        self.screen.blit(title, (sidebar_x + 25, 20))
        
        # Player 1 info
        p1_label = FONT_MEDIUM.render("Player 1", True, COLOR_PLAYER1)
        self.screen.blit(p1_label, (sidebar_x + 25, 80))
        p1_walls = FONT_SMALL.render(f"Walls: {self.game_state.players[0].walls_remaining}",
                                     True, COLOR_TEXT_DARK)
        self.screen.blit(p1_walls, (sidebar_x + 25, 110))
        
        # Player 2 info
        p2_label = FONT_MEDIUM.render("Player 2", True, COLOR_PLAYER2)
        self.screen.blit(p2_label, (sidebar_x + 25, 160))
        p2_walls = FONT_SMALL.render(f"Walls: {self.game_state.players[1].walls_remaining}",
                                     True, COLOR_TEXT_DARK)
        self.screen.blit(p2_walls, (sidebar_x + 25, 190))
        
        # Turn indicator
        current_player = self.game_state.get_current_player()
        turn_color = COLOR_PLAYER1 if current_player.player_id == 0 else COLOR_PLAYER2
        turn_text = FONT_MEDIUM.render(f"Turn: Player {current_player.player_id + 1}",
                                       True, turn_color)
        self.screen.blit(turn_text, (sidebar_x + 25, 250))
        
        # Message
        message = FONT_SMALL.render(self.game_state.message, True, COLOR_TEXT_GRAY)
        self.screen.blit(message, (sidebar_x + 25, 290))
        
        # Buttons
        for button in self.buttons:
            button.draw(self.screen, FONT_BUTTON)
        
        pygame.display.flip()
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                self.handle_event(event)
            
            if self.return_to_menu:
                return True
            
            self.process_ai_turn()
            self.draw()
            clock.tick(60)
        
        return False
