import pygame
from Constants import Constants as con
from classes.AgentTemplate import AgentTemplate


class BattleArena(object):
    def __init__(self) -> None:
        self.game_over = False

        # Create spritelist
        self.agent_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create players

        self.player = AgentTemplate(0, self.all_sprites_list, self.bullet_list)
        self.agent_list.add(self.player)
        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.shoot()
            # Other events

        return False

    def run_logic(self):
        if not self.game_over:
            # Move all sprites
            self.all_sprites_list.update()

            # Check for collisions

            # player colides with bullet,
            # False: does not remove bullet from sprite list
            bullet_collision = pygame.sprite.spritecollide(
                self.player, self.bullet_list, False
            )

            # for bullet in bullet_collision:
            #     print("Player got hit")

            # Update on collisions

            # If one player left
            # game over

            if self.agent_list.__len__() == 0:
                self.game_over = True

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
