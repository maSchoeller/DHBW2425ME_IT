import random;

grid = []
ships =[3,3,5,2,1,5,4,2]

def render_grid(_grid):
    for _row in _grid:
        print(_row)

def place_ship_on_grid(_grid, ship, x_pos, y_pos, direction):
    ship_id = 0
    while ship_id < ship:
        match direction:
            case 'n':
                _grid[y_pos-ship_id][x_pos] = 'S'
            case 's':
                _grid[y_pos+ship_id][x_pos] = 'S'
            case 'w':
                _grid[y_pos][x_pos-ship_id] = 'S'
            case 'o':
                _grid[y_pos][x_pos+ship_id] = 'S'
        ship_id+=1

def is_area_free(_grid, x, y):
    # Prüft, ob das Feld (x, y) und alle angrenzenden Felder frei sind
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10:
                if _grid[ny][nx] != '~':
                    return False
    return True

def place_ships(_ships, _grid):
    directions = ['n','s','w','o']
    for ship in _ships:
        placed = False
        while not placed:
            x_pos = random.randint(0,9)
            y_pos = random.randint(0,9)
            direction = random.choice(directions)
            ship_place_is_ok = True
            coords = []
            match direction:
                case 'n':
                    if y_pos - ship + 1 < 0:
                        ship_place_is_ok = False
                    else:
                        for i in range(ship):
                            x, y = x_pos, y_pos - i
                            coords.append((x, y))
                case 's':
                    if y_pos + ship > 10:
                        ship_place_is_ok = False
                    else:
                        for i in range(ship):
                            x, y = x_pos, y_pos + i
                            coords.append((x, y))
                case 'w':
                    if x_pos - ship + 1 < 0:
                        ship_place_is_ok = False
                    else:
                        for i in range(ship):
                            x, y = x_pos - i, y_pos
                            coords.append((x, y))
                case 'o':
                    if x_pos + ship > 10:
                        ship_place_is_ok = False
                    else:
                        for i in range(ship):
                            x, y = x_pos + i, y_pos
                            coords.append((x, y))
            # Prüfe, ob alle Felder und angrenzenden Felder frei sind
            if ship_place_is_ok:
                for x, y in coords:
                    if not is_area_free(_grid, x, y):
                        ship_place_is_ok = False
                        break
            if ship_place_is_ok:
                place_ship_on_grid(_grid, ship, x_pos, y_pos, direction)
                placed = True



for i in range(10):
    row = []
    grid.append(row)
    for ii in range(10):
        row.append('~')

# render_grid(grid)
place_ships(ships,grid)
render_grid(grid)

