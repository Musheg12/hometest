"""1. "1 2 3 4 5" найдите самое большое и маленькое число в этой строке и верните их кортежем."""
string = '1 2 3 4 5'
lst_numb = list(map(int, string.split()))
tpl_numb = tuple(lst_numb)
print(lst_numb)
print(tpl_numb)
tpl_numb_1 = min(tuple(tpl_numb))
tpl_numb_2 = max(tuple(tpl_numb))
tpl = (tpl_numb_1, tpl_numb_2)
print(tpl)
"""2. Написать программу, которая может принимать любое неотрицательное целое число в качестве аргумента 
и возвращать новое максимально возможное значение, составленное из цифр этого же числа. 
По сути, просто переставить цифры, чтобы создать максимально возможное число."""
numb = 894539
str_numb = list(str(numb))
in_numb = (sorted(str_numb, reverse=True))
print(int(''.join(in_numb)))
print(in_numb)
"""3. Передается список, состоящий из строк и чисел, нужно вернуть новый список, содержащий только цифры."""
lst = [1, '2', 6, 'a', 'v', 'q', '8', 'e', 0]
lst_1 = []
for i in lst:
    if type(i) == int:
        lst_1.append(i)
print(lst_1)


"""4. С клавиатуры вводится натуральное число. Найти его наибольшую цифру. 
Например, введено число 764580. Наибольшая цифра в нем 8."""
num = 764580
num_2 = num % 10
num = num//10
while num > 0:
    if num % 10 > num_2:
        num_2 = num % 10
    num = num//10
print(num_2)