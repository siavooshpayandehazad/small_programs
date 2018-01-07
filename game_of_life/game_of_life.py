# copyright siavoosh payandeh azad 2017

import time
import curses
from math import log10, ceil


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

x_size = 20
y_size = 30
steps = 100

dict_of_items = {}

# generating the items
for i in range(0, x_size):
    for j in range(0, y_size):
        dict_of_items[i + j * x_size] = Item(i, j, False)



# initializing the system

# glider
"""
dict_of_items[397].life = True
dict_of_items[377].life = True
dict_of_items[357].life = True
dict_of_items[358].life = True
dict_of_items[379].life = True
"""


# Exploder
dict_of_items[308].life = True
dict_of_items[310].life = True
dict_of_items[312].life = True
dict_of_items[288].life = True
dict_of_items[292].life = True
dict_of_items[268].life = True
dict_of_items[272].life = True
dict_of_items[248].life = True
dict_of_items[252].life = True
dict_of_items[228].life = True
dict_of_items[230].life = True
dict_of_items[232].life = True

"""
# small exploder
dict_of_items[290].life = True
dict_of_items[291].life = True
dict_of_items[292].life = True
dict_of_items[311].life = True
dict_of_items[270].life = True
dict_of_items[272].life = True
dict_of_items[251].life = True
"""

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
    for i in range(1, number_of_digits):
        stdscr.addstr(number_of_digits-i, 0,"      ")
        for k in range(0, x_size):
            if len(str(k)) >= i:
                stdscr.addstr(number_of_digits-i, k+6, str(k)[len(str(k))-i])
            else:
                stdscr.addstr(number_of_digits-i, k+6, "0")


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
    time.sleep(0.5)
    stdscr.refresh()

    for item in dict_of_items.keys():
        dict_of_items[item].update_life(next_dict[item])
    k += 1
    next_dict = {}


curses.echo()
curses.nocbreak()
curses.endwin()
