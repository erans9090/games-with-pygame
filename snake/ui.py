import os
import pygame
import properties
import Snake
import random
from sys import exit


class UI:
     
    def __init__(self,logger):

        self.logger = logger
        self.logger.log("UI: init")
        pygame.init()
        self.screen = pygame.display.set_mode((properties.window_width, properties.window_height))
        self.screen.fill(properties.background_color)
        pygame.display.set_caption("Snake")
        pygame.display.update()
        self.food = [random.randint(0,properties.window_width) - random.randint(0,properties.window_width)%10,random.randint(0,properties.window_height) - random.randint(0,properties.window_height)%10]
        self.snake = Snake.Snake(properties.window_width/2,properties.window_height/2)

    def main_menu(self):

        self.logger.log("UI: main_menu")

        self.draw_main_menu()
        
        # main menu loop
        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:                    

                    if properties.window_width//2 - 100 < pygame.mouse.get_pos()[0] < properties.window_width//2 + 100:
                        if properties.window_height//2 - 100 < pygame.mouse.get_pos()[1] < properties.window_height//2 - 20:
                            properties.hard()
                            self.logger.log("UI: GAME STARTED: hard")
                            return
                        elif properties.window_height//2 - 20 < pygame.mouse.get_pos()[1] < properties.window_height//2 + 60:
                            self.logger.log("UI: GAME STARTED: medium")
                            properties.medium()
                            return
                        elif properties.window_height//2 + 60 < pygame.mouse.get_pos()[1] < properties.window_height//2 + 140:
                            self.logger.log("UI: GAME STARTED: easy")
                            properties.easy()
                            return
                        elif properties.window_height//2 + 140 < pygame.mouse.get_pos()[1] < properties.window_height//2 + 220:
                            self.properties_menu()

                self.draw_main_menu()



    
    def draw_main_menu(self):

        self.screen.fill(properties.background_color)
        
        # level buttons
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 - 100, properties.window_width//4, properties.window_height//8))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 - 20, properties.window_width//4, properties.window_height//8))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 + 60, properties.window_width//4, properties.window_height//8))

        # properties button
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 + 140, properties.window_width//4, properties.window_height//8))


        header = pygame.font.SysFont("Arial", properties.window_width//12).render("Snake", True, "white")
        text = pygame.font.SysFont("Arial", properties.window_width//20).render("choose level", True, "white")
        easy = pygame.font.SysFont("Arial", properties.window_width//20).render("easy", True, "black")
        medium = pygame.font.SysFont("Arial", properties.window_width//20).render("medium", True, "black")
        hard = pygame.font.SysFont("Arial", properties.window_width//20).render("hard", True, "black")
        properties_button = pygame.font.SysFont("Arial", properties.window_width//20).render("properties", True, "black")

        self.screen.blit(easy, (properties.window_width//2 - 40 , properties.window_height//2 + 60))
        self.screen.blit(medium, (properties.window_width//2 - 60, properties.window_height//2 - 15))
        self.screen.blit(hard, (properties.window_width//2 - 40, properties.window_height//2 - 95))

        self.screen.blit(header, (properties.window_width//2 - 80 , properties.window_height//2 - 220))
        self.screen.blit(text, (properties.window_width//2 - 90 , properties.window_height//2 - 150))
        self.screen.blit(properties_button, (properties.window_width//2 - 75    , properties.window_height//2 + 145))

        pygame.display.update()

                        
    def properties_menu(self):

        self.logger.log("UI: properties_menu")

        # graphics
        self.draw_properties()
        
        # properties main loop
        while True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(properties.window_height//2 + 100)
                    print(properties.window_height//2 + 160)
                    print(pygame.mouse.get_pos())
                    if properties.window_width//2 - 100 < pygame.mouse.get_pos()[0] < properties.window_width//2 + 100:
                        if properties.window_height//2 - 100 < pygame.mouse.get_pos()[1] < properties.window_height//2 - 60:
                            properties.snake_color = properties.change_color("snake")
                            self.logger.log("UI: snake color changed to " + str(properties.snake_color))
                            self.properties_menu()
                            return 
                        elif properties.window_height//2 - 60 < pygame.mouse.get_pos()[1] < properties.window_height//2 - 20:
                            properties.food_color = properties.change_color("food")
                            self.logger.log("UI: food color changed to " + str(properties.food_color))
                            self.properties_menu()
                            return 
                        elif properties.window_height//2 - 20 < pygame.mouse.get_pos()[1] < properties.window_height//2 + 20:
                            properties.background_color = properties.change_color("background")
                            self.logger.log("UI: background color changed to " + str(properties.background_color))
                            self.properties_menu()
                            return 
                        # elif properties.window_height//2 + 20 < pygame.mouse.get_pos()[1] < properties.window_height//2 + 60:
                        #     out = True
                        #     break
                        elif properties.window_height//2 + 100 < pygame.mouse.get_pos()[1] < properties.window_height//2 + 160:
                            # out = True
                            self.logger.log("UI: properties menu closed")
                            return
                            # break





    def draw_properties(self):

        self.screen.fill(properties.background_color)
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 - 100, properties.window_width//5, properties.window_height//16))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 - 60, properties.window_width//5, properties.window_height//16))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 - 20, properties.window_width//5, properties.window_height//16))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 + 20, properties.window_width//5, properties.window_height//16))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 + 60, properties.window_width//5, properties.window_height//16))
        pygame.draw.rect(self.screen,"grey", (properties.window_width//2 - 100, properties.window_height//2 + 100, properties.window_width//5, properties.window_height//16))

        header = pygame.font.SysFont("Arial", properties.window_width//12).render("Properties", True, "white")
        snake_color = pygame.font.SysFont("Arial", properties.window_width//40).render("snake color", True, "black")
        snake_color_current = pygame.font.SysFont("Arial", properties.window_width//40).render(properties.snake_color, True, "white")
        food_color = pygame.font.SysFont("Arial", properties.window_width//40).render("food color", True, "black")
        food_color_current = pygame.font.SysFont("Arial", properties.window_width//40).render(properties.food_color, True, "white")
        background_color = pygame.font.SysFont("Arial", properties.window_width//40).render("background color", True, "black")
        background_color_current = pygame.font.SysFont("Arial", properties.window_width//40).render(properties.background_color, True, "white")
        return_button = pygame.font.SysFont("Arial", properties.window_width//40).render("return", True, "black")

        self.screen.blit(snake_color, (properties.window_width//2 - 95 , properties.window_height//2 - 100))
        self.screen.blit(snake_color_current, (properties.window_width//2 + 100 , properties.window_height//2 - 100))
        self.screen.blit(food_color, (properties.window_width//2 - 95 , properties.window_height//2 - 60))
        self.screen.blit(food_color_current, (properties.window_width//2 + 100 , properties.window_height//2 - 60))
        self.screen.blit(background_color, (properties.window_width//2 - 95 , properties.window_height//2 - 20))
        self.screen.blit(background_color_current, (properties.window_width//2 + 100 , properties.window_height//2 - 20))
        self.screen.blit(header, (properties.window_width//2 - 80 , properties.window_height//2 - 220))
        self.screen.blit(return_button, (properties.window_width//2 - 95 , properties.window_height//2 + 100))


        pygame.display.update()


    def gameover(self):

        
        self.handle_highscore(self.snake.score)
            
                
        print(self.snake.body)
        # text = pygame.font.SysFont("Arial", properties.window_width//12).render("Game Over", True, "grey")
        # self.screen.blit(text, (properties.window_width//2 - 90, properties.window_height//2 - properties.window_height//4))
        # score = pygame.font.SysFont("Arial", properties.window_width//20).render(f"Your score: {self.snake.score}", True, "grey")
        # highscore = pygame.font.SysFont("Arial", properties.window_width//20).render(f"Highscore: {highscore}", True, "grey")
        # self.screen.blit(score, (properties.window_width//2 - properties.window_width//4 , properties.window_height//2 - properties.window_height//12))
        # self.screen.blit(highscore, (properties.window_width//2 - properties.window_width//4 ,properties.window_height//2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        exit()

    def update_direction(self,key):

        # handle case direction changed but self.snake didn't move yet
        # happens when player presses two keys in the same frame
        tmp = self.snake.direction
        
        if key == pygame.K_UP:
            if self.snake.direction == Snake.Direction.DOWN or self.snake.last_direction == Snake.Direction.DOWN:
                return
            self.snake.direction = Snake.Direction.UP
        elif key == pygame.K_DOWN:
            if self.snake.direction == Snake.Direction.UP or self.snake.last_direction == Snake.Direction.UP:
                return
            self.snake.direction = Snake.Direction.DOWN
        elif key == pygame.K_LEFT:
            if self.snake.direction == Snake.Direction.RIGHT or self.snake.last_direction == Snake.Direction.RIGHT:
                return
            self.snake.direction = Snake.Direction.LEFT
        elif key == pygame.K_RIGHT:
            if self.snake.direction == Snake.Direction.LEFT or self.snake.last_direction == Snake.Direction.LEFT:
                return
            self.snake.direction = Snake.Direction.RIGHT

        self.snake.last_direction = tmp

    def is_food_eaten(self):
        if abs(self.snake.head[0] - self.food[0]) <= properties.link_size and abs(self.snake.head[1] - self.food[1]) <= properties.link_size:
            self.snake.score += 1
            self.logger.log(f"Score: {self.snake.score}")
            properties.speed += properties.speed_increase
            self.snake.body.append([self.snake.head[0],self.snake.head[1]])
            self.food = [random.randint(0,properties.window_width) - random.randint(0,properties.window_width)%10,random.randint(0,properties.window_height) - random.randint(0,properties.window_height)%10]

    def draw_snake(self):

        for i in self.snake.body:
            pygame.draw.rect(self.screen,properties.snake_color,(i[0],i[1],properties.link_size,properties.link_size))

    def draw_food(self):

        pygame.draw.rect(self.screen,properties.food_color,(self.food[0],self.food[1],properties.link_size,properties.link_size))   

    def draw_borders(self):

        pygame.draw.rect(self.screen,"grey",(0,0,properties.window_width,properties.borders_width))
        pygame.draw.rect(self.screen,"grey",(0,0,properties.borders_width,properties.window_height))
        pygame.draw.rect(self.screen,"grey",(0,properties.window_height-properties.borders_width,properties.window_width,properties.borders_width))
        pygame.draw.rect(self.screen,"grey",(properties.window_width-properties.borders_width,0,properties.borders_width,properties.window_height))

    def handle_highscore(self,score):

        if "highscore.txt" in os.listdir():
            with open("highscore.txt","r") as f:
                highscore = f.read().split(" ")
                highscore[1] = int(highscore[1])
                print("highscore: ",highscore[0], " - ",highscore[1])

        else:
            highscore = ["",0]

        if self.snake.score > highscore[1]:

            # get name of player
            name = ""
            out = False
            while True:

                if out:
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            out = True
                            break
                        elif event.key == pygame.K_BACKSPACE:
                            name = name[:-1]

                        else:
                            name += event.unicode

                self.screen.fill("black")
                txt = pygame.font.SysFont("Arial", properties.window_width//20).render(f"New Highscore!  {score}", True, "grey")
                self.screen.blit(txt, (properties.window_width//2 - properties.window_width//4 ,properties.window_height//2 - properties.window_height//12))
                txt = pygame.font.SysFont("Arial", properties.window_width//20).render(f"Your Name: {name}", True, "grey")
                self.screen.blit(txt, (properties.window_width//2 - properties.window_width//4 ,properties.window_height//2))
                pygame.display.update()

            with open("highscore.txt","w") as f:
                record = f"{name} {score}"
                f.write(record) 


        else:

            txt = pygame.font.SysFont("Arial", properties.window_width//20).render("Game Over", True, "grey")
            self.screen.blit(txt, (properties.window_width//2 - properties.window_width//4 ,properties.window_height//2 - properties.window_height//12))
            txt = pygame.font.SysFont("Arial", properties.window_width//20).render(f"Your Score: {score}", True, "grey")
            self.screen.blit(txt, (properties.window_width//2 - properties.window_width//4 ,properties.window_height//2))
            txt = pygame.font.SysFont("Arial", properties.window_width//20).render(f"Highscore: {highscore[0]}:  {highscore[1]}", True, "grey")
            self.screen.blit(txt, (properties.window_width//2 - properties.window_width//4 ,properties.window_height//2 + properties.window_height//12))
            pygame.display.update()

        
        