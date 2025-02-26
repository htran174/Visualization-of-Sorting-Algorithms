"""
=================================================================================
                                Main.py
Program by Hien Tran
Baisc GUI that has:
    Textbox that let the user input number of elements in the arrary
    Allow user to select which sort they want to use
    A Generate button that makes a random array and sends it to select sorts
=================================================================================
"""

import graph
import tkinter as tk
from tkinter import messagebox
import random
import time as tm

def bubble_sort(random_array):
    start_time = tm.time()
    print("Using Bubble Sort")
    end_time = tm.time()
    return (end_time - start_time)

def merge_sort(random_array):
    start_time = tm.time()
    print("Using Merge Sort")
    end_time = tm.time()
    return (end_time - start_time)

def quick_sort(random_array):
    start_time = tm.time()
    print("Using Quick Sort")
    end_time = tm.time()
    return (end_time - start_time)

def radix_sort(random_array):
    start_time = tm.time()
    print("Using Radix Sort")
    end_time = tm.time()
    return (end_time - start_time)

def linear_search(search_value,random_array ):
    start_time = tm.time()
    print(f"Using Linear Search Algorithm and look for {search_value}")
    end_time = tm.time()
    return (end_time - start_time)

def generate_sorting():
    num_elements = entry.get()
    search_value = search_entry.get()
    
    if not num_elements.isdigit() or int(num_elements) <= 0: #show error box if num of elements is not inputed
        messagebox.showerror("Input Error", "Please enter a valid positive integer for the number of elements.")
        return
    
    if (not search_value.isdigit() or int(search_value) <= 0) and sort_var[4].get(): #show error box if search is not inputed
        messagebox.showerror("Input Error", "Please enter a valid positive integer for Linear Search.")
        return
    
    num_elements = int(num_elements)
    random_array = [random.randint(1, 999) for _ in range(num_elements)]
    print(f"Generated Array: {random_array}")

    sort_time_dictionary = {}

    if sort_var[0].get():
        time = bubble_sort(random_array.copy())
        sort_time_dictionary['Bubble Sort'] = time * 1000000

    if sort_var[1].get():
        time = merge_sort(random_array.copy())
        sort_time_dictionary['Merge Sort'] = time * 1000000

    if sort_var[2].get():
        time = quick_sort(random_array.copy())
        sort_time_dictionary['Quick Sort'] = time * 1000000

    if sort_var[3].get():
        time = radix_sort(random_array.copy())
        sort_time_dictionary['Radix Sort'] = time * 1000000

    if sort_var[4].get():
        time = linear_search(search_value,random_array.copy())
        sort_time_dictionary['Linear Search'] = time * 1000000
    
    messagebox.showinfo("Selection Confirmed", f"Number of elements: {num_elements}\nGenerated Array: {random_array}")

    #sends dictionary to graph
    graph.show_graph(sort_time_dictionary)

if __name__ == "__main__":

    # Initialize main window
    root = tk.Tk()
    root.title("Visualization of Sorting Algorithms")
    root.geometry("400x350")

    # Input field for number of elements
    tk.Label(root, text="Enter number of elements:").pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(pady=5)

    # Sorting algorithm checkboxes
    sorting_algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search Algorithm"]
    sort_var = [tk.BooleanVar() for _ in range(5)]

    for i in range(4):
        tk.Checkbutton(root, text=sorting_algorithms[i], variable=sort_var[i]).pack(anchor='w')

    # Linear Search Algorithm with input field
    linear_search_frame = tk.Frame(root)
    linear_search_frame.pack(anchor='w', pady=5)
    tk.Checkbutton(linear_search_frame, text="Linear Search Algorithm", variable=sort_var[4]).pack(side='left')
    search_entry = tk.Entry(linear_search_frame)
    search_entry.pack(side='left', padx=5)

    # Generate button
    tk.Button(root, text="Generate", command=generate_sorting).pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()
    
