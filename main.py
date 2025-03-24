import pygame
from sys import exit

def display_score():
    curent_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f"Score: {curent_time}", False, "black").convert()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)
    # print(curent_time)


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


player_surafce = pygame.image.load( "graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surafce.get_rect(midbottom=(80, 300))  # lager et rektangel runt player
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
    keys = pygame.key.get_pressed()
    
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        display_score()


        # Snail
        screen.blit(snail_surface, (snail_rec))  # viser snailen

        snail_rec.x -= 4
        if snail_rec.right <= 0:
            snail_rec.left = 800

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:<<<<<<<
            player_rect.bottom = 300
        screen.blit(player_surafce, (player_rect))

        # Movement
        

        if keys[pygame.K_SPACE]:
            if player_rect.bottom >= 300:
                player_gravity = -20

        if keys[pygame.K_w]:
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
        if player_rect.colliderect(snail_rec):
            game_active = False
            
            
    else:
        screen.fill("black")
        screen.blit(game_over_surface,(game_over_rec))
        
        
        if keys[pygame.K_r]:
            snail_rec = snail_surface.get_rect(midbottom=(800, 300)) 
            player_rect = player_surafce.get_rect(midbottom=(80, 300))
            start_time = int(pygame.time.get_ticks() / 1000) 
            game_active = True
            
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
            

    # "Config"
    pygame.display.update()  # Updates the screen
    clock.tick(60)  # 60 frames per second
