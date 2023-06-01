
"""1. Напишите функцию, которая принимает список чисел и возвращает список квадратов этих чисел."""
def set_number(s):
    print([i ** 2 for i in s])
set_number([1, 2, 3])

"""2. Напишите функцию, которая принимает на вход список строк и возвращает список строк,  
длина которых больше 5 символов."""
lst_1 = ['qwerty', 'python', 'son', 'hello']
lst = []
def functions(lst):
    for q in lst_1:
       if len(q) > 5:
            lst.append(q)
    return lst
print(functions(lst))
functions(lst)

"""3. Напишите функцию, которая принимает на вход список чисел и возвращает только четные числа из этого списка."""
division = []
def fun(division):
    nums = [34, 89, 56, 90, 11, 27, 16, 13, 53]
    for w in nums:
        if w % 2 == 0:
            division.append(w)
    return division
print(fun(division))
fun(division)

"""4. Напишите функцию, которая принимает на вход список чисел и возвращает сумму
 квадратов четных чисел из этого списка."""
ns = [6, 89, 2, 10, 11, 27, 8, 13, 53]
def sum_nums_Q():
    nums_Q = [num ** 2 for num in ns if num % 2 == 0]
    return sum(nums_Q)
print(sum_nums_Q())
sum_nums_Q()

"""5. Напишите функцию, которая принимает на вход список строк и возвращает список строк,
 которые начинаются с буквы "a"."""
def f():
    a = ['Alexander', 'Katy', 'Andrew', 'Elena', 'arduino', 'Elizabeth', 'Brain']
    b = ('a', 'A')
    name = []
    for i in a:
        if i.lower()[0] in b:
            name.append(i)
    print(name)
f()

"""6. Напишите функцию, которая принимает на вход список чисел и возвращает список чисел, 
которые больше 10 и меньше 20."""
r = []
def func(r):
    f = [11, 15, 22, 17, 30, 12, 19, 98]
    for i in f:
        if i > 10 and i < 20:
            r.append(i)
    return r
print(func(r))
func(r)

"""7. Напишите функцию, которая принимает на вход список строк и возвращает список строк,
которые содержат букву "e"."""
stl = ['werdum', 'blessed', 'masvidal', 'chendler', 'usman']
l = []
def let(l):
    for symbol in stl:
        if 'e' in symbol:
            l.append(symbol)
    return l
print(let(l))
let(l)
"""8. Напишите функцию, которая принимает на вход список чисел и возвращает True, если все числа в списке положительные,
 и False в противном случае."""
spisok = [1, 56, 78, 89, 34]
def bool():
    for j in spisok:
        if j < 0 in spisok:
            print(False)
    return True
print(bool())
bool()
"""9. Напишите функцию, которая принимает на вход список строк и возвращает список строк,
которые содержат только цифры."""
title_1 = []
def numbers(title_1):
    title = [1, 2, 4, 89, 56, 'qwerty', 'solo', 'phyton']
    for x in title:
        if type(x) == int:
            title_1.append(x)
    return title_1
numbers(title_1)
print(title_1)

"""10. Напишите функцию, которая принимает на вход список чисел и возвращает список чисел,
 которые являются степенями двойки."""
num = []
def fun(num):
    res = [2, 11, 8, 91, 16, 7, 13, 1, 4]
    count = 0
    for s in res:
        if s == 2**count:
            count += 1
        num.append(s)
    return num
print(fun(num))

