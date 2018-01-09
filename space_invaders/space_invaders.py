# copyright siavoosh payandeh azad 2017

import random
import time
import curses
import threading

class invader():
	x = None
	y = 0
	speed = 0

	def __init__(self, x, speed):
		self.x = x
		self.speed = speed

	def move(self):
		self.y += self.speed

	def update_speed(self, speedup):
		self.speed = slef.speed * speedup

	def report_y(self):
		return self.y

	def report_x(self):
		return self.x

class cannon():
	x = None 

	def __init__(self, x):
		self.x = x

	def move_right(self):
		self.x += 1

	def move_left(self):
		self.x -= 1

class missile():
	x = None 
	y = None

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def move(self):
		self.y -= 1


screen_x = 30
screen_y = 35
invader_width = 10
invader_length = 10

invaders_list = []
missile_list = []
lost = False
end = False

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

injection_counter = 0
injection_threshold = 50
level = 1

cannon = cannon(screen_x/2)
score = 0
kill_list = []
while not (lost or end):
	stdscr.nodelay(1)
	if injection_counter == injection_threshold:	
		injection_point = random.randint(invader_width/2, screen_x-(invader_width/2))
		new_invader = invader(injection_point, 1)
		invaders_list.append(new_invader)
		injection_counter = 0

	for i in range(0, screen_x):
		for j in range(0, screen_y):
			stdscr.addstr(j, i, " ")

	for missile_i in missile_list:
		stdscr.addstr(missile_i.y, missile_i.x, "^")

	for invader_i in invaders_list:
		if invader_i not in kill_list:
			if invader_i.y-2>0:
				stdscr.addstr(invader_i.y-2, invader_i.x-2, "*| |*")
			if invader_i.y-1>0:
				stdscr.addstr(invader_i.y-1, invader_i.x-1, "* *")
			stdscr.addstr(invader_i.y,   invader_i.x, "*")
		else:
			if invader_i.y-2>0:
				stdscr.addstr(invader_i.y-2,   invader_i.x-3, ".  *  .")
			if invader_i.y-1>0:
				stdscr.addstr(invader_i.y-1,   invader_i.x-3, ". * * .")
			stdscr.addstr(invader_i.y,   invader_i.x-2, ". * .")

	for invader_i in kill_list:
		if invader_i in invaders_list:
			invaders_list.remove(invader_i)

	stdscr.addstr(screen_y-2, cannon.x, " ||")
	stdscr.addstr(screen_y-1, cannon.x, "|**|")

	for missile_i  in missile_list:
		missile_i.move()

	kill_list = []
	dead_missile_list = []
	for invader_i in invaders_list:
		invader_i.move()
		if invader_i.report_y() == screen_y:
			lost = True
		for missile_i in missile_list:
			if invader_i.report_y()+1 >  missile_i.y > invader_i.report_y()-3:
				if invader_i.report_x()-3 < missile_i.x < invader_i.report_x()+3:
					score += 1
					kill_list.append(invader_i)
					dead_missile_list.append(missile_i)

	for missile_i in missile_list:
		if missile_i.y == 0:
			dead_missile_list.append(missile_i)

	for missile_i in dead_missile_list:
		if missile_i in missile_list:
			missile_list.remove(missile_i)

	stdscr.addstr(screen_y, 0, "."+"-"*(screen_x-2)+".")

	char = stdscr.getch()
	if char == curses.KEY_LEFT:
		if cannon.x-1 > 0:
			cannon.move_left()
	elif char == curses.KEY_RIGHT:
		if cannon.x+4 < screen_x:
			cannon.move_right()
	elif char == ord('e'):
		end = True
	elif char == ord('a'):
		new_missile = missile(cannon.x+1, screen_y-3)
		missile_list.append(new_missile)
 	
 	elif char == ord('p'):
 		char = " "
 		stdscr.addstr(int(screen_y/2)-1, int(screen_x/2)-10, "===================")
		stdscr.addstr(int(screen_y/2), int(screen_x/2)-10,   "=    Paused!      =")		
		stdscr.addstr(int(screen_y/2)+1, int(screen_x/2)-10, "===================")
 		while char != ord('p'):
 			char = stdscr.getch()

	stdscr.addstr(screen_y+1, 0, "| score:  "+'%5s' %str(score)+"              |")
	stdscr.addstr(screen_y+2, 0, "| level:  "+'%5s' %str(level)+"              |")
	stdscr.addstr(screen_y+3, 0, "| kills to next level: "+'%5s' %str((2*level)*10-score) +" |")
	stdscr.addstr(screen_y+4, 0, "-"*screen_x)
	stdscr.addstr(screen_y+5, 0, "Game Controls:")
	stdscr.addstr(screen_y+6, 0,  "  * Fire: \"a\"")
	stdscr.addstr(screen_y+7, 0,  "  * Move right: arrow keys ->")
	stdscr.addstr(screen_y+8, 0,  "  * Move left:  arrow keys <-")
	stdscr.addstr(screen_y+9, 0,  "  * Pause: \"p\"")
	stdscr.addstr(screen_y+10, 0, "  * End game: \"e\"")
	stdscr.addstr(screen_y+11, 0, "-"*screen_x)
	time.sleep(0.1)
	stdscr.refresh()

	injection_counter += 1 
	if score == (2*level)*10: 
		if injection_threshold >10:
			injection_threshold -= 5
		level +=1

for i in range(0, screen_x):
		for j in range(0, screen_y):
			stdscr.addstr(j, i, " ")
stdscr.refresh()
stdscr.addstr(int(screen_y/2)-1, int(screen_x/2)-10, "===================")
stdscr.addstr(int(screen_y/2)+1, int(screen_x/2)-10, "= your score:"+'%3s' %str(score)+"  =")
stdscr.addstr(int(screen_y/2)+2, int(screen_x/2)-10, "===================")
if lost:
	stdscr.addstr(int(screen_y/2), int(screen_x/2)-10,   "=    YOU LOST!    =")
else:
	stdscr.addstr(int(screen_y/2), int(screen_x/2)-10,   "=   GAME ENDED!   =")

stdscr.refresh()
time.sleep(5)
curses.echo()
curses.nocbreak()
curses.endwin()

