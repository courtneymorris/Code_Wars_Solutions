# Opposite Number

def opposite(number):
     if  number >= 1:
        neg_value = number - (number*2)
        return neg_value
     else:
        return abs(number)


# Convert a Number to a String

def number_to_string(num):
    return f'{num}'



# List Filtering

def filter_list(l):
    num_list = [ele for ele in l if isinstance(ele, int)]
    return num_list



# Keep Hydrated!

import math

def litres(time):
    return math.floor(time * 0.5) 



# Remove String Spaces

def no_space(x):
    return x.replace(" ", "")



# Thinkful - Number Drills: Blue and Red Marbles

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    start_total = blue_start + red_start
    blue_remaining = blue_start - blue_pulled
    total_pulled = blue_pulled + red_pulled
    total_remaining = start_total - total_pulled
    chance_of_blue = blue_remaining / total_remaining
    
    return chance_of_blue



# IQ Test

def iq_test(numbers):
    list_of_numbers = numbers.split(" ")
    
    first_num_evenness = True if int(list_of_numbers[0]) % 2 == 0 else False
    second_num_evenness = True if int(list_of_numbers[1]) % 2 == 0 else False
    third_num_evenness = True if int(list_of_numbers[2]) % 2 == 0 else False
    
    if first_num_evenness and second_num_evenness:
        evenness_check = True
    elif first_num_evenness and third_num_evenness:
        evenness_check = True
    elif second_num_evenness and third_num_evenness:
        evenness_check = True
    else:
        evenness_check = False
        
    odd_num_out = None
    for num in list_of_numbers:
        if int(num) % 2 == 0 and evenness_check == False:
            odd_num_out = num
            break
        elif int(num) % 2 == 1 and evenness_check == True:
            odd_num_out = num
            break
            
    
    return list_of_numbers.index(odd_num_out) + 1




# Summing a Number's Digits

from functools import reduce

def sum_digits(number):
    abs_val = abs(number)
    num_list = [int(d) for d in str(abs_val)]                              
    return reduce(lambda x, y: x+y, num_list)



# Remove First and Last Character

def remove_char(s):
    return s[1:len(s) - 1]



