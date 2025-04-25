import pygame
import random
from sys import exit
from player import Player  # Import the Player class
from snail import Snail  # Import the Snail class
from db import *

# Creates a database if it doesnt exist

# mycursor.execute("CREATE DATABASE IF NOT EXISTS Pygame")


# # Creates Tabels.
# mycursor.execute(""" CREATE TABLE IF NOT EXISTS USERS( 
#                  score int(200) NOT NULL,
#                  time_survived int(200) NOT NULL,
#                  user varchar(20) NOT NULL )
#                  """)

# for i in mycursor:
#     print(i)

# adding data

sql_statement = "INSERT INTO USERS (score, time_survived, user) VALUES (%s, %s, %s)"

dbconn.commit()

    




def display_score():
    score_surface = test_font.render(f"Score: {score_hit}", False, "black").convert()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)

def display_score_death():
    score_surface = test_font.render(f"Score: {score_hit}", False, "white").convert()
    score_rec = score_surface.get_rect(center=(400, 100))
    screen.blit(score_surface, score_rec)


# Game variables
floor_top = 300
snail_respawn = 800
screen_res = 800, 400
score_hit = 0

snail_spawn_speed = 3




pygame.init()
screen = pygame.display.set_mode((screen_res))
pygame.display.set_caption("Learn Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True
start_time = int(pygame.time.get_ticks() / 1000)  # Initialize start_time

# Background
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Text
game_over_surface = test_font.render("Game Over", False, "white").convert()
game_over_rec = game_over_surface.get_rect(center=(400, 50))

# Initialize classes
player = Player(floor_top)
snail_spawn_time = 0
snails = [Snail(floor_top)]

def new_func(player, snail):
    player.rect.bottom = snail.rect.top
    

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
                
    keys = pygame.key.get_pressed()
    

    if game_active:
        data_sent = False
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, floor_top))
        display_score()
        
    

        # Snail
        for snail in snails:
            snail.snail_move()
            snail.draw(screen)
            
        current_time = int(pygame.time.get_ticks() / 1000 ) 
        if current_time - snail_spawn_time >= snail_spawn_speed:
            snails.append(Snail(floor_top))
            snail_spawn_time = current_time
            
        if score_hit >= 5:
            snail_spawn_speed = random.uniform(1, 20)

        # print(snail_spawn_speed)
        
        for snail in snails:
            if player.rect.colliderect(snail.rect):
                
                if player.rect.bottom <= snail.rect.top + 20:
                    player.gravity -= 30
                    snails.remove(snail)
                    score_hit += 1
                else:
                    # Ends game 
                    if player.rect.right >= snail.rect.left and player.rect.left < snail.rect.left: # check if the player collides with the snail from the right side
                        game_active = False
                    if player.rect.left <= snail.rect.right and player.rect.right > snail.rect.right: 
                        game_active = False

        
        
        # Player
        player.player_grav()
        player.input(keys)
        player.draw(screen)
        player.border()


    else:
        screen.fill("black")
        screen.blit(game_over_surface, game_over_rec)
        display_score_death()
        
        # Sending data to database 
        if not data_sent:
            time_survived = int(pygame.time.get_ticks() / 1000) - start_time
            
            added_date = (score_hit, time_survived, "test")
            mycursor.execute(sql_statement, added_date)
            
            dbconn.commit()
            data_sent = True

    if keys[pygame.K_r]:
        snails = [Snail(floor_top)]
        player = Player(floor_top)
        start_time = int(pygame.time.get_ticks() / 1000)
        game_active = True
        score_hit = 0
        snail_spawn_time = 3
        snail_spawn_speed = 3
        data_sent = False
    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)