a = input()
b = a[::-1]
print(b)

a = input()
b = []
for i in range(0, len(a)):
    if a[i] == '"':
        b.append(i)
if len(b) > 1:
    for i in range(0, len(b)//2):
        print(a[b[i]+1:b[i+1]])

print(int(input())*2)

a = input()
c = 0
for i in range(0, len(a)):
    if a[i] == ' ':
        c = i
        break
b = a[c+1:] + ' ' + a[:c]
print(b)