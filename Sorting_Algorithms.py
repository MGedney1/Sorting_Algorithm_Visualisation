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


def bubble_sort(arr):        #Bubble sort
    start = time.time()
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
    time_taken = time.time() - start
    return time_taken


n = list(range(10,1000,10))     #Running bubble sort for a range of array lengths and showing a graph of the times taken against array size


times_bubble = []
times_bubble_worst_case = []

for x in range(len(n)):
    times_bubble.append(bubble_sort(random_numbers(n[x])))
    times_bubble_worst_case.append(bubble_sort(worst_case(n[x])))


plt.plot(n,times_bubble,label='Random Run')
plt.plot(n,times_bubble_worst_case,label='Worst Case')
plt.xlabel('Array Length')
plt.ylabel('Time Taken /s')
plt.title('Bubble Sort')
plt.legend()
plt.show()
