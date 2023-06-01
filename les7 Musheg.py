'''1. Напишите функцию, которая принимает строку и возвращает список всех уникальных символов в этой строке.'''

def unic(list):
    spk = set()
    for word in list:
        for _ in word:
            spk.add(_)
    return spk
list = ['67356357', 'defbhjnm', '/,./l' '.kgfhesfvser']
print(unic(list))

'''2. Напишите функцию, которая принимает на вход список строк и возвращает новый список,
 содержащий только те строки, которые начинаются с буквы 'a' (большой или малой).'''
def f(a):
    b = ('a', 'A')
    name = []
    for i in a:
        if i.lower()[0] in b:
            name.append(i)
    return name
a = ['Alexander', 'Katy', 'Andrew', 'Elena', 'arduino', 'Elizabeth', 'Brain']
print(f(a))

'''3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
 содержащий только те числа, которые больше среднего значения всех чисел в списке.'''
def func_middle(numbers):
    n = []
    for q in numbers:
        if sum(numbers)/(len(numbers)) < q:
            n.append(q)
    return n
numbers = [1, 2, 3, 4, 5]
print(func_middle(numbers))


'''4. Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий те же строки, но с замененным первым символом на символ '*' (например, "hello" станет "*ello").'''
def func_replace(names):
    change_names = []
    for x in names:
        change_names.append(x.replace(x[0], '*'))
    return change_names
c = ['Alexander', 'Katy', 'Andrew', 'Elena', 'arduino', 'Elizabeth', 'Brain']
print(func_replace(c))


'''5. Напишите функцию, которая принимает на вход список списков чисел и возвращает новый список,
 содержащий те же числа, но увеличенные на 1.'''
points = []
def plus_one(lst: list[list]):
    point = [[2, 8], [12, 20], [16, 20, 27], [67, 11]]
