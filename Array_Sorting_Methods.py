# Array Sorting Methods

# 1.) Bubble Sort
def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j] 
arr = [23, 54, 11, 16, 44, 39, 64, 28]
Bubble_Sort(arr)
print(f"Sorted array using Bubble Sort => {arr}")

# 2.) Selection Sort
def Selection_Sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_val_ind = i
        for j in range(i + 1, n):
            if arr[min_val_ind] > arr[j]:
                min_val_ind = j
        min_val = arr.pop(min_val_ind)
        arr.insert(i, min_val)
arr = [23, 54, 11, 16, 44, 39, 64, 28]
Selection_Sort(arr)
print(f"Sorted Array using Selection Sort => {arr}")

# 2.) Insertion Sort
def Insertion_Sort(nums):
    n = len(nums)
    for i in range(1, n):
        min_index = i
        min_value = nums.pop(i)
        for j in range(i - 1, -1, -1):
            if nums[j] > min_value:
                min_index = j
        nums.insert(min_index, min_value)

nums = [23, 56, 1, 4, 3, 14, 87, 33, 39, 20]
Insertion_Sort(nums)
print(nums)



