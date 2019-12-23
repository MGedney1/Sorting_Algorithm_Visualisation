import random
import time
from matplotlib import pyplot as plt

def random_numbers(n):      #Creating the random array
    start_list = []
    for i in range(n):
        start_list.append(random.randint(0,100))
    return start_list

def worst_case(n):
    worst_case = list(range(n))
    worst_case.reverse()
    return worst_case


def bubble_sort(arr):        #Bubble Sort
    index = len(arr) - 1
    while index >= 0:
        test_index = index
        while test_index >= 0:
            if arr[index] < arr[test_index]:
                temp = arr[index]
                arr[index] = arr[test_index]
                arr[test_index] = temp
            test_index -= 1
        index -= 1
    return 

def merge_sort(list):     #Merge sort splitting the list (recursive) then merging (calls a seperate function)
    if len(list) <= 1:      #Base case
        return list
    
    center = len(list)//2       #Finding the center
    left_list = list[:center]       #Splitting to two lists
    right_list = list[center:]

    left_list = merge_sort(left_list)     #Recursion Step 
    right_list = merge_sort(right_list)

    return merge_sort_merge(left_list,right_list)

def merge_sort_merge(left_list,right_list):      #Merging the lists
    result = []
    while len(left_list) != 0 and len(right_list) != 0:     #Comparing the smallest values in each list
        if left_list[0] < right_list[0]:
            result .append(left_list[0])
            left_list.remove(left_list[0])
        else:
            result.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list) == 0:             #When one list is empty, the other list is appened to the result
        result  = result  + right_list
    else:
        result  = result  + left_list
    return result 

n = list(range(10,1000,10))     #Running sorting algorithms for a range of array lengths and showing a graph of the times taken against array size


times_bubble = []
times_bubble_worst_case = []
times_merge = []
times_merge_worst_case = []

for x in range(len(n)):             #Working out times taken
    start_bubble_random = time.time()      #Bubble sort on random array
    bubble_sort(random_numbers(n[x]))
    time_bubble_random = time.time() - start_bubble_random

    start_bubble_worst_case = time.time()      #Bubble sort on worst case array
    bubble_sort(worst_case(n[x]))
    time_bubble_worst_case = time.time() - start_bubble_worst_case

    start_merge_random = time.time()      #Merge sort on random array
    merge_sort(random_numbers(n[x]))
    time_merge_random = time.time() - start_merge_random

    start_merge_worst_case = time.time()      #Merge sort on worst case array
    merge_sort(worst_case(n[x]))
    time_merge_worst_case = time.time() - start_merge_worst_case

    times_bubble.append(time_bubble_random)        #Appending times to relevent lists
    times_bubble_worst_case.append(time_bubble_worst_case)
    times_merge.append(time_merge_random)
    times_merge_worst_case.append(time_merge_worst_case)


plt.plot(n,times_bubble,label='Bubble Sort Random Run')
plt.plot(n,times_bubble_worst_case,label='Bubble Sort Worst Case')
plt.plot(n,times_merge,label='Merge Sort Random Run')
plt.plot(n,times_merge_worst_case,label='Merge Sort Worst Case')
plt.xlabel('Array Length')
plt.ylabel('Time Taken /s')
plt.title('Bubble Sort')
plt.legend()
plt.show()
