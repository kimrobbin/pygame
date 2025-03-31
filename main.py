import pygame
import asyncio
from sys import exit
from player import Player  # Import the Player class
from snail import Snail  # Import the Snail class

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, "black").convert()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)

floor_top = 300
snail_respawn = 800
screen_res = 800, 400

pygame.init()
screen = pygame.display.set_mode((screen_res))
pygame.display.set_caption("Learn Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True

# Background
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Text
game_over_surface = test_font.render("Game Over", False, "white").convert()
game_over_rec = game_over_surface.get_rect(center=(400, 50))

    # Initialize classes
player = Player(floor_top)
snail = Snail(floor_top)

start_time = int(pygame.time.get_ticks() / 1000)
snail_spawn_time = 0
snails = [Snail(floor_top)]

async def main():
    
    while True:  # Correctly indented
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()

        if game_active:
            screen.blit(sky_surface, (0, 0))
            screen.blit(ground_surface, (0, floor_top))
            display_score()

            # Snail
            for snail in snails:
                snail.snail_move()
                snail.draw(screen)

         
            current_time = int(pygame.time.get_ticks() / 1000)
            if current_time - snail_spawn_time >= 63:
                snails.append(Snail(floor_top))
                snail_spawn_time = current_time

            # for snail in snails:
            #     snail.move_speed += 1
            #     snail.snail_move()
            #     print(snail.snail_move)

            # Player
            player.player_grav()
            player.input(keys)
            player.draw(screen)
            player.reset(keys)

            # End game
            if any(player.rect.colliderect(snail) for snail in snails):
                game_active = False

        else:
            screen.fill("black")
            screen.blit(game_over_surface, game_over_rec)

            if keys[pygame.K_r]:
                snails = [Snail(floor_top)]
                player = Player(floor_top)
                start_time = int(pygame.time.get_ticks() / 1000)
                game_active = True

            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)  # Allow the event loop to process other tasks

# Run the async main function
asyncio.run(main())