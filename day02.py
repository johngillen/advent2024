f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

for line in lines:
    ints = list(map(int, line.split()))
    
    for a, b in zip(ints, ints[1:]):
        if 1 > abs(a - b) or abs(a - b) > 3: break
    else:
        if ints == sorted(ints) or ints == sorted(ints)[::-1]:
            part1 += 1
            part2 += 1
            continue

    for i, _ in enumerate(ints):
        tmp = ints.copy()
        tmp.pop(i)
        for a, b in zip(tmp, tmp[1:]):
            if 1 > abs(a - b) or abs(a - b) > 3: break
        else:
            if tmp == sorted(tmp) or tmp == sorted(tmp)[::-1]:
                part2 += 1
                break

print(f'part 1: {part1}')
print(f'part 2: {part2}')
