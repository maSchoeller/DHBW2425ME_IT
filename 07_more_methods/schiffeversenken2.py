from random import randint


grid = [["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","#","~",],
        ["~","#","~","#","#","#","#","#","~","~",],
        ["~","#","~","~","~","~","~","~","~","~",],
        ["~","#","~","#","#","#","#","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","#","#","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","#","~","~","~","~","~","~",],
        ["~","~","~","~","~","~","~","~","~","~",],]
schiff_getroffen = "X"
wasser_getroffen = "O"
wasser = "~"
schiff = "#"


def render_grid(l_grid):
    for row in l_grid:
        for field in row:
            print(field,end="")
        print()

def shoot_on_board(l_grid):
    y = randint(0,9)
    x = randint(0,9)
    while l_grid[y][x] == schiff_getroffen or l_grid[y][x] == wasser_getroffen:
        y = randint(0,9)
        x = randint(0,9)
    return x,y

def check_end_game(l_grid : list[list[str]]):
    for row in l_grid:
        for field in row:
            if field == schiff:
                return False
    return True

render_grid(grid)
counter = 0
while not check_end_game(grid):
    x,y = shoot_on_board(grid)
    if grid[y][x] == schiff:
        grid[y][x] = schiff_getroffen
    if grid[y][x] == wasser:
        grid[y][x] = wasser_getroffen
    counter += 1
    render_grid(grid)
    print()

print(counter)