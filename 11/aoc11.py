import copy


PUZZLE_INPUT = 'aoc11-data'
EMPTY = 'L'
OCCUPIED = '#'
DIRECTIONS = [
    {'x': 0, 'y': -1},  # N
    {'x': 1, 'y': -1},  # NE
    {'x': 1, 'y': 0},   # E
    {'x': 1, 'y': 1},   # SE
    {'x': 0, 'y': 1},   # S
    {'x': -1, 'y': 1},  # SW
    {'x': -1, 'y': 0},  # W
    {'x': -1, 'y': -1}  # NW
]


def get_seat_layout() -> list:
    with open(PUZZLE_INPUT, 'r') as f:
        data = f.read().split('\n')
    return [list(line) for line in data]


def get_settled_layout(layout: list) -> list:
    working_layout = copy.deepcopy(layout)
    last_layout = None
    while last_layout != working_layout:
        last_layout = copy.deepcopy(working_layout)
        for row_number, row in enumerate(last_layout):
            for col_number, seat in enumerate(row):
                if seat == EMPTY and get_adjacent_occupied_seats(last_layout, col_number, row_number) == 0:
                    working_layout[row_number][col_number] = OCCUPIED
                if seat == OCCUPIED and get_adjacent_occupied_seats(last_layout, col_number, row_number) >= 4:
                    working_layout[row_number][col_number] = EMPTY
    return working_layout


def get_adjacent_occupied_seats(layout: list, x: int, y: int) -> int:
    width, height = len(layout[0]), len(layout)
    adjacent_occupied_seats = 0
    for direction in DIRECTIONS:
        adjacent_x, adjacent_y = x + direction['x'], y + direction['y']
        if 0 <= adjacent_x < width and 0 <= adjacent_y < height and layout[adjacent_y][adjacent_x] == OCCUPIED:
            adjacent_occupied_seats += 1
    return adjacent_occupied_seats


def get_occupied_seats(layout: list) -> int:
    occupied_seats = 0
    for row in layout:
        occupied_seats += row.count(OCCUPIED)
    return occupied_seats


def get_settled_layout_from_a_distance(layout: list) -> list:
    working_layout = copy.deepcopy(layout)
    last_layout = None
    while last_layout != working_layout:
        last_layout = copy.deepcopy(working_layout)
        for row_number, row in enumerate(last_layout):
            for col_number, seat in enumerate(row):
                if seat == EMPTY and get_visible_occupied_seats(last_layout, col_number, row_number) == 0:
                    working_layout[row_number][col_number] = OCCUPIED
                if seat == OCCUPIED and get_visible_occupied_seats(last_layout, col_number, row_number) >= 5:
                    working_layout[row_number][col_number] = EMPTY
    return working_layout


def get_visible_occupied_seats(layout: list, x: int, y: int) -> int:
    width, height = len(layout[0]), len(layout)
    visible_occupied_seats = 0
    for direction in DIRECTIONS:
        x_sight, y_sight = x + direction['x'], y + direction['y']
        while 0 <= x_sight < width and 0 <= y_sight < height:
            visible_square = layout[y_sight][x_sight]
            if visible_square == OCCUPIED:
                visible_occupied_seats += 1
                break
            if visible_square == EMPTY:
                break
            x_sight += direction['x']
            y_sight += direction['y']
    return visible_occupied_seats


if __name__ == "__main__":
    seat_layout = get_seat_layout()
    settled_layout = get_settled_layout(seat_layout)
    print(get_occupied_seats(settled_layout))
    settled_layout_from_a_distance = get_settled_layout_from_a_distance(seat_layout)
    print(get_occupied_seats(settled_layout_from_a_distance))
