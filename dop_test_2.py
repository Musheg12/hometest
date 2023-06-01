'''1. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
содержащий те же числа, но отсортированные по возрастанию.'''
def spk():
    pfl = [12, 2, 10, 27, 16, 20, 8]
    pfl.sort()
    print(pfl)
spk()


'''2. Напишите функцию, которая принимает на вход список слов и возвращает новый список, 
содержащий только те слова, которые состоят только из букв (верхнего или нижнего регистра).'''
lst = []
def words(lst):
    l = ['HELLO', 'WORLD', 'python', 'IT', 'qwerty']
    for word in l:
        if word == word.upper():
            lst.append(word)
    return lst
print(words(lst))
words(lst)

'''3. Напишите функцию, которая принимает на вход список чисел и возвращает новый список,
 содержащий только те числа, которые делятся на 3 без остатка.'''
division = []
def fun(division):
    nums = [34, 89, 56, 90, 11, 27, 16, 13, 53]
    for w in nums:
        if w % 3 == 0:
            division.append(w)
    return division
print(fun(division))
fun(division)

'''4. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, 
содержащий только те числа, которые являются простыми.'''
s_numb = []
def simple_numbers(s_numb):
    s_numbers = [-1, 23.4, 39.5, 71.2, 20, 16, 24, 12, 27, 17.5, 18.7]
    for numb in s_numbers:
        if numb > 1 and type(numb) == int:
            s_numb.append(numb)
    return s_numb
print(simple_numbers(s_numb))
simple_numbers(s_numb)

'''5. Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий только те строки, которые длиннее 5 символов.'''
lst_1 = ['qwerty', 'python', 'son', 'hello']
ls = []
def functions(ls):
    for q in lst_1:
        if len(q) > 4:
            ls.append(q)
    return ls
print(functions(ls))
functions(ls)

'''6. Напишите функцию, которая принимает на вход список чисел и возвращает новый список, 
содержащий те же числа, но умноженные на 2.'''
def set_number(s):
    print([i * 2 for i in s])
set_number([4, 7, 9])

'''7. Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий только те строки, которые содержат хотя бы одну цифру.'''
lst_2 = []
def Q(lst_2):
    lst_ = [1, 'w', 6, 'a', 'v', 'q', 8.6, 'e', 0.2, 7.9]
    for i in lst_:
        if type(i) == int or type(i) == float:
            lst_2.append(i)
    return lst_2
print(Q(lst_2))
Q(lst_2)

'''8. Напишите функцию, которая принимает на вход список строк и возвращает новый список, 
содержащий те же строки, но в верхнем регистре.'''
q = []
k = ['hello', 'print', 'qwerty']
def set_register(q):
    for element in k:
        if element.upper():
            q.append(element.upper())
    return q
print(set_register(q))
set_register(q)