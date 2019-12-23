import random

def random_numbers(n):      #Creating the random array
    start_list = []
    for i in range(n):
        start_list.append(random.randint(0,100))
    return start_list

def worst_case(n):      #Creates a worst case array
    worst_case = list(range(n))
    worst_case.reverse()
    return worst_case

def worst_case_alt(n):      #Alternate worst case
    worst_case = list(range(n))
    return worst_case