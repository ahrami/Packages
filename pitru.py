file = open('input.txt')
a = list()
for text in file:
    text = text[1: len(text)-1]
    a = text.split(sep = "', '")
a = a[len(a)//2:3*len(a)//4:3]
for book in a:
    print(book);
file.close()
