import random
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import Frame,Label,Entry,Button

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
            yield lst
        index -= 1
    

def merge_sort(lst, start, end):        #Merge sort

    if end <= start:        
        return

    mid = start + ((end - start + 1) // 2) - 1      #Finding mid point for split
    yield from merge_sort(lst, start, mid)        #Further splitting first half 
    yield from merge_sort(lst, mid + 1, end)      #Further splitting second half
    yield from merge(lst, start, mid, end)        #Merging
    yield lst

def merge(lst, start, mid, end):
    
    result = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:       #checking if next index of first or second list is larger and appending to the result list
        if lst[leftIdx] < lst[rightIdx]:
            result.append(lst[leftIdx])
            leftIdx += 1
        else:
            result.append(lst[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:       #If only first list filled then appending that to result
        result.append(lst[leftIdx])
        leftIdx += 1

    while rightIdx <= end:      #Vice versa for the second list
        result.append(lst[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(result):     #Copying values and order to the origional array
        lst[start + i] = sorted_val
        yield lst

def insertion_sort(lst):        
    for i in range(1,len(lst)):     
        j = i-1     #Starting comparison to just the first element of the list
        next_element = lst[i]       #Iterating through the test values from start (indexed 1 intially) to insert
        while (lst[j] > next_element) and (j >= 0):     #iterating through each element already ordered to find position of test value
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = next_element
        yield lst

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
        yield lst

def create_array():
    n = int(input('Input the length of the arrays to sort:\n>'))        #Taking user input for array length

    unordered = [i + 1 for i in range(n)]       #Creating a list of subsequent values
    random.seed(time.time())
    random.shuffle(unordered)       #Shuffling the list

    return n,unordered

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.master = master
        self.set_up_window()

    def update_fig(unordered, rects, iteration):        #Update fig function
        for rect, val in zip(rects, unordered):     #Setting height of the rectangles
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    def set_up_window(self):
        n,unordered = create_array()
        title = 'Test'
        generator = bubble_sort(unordered)


        self.fig,self.ax = plt.subplots()        #Creating axis and figure
    
        self.bar_rects = self.ax.bar(range(len(unordered)), unordered, align="edge")      #Creating the rectangular bars

        self.ax.set_xlim(0, n)       #Axis limits
        self.ax.set_ylim(0, int(1.07 * n))

        self.text = self.ax.text(0.02, 0.95, "", transform=self.ax.transAxes)      #Number of operations counter

        self.iteration = [0]

        self.anim = animation.FuncAnimation(self.fig, func=self.update_fig, fargs=(self.bar_rects, self.iteration), frames=generator, interval=1,repeat=False)       #Creating the animatio
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().grid(column=0,row=1)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x400")
    app = Window(root)
    tk.mainloop()

    
   