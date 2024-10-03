import pygame
class Player:
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
        self.char = pygame.image.load('pygame_game\standing.png')
        self.walkRight = [pygame.image.load('pygame_game\R1.png'), pygame.image.load('pygame_game\R2.png'), pygame.image.load('pygame_game\R3.png'), pygame.image.load('pygame_game\R4.png'), pygame.image.load('pygame_game\R5.png'), pygame.image.load('pygame_game\R6.png'), pygame.image.load('pygame_game\R7.png'), pygame.image.load('pygame_game\R8.png'), pygame.image.load('pygame_game\R9.png')]
        self.walkLeft = [pygame.image.load('pygame_game\L1.png'), pygame.image.load('pygame_game\L2.png'), pygame.image.load('pygame_game\L3.png'), pygame.image.load('pygame_game\L4.png'), pygame.image.load('pygame_game\L5.png'), pygame.image.load('pygame_game\L6.png'), pygame.image.load('pygame_game\L7.png'), pygame.image.load('pygame_game\L8.png'), pygame.image.load('pygame_game\L9.png')]

    def draw(self,win):
        if self.walk_count +1 >= 27:
            self.walk_count = 0
        if self.left:
            win.blit(self.walkLeft[self.walk_count//3],(self.x,self.y))
            self.walk_count += 1
        elif self.right:
            win.blit(self.walkRight[self.walk_count//3],(self.x,self.y))
            self.walk_count += 1
        else:
            win.blit(self.char,(self.x,self.y))