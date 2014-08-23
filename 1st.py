import random
print("Угадай какое число от 1 до 100 я загадал")
x = 0
s = 0
s = random.random()*100
x = input()
while x != s:
    x = int(x)
    s = int(s)
    if x > s:
        print("Слишком большое число!")
        x = input()
        continue
    if x < s:
        print("Слишком маленькое число!")
        x = input()
        continue
print("Ты угадал")
input()
