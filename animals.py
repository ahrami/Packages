file = open("animals.txt", "r")

males = set()
females = set()

animals = dict()

for line in file:
    args = line.split()
    if args[2] == 'male':
        males.add(args[1])
    if args[2] == 'female':
        females.add(args[1])
    if args[1] in animals:
        animals[args[1]] += 1
    else:
        animals[args[1]] = 1
file.close()

b = []
for a in males:
    if a in females:
        b.append(a)
        
print(sorted(b, key = lambda c: len(c)))

print(sorted(list(males.intersection(females)), key = lambda c: len(c)))

d = []
for a in animals:
    d.append((a, animals[a]))

print(list(reversed(sorted(d, key = lambda c: c[1]))))
