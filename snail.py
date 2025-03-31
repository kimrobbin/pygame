import pygame

class Snail:
    
    def __init__(self, floor_top):
        self.surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
        self.rect = self.surface.get_rect(midbottom=(800, floor_top))
        self.respawn = self.surface.get_rect(midbottom=(800, floor_top))
        self.floor_top = floor_top
        self.move_speed = 4 
        
    def snail_move(self):
        self.rect.x -= self.move_speed
        if self.rect.right <= 0:
            self.rect.left = self.respawn.left
        
        
    def draw(self, screen):
        screen.blit(self.surface, self.rect)  
    
