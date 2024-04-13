import pygame
import random

pygame.init()
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,255,0)
green = (0,0,255)

screen_width = 1000
screen_height =600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake Master")
pygame.display.update()
clock = pygame.time.Clock()



text_font = pygame.font.SysFont("Comic Sans MS",40,)
def text_on_screen(text,color,x,y):
    screen_text = text_font.render(text,True,color)
    gameWindow.blit(screen_text,(x,y))


def plot_snake(gameWindow,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])

def game_loop():
    speed = [0, 5]
    exit_game = False
    game_over = False
    snake_x = 250
    snake_y = 250
    snake_size = 20
    fps = 60
    v_x = 0
    v_y = 0
    food_x = random.randint(40, (int)(screen_width / 1.25))
    food_y = random.randint(40, (int)(screen_height / 1.25))
    score = 0
    snk_list = []
    snk_length = 1
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_on_screen("Game Over! Press Enter To Continue",red,115,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if v_x != -speed[1]:
                            v_x = speed[1]
                            v_y = speed[0]
                    if event.key == pygame.K_LEFT:
                        if v_x != speed[1]:
                            v_x = -speed[1]
                            v_y = speed[0]
                    if event.key == pygame.K_UP:
                        if v_y != speed[1]:
                            v_y = -speed[1]
                            v_x = speed[0]
                    if event.key == pygame.K_DOWN:
                        if v_y != -speed[1]:
                            v_y = speed[1]
                            v_x = speed[0]

            snake_x = snake_x +v_x
            snake_y += v_y



            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True
            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score +=10
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length +=5

            x_pos = head[0]
            y_pos = head[1]
            if (x_pos >= 1000 or x_pos <=0) or (y_pos >= 600 or y_pos <=0):
                game_over = True

            #print(snk_list)
            gameWindow.fill(white)
            text_on_screen("Score = "+ str(score),green,10,10)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            plot_snake(gameWindow,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
game_loop()
