import pygame
from player import Player
from projectile import Projectile
from enemy import Enemy
pygame.init()
import time

pygame.display.set_caption('First Game')
screen_width = 500
screen_length = 480
win = pygame.display.set_mode((screen_width,screen_length))
clock = pygame.time.Clock()
bg = pygame.image.load('pygame_game\\resources\\bg.jpg')

#redraw screen function
def redraw_game_window():
    win.blit(bg,(0,0))
    man.draw(win)
    
    for bullet in bullets:
        bullet.draw(win)

    goblin.draw(win)
    pygame.display.update()

#main loop
man = Player(20,410,64,64)
bullets = []
goblin = Enemy(100,410,64,64,450)
shoot_loop = 0
score = 0
run = True
while run:
    clock.tick(27)
    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    #event for hitting the red "X" button to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                goblin.hit()
                bullets.pop(bullets.index(bullet))

        if  bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
        if man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1] and man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3]:
            goblin.hit()

    if keys[pygame.K_SPACE] and shoot_loop == 0:
        if man.left:
            direction = -1
        else:
            direction = 1
        
        if len(bullets) < 5:
            bullets.append(Projectile(round(man.x + man.char_width // 2), round(man.y + man.char_height // 2), 6, (255,0,0), direction))

        shoot_loop = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.char_width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walk_count = 0
    if not(man.is_jump):
        if keys[pygame.K_UP]:
            man.is_jump = True
            man.walk_count = 0
            man.right = False
            man.left = False
    else:
        neg = 1
        if man.jump_count >= -10:
            if man.jump_count < 0:
                neg = -1
            man.y -= (man.jump_count ** 2) * 0.5 * neg
            man.jump_count -= 1
        else:
            man.is_jump = False
            man.jump_count = 10
            
    redraw_game_window()

pygame.quit()