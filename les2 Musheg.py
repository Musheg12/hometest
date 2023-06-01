'''1. Написать программу, которая удаляет первый и последний символы строки.
Если строка содержит меньше  двух символов- вывести сообщение об ошибке.'''
a = (str(input('enter the string:')))
if len(a) > 2:
    print(a[1:-1])
else:
    raise ValueError("Incorrect code")



'''2. Напишите программу которая настроит отображение комментария к отметке 'мне нравится' в условном посте.
 Список имен передается в кач-ве аргумента.  
Например:   
[]                                -->  "no one likes this"   
["Peter"]                         -->  "Peter likes this"   
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"   
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"   
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this" '''
a = (str(input('enter the string:')))
if len(a) < 10:
    print("no one likes this")
elif len(a) == 10:
    print("not bad")
elif len(a) > 10:
    print("I likes this")
else:
    print("It`s not good")


'''3.Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.'''
phone = ['LG', 'Samsung', 'Iphone', 'Honor', 'OnePlus', 'Huawei', 'Sony', 'Xiaomi']
TV = ['LG', 'Samsung', 'Philips', 'Sony', 'Xiaomi', 'Toshiba', 'Panasonic']
print(set(phone)-set(TV))


'''4. Создайте простой калькулятор, который считывает из строки ввода(пример: «1 + 13» три подстроки: 1-ое число,
 2-ое число и операцию, после чего применяет операцию к введённым числам, а затем выводит результат на экран.'''
x = (float(input('enter the first number:')))
y = (float(input('enter the second number:')))
d = input('')
if d == '+':
    print(x + y)
elif d == '-':
    print(x - y)
elif d == '/':
    print(x / y)
elif d == '*':
    print(x * y)
else:
    print('Operation note found')

'''5. Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
Составьте список и кортеж с этими числами.'''
c = input("enter the string:")
a = list(c)
b = tuple(c)
print(a, b)