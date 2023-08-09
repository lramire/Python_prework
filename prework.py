#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. 

def hello_name(user_name):
    print(f"{user_name}!")

hello_name("hello_USERNAME")


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 

def first_odds():
    for i in range(1,101,2):
        print(i)
        

first_odds()

print()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. 

def max_num_in_list(a_list):
    return max(a_list)

print(max_num_in_list([0,1,-1])) #or other values


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). 

def is_leap_year(a_year):
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(1990))
print(is_leap_year(2013))
print(is_leap_year(2000))

print()


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. 

a_list = input([]) #looking for user input to make a list and return True/False. Something is not right.
def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 == a_list[i + 1]:
            return False
    return True
    