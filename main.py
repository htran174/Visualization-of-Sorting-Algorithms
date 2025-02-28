"""
=================================================================================
                                Main.py
Program by Hien Tran, and Salvador Rios
Baisc GUI that has:
    Textbox that let the user input number of elements in the arrary
    Allow user to select which sort they want to use
    A Generate button that makes a random array and sends it to select sorts
=================================================================================
"""



import graph
import sort as so 
import tkinter as tk
from tkinter import messagebox
import random
import time as tm

def bubble_sort(array):
    start_time = tm.time()
    so.bubble_sort(array)
    end_time = tm.time()
    return (end_time - start_time)

def merge_sort(array):
    start_time = tm.time()
    so.merge_sort(array)
    end_time = tm.time()
    return (end_time - start_time)

def quick_sort(array):
    start_time = tm.time()
    so.quick_sort(array)
    end_time = tm.time()
    return (end_time - start_time)

def radix_sort(array, type):
    if type == 0: # LSD
        start_time = tm.time()
        so.lsd_radix_sort(array)
        end_time = tm.time()
    else: #MSD
        start_time = tm.time()
        so.msd_radix_sort(array)
        end_time = tm.time()
    return (end_time - start_time)

def linear_search(search_value, array):
    start_time = tm.time()
    result = so.linear_search_all(search_value, array)
    end_time = tm.time()
    if result:
        messagebox.showinfo("Linear Search", f"Element {search_value} found at indexes: {result}")
       
    else:
        messagebox.showinfo("Linear Search", f"Element {search_value} not found in list")
       

    return (end_time - start_time)

def generate_sorting():
    user_input = entry.get()
    search_value = search_entry.get()
    
    if input_mode.get() == "Random": #if user select Random
        if not user_input.isdigit() or int(user_input) < 0: #value needs to be digit and > 0
            messagebox.showerror("Input Error", "Please enter a valid positive integer for the number of elements.")
            return
        num_elements = int(user_input)
        array = [random.randint(1, 999) for _ in range(num_elements)]
    else: #if user input own array
        try:
            array = list(map(int, user_input.split(',')))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid list of integers separated by commas.")
            return
    
    if (not search_value.isdigit()) and sort_var[4].get(): #show error box if search is not inputed
        messagebox.showerror("Input Error", "Please enter a valid positive integer for Linear Search.")
        return
    if search_value.isdigit() and not sort_var[4].get(): #show error box if user inputed search value without selcting Linear Search
        messagebox.showerror("Input Error", "Please check Linear Search if you want to use it")
        return
    
    sort_time_dictionary = {} #creating a dictionary 
    
    messagebox.showinfo("Selection Confirmed", f"Array: {array}")
    
    if sort_var[0].get():
        time = bubble_sort(array.copy())
        sort_time_dictionary['Bubble Sort'] = time * 1000000 #adding to dictionary and converting time to microseconds

    if sort_var[1].get():
        time = merge_sort(array.copy())
        sort_time_dictionary['Merge Sort'] = time * 1000000 #adding to dictionary and converting time to microseconds

    if sort_var[2].get():
        time = quick_sort(array.copy())
        sort_time_dictionary['Quick Sort'] = time * 1000000 #adding to dictionary and converting time to microseconds

    if sort_var[3].get():
        time = radix_sort(array.copy(), 0)
        sort_time_dictionary['LSD Radix Sort'] = time * 1000000 #adding to dictionary and converting time to microseconds
        time = radix_sort(array.copy(), 1)
        sort_time_dictionary['MSD Radix Sort'] = time * 1000000 #adding to dictionary and converting time to microseconds

    if sort_var[4].get():
        time = linear_search(int(search_value), array.copy())
        sort_time_dictionary['Linear Search'] = time * 1000000 #adding to dictionary and converting time to microseconds

    graph.show_graph(sort_time_dictionary, len(array))

if __name__ == "__main__":
    #color
    black = "#000000"    # Black text
    white = "#FFFFFF"  # White text
    dark_gray = "#2E2E2E"  # Dark gray



    #Creating main GUI for user input
    root = tk.Tk()
    root.title("Visualization of Sorting Algorithms")
    root.geometry("500x400")
    
    root.configure(bg=dark_gray)

    input_mode = tk.StringVar(value="Random")
    tk.Label(root, text="Select input mode:", bg= dark_gray, fg= white).pack()
    tk.Radiobutton(root, text="Random", variable=input_mode, value="Random", bg=dark_gray, fg= white).pack()
    tk.Radiobutton(root, text="Manual Input", variable=input_mode, value="Manual", bg=dark_gray, fg= white).pack()
    
    tk.Label(root, text="Enter number of elements or Enter list elements separated by comma:", bg=dark_gray, fg= white).pack(pady=5)
    entry = tk.Entry(root, bg=dark_gray, fg= white, insertbackground=white, highlightthickness=0) #for num of elements array or user inputed array
    entry.pack()
    
    sorting_algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search Algorithm"]
    sort_var = [tk.BooleanVar() for _ in range(5)]
    
    for i in range(4): # only going from 0-3
        tk.Checkbutton(root, text=sorting_algorithms[i], variable=sort_var[i], bg=dark_gray, fg= white).pack(anchor='w')
    
    linear_search_frame = tk.Frame(root)
    linear_search_frame.pack(anchor='w')
    tk.Checkbutton(linear_search_frame, text="Linear Search Algorithm", variable=sort_var[4],bg=dark_gray, fg= white).pack(side='left')
    search_entry = tk.Entry(linear_search_frame, bg=dark_gray, fg= white, insertbackground=white, highlightthickness=0) #for search value
    search_entry.pack()
    
    tk.Button(root, text="Generate", command=generate_sorting, bg=dark_gray, fg= black).pack(pady=10) 
    
    root.mainloop()
