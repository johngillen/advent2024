f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

part1 = 0
part2 = 0

la, lb = [], []

for line in lines:
    a, b = map(int, line.split())
    la.append(a)
    lb.append(b)

la.sort()
lb.sort()

for a, b in zip(la, lb):
    part1 += abs(a - b)

for a in la:
    part2 += a * lb.count(a)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
