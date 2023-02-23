import random

window_width = 800
window_height = 460

speed = 20
speed_increase = 1

# snake
snake_size = 5
link_size = 20
snake_color = "BLUE"

# borders
borders = False
borders_color = "WHITE"
borders_width = 5

# background
background_color = "BLACK"

mode = "medium"

food_color = "green"

def change_color(obj):

    if obj == "snake":
        snake_color = random.choice(["BLUE","RED","GREEN","YELLOW","WHITE","BLACK"])
        return snake_color
    elif obj == "borders":
        borders_color = random.choice(["BLUE","RED","GREEN","YELLOW","WHITE","BLACK"])
        return borders_color
    elif obj == "background":
        background_color = random.choice(["BLUE","RED","GREEN","YELLOW","WHITE","BLACK"])
        return background_color
    elif obj == "food":
        food_color = random.choice(["BLUE","RED","GREEN","YELLOW","WHITE","BLACK"])
        return food_color
    
        


def hard():

    global speed
    speed = 20
    global speed_increase
    speed_increase = 2
    global link_size
    link_size = 20

def medium():

    global speed
    speed = 20
    global speed_increase
    speed_increase = 1
    global link_size
    link_size = 20

def easy():

    global speed
    speed = 10
    global speed_increase
    speed_increase = 0
    global snake_size
    snake_size = 10
    global link_size
    link_size = 20