'''
Python oferuje szereg funkcji wbudowanych, 
które są dostępne bez konieczności importowania 
jakichkolwiek bibliotek.
'''

# eval - zamienia na inta i oblicza jego wartość

x = -1.5

expression = 'x**2 + x'

def yourResult (x):
    result = eval(expression)
    print(result)

yourResult(x)


print('---')

# sprawdź, czy wszystkie elementy poniższej krotki zwracają wartość logiczną True:
items = (' ', '0', 0.1, True)
print(all(items))

print('---')

# sprawdź, czy jakikolwiek element poniższej krotki zwracają wartość logiczną True:
itemsTwo = ('', 0.0, 0, False)
print(any(itemsTwo))

print('---')

# Zlicz liczbę jedynek w binarnej reprezentacji liczby
number = 234
binary = bin(number)[2:]
count_ones = binary.count('1')
print(count_ones)

print('---')

# wyznacz wartość największą podanej listy
# wyznacz wartość najmniejszą podanej listy 
# wyznacz sumę elementów listy numbers
# wyznacz wartość bezwzględną najmniejszej wartości z podanej listy
numbers = [3, -5, -2, 8, 1, 9]

max_number = max(numbers)
min_number = min(numbers)
sum_numbers = sum(numbers)
abs_min = abs(min_number)

print(max_number)
print(min_number)
print(sum_numbers)
print(abs_min)

print('---')

# oblicz wartość silni z danej liczby
from functools import reduce

number = 6
numberTwo = 10

def factorial (number):
    num = 1
    yourNumber = [1]

    while num < number:
        num += 1
        yourNumber.append(num)
        result = reduce(lambda x,y: x * y, yourNumber)

    return result


print(factorial(number))
print(factorial(numberTwo))

