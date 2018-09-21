import time
import Screen as screen
import Map

screen_size = 300

map_class = Map.Map(screen_size, 10)

def init():
    screen.init(400)
    pass

def run():

    solved = False
    while not solved:
        screen.update(map_class)
        time.sleep(1)
        
    quit()
    sys.exit()


if __name__=="__main__":
    init()
    run()
