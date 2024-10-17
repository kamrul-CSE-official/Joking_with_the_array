my_array = [ 12, 21, 45, 2, 0, 18, 12]

array_len = len(my_array)

for i in range(array_len - 1):
    for j in range(array_len - i -1):
        if my_array[j] > my_array[j+1] :
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]


print("Sorted array: ", my_array)