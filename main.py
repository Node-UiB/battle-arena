import pygame
from BattleArena import BattleArena
from Constants import Constants as con


def main():
    pygame.init()

    size = (con.SCREEN_WIDTH, con.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Battle Arena")
    pygame.mouse.set_visible(False)

    done = False
    clock = pygame.time.Clock()

    arena = BattleArena()
    # Main game loop
    while not done:
        # Process events
        done = arena.process_events()

        # Update object positions, check for collisions
        arena.run_logic()

        # Draw the current frame
        arena.display_frame(screen)

        # Pause for the next frame
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
