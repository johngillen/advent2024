import re

f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]
              
part1 = 0
part2 = 0

doing = True
for line in lines:
    matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
        
    for match in matches:
        doing = False if 'don\'t' in match else True if 'do' in match else doing
        if 'mul' in match:
            ints = re.findall(r'\d+', match)
            part1 += int(ints[0]) * int(ints[1])
            part2 += int(ints[0]) * int(ints[1]) if doing else 0
    
print(f'part 1: {part1}')
print(f'part 2: {part2}')
