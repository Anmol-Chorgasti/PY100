
#q3
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

print("Using For loop now")
for element in my_list:
    print(element)

#q4
print()
print("Question 4")

index = 0
while index < len(my_list):
    if my_list[index] % 2 != 0:
        index += 1
        continue

    print(my_list[index])
    index += 1

odd_list = [element for element in my_list
            if element % 2 != 0]
for value in odd_list:
    print(value)

#q5
print()
print("Question 5")
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for nested_element in my_list:
    for element in nested_element:
        if element % 2 == 0:
            print (element)

#q6
print()
print("Question 6")
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
new_list = []
for element in my_list:
    if element % 2 == 0:
        new_list.append("even")
    else:
        new_list.append("odd")
print(new_list)

#q7
print()
print("Question 7")
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(sequence):
    int_list = [element for element in sequence
                if type(element) is int]
    return int_list

print(find_integers(my_tuple))

#q8
print()
print("Question 8")

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result_dict = {element:len(element)
               for element in my_set
               if len(element) % 2 != 0 }
print(result_dict)

#q9
print()
print("Question 9")
def factorial(n):
    result = 1
    count = 1
    while count <= n:
        result *= count
        count += 1

    return result
print(factorial(5))

#q10
print()
print("Question 10")
import random

highest = 10
number = 0
while number != highest:
    number = random.randrange(highest + 1)
    print(number)

#q11
print()
print("Question 11")
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

#not using any for loops
index1 = 0
index2 = 0
while index1 < len(my_list):
    nested_list = my_list[index1]

    while index2 < len(nested_list):
        if nested_list[index2] % 2 == 0:
            print(nested_list[index2])
        index2 += 1
    
    index2 = 0
    index1 += 1

