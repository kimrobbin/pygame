import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Score: {current_time}", False, "black").convert()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)
    # print(current_time)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Learn Game")  # navn på vinduet
clock = pygame.time.Clock()  # for fps cap
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = 0

 # Background
sky_surface = pygame.image.load("graphics/sky.png").convert()  # Load the image

ground_surface = pygame.image.load("graphics/ground.png").convert() # .convert() gjør at det er lettere å jobbe med for pygame

# Text 


game_over_surface = test_font.render("Game Over",False, "white").convert()
game_over_rec = game_over_surface.get_rect(center=(400, 50))
# Enteties 
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rec = snail_surface.get_rect(midbottom=(600, 300))

snail_surface2 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rec2 = snail_surface2.get_rect(midbottom=(800, 300))


player_surface = pygame.image.load( "graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))  # lager et rektangel runt player
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        display_score()

        # Snail
        screen.blit(snail_surface, (snail_rec))  # viser snailen
        snail_rec.x -= display_score
        if snail_rec.right <= 0:
            snail_rec.left = 800

        # Additional snail after 30 seconds
        if int(pygame.time.get_ticks() / 1000) - start_time >= 30:
            screen.blit(snail_surface2, (snail_rec2))  # viser den andre snailen
            snail_rec2.x -= 4
            if snail_rec2.right <= 0:
                snail_rec2.left = 800

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, (player_rect))

        # Movement
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            if player_rect.bottom >= 300:
                player_gravity = -20

        if keys[pygame.K_d]:
            player_rect.x += 4

        if keys[pygame.K_a]:
            player_rect.x -= 4
            
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
            
        # End game
        if player_rect.colliderect(snail_rec) or player_rect.colliderect(snail_rec2):
            game_active = False
        
            
    else:
        screen.fill("black")
        screen.blit(game_over_surface,(game_over_rec))
        
         
        if keys[pygame.K_r]:
            snail_rec = snail_surface.get_rect(midbottom=(800, 300)) 
            player_rect = player_surface.get_rect(midbottom=(80, 300))
            start_time = int(pygame.time.get_ticks() / 1000) 
            game_active = True
            
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
            

    # "Config"
    pygame.display.update()  # Updates the screen
    clock.tick(60)  # 60 frames per second