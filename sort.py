#Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #recursuvley apply merge sort on both halves
        merge_sort(left_half)
        merge_sort(right_half)

        #merge the two sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        #add remaining elements from left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        #add remaining elements from left half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


#Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] #Choosing the middle element as a pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return quick_sort(left) + middle + quick_sort(right)


#Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    #Count occurance of each digit at the 'exp' place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count[i] to be the actual position index in our output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    #Build Arry
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    #Copy stored values from output[] into original array
    for i in range(n):
        arr[i] = output[i]

def lsd_radix_sort(arr):
    max_num = max(arr)
    exp = 1 #we are starting with 1s place

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr #return sorted array

def msd_radix_sort(arr):
    max_num = max(arr)
    max_digits = len(str(max_num))

    def msd_radix_helper(arr, digit_place): 
        #recursive function for MSD Radix Sort
        if len(arr) <= 1 or digit_place < 0:
            return arr
        
        #Create 10 buckets for digits 0-9
        buckets = [[] for _ in range(10)]

        for num in arr:
            digit = (num // (10 ** digit_place)) % 10
            buckets[digit].append(num)

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(msd_radix_helper(bucket, digit_place - 1))
        return sorted_arr
    return msd_radix_helper(arr, max_digits - 1)


#Linear Search
def linear_search_all(arr, target):
    indices = []
    for index in range(len(arr)):
        if arr[index] == target:
            indices.append(index)

    return indices