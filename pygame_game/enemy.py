import pygame
class Enemy():
    walk_right = [pygame.image.load('pygame_game\\resources\R1E.png'), pygame.image.load('pygame_game\\resources\R2E.png'), pygame.image.load('pygame_game\\resources\R3E.png'), pygame.image.load('pygame_game\\resources\R4E.png'), pygame.image.load('pygame_game\\resources\R5E.png'), pygame.image.load('pygame_game\\resources\R6E.png'), pygame.image.load('pygame_game\\resources\R7E.png'), pygame.image.load('pygame_game\\resources\R8E.png'), pygame.image.load('pygame_game\\resources\R9E.png'), pygame.image.load('pygame_game\\resources\R10E.png'), pygame.image.load('pygame_game\\resources\R11E.png')]
    walk_left  = [pygame.image.load('pygame_game\\resources\L1E.png'), pygame.image.load('pygame_game\\resources\L2E.png'), pygame.image.load('pygame_game\\resources\L3E.png'), pygame.image.load('pygame_game\\resources\L4E.png'), pygame.image.load('pygame_game\\resources\L5E.png'), pygame.image.load('pygame_game\\resources\L6E.png'), pygame.image.load('pygame_game\\resources\L7E.png'), pygame.image.load('pygame_game\\resources\L8E.png'), pygame.image.load('pygame_game\\resources\L9E.png'), pygame.image.load('pygame_game\\resources\L10E.png'), pygame.image.load('pygame_game\\resources\L11E.png')]
    
    def __init__(self,x,y,char_width,char_height,end):
        self.x = x
        self.y = y
        self.char_width = char_width
        self.char_height = char_height
        self.end = end
        self.walk_count = 0
        self.path = [self.x,self.end]
        self.vel = 3
        self.hitbox = (self.x + 17, self.y, 31, 60)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walk_count + 1 >= 33:
                self.walk_count = 0

            if self.vel > 0:
                win.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            else:
                win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            self.hitbox = (self.x + 17, self.y, 31, 60)
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-15,50 ,7))
            pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-15,self.health *5,7))
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walk_count = 0

    def hit(self):
        if self.health > 0 :
            self.health -= 1
            # self.visible = True
        else:
            self.visible = False
        print("hit")