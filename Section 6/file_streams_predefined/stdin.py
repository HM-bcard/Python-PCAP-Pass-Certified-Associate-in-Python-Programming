import sys

for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    print(line)

print('Since You pressed "q" the program is going to shut off')