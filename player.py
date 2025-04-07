import pygame


class Player:
    def __init__(self, floor_top):
        self.surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        self.rect = self.surface.get_rect(midbottom=(80, floor_top))
        self.gravity = 0
        self.floor_top = floor_top
        self.jump_gravity = -20
        self.move_speed = 4 
        
    def player_grav(self):
        self.gravity += 1 
        self.rect.y += self.gravity
        if self.rect.bottom >= self.floor_top:
            self.rect.bottom = self.floor_top
            
    def input(self, keys):
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            if self.rect.bottom >= self.floor_top:
                self.gravity = self.jump_gravity
        if keys[pygame.K_d]:
            self.rect.x += self.move_speed
        if keys[pygame.K_a]:
            self.rect.x -= self.move_speed
            
    def reset(self, keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
            
        if keys[pygame.K_r]:
            self.rect = self.rect
            
            
    def draw(self, screen):
        screen.blit(self.surface, self.rect)    
        
        