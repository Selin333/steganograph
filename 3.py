file_name = "C:\\Users\\Gdl\\Desktop\\ВКБ\\Сафарьян\\3\\text.txt"
file_text = open(file_name, "r",encoding='utf8')
lines = file_text.readlines()


bits = []
da = []
no = []


for i in range(len(lines)):
    linia = []
    a = lines[i].split(" ")
    b = [''.join([l for l in x if l.isalpha()]) for x in a]
    b = list(filter(None, b))
    print(b)
    c = len(lines[i])

    countchet = 0
    countnechet = 0
    for j in b:
        o = len(j)

        if o % 2 == 0:
            countchet = countchet + 1
        else:
            countnechet = countnechet + 1

    if countchet >= countnechet and c % 2 ==0:
        bits.append(1)
        print(len(lines[i]))
        print("Строка", i+1, "- Да:", lines[i])

    else:
        bits.append(0)
        print(len(lines[i]))

        print("Строка", i+1, "- Нет:", lines[i])



print(bits)
print(f'\nДа: {bits.count(1)}\nНет: {bits.count(0)}')
