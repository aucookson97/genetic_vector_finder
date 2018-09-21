import random
from pygame import Rect

MAX_BOX_SIZE = 30

class Map():

    boxes = []
    start = (0, 0)
    goal= (0, 0)

    def __init__(self, screen_size, density):
        
        for i in range(density):
            rect = Rect(random.randint(0, screen_size), random.randint(0, screen_size),
                        random.randint(10, MAX_BOX_SIZE), random.randint(10, MAX_BOX_SIZE))
            self.boxes.append(rect)

        self.start = (random.randint(0, screen_size), random.randint(0, screen_size))
        start_valid = True
        while (not start_valid):
            start_valid = True
            for b in boxes:
                if b.collidepoint(start):
                    start_valid = False
                    self.start = (random.randint(0, screen_size), random.randint(0, screen_size))
                    break

        self.goal = (random.randint(0, screen_size), random.randint(0, screen_size))
        goal_valid = True
        while (not goal_valid):
            goal_valid = True
            for b in boxes:
                if b.collidepoint(goal):
                    goal_valid = False
                    self.goal = (random.randint(0, screen_size), random.randint(0, screen_size))
                    break

        


