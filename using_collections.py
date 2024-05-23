"""
File containing solutions for end of 'Using collections' chapter exercises
All questions omitted were 'what is the displayed output' style questions

"""

#q1
#you can also directly iterate through a range
print(range(0,25,3)[6])

#q2
text = "Launch School"
start_index = text.find('c')
stop_index = start_index + 6
print(text[start_index:stop_index])

#q3
curr_tuple = (1,2,3,4,5)
new_tuple = curr_tuple[-2:0:-1] #start = -2, second from last, stop = index - 1
print(new_tuple)

#q4
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard')) #default value assigned to KEY Lizard is None
print(pets.get('Lizard', '<silence>'))

#q7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info.replace(':','+')) #can also use split by : and then join using +

#q9
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][-2] = 606
print(stuff)

#q10
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}
print(cats['Pete']['Cocoa']['enjoys'])

#q12
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']
print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

#q14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

combined_tuple = list(zip(my_str, my_list, my_tuple, my_range))
print(combined_tuple)