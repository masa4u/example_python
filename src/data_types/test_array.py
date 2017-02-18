from array import array
a = array('c', 'hello world')
print(a)
print (dir(a))

int_array = array('l', [1,2,3,4,5,7,10])

print (int_array)

int_array.append(9)


print (int_array.itemsize)

print (int_array.tostring())