import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


# direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# iniciando o pygame
pygame.init()

# criando a tela
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')


snake = [(200,200), (210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))
my_direction = LEFT


apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill((255,255,255))


clock = pygame.time.Clock()


# laço do jogo
while True:
    clock.tick(20)

    # pegando os eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            #fecha o jogo
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == k_UP:
                my_direction = UP
            if event.key == k_DOWN:
                my_direction = DOWN
            if event.key == k_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT 
    

    #testando colisao
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))


    # movendo a snake
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN :
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0]  + 10, snake[0][1])
    if my_direction == UP:
        snake[0] = (snake[0][0]  - 10, snake[0][1])



    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #limpa a tela
    screen.fill((0,0,0))
    #cria maça
    screen.blit(apple, apple_pos)
    
    # cria snake 
    for pos in snake:
        screen.blit(snake_skin,pos)



    pygame.display.update()