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