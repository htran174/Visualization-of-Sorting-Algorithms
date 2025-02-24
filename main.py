import tkinter as tk
from tkinter import messagebox
import random

def bubble_sort():
    print("Using Bubble Sort")

def merge_sort():
    print("Using Merge Sort")

def quick_sort():
    print("Using Quick Sort")

def radix_sort():
    print("Using Radix Sort")

def linear_search():
    print("Using Linear Search Algorithm")

def generate_sorting():
    num_elements = entry.get()
    
    if not num_elements.isdigit() or int(num_elements) <= 0:
        messagebox.showerror("Input Error", "Please enter a valid positive integer for the number of elements.")
        return
    
    num_elements = int(num_elements)
    random_array = [random.randint(1, 999) for _ in range(num_elements)]
    print(f"Generated Array: {random_array}")
    
    if sort_var[0].get():
        bubble_sort()
    if sort_var[1].get():
        merge_sort()
    if sort_var[2].get():
        quick_sort()
    if sort_var[3].get():
        radix_sort()
    if sort_var[4].get():
        linear_search()
    
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