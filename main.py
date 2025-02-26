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


import tkinter as tk
from tkinter import messagebox
import random

def bubble_sort(random_array):
    print("Using Bubble Sort")

def merge_sort(random_array):
    print("Using Merge Sort")

def quick_sort(random_array):
    print("Using Quick Sort")

def radix_sort(random_array):
    print("Using Radix Sort")

def linear_search(search_value,random_array ):
    print(f"Using Linear Search Algorithm and look for {search_value}")

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

    #sort_time_dictionary = {}

    if sort_var[0].get():
        bubble_sort(random_array.copy())
        '''
        example code
        time = #get back the time it took for doing the sort
        
        sort_time_dictionary[bubble_sort] = time 
        '''
    if sort_var[1].get():
        merge_sort(random_array.copy())
    if sort_var[2].get():
        quick_sort(random_array.copy())
    if sort_var[3].get():
        radix_sort(random_array.copy())
    if sort_var[4].get():
        linear_search(search_value,random_array.copy())
    
    messagebox.showinfo("Selection Confirmed", f"Number of elements: {num_elements}\nGenerated Array: {random_array}")

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
