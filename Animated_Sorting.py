import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')
from tkinter import Tk,Label,Entry,Button


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

def create_array(n):

    unordered = [i + 1 for i in range(n)]       #Creating a list of subsequent values
    random.seed(time.time())
    random.shuffle(unordered)       #Shuffling the list

    return unordered

def update_fig(unordered, rects, iteration,text):        #Update fig function
        for rect, val in zip(rects, unordered):     #Setting height of the rectangles
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

def create_animation(generator,unordered,n):
    title = 'Sorting Animation'

    fig, ax = plt.subplots()        #Creating axis and figure
    ax.set_title(title)     #Adding a title

    
    bar_rects = ax.bar(range(len(unordered)), unordered, align="edge")      #Creating the rectangular bars

    ax.set_xlim(0, n)       #Axis limits
    ax.set_ylim(0, int(1.07 * n))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)      #Number of operations counter

    iteration = [0]

    if generator != merge_sort:
        anim = animation.FuncAnimation(fig, func=update_fig,        #Creating the animation
            fargs=(bar_rects, iteration,text), frames=generator(unordered), interval=1,
            repeat=False)
    else:
        anim = animation.FuncAnimation(fig, func=update_fig,        #Creating the animation for merge sort
            fargs=(bar_rects, iteration,text), frames=generator(unordered,0,n-1), interval=1,
            repeat=False)

    plt.show()      #Showing the plot

class GUI:
    def __init__(self,master):
        self.master = master
        master.title('Sorting Algorithm Visualisation')


        self.instruct = Label(master, text="Please enter a length for the array to sort: ")
        self.instruct.grid(row = 1, column = 1,columnspan=2,ipadx=50)

        self.length = Entry(master)
        self.length.grid(row=1,column=3,padx=5,pady=5,columnspan=2,ipadx=50)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1,column=6,padx=5,pady=5)

        self.bubble_sort = Button(master, text="Bubble Sort",command=self.bubble_s)
        self.bubble_sort.grid(row=2,column=1,padx=5,pady=5)

        self.merge_sort = Button(master, text="Merge Sort",command=self.merge_s)
        self.merge_sort.grid(row=2,column=2,padx=5,pady=5)

        self.insertion_sort = Button(master, text="Insertion Sort",command=self.insertion_s)
        self.insertion_sort.grid(row=2,column=3,padx=5,pady=5)

        self.shell_sort = Button(master, text="Shell Sort",command=self.shell_s)
        self.shell_sort.grid(row=2,column=4,padx=5,pady=5)

        
    def get_length(self):
        self.n = int(self.length.get())


    def bubble_s(self):
        self.animate(bubble_sort)
    
    def merge_s(self):
        self.animate(merge_sort)

    def insertion_s(self):
        self.animate(insertion_sort)

    def shell_s(self):
        self.animate(shell_sort)
    

    def animate(self,generator):
        self.get_length()
        unordered = create_array(self.n)
        create_animation(generator,unordered,self.n)


if __name__ == '__main__':
    root = Tk()
    gui = GUI(root)
    root.mainloop()

    