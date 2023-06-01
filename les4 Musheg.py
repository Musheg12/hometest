"""1. Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания,
если A < B, или в порядке убывания в противном случае."""
from typing import List

a, b = 12, 45
c = range(a, b+1)
r_c = []
for number in c:
    if a < b:
        r_c.append(number)
print(r_c)


"""2. Есть число n, вывести первые n чисел последовательности Фибоначчи."""
n = int(input("enter the number:"))
y = z = 1
while n < 100:
    n = y
    y = z
    z = n + y
    print(z)



"""3*. Дан список чисел. Реализуйте "bubble sort" для этого списка и верните, получившееся значение."""
numbers = [1, 25, 9, 6, 75, 12, 20]
numbers.sort()
print(numbers)

"""3*. Дан список чисел. Реализуйте "bubble sort" для этого списка и верните, получившееся значение."""
numbers_ = [1, 25, 6, 8, 12]
for i in range(len(numbers_)-1):
    print(f"compare {numbers_[i]} with {numbers_[i+1]}")
    if numbers_[i] > numbers_[i+1]:
        numbers_[i], numbers_[i+1] = numbers_[i+1], numbers_[i]
    print(numbers_)

"""4. Написать программу, которая будет конвертировать строку в CamelCase. Например: 
"the-stealth-warrior" -> "theStealthWarrior"  
"The_Stealth_Warrior" -> "TheStealthWarrior"  
"The_Stealth-Warrior" -> "TheStealthWarrior"""""

string = "the-stealth-warrior"
to_delete = "-_"
to_convert = "the-stealth-warrior"

for element in to_convert:
    if element in to_delete:
        to_convert = to_convert.replace(element, " ")

result = [[to_convert.split()[0]]]

for word in to_convert.split()[1:]:
    result.append(word.capitalize())
print("".join(result))