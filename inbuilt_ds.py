'''
------ LIST -----

List is the dynamic array in python. It allocates contiguous block of memory.
It is mutable(changeable) that means it can be used to aadd new element, remove element and so on.
list()- It is a keyword and used to typecast the list in python.

'''

#List creation and adding element at the end of the list
lis1 = [1,2,3]
lis1.append(4)
print(lis1,'\n')

#here extend will add the elements(similar or distinct) of the list whiich is passed in extend() function and make a single list.
lis2 = [1,2,3]
lis2.extend([2,3,4,2,5])
print(lis2,'\n')


#insert(): It will take 2 values, index(as per 0 indexing) position and the value to put there
lis3 = [1,2,4,5]
lis3.insert(2,3)
print(lis3,'\n')

#deleting using del[] in the del mention the index(as per 0 indexing)
lis4 = [2,3,4,2]
del lis4[3]
print(lis4,'\n')

#removing the mentioned element using remove(). It will remove the element mentioned not the postion
lis5 = [1,2,3,4,6,5]
lis5.remove(6)
print(lis5,'\n')

#pop(). It takes the index(as per 0 indexing) of the element to be popped.
lis6= [1,2,5,3,4]
a = lis6.pop(2)
print(a,'Popped element','\n')
print(lis6,'\n')

#clear. It is used to clear the list
lis7 = [1,24,5]
lis7.clear()
print(lis7,'\n')

#Sorting the list
lis8 = [2,34,1,34,434,56]
lis8.sort()
print(lis8,'Sorted in ascending order by defalut \n')
lis8.sort(reverse= True) #will sort it in descending order
print(lis8,'Sorted in descending order \n')

#index of the element as per 0 indexing
lis9= [1,2,3,4,4,5,5,]
a = lis9.index(2)
b = lis9.index(4)
print(a,'Index of non repeating element \n')
print(b, 'Index of 1st occurence of the repeating element \n')

#count. it can give the count of a particular element in the list. len(list_name) is used to get the length of the list
lis10= [1,2,2,2,3,4,5,3,5,5,5]
a = lis10.count(5)
b =lis10.count(1)
c = lis10.count(92)
d =len(lis10)
print(a,'count of repeating element in the list.','\n',b,'Count of non repeating ele in the list.')
print(c,'count of element NOT in the list.','\n',d,'Length of the list.\n')
print(max(lis10)) #it prints the max element of the list
print(min(lis10)) #it prints the min element of the list
print(int(4 ** (1/2))) # ** is similar to pow if you give 4 ** (1/2) it will give square root of 4 in float
print(5 // 2) #It will give the floor 



'''

-----Tuples-------

'''