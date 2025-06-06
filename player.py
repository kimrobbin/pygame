import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, floor_top):
        super().__init__()
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
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            if self.rect.bottom >= self.floor_top:
                self.gravity = self.jump_gravity
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.move_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.move_speed
        
     
     
    # Makes a boder so player cant leave the screen        
    def border (self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 800:
            self.rect.right = 800
            
            
            
    def reset(self, keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
            
        if keys[pygame.K_r]:
            self.rect = self.rect
            
            
    def draw(self, screen):
        screen.blit(self.surface, self.rect)

