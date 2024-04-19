"""
File containing solutions for end of 'Flow Control' chapter exercises
All questions omitted were 'what is the displayed output' style questions

"""
#q2
def even_or_odd(number):
    if number >= 0:
        if number % 2 == 0:
            print('even')
            return 'even'
        print('odd')
        return 'odd'
    return 'negative number is neither even nor odd'


#q4
"""
if foo():
    return 'bar'
else:
    return qux()

"""

#q7
def range_of_value(number):
    if isinstance(number, int) or isinstance(number, float):
        if number > 100:
            print(f"{number} is greater than 100")
        elif number > 50 and number < 101:
            print(f"{number} is between 51 and 100")
        elif number > -1 and number < 51:
            print(f"{number} is between 0 and 50")
        else:
            print(f"{number} is less than 0")
        return
    return