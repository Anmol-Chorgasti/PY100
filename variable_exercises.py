"""
This file has the solutions for exercises asked at the end of 
the variables chapter

q1-q4, q7, q10 were 'what would python display' style questions, so their solutions 
have been omitted

"""

#q5
name = "Victor"
print(f"Good Morning, {name}")
print(f"Good Afternoon, {name}")
print(f"Good Evening, {name}")

#q6
age = 22
print(f"You are {age} years old")
i = 1
while i <= 4:
    age += 10
    print(f"In {i*10} years, you will be {age} years old")
    i += 1

#q8
initial_balance = 1000
years = 1
while years <= 5:
    initial_balance *= 1.05
    years += 1
print(f"Balance after {years - 1} years: {initial_balance}")
