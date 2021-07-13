'''
-----Linear Search------

In this we run through the array/list to search the element. and return -1 if not found.
The complexity of this algo is O(n)

'''
# def linear_search(arr, key):
#     for i in range(0,len(arr)):
#         if int(arr[i]) == int(key):
#             return True

# if __name__ == '__main__':
#     print('Enter the array: ')
#     ar = list(map(int, input().split()))
#     print("Enter the key to be search :")
#     k = int(input())
#     res = linear_search(ar,k)
#     if res:
#         print('Yes Key found')
#     else:
#         print('OOPss No Key')


'''
--------Binary Search----------

In this we check the middle postio of the array/list and if key < value at middle postion then we check for the value in 1st half
of the list else we check it in the other half of the list.
As we divide the array again and again into half... n/2, (n/2)/2 [half of the previous half], ..... n/2^k...
1 = n/2 ^ k
n =  2^k
log n = k log 2 == log n
From the above we can say that the complexity of this algo is O(Log(n)) which is better than O(n).
'''
# code the problem here 


'''
This is the question to add the char at the begining and at the end of the string and it also used string reverse.

Check here to know about ---- string to char array and vice versa ----- .
Check here for string --revere-- using keyword.
'''

# print('Enter the String: ')
# st = input()
# char_st= list(st)
# print('Enter the character to be inserted at the front of the string:')
# char_front= input()
# print('Enter the character to be inserted at the end of the string:')
# char_end = input()
# str_len= len(char_st)-1
# char_st[0] = char_front
# char_st[str_len] = char_end
# res = ""
# res = res.join(char_st)
# resRev = "".join(reversed(res))
# print(resRev)

'''
------KADANE's ALGORITHM : Sum of contiguous SUBARRAY------
If you have an array then you have to find the maximum sum of the sub array of size k. 
The size of the k will be less than the size of the array.
This type of problem can be solved using ** sliding window technique **.


----The following is to take list(array) input in one line during coding:-----
arr = list(map(int,input().split())) ------ taking int list input

'''

#In the follwoing code if you replace 2 with the k-1(lenght of subarray-1). We use -1 because of 0 indexing.

# print("Enter the array size:")
# length = int(input())
# arr = list(map(int,input().split()))
# s = 0
# max_sum = 0
# for i in range(0, length):
#     s+= arr[i]
#     if i >= 2:   #this is for sub array of size 3. Replace it with k-1 for any size k.
#         max_sum = max(s, max_sum)
#         s-= arr[i-2]
# print(max_sum)



#Code to find the triplet that sums to  give value.



#Recursion
# def binary_to_decimal(n):
#     ans = ''
#     if n>0:
#         binary_to_decimal(n//2)
#         ans+= str(n%2)
# print("Enter the number in decimal form")
# n = int(input())
# binary_to_decimal(n)
# print()
# if(l[pos] == '1'):
#     l[pos] = 0
# else:
#     l[pos] = 1


#Recurssion:

def fibonacci(num):
    if num <= 0:
        return 0
    elif num==1:
        return 1
    else:
        fib = fibonacci(num-1) + fibonacci(num-2)
        return fib

def factorial(num):
    if num == 0:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact

if __name__ == '__main__':
    print(factorial(6),'Factorial')
    print(fibonacci(6),'Fibonacci')


