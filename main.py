import random

grid:list[list[int|None]] = [[None for _ in range(9)] for _ in range(9)]

def get_value(pointer:int) -> int|None:
    return grid[pointer//9][pointer%9]

def set_value(pointer:int, value: int|None) -> None:
    grid[pointer//9][pointer%9] = value

def check_validity() -> bool:
    for x in range(9):
        for y in range(9):
            cell = grid[x][y]
            if cell is not None:
                if any(grid[x][check_y] == cell and check_y != y for check_y in range(9)) or any(grid[check_x][y] == cell and check_x != x for check_x in range(9)) or any(grid[check_x][check_y] == cell and check_y != y and check_x != x for check_x in range((x//3)*3,(x//3)*3+3) for check_y in range((y//3)*3,(y//3)*3+3)):
                    return False
    return True

def print_grid() -> None:
    for i, row in enumerate(grid):
        for j in range(3):
            print(*[str(cell) for cell in row[j*3:j*3+3]],sep=" ",end="  ")
        print()
        if i%3 == 2: print()

def attempt(pointer:int) -> bool:
    original_value: int = 0
    blacklist: set[int] = set()
    while True:
        cell = get_value(pointer)
        if cell is None:
            original_value = random.randint(1,9)
            set_value(pointer,original_value)
        elif not check_validity():
            if (cell%9)+1 in blacklist and (cell%9)+1 != original_value:
                cell = (cell%9)+1
            if (cell%9)+1 != original_value:
                set_value(pointer,(cell%9)+1)
            else:
                set_value(pointer,None)
                return False
        else:
            if pointer < 9*9-1:
                if attempt(pointer+1):
                    return True
                else:
                    blacklist.add(cell)
                    set_value(pointer,(cell%9)+1)
            else:
                return True
            

pointer:int = 0
original_value: int = 0

attempt(0)
        
print_grid()