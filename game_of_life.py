# copyright siavoosh payandeh azad 2017
# this is game of life with a glider as initial state
# if your system is not mac you need to change line 101 (clear command) accordingly

__author__ = 'siavoosh'

import time
import os


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
y_size = 20
steps = 100

dict_of_items = {}

# generating the items
for i in range(0, x_size):
    for j in range(0, y_size):
        dict_of_items[i + j * y_size] = Item(i, j, False)


# initializing the system

dict_of_items[397].life = True
dict_of_items[377].life = True
dict_of_items[357].life = True
dict_of_items[358].life = True
dict_of_items[379].life = True


# running it
k = 0
while (k < steps):
    next_dict = {}
    for item in dict_of_items.keys():
        x, y = dict_of_items[item].report_coordinate()
        locations = []
        if x != x_size -1 :
            locations.append(x + 1 + y_size * y)
            if y != y_size - 1:
                locations.append(x + 1 + y_size * (y + 1))
            if y != 0:
                locations.append(x + 1 + y_size * (y - 1))

        if x != 0:
            locations.append((x - 1) + y_size * y)
            if y != y_size - 1:
                locations.append(x - 1 + y_size * (y + 1))
            if y != 0:
                locations.append(x - 1 + y_size * (y - 1))

        if y != y_size - 1:
            locations.append(x + y_size * (y + 1))
        if y != 0:
            locations.append(x + y_size * (y - 1))

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

    string = ""
    for j in range(y_size-1, 0, -1):
        #string += str(y_size*j)
        for i in range(0, x_size):
            if dict_of_items[i + j*y_size].life:
                string += "* "
            else:
                string += "  "
        string += "\n"
    sys.stdout.write("\r"+string)
    time.sleep(0.05)
    clear = lambda: os.system('clear')
    clear()

    for item in dict_of_items.keys():
        dict_of_items[item].update_life(next_dict[item])
    k += 1
    next_dict = {}