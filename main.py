import random

def get_value(grid: list[list[int|None]], pointer: int) -> int|None:
    return grid[pointer//9][pointer%9]

def set_value(grid: list[list[int|None]], pointer: int, value: int|None) -> None:
    grid[pointer//9][pointer%9] = value

def check_validity(grid: list[list[int|None]]) -> bool:
    for x in range(9):
        for y in range(9):
            cell = grid[x][y]
            if cell is not None:
                if any(grid[x][check_y] == cell and check_y != y for check_y in range(9)) or any(grid[check_x][y] == cell and check_x != x for check_x in range(9)) or any(grid[check_x][check_y] == cell and check_y != y and check_x != x for check_x in range((x//3)*3,(x//3)*3+3) for check_y in range((y//3)*3,(y//3)*3+3)):
                    return False
    return True

def print_grid(grid: list[list[int|None]]) -> None:
    for i, row in enumerate(grid):
        for j in range(3):
            print(*[str(cell) if isinstance(cell,int) else "?" for cell in row[j*3:j*3+3]],sep=" ",end="  ")
        print()
        if i%3 == 2: print()

def attempt(grid:list[list[int|None]], pointer: int) -> bool:
    unchecked: list[int] = [1,2,3,4,5,6,7,8,9]
    while True:
        cell = get_value(grid,pointer)
        if cell is None:
            value = random.choice(unchecked)
            unchecked.remove(value)
            set_value(grid,pointer,value)
        elif not check_validity(grid):
            if len(unchecked) != 0:
                value = random.choice(unchecked)
                unchecked.remove(value)
                set_value(grid,pointer,value)
            else:
                set_value(grid,pointer,None)
                return False
        else:
            if pointer < 9*9-1:
                if attempt(grid,pointer+1):
                    return True
                elif len(unchecked) > (1 if cell in unchecked else 0):
                    if cell in unchecked:
                        unchecked.remove(cell)
                    set_value(grid,pointer,random.choice(unchecked))
                else:
                    return False
            else:
                return True
    
def count_solutions(grid: list[list[int|None]], pointer:int = 0) -> int:
    cell = get_value(grid,pointer)
    if cell is None:
        solutions: int = 0
        cell = 0
        while cell < 9:
            cell += 1
            set_value(grid,pointer,cell)
            if check_validity(grid):
                if pointer < 9*9-1:
                    solutions += count_solutions(grid,pointer+1)
                    pass
                else:
                    solutions += 1
        set_value(grid, pointer, None)
        return solutions
    elif pointer < 9*9-1:
        return count_solutions(grid,pointer+1)
    else:
        assert check_validity(grid)
        set_value(grid, pointer, None)
        return 1


if __name__ == "__main__":
    grid:list[list[int|None]] = [[None for _ in range(9)] for _ in range(9)]
    pointer:int = 0
    original_value: int = 0
    attempt(grid,0)
    print_grid(grid)
    grid_copy = [[cell if i < 7 else None for i, cell in enumerate(row)] for row in grid]
    print_grid(grid_copy)
    print(count_solutions(grid_copy))