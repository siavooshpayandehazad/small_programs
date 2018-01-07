# copyright siavoosh payandeh azad 2017

import time
import curses
from math import log10, ceil
import sys

class Item():
    x = None
    y = None
    life = False

    def __init__(self, x, y, life):
        self.x = x
        self.y = y
        self.life = life

    def update_life(self, life):
        self.life = life
        return None

    def report_coordinate(self):
        return self.x, self.y





# initializing the system
if "--help" in sys.argv[1:]:
    print "welcome to the terminal based Game of Life!"
    print "----------------------------"
    print "here are the program arguments:"
    print "\t\033[93m\033[1m-steps\033[0m           sets the number of steps that the program will run!"
    print "\t\033[93m\033[1m-x\033[0m               sets the horizontal size of the screen"
    print "\t\033[93m\033[1m-y\033[0m               sets the vertical size of the screen"
    print "\t\033[93m\033[1m-glider\033[0m          initializes the glider"
    print "\t\033[93m\033[1m-exploder\033[0m        initializes the exploder"
    print "\t\033[93m\033[1m-small_exploder\033[0m  initializes the small_exploder"
    sys.exit()
if "-steps" in sys.argv[1:]:
    steps = int(sys.argv[sys.argv.index("-steps")+1])
else:
    steps = 100

if "-x" in sys.argv[1:]:
    x_size = int(sys.argv[sys.argv.index("-x")+1])
else:
    x_size = 30

if "-y" in sys.argv[1:]:
    y_size = int(sys.argv[sys.argv.index("-y")+1])
else:
    y_size = 20

center_x = int(ceil(x_size/2))
center_y = int(ceil(y_size/2))

dict_of_items = {}

# generating the items
for i in range(0, x_size):
    for j in range(0, y_size):
        dict_of_items[i + j * x_size] = Item(i, j, False)


if "-glider" in sys.argv[1:]:
    # glider
    dict_of_items[center_x+ (center_y+2)*x_size].life = True 
    dict_of_items[center_x+ (center_y+1)*x_size].life = True 
    dict_of_items[center_x+ (center_y+1)*x_size+2].life = True 
    dict_of_items[center_x+ center_y*x_size].life = True 
    dict_of_items[center_x+ center_y*x_size+1].life = True 

elif "-exploder" in sys.argv[1:]:
    # Exploder
    dict_of_items[center_x+ (center_y+1)*x_size-4].life = True 
    dict_of_items[center_x+ center_y*x_size-4].life = True 
    dict_of_items[center_x+ center_y*x_size].life = True 
    dict_of_items[center_x+ (center_y+1)*x_size].life = True 
    dict_of_items[center_x+ (center_y+2)*x_size].life = True 
    dict_of_items[center_x+ (center_y+2)*x_size-2].life = True 
    dict_of_items[center_x+ (center_y+2)*x_size-4].life = True 
    dict_of_items[center_x+ (center_y-1)*x_size].life = True 
    dict_of_items[center_x+ (center_y-1)*x_size-4].life = True 
    dict_of_items[center_x+ (center_y-2)*x_size].life = True 
    dict_of_items[center_x+ (center_y-2)*x_size-2].life = True 
    dict_of_items[center_x+ (center_y-2)*x_size-4].life = True 

elif "-small_exploder" in sys.argv[1:]:
    # small exploder
    dict_of_items[center_x+(center_y+1)*x_size].life = True
    dict_of_items[center_x+(center_y+1)*x_size+1].life = True
    dict_of_items[center_x+(center_y+1)*x_size+2].life = True
    dict_of_items[center_x+(center_y+2)*x_size+1].life = True
    dict_of_items[center_x+ center_y*x_size].life = True
    dict_of_items[center_x+ center_y*x_size+2].life = True
    dict_of_items[center_x+(center_y-1)*x_size+1].life = True


# running it
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

k = 0
while (k < steps):
    next_dict = {}
    for item in dict_of_items.keys():
        x, y = dict_of_items[item].report_coordinate()
        locations = []
        if x != x_size -1 :
            locations.append(x + 1 + x_size * y)
            if y != y_size - 1:
                locations.append(x + 1 + x_size * (y + 1))
            if y != 0:
                locations.append(x + 1 + x_size * (y - 1))

        if x != 0:
            locations.append((x - 1) + x_size * y)
            if y != y_size - 1:
                locations.append(x - 1 + x_size * (y + 1))
            if y != 0:
                locations.append(x - 1 + x_size * (y - 1))

        if y != y_size - 1:
            locations.append(x + x_size * (y + 1))
        if y != 0:
            locations.append(x + x_size * (y - 1))

        alive_around = 0
        for loc in locations:
            if loc in dict_of_items.keys():
                if dict_of_items[loc].life:
                    alive_around += 1

        # print y, x, locations, alive_around
        if (dict_of_items[item].life == True) and (alive_around == 2 or alive_around == 3):
            next_dict[item] = True
        else:
            next_dict[item] = False

        if (not dict_of_items[item].life) and alive_around == 3:
            next_dict[item] = True

    number_of_digits = int(ceil(log10(x_size)))+1 
    stdscr.addstr(0, 0,"step: "+'%5s' % str(k))
    for m in range(1, number_of_digits):
        stdscr.addstr(number_of_digits-m, 0,"      ")
        for l in range(0, x_size):
            if len(str(l)) >= m:
                stdscr.addstr(number_of_digits-m, l+6, str(l)[len(str(l))-m])
            else:
                stdscr.addstr(number_of_digits-m, l+6, "0")

    stdscr.addstr(number_of_digits, 0, "     |"+"-"*x_size+"|")
    string = ""
    for j in range(y_size-1, -1, -1):
        #string += str(y_size*j)
        stdscr.addstr(j+1+number_of_digits, 0, '%5s' % j + "|")
        for i in range(0, x_size):
            if dict_of_items[i + j*x_size].life:
                stdscr.addstr(j+1+number_of_digits, i+6, "*")
            else:
                stdscr.addstr(j+1+number_of_digits, i+6, " ")
        string += "\n"
        stdscr.addstr(j+1+number_of_digits, x_size+6, "|")
    stdscr.addstr(y_size+number_of_digits, 0, "     |"+"-"*x_size+"|")
    time.sleep(0.1)
    stdscr.refresh()

    for item in dict_of_items.keys():
        dict_of_items[item].update_life(next_dict[item])
    k += 1
    next_dict = {}
    

curses.echo()
curses.nocbreak()
curses.endwin()
