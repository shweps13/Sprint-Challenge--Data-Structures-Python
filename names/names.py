import time

def quicksort_out_of_place(arr):
    # 1. Pick a pivot and move it until everything
    # on the left is smaller & everything on the right is greater
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller = []
    larger = []
    for i in range(len(arr) - 1):
        element = arr[i]
        if element < pivot:
            smaller.append(element)
        else:
            larger.append(element)
    return quicksort_out_of_place(smaller) + [pivot] + quicksort_out_of_place(larger)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Original runtime is: 9.574947834014893 seconds
# Runtime complexity is: O(n^2)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
