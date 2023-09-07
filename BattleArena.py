import pygame
from Constants import Constants as con
from players.PlayerTemplate import PlayerTemplate


class BattleArena(object):
    def __init__(self) -> None:
        self.game_over = False

        # Create spritelist
        self.player_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create players

        player = PlayerTemplate()
        self.player_list.add(player)
        self.all_sprites_list.add(player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
            # Other events

        return False

    def run_logic(self):
        if not self.game_over:
            # Move all sprites
            self.all_sprites_list.update()

            # Check for collisions

            # Update on collisions

            # If one player left
            # game over

    def display_frame(self, screen):
        """Display everything to the screen for the game."""
        screen.fill(con.WHITE)

        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game over, player n won", True, con.BLACK)
            center_x = (con.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (con.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, (center_x, center_y))

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()
