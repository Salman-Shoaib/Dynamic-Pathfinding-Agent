import pygame
import random
import math
import time
from queue import PriorityQueue

# -------- USER INPUT --------
ROWS = int(input("Enter number of rows: "))
COLS = int(input("Enter number of columns: "))

WIDTH = 600
HEIGHT = 600
CELL = WIDTH // COLS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT+80))
pygame.display.set_caption("Dynamic Pathfinding Agent")

font = pygame.font.SysFont("Arial",18)

# -------- COLORS --------
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GRAY = (200,200,200)

# -------- GRID --------
grid = [[0 for j in range(COLS)] for i in range(ROWS)]

start = (0,0)
goal = (ROWS-1,COLS-1)

grid[start[0]][start[1]] = 2
grid[goal[0]][goal[1]] = 3

# -------- SETTINGS --------
algorithm = "astar"
heuristic_type = "manhattan"
dynamic_mode = False
spawn_probability = 0.05

nodes_visited = 0
path_cost = 0
exec_time = 0

# -------- HEURISTICS --------
def heuristic(a,b):

    x1,y1 = a
    x2,y2 = b

    if heuristic_type == "manhattan":
        return abs(x1-x2)+abs(y1-y2)

    if heuristic_type == "euclidean":
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# -------- NEIGHBORS --------
def neighbors(node):

    x,y = node
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    result = []

    for dx,dy in moves:
        nx = x+dx
        ny = y+dy

        if 0<=nx<ROWS and 0<=ny<COLS:
            if grid[nx][ny] != 1:
                result.append((nx,ny))

    return result

# -------- PATH RECONSTRUCT --------
def build_path(came_from,current):

    path = []

    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path

# -------- SEARCH --------
def search():

    global nodes_visited, exec_time

    start_time = time.time()

    open_set = PriorityQueue()
    open_set.put((0,start))

    came_from = {}

    g = {start:0}

    visited = set()

    frontier = set([start])

    while not open_set.empty():

        current = open_set.get()[1]

        frontier.discard(current)
        visited.add(current)

        nodes_visited += 1

        if current == goal:

            exec_time = (time.time()-start_time)*1000
            return build_path(came_from,current),visited,frontier

        for n in neighbors(current):

            new_cost = g[current] + 1

            if n not in g or new_cost < g[n]:

                g[n] = new_cost

                if algorithm == "gbfs":
                    f = heuristic(n,goal)
                else:
                    f = new_cost + heuristic(n,goal)

                open_set.put((f,n))

                frontier.add(n)

                came_from[n] = current

    exec_time = (time.time()-start_time)*1000
    return [],visited,frontier

# -------- RANDOM MAP --------
def random_map(density):

    for i in range(ROWS):
        for j in range(COLS):

            if (i,j)!=start and (i,j)!=goal:

                if random.random()<density:
                    grid[i][j]=1
                else:
                    grid[i][j]=0

# -------- DRAW GRID --------
def draw(path,visited,frontier):

    screen.fill(WHITE)

    for i in range(ROWS):
        for j in range(COLS):

            rect = pygame.Rect(j*CELL,i*CELL,CELL,CELL)

            if grid[i][j]==1:
                pygame.draw.rect(screen,BLACK,rect)

            if (i,j) in visited:
                pygame.draw.rect(screen,BLUE,rect)

            if (i,j) in frontier:
                pygame.draw.rect(screen,YELLOW,rect)

            if (i,j) in path:
                pygame.draw.rect(screen,GREEN,rect)

            if (i,j)==start:
                pygame.draw.rect(screen,(255,165,0),rect)

            if (i,j)==goal:
                pygame.draw.rect(screen,(128,0,128),rect)

            pygame.draw.rect(screen,GRAY,rect,1)

    text1 = font.render(f"Visited: {nodes_visited}",True,(0,0,0))
    text2 = font.render(f"Path Cost: {path_cost}",True,(0,0,0))
    text3 = font.render(f"Time(ms): {round(exec_time,2)}",True,(0,0,0))
    text4 = font.render(f"Algo:{algorithm}  Heuristic:{heuristic_type}  Dynamic:{dynamic_mode}",True,(0,0,0))

    screen.blit(text1,(10,610))
    screen.blit(text2,(160,610))
    screen.blit(text3,(300,610))
    screen.blit(text4,(10,640))

    pygame.display.update()

# -------- MAIN LOOP --------
running = True
path=[]
visited=set()
frontier=set()

agent = start
step = 0

while running:

    pygame.time.delay(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running=False

        if pygame.mouse.get_pressed()[0]:

            mx,my = pygame.mouse.get_pos()
            r = my//CELL
            c = mx//CELL

            if (r,c)!=start and (r,c)!=goal:
                grid[r][c] = 1-grid[r][c]

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                random_map(0.3)

            if event.key == pygame.K_1:
                algorithm="gbfs"

            if event.key == pygame.K_2:
                algorithm="astar"

            if event.key == pygame.K_m:
                heuristic_type="manhattan"

            if event.key == pygame.K_e:
                heuristic_type="euclidean"

            if event.key == pygame.K_d:
                dynamic_mode = not dynamic_mode

            if event.key == pygame.K_SPACE:

                nodes_visited=0
                path,visited,frontier = search()
                path_cost = len(path)

                agent = start
                step = 0

    # -------- AGENT MOVEMENT --------
    if step < len(path):

        agent = path[step]
        step+=1

        if dynamic_mode:

            if random.random() < spawn_probability:

                rx = random.randint(0,ROWS-1)
                ry = random.randint(0,COLS-1)

                if (rx,ry)!=goal and (rx,ry)!=agent:
                    grid[rx][ry] = 1

                    if (rx,ry) in path:

                        nodes_visited=0
                        path,visited,frontier = search()
                        step = 0

    draw(path,visited,frontier)

pygame.quit()