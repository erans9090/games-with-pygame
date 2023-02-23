import properties
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Snake:

    def __init__(self,i,j) -> None:
        
        self.head = [i , j]
        self.body = [[i-x*properties.link_size,j] for x in range(properties.snake_size)]
        self.last_direction = None
        self.direction = Direction.RIGHT
        self.score = 0

    def gameover(self):

        if self.head in self.body[1:]:  
            return True
        if properties.borders:
            if self.head[1] > properties.window_height - properties.borders_width or self.head[0] < properties.borders_width:
                print(self.head[0])

                return True
        
    def move_snake(self):

        if self.direction == Direction.UP and self.last_direction != Direction.DOWN:
            self.moveup()
        elif self.direction == Direction.DOWN and self.last_direction != Direction.UP:
            self.movedown()
        elif self.direction == Direction.LEFT and self.last_direction != Direction.RIGHT:
            self.moveleft()
        elif self.direction == Direction.RIGHT and self.last_direction != Direction.LEFT:
            self.moveright()
        
        self.last_direction = None

        if self.head[0] > properties.window_width - properties.link_size:
            self.head[0] = 0
        
        if self.head[0] < 0:
            self.head[0] = properties.window_width

        if self.head[1] > properties.window_height - properties.link_size:
            self.head[1] = 0
        
        if self.head[1] < 0:
            self.head[1] = properties.window_height

    

    
    def moveup(self):

        self.body.insert(0,[self.head[0],self.head[1]-properties.link_size])
        self.head = self.body[0]
        self.body.pop()
    
    def movedown(self):

        self.body.insert(0,[self.head[0],self.head[1]+properties.link_size])
        self.head = self.body[0]
        self.body.pop()
    
    def moveleft(self):

        self.body.insert(0,[self.head[0]-properties.link_size,self.head[1]])
        self.head = self.body[0]
        self.body.pop()
    
    def moveright(self):
            
        self.body.insert(0,[self.head[0]+properties.link_size,self.head[1]])
        self.head = self.body[0]
        self.body.pop()



