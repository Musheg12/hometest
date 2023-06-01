'''1. Напишите функцию, которая принимает на вход список строк и возвращает наиболее часто встречающуюся строку.'''
from collections import Counter
def double(lst):
    counterList = Counter(lst)
    maxAppearance = 0
    needWord = ''
    for x in counterList:
            if counterList[x] > maxAppearance:
                  maxAppearance = counterList[x]
                  needWord = x
    return needWord
print(double(['python', 'hello', 'world', 'python', 'qwerty', 'python', 'qwerty']))

'''2. Напишите функцию, которая принимает на вход два списка и возвращает новый список, содержащий элементы,
которые есть в обоих списках. '''
phone = ['LG', 'Samsung', 'Iphone', 'Honor', 'OnePlus', 'Huawei', 'Sony', 'Xiaomi']
TV = ['LG', 'Samsung', 'Philips', 'Sony', 'Xiaomi', 'Toshiba', 'Panasonic']
list = []
def func_l(list):
    for i in phone:
        for q in TV:
            if i == q:
                list.append(i)
    return list
print(func_l(list))
func_l(list)

'''3. Напишите функцию, которая принимает на вход строку и возвращает количество слов в этой строке,
в которых есть более 3-х гласных (a, e, i, o, u).'''
def count_words(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for word in words:
        vowel_count = sum(1 for letter in word if letter in vowels)
        if vowel_count > 3:
            count += 1
    return count
print(count_words(['asdertuj', 'sdwsdwsd', 'qwertyouo'])) # Output: 0


'''4. Написать функцию, которая принимает список словарей, где каждый словарь представляет собой запись об ученике
(с ключами 'имя', 'возраст', 'оценки'), и возвращает список словарей, отсортированный по возрасту учеников
в порядке убывания средней оценки каждого ученика. '''
magazine = [{'name': 'Jack', 'age': 16, 'point': 5},
            {'name': 'Mark', 'age': 17, 'point': 3},
            {'name': 'John', 'age': 18, 'point': 4}]



'''5*. Написать функцию, которая принимает дерево, представленное в виде списка списков,
где каждый элемент списка может быть либо числом, либо подсписком, и возвращает сумму всех чисел в дереве.'''
tree = [12, [3, 2, 31], [123, 23], 18], [12, [], [0, 0, 4]]
tree = str(tree)
for i in tree:
    if i in '][ ':
        tree = tree.replace(i, '')
        tree = tree.split(',')
        tree.remove('')
print(sum(map(int, tree)))
'''6. Написать функцию, которая принимает список дат в формате 'ДД.ММ.ГГГГ' и возвращает список дат
в формате 'ГГГГ-ММ-ДД', отсортированный по возрастанию.'''
from datetime import datetime
mag = [{'12.10.1989'}, {'20.08.1989'}, {'24.04.2023'}, {'27.11.1987'}, {'16.12.1963'}, {'02.10.2020'}]
d = datetime.strptime(mag, '%d/%m/%Y')
dst = d.strftime('%y-%m-%d')
print(dst)



