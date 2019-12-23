import time
from matplotlib import pyplot as plt
from Start_Array import random_numbers, worst_case, worst_case_alt
from Sorting_Algorithms import bubble_sort,merge_sort,insertion_sort,shell_sort


n = list(range(10,1000,10))     #Running sorting algorithms for a range of array lengths and showing a graph of the times taken against array size

times_bubble = []
times_bubble_worst_case = []
times_merge = []
times_merge_worst_case = []
times_insertion = []
times_insertion_worst_case = []
times_shell = []
times_shell_worst_case = []

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
    merge_sort(worst_case_alt(n[x]))
    time_merge_worst_case = time.time() - start_merge_worst_case

    start_insertion_random = time.time()      #Insertion sort on random array
    insertion_sort(random_numbers(n[x]))
    time_insertion_random = time.time() - start_insertion_random

    start_insertion_worst_case = time.time()      #Insertion sort on worst case array
    insertion_sort(worst_case(n[x]))
    time_insertion_worst_case = time.time() - start_insertion_worst_case

    start_shell_random = time.time()      #Shell sort on random array
    shell_sort(random_numbers(n[x]))
    time_shell_random = time.time() - start_shell_random

    start_shell_worst_case = time.time()      #Shell sort on worst case array
    shell_sort(worst_case(n[x]))
    time_shell_worst_case = time.time() - start_shell_worst_case


    times_bubble.append(time_bubble_random)        #Appending times to relevent lists
    times_bubble_worst_case.append(time_bubble_worst_case)
    times_merge.append(time_merge_random)
    times_merge_worst_case.append(time_merge_worst_case)
    times_insertion.append(time_insertion_random)
    times_insertion_worst_case.append(time_insertion_worst_case)
    times_shell.append(time_shell_random)
    times_shell_worst_case.append(time_shell_worst_case)


plt.plot(n,times_bubble,label='Bubble Sort Random Run')
plt.plot(n,times_bubble_worst_case,label='Bubble Sort Worst Case')
plt.plot(n,times_merge,label='Merge Sort Random Run')
plt.plot(n,times_merge_worst_case,label='Merge Sort Worst Case')
plt.plot(n,times_insertion,label='Insertion Sort Random Run')
plt.plot(n,times_insertion_worst_case,label='Insertion Sort Worst Case')
plt.plot(n,times_shell,label='Shell Sort Random Run')
plt.plot(n,times_shell_worst_case,label='Shell Sort Worst Case')

plt.xlabel('Array Length')
plt.ylabel('Time Taken /s')
plt.title('Bubble Sort')
plt.legend()
plt.show()
