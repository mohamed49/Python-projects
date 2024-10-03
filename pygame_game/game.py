import pygame
from player import Player
pygame.init()

pygame.display.set_caption('First Game')
screen_width = 500
screen_length = 480
win = pygame.display.set_mode((screen_width,screen_length))
clock = pygame.time.Clock()
bg = pygame.image.load('pygame_game\\bg.jpg')

#redraw screen function
def redraw_game_window():
    win.blit(bg,(0,0))
    man.draw(win)
    pygame.display.update()

#main loop
man = Player(20,410,64,64)
run = True
while run:
    clock.tick(27)

    #event for hitting the red "X" button to quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screen_length - man.char_height - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
    else:
        man.left = False
        man.right = False
        man.walk_count = 0
    if not(man.is_jump):
        if keys[pygame.K_SPACE]:
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