import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption('First Game')

run = True
clock = pygame.time.Clock()
walkRight = [pygame.image.load('pygame_game\R1.png'), pygame.image.load('pygame_game\R2.png'), pygame.image.load('pygame_game\R3.png'), pygame.image.load('pygame_game\R4.png'), pygame.image.load('pygame_game\R5.png'), pygame.image.load('pygame_game\R6.png'), pygame.image.load('pygame_game\R7.png'), pygame.image.load('pygame_game\R8.png'), pygame.image.load('pygame_game\R9.png')]
walkLeft = [pygame.image.load('pygame_game\L1.png'), pygame.image.load('pygame_game\L2.png'), pygame.image.load('pygame_game\L3.png'), pygame.image.load('pygame_game\L4.png'), pygame.image.load('pygame_game\L5.png'), pygame.image.load('pygame_game\L6.png'), pygame.image.load('pygame_game\L7.png'), pygame.image.load('pygame_game\L8.png'), pygame.image.load('pygame_game\L9.png')]
bg = pygame.image.load('pygame_game\\bg.jpg')
char = pygame.image.load('pygame_game\standing.png')
screen_width = 500
screen_length = 480
char_width = 64
char_height =64
x = 20
y = 400
vel = 10
is_jump = False
jump_count = 10
left= False
right= False
walk_count = 0

#redraw screen function
def redraw_game_window():
    global walk_count
    win.blit(bg,(0,0))
    
    if walk_count +1 >= 27:
        walk_count = 0
    
    if left:
        win.blit(walkLeft[walk_count//3],(x,y))
        walk_count += 1
    elif right:
        win.blit(walkRight[walk_count//3],(x,y))
        walk_count += 1
    else:
        win.blit(char,(x,y))
    pygame.display.update()

#main loop
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screen_length - char_height - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walk_count = 0
    if not(is_jump):
        if keys[pygame.K_SPACE]:
            is_jump = True
            walk_count = 0
            right = False
            left = False
    else:
        neg = 1
        if jump_count >= -10:
            if jump_count < 0:
                neg = -1
            y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 10
    redraw_game_window()

pygame.quit()