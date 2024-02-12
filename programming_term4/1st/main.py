#!/usr/bin/python
from random import uniform #uniform import(special for float nums)

array = [] 
counter = 0

#filling the array with random numbers from -100 to 100
for _ in range(20):
    array.append(round(uniform(-10, 10), 1))
print("Our array:", array)

#finding negative_numbers in array
for number in array:
    if number < 0:
        counter += 1
print("\nAmount of negative numbers:", counter)
