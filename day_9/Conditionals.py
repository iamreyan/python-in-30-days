import math
a = int(input('Enter your age:'))
b = 18 - a
if a >= 18:
    print("You are old enough to drive.")
elif a < 18:
     print('You need ',b,' more years to learn to drive.')
else:
     print("You are so young to drive.")

my_age = 25
your_age = int(input('What is your age?:'))
difference = my_age - your_age
differ = your_age - my_age
if my_age == your_age:
    print('We are at same age now!')
elif my_age > your_age:
    print('I am',difference,'elder than you.')
else:  
    print('You are ',differ,' years older than me.')
    
first_num = input('Enter number one:')
second_num = input('Enter number two:')
if first_num == second_num:
    print("First number is equal to second number.")
elif first_num > second_num:
    print(first_num,"is greater than",second_num)
else:
    print(first_num,"is smaller than",second_num)

score = int(input('What is your score?'))
if score >= 80:
    print("Your grade is A.")
elif score >= 70 < 80:
    print("Your grade is B.")
elif score >= 60 < 70:
    print("Your grade is C.")
elif score >= 50 < 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")

months = input("What are the months that you want to know about the seson?")
if months == 'September, October and November':
    print("The season is Autumn.")
elif months == 'December, January and February':
    print("The season is Winter.")
elif months == 'March, April and May':
    print("The season is Spring.")
elif months == 'June, July and August':
    print("The season is Summer.")
else:                                              
    print("The name of months are wrong.")







































































































































































































































































































































































