n = int(input("enter the size of the array\n"))
array = []
for i in range(n):
    value = int(input("enter the element \n"))
    array.append(value)

# insertion sort implementation
for i in range(1, len(array)):
    j = i-1
    while j>=0 and array[j+1] < array[j]:
        temp = array[j+1]
        array[j+1] = array[j]
        array[j]=temp
        j = j -1 

print(array)