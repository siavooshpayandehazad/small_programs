import curses
import time
import random

screen_size_x = 30
screen_size_y = 30

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

snake = [(screen_size_x/2, screen_size_y/2),(screen_size_x/2-1, screen_size_y/2), (screen_size_x/2-2, screen_size_y/2)]
lost = False
end  = False
direction =(+1,0)
counter = 0
food = []

while(not (end or lost)):
	stdscr.nodelay(1)
	for i in range(0, screen_size_x):
		for j in range(0, screen_size_y):
			stdscr.addstr(j,i, " ")
	stdscr.addstr(0,0, "-"*screen_size_x)

	for item in snake:
		stdscr.addstr(item[1],item[0], "*")

	if counter%50 == 0:
		x = random.randint(1,screen_size_x-1)
		y = random.randint(1,screen_size_y-1)
		food.append([x,y])

	for food_item in food:
		stdscr.addstr(food_item[1],food_item[0], "*")

	stdscr.addstr(screen_size_y,0, "-"*screen_size_x)

	

	char = stdscr.getch()
	if char == ord('e'):
		stdscr.addstr(screen_size_y/2,screen_size_x/2-5, "GAME ENDED!")
		end = True
	elif char == curses.KEY_LEFT:
		if direction in [(0,-1), (0,1)]:
			direction = (-1,0)
	elif char == curses.KEY_RIGHT:
		if direction in [(0,-1), (0,1)]:
			direction = (1,0)
	elif char == curses.KEY_UP:
		if direction in [(1,0), (-1,0)]:
			direction = (0,-1)
	elif char == curses.KEY_DOWN:
		if direction in [(1,0), (-1,0)]:
			direction = (0,1)
	
	snake_head = snake[0]
	for food_item in food:
		if snake_head[0]+direction[0] == food_item[0] and snake_head[1]+direction[1] == food_item[1]:
			food.remove(food_item)
			snake.insert(0,(snake[0][0]+direction[0],snake[0][1]+direction[1]))
			
	snake.insert(0,(snake[0][0]+direction[0],snake[0][1]+direction[1]))

	if snake[0] in snake[1:]:
		lost = True

	if snake[0][0]+direction[0]== screen_size_x+1:
		lost = True
	elif snake[0][0]+direction[0] == -1:
		lost = True
	elif snake[0][1]+direction[1] == -1:
		lost = True
	elif snake[0][1]+direction[1] == screen_size_y+1:
		lost = True
	del snake[-1]
	
	stdscr.addstr(screen_size_y+2,0, str(direction))
	stdscr.refresh()
	time.sleep(.2)
	counter += 1

if lost:
	stdscr.addstr(screen_size_y/2,screen_size_x/2-5, "YOU LOST!")
	stdscr.refresh()
	time.sleep(.2)
time.sleep(1)
curses.echo()
curses.nocbreak()
curses.endwin()
