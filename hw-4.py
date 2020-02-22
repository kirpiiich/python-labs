import random

f = open('text.txt')
for line in f:
    list = line.split(' ')
print(list)
f.close()
list.reverse()
f = open('text.txt', 'a')
f.write('\n')
for i in list:
    f.write(i + ' ')
f.write(str(random.randint(10, 99)))
f.close()
a=input('Press any key to quit ')