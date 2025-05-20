import pygame
import random
from sys import exit
from player import Player  # Import the Player class
from snail import Snail  # Import the Snail class
from db import *


# Game variables
floor_top = 300
snail_respawn = 800
screen_res = 800, 400
score_hit = 0

snail_spawn_speed = 3

# Creates a database if it doesnt exist

mycursor.execute("CREATE DATABASE IF NOT EXISTS Pygame")

mycursor.execute("USE Pygame")

# Creates Tabels.
mycursor.execute(""" CREATE TABLE IF NOT EXISTS USERS( 
                 score int(200) NOT NULL,
                 time_survived int(200) NOT NULL,
                 user varchar(20) NOT NULL )
                 """)





dbconn.commit()


# Makes the user have to enter ther name
username = input("Enter your name: ")
if username == "":
    game_active = False
else:
    game_active = True    




def display_score():
    score_surface = normal_font.render(f"Score: {score_hit}", False, "black").convert()
    score_rec = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rec)

def display_score_death():
    score_surface = normal_font.render(f"Score: {score_hit}", False, "white").convert()
    score_rec = score_surface.get_rect(center=(400, 100))
    screen.blit(score_surface, score_rec)
    
def display_leaderboard():
    sql_statement = "SELECT * FROM USERS ORDER BY score DESC LIMIT 10"  
    mycursor.execute(sql_statement)
    result = mycursor.fetchall()
    
    y_offset = 25 
    x_offset = 150  
    for index, row in enumerate(result):
        user, score = row[2], row[0]  
        leaderboard_text = f"{index + 1}. {user}: {score} pts"
        score_surface = mindre_font.render(leaderboard_text, False, "white").convert()
        score_rec = score_surface.get_rect(center=(x_offset, y_offset))
        screen.blit(score_surface, score_rec)
        y_offset += 40  # Move down for the next entry

def score_to_db():
    sql_statement = "INSERT INTO USERS (score, time_survived, user) VALUES (%s, %s, %s)"
    added_date = (score_hit, time_survived, username)
    mycursor.execute(sql_statement, added_date)






pygame.init()
screen = pygame.display.set_mode((screen_res))
pygame.display.set_caption("Learn Game")
clock = pygame.time.Clock()

#Fonts
normal_font = pygame.font.Font("font/Pixeltype.ttf", 50)
mindre_font = pygame.font.Font("font/Pixeltype.ttf", 25)



game_active = True
start_time = int(pygame.time.get_ticks() / 1000)  # Initialize start_time

# Background
sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# Text
game_over_surface = normal_font.render("Game Over", False, "white").convert()
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
            
        # If the player has killed 5 snails, increase the spawn speed of the snails
        if score_hit >= 5:
            snail_spawn_speed = random.uniform(1, 10)
        elif score_hit >= 15:
            snail_spawn_speed = random.uniform(1, 5)
        elif score_hit >= 30:
            snail_spawn_speed = random.uniform(1, 2)
            snail.snail_move = random.uniform(1, 5)

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
                    if player.rect.left <= snail.rect.right and player.rect.right > snail.rect.right: # Check if the player collides with the snail from the left side
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
        display_leaderboard()
        
        # Sending data to database 
        if not data_sent:
            time_survived = int(pygame.time.get_ticks() / 1000) - start_time
            score_to_db()
            
            
            
            dbconn.commit()
            
            if keys[pygame.K_l]:
                sql_statement = "SELECT * FROM USERS"
                mycursor.execute(sql_statement)
                result = mycursor.fetchall()
                print(result)
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