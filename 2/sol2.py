
f = open('gaver.txt', 'r')
ls = f.readlines()

count = 0
objects = 0
linesPerVerse = 2

for l in ls:
    if not "alv" in l:
        objects += 1
        if objects > 3:
            linesPerVerse += 1
        count += linesPerVerse
    else:
        if objects > 3:
            count += linesPerVerse + 1
        else:
            count += linesPerVerse

print(count)
