my_array = [ 10, 34, 94, 5, 20, 87, 3, 76, 4]

lowestValue = my_array[0]

for i in my_array:
    if i < lowestValue:
        lowestValue = i


print("The lowest value is: ", lowestValue);