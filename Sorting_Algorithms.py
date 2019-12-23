import random
import time

def random_numbers(n):      #Creating the random array
    start_list = []
    for i in range(n):
        start_list.append(random.randint(0,100))
    return start_list

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


n = list(range(10,1000,10))
times_bubble = []
for x in range(len(n)):
    times_bubble.append(bubble_sort(random_numbers(n[x])))
print(times_bubble)
