"""Conway's Game of Live
The classic cellular automata simulation.
Press Ctrl-C to stop.
"""

import copy, random, sys, time

#Set up the constants:
WIDTH = 79 #The width of the cell grid
HEIGHT = 20 #The height of the cell grid
ALIVE = '0' #The character representing a living cell
DEAD = ' ' #The character representing a dead cell

#The cells and nextCells are dictionaries for the state of the game.
#Their keys are (x, y) tuples and their values are one of the ALIVE/DEAD.

nextCells = {}

#Adjust percentage of starting active cells
while True:
    percentage = int(input("Choose how many % of active "
                   "cells should be placed as a starter (range 10-90): %"))
    if percentage in range(10,91):
        break
    else:
        print("Invalid input. % Range should be between 10-90%.")

alive_percentage = percentage
dead_percentage = 100 - alive_percentage
alive_percentage_range = [1 for i in range(alive_percentage//10)]
dead_percentage_range = [0 for i in range(dead_percentage//10)]
alive_percentage_range.extend(dead_percentage_range)

#Put random dead and alive cells into nextCells:
for x in range(WIDTH):
    for y in range(HEIGHT):
        #Chosen % chances for starting cells being alive/dead
        if random.choice(alive_percentage_range) == 1:
            nextCells[(x,y)] = ALIVE #Add living cell
        else:
            nextCells[(x,y)] = DEAD #Add dead cell

while True: #Main program loop
    #Each iteration of this loop is a step of the simulation
    print('\n' * 50) #Separate each step with newlines
    cells = copy.deepcopy(nextCells)

    #Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)],end='') #Print the 0 or space
        print() #Print a newline at the end of the row
    print("Press Ctrl-C to quit.")

    #Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #Get the neighboring coordinates of (x,y), even if
            #they wrap around the edge
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            #Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left,above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left,y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[right, below] == ALIVE:
                numNeighbors += 1

            #Set cell based on Conway's Game of Life rules:
            if cells[(x,y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbors stay alive:
                nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbors == 3:
                #Dead cells with 3 neighbors become alive:
                nextCells[(x,y)] = ALIVE
            else:
                #Everything else dies or stays dead
                nextCells[(x,y)] = DEAD

    try:
        time.sleep(1) #Add a 1 second pause to reduce flickering
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        print("By Al Sweigart")
        sys.exit() #When Ctrl-C is pressed, end the program




