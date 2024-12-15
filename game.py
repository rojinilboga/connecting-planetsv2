import pgzrun
from random import randint
from time import time

WIDHT = 800
HEIGHT = 600


TITLE = "Connecting the planets"

#declearing variables
planets = []
lines = []
next_planet = 0

start_time = 0
total_time = 0
end_time = 0

number_of_planets = 8

def create_planets():
    global start_time
    for count in range(0,number_of_planets):
        planet = Actor("planet")
        planet.pos = randint(40, WIDHT - 40), randint(40, HEIGHT - 40)
        planets.append(planet)
    start_time = time()

def draw():
    global total_time
    number = 1
    for planet in planets:
        screen.draw.text(str(number), (planet.pos[0], planet.pos[1] + 25))
        planet.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))
    
    if next_planet < number_of_planets:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)

create_planets()
pgzrun.go()
    
    
