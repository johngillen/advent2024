f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

grid = [[c for c in line] for line in lines]
translations = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

ok = lambda x, y: 0 <= x < len(grid) and 0 <= y < len(grid[x])

for x, row in enumerate(grid):
    for y, char in enumerate(row):
        if char == 'X':
            for dx, dy in translations:
                if ok(x + (1 * dx), y + (1 * dy)) and grid[x + (1 * dx)][y + (1 * dy)] == 'M' and \
                   ok(x + (2 * dx), y + (2 * dy)) and grid[x + (2 * dx)][y + (2 * dy)] == 'A' and \
                   ok(x + (3 * dx), y + (3 * dy)) and grid[x + (3 * dx)][y + (3 * dy)] == 'S':
                    part1 += 1
        
        if char == 'A':
            hits = 0
            for dx, dy in translations[4:]:
                nx, ny = dx * -1, dy * -1
                if ok(x + (1 * dx), y + (1 * dy)) and grid[x + (1 * dx)][y + (1 * dy)] == 'M' and \
                   ok(x + (1 * nx), y + (1 * ny)) and grid[x + (1 * nx)][y + (1 * ny)] == 'S':
                    hits += 1
            if hits == 2: part2 += 1

print(f'part 1: {part1}')
print(f'part 2: {part2}')
