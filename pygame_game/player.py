import pygame
class Player:
    walk_right = [pygame.image.load('pygame_game\\resources\R1.png'), pygame.image.load('pygame_game\\resources\R2.png'), pygame.image.load('pygame_game\\resources\R3.png'), pygame.image.load('pygame_game\\resources\R4.png'), pygame.image.load('pygame_game\\resources\R5.png'), pygame.image.load('pygame_game\\resources\R6.png'), pygame.image.load('pygame_game\\resources\R7.png'), pygame.image.load('pygame_game\\resources\R8.png'), pygame.image.load('pygame_game\\resources\R9.png')]
    walk_left = [pygame.image.load('pygame_game\\resources\L1.png'), pygame.image.load('pygame_game\\resources\L2.png'), pygame.image.load('pygame_game\\resources\L3.png'), pygame.image.load('pygame_game\\resources\L4.png'), pygame.image.load('pygame_game\\resources\L5.png'), pygame.image.load('pygame_game\\resources\L6.png'), pygame.image.load('pygame_game\\resources\L7.png'), pygame.image.load('pygame_game\\resources\L8.png'), pygame.image.load('pygame_game\\resources\L9.png')]
    char = pygame.image.load('pygame_game\\resources\standing.png')
    def __init__(self,x,y,width,height):
        self.char_width = width
        self.char_height = height
        self.x = x
        self.y = y
        self.vel = 10
        self.is_jump = False
        self.jump_count = 10
        self.left= False
        self.right= False
        self.walk_count = 0
        self.standing = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self,win):
        if not(self.standing):
            if self.walk_count +1 >= 27:
                self.walk_count = 0
            if self.left:
                win.blit(self.walk_left[self.walk_count//3],(self.x,self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(self.walk_right[self.walk_count//3],(self.x,self.y))
                self.walk_count += 1
        else:
            if (self.right):
                win.blit(self.walk_right[0],(self.x,self.y))
            elif(self.left):
                win.blit(self.walk_left[0],(self.x,self.y))
            else:
                win.blit(self.char,(self.x,self.y))

        self.hitbox = (self.x +17 ,self.y + 11, 29, 52)
        # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

