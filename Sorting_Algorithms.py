
def bubble_sort(lst):        #Bubble Sort
    index = len(lst) - 1
    while index >= 0:
        test_index = index
        while test_index >= 0:
            if lst[index] < lst[test_index]:
                temp = lst[index]
                lst[index] = lst[test_index]
                lst[test_index] = temp
            test_index -= 1
        index -= 1
    return lst

def merge_sort(lst):     #Merge sort splitting the list (recursive) then merging (calls a seperate function)
    if len(lst) <= 1:      #Base case
        return lst
    
    center = len(lst)//2       #Finding the center
    left_list = lst[:center]       #Splitting to two lists
    right_list = lst[center:]

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

def insertion_sort(lst):        
    for i in range(1,len(lst)):     
        j = i-1     #Starting comparison to just the first element of the list
        next_element = lst[i]       #Iterating through the test values from start (indexed 1 intially) to insert
        while (lst[j] > next_element) and (j >= 0):     #iterating through each element already ordered to find position of test value
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = next_element
    return lst

def shell_sort(lst):
    
    split_point = len(lst) // 2     #Initially splitting the list in half
    while split_point > 0:

        for i in range(split_point, len(lst)):
            temp = lst[i]
            j = i

            while j >= split_point and lst[j - split_point] > temp:     #Sorting the subsection of the list
                lst[j] = lst[j - split_point]
                j = j - split_point
            lst[j] = temp

        split_point = split_point // 2      #splitting the unordered part of the list in half
    return lst

