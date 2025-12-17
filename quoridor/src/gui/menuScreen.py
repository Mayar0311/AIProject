import pygame
from gui.constants import (
    MENU_WIDTH, MENU_HEIGHT,
    COLOR_BACKGROUND, COLOR_BUTTON, COLOR_BUTTON_HOVER, COLOR_TEXT, COLOR_TEXT_DARK,
    FONT_LARGE, FONT_TITLE, BUTTON_WIDTH, BUTTON_HEIGHT
)

class Button:

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

class MenuScreen:

    def __init__(self, screen):
        self.screen = screen
        self.buttons = []
        self.selected_mode = None
        self.selected_difficulty = None
        
        # Create buttons with dynamic width based on text
        button_texts = [
            ("2 Players", "human_vs_human", None),
            ("Human vs AI (Easy)", "human_vs_ai", "easy"),
            ("Human vs AI (Medium)", "human_vs_ai", "medium"),
            ("Human vs AI (Hard)", "human_vs_ai", "hard")
        ]
        
        start_y = 200
        spacing = BUTTON_HEIGHT + 20
        padding = 40  # Horizontal padding for text
        
        for i, (text, mode, difficulty) in enumerate(button_texts):
            # Calculate button width based on text
            text_surf = FONT_TITLE.render(text, True, COLOR_TEXT)
            button_width = text_surf.get_width() + padding
            button_x = (MENU_WIDTH - button_width) // 2
            
            self.buttons.append(Button(
                button_x, start_y + i * spacing, button_width, BUTTON_HEIGHT,
                text,
                lambda m=mode, d=difficulty: self.start_game(m, d)
            ))
    
    def start_game(self, mode, difficulty):
        self.selected_mode = mode
        self.selected_difficulty = difficulty
    
    def handle_event(self, event):
        for button in self.buttons:
            if button.handle_event(event):
                return True
        return False
    
    def draw(self):
        self.screen.fill(COLOR_BACKGROUND)
        
        # Title
        title = FONT_LARGE.render("QUORIDOR", True, COLOR_TEXT_DARK)
        title_rect = title.get_rect(center=(MENU_WIDTH // 2, 80))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = FONT_TITLE.render("Select Game Mode", True, (102, 102, 102))
        subtitle_rect = subtitle.get_rect(center=(MENU_WIDTH // 2, 140))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Buttons
        for button in self.buttons:
            button.draw(self.screen, FONT_TITLE)
        
        pygame.display.flip()
    
    def run(self):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None, None
                
                self.handle_event(event)
                
                if self.selected_mode:
                    return self.selected_mode, self.selected_difficulty
            
            self.draw()
            clock.tick(60)
        
        return None, None
