def length_of_string(s):

  if s == '':
    return 0
  else:
    return 1+length_of_string(s[1:])

def sum_of_integers(n):

  if n == 0:
    return 0
  else:
    return n + sum_of_integers(n-1)

def exponent(a,n):

  if (n==0):
    return 1
  else:
    m=exponent(a,n-1)
    return m*a 

def bin_to_dec(string,i,num):

  if len(string) == i :
    return num
  else:
    if string[i] == '0':
      num=2*num
    else:
      num=2*num+1
  return bin_to_dec(string,i+1,num)

#sum of digits

def sum_of_digits(num,sum):

  if num == 0:
    return sum
  return sum_of_digits(int(num/10), sum+(num%10))

#factorial

def fact(num):

  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return num*fact(num-1)

#recursive sort
#selection sort
def selection_sort(a):
  i=0
  j=i+1
  l=len(a)
  if i == l and j==l:
    return -1
  if i < l-1:
    min=i
    while j < l:
      if a[j] < a[min]:
        min = j
      j=j+1
    if min != i:
      temp=a[i]
      a[i]=a[min]
      a[min]=temp
    selection_sort(a,i+1,i+2)

#insertion sort
def insertion_sort(a,i):

  l=len(a)
  if i == l:
    return -1
  if i < l:
    j=i-1
    key=a[i]
    while j>=0 and key<a[j]:
      a[j+1]=a[j]
      j=j-1
    a[j+1]=key
    insertion_sort(a,i+1)


#fibonacci [Memoization]
def fibonacci(num):

  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return (fibonacci(num-1)+fibonacci(num-2))

#grid walking function
def grid_walk(m,n):

  if m == 1 or n == 1:
    return 1
  else:
    return grid_walk(m-1,n)+grid_walk(m,n-1)

#bubble sort 
def bubble_sort(a):

    for i in range(len(a)-1,-1,-1):
        for j in range(0,i):    
          if a[j]>a[j+1]:    
            temp = a[j]    
            a[j]=a[j+1]    
            a[j+1]=temp
    print(a)

#selection_sort
def selection_sort(A):

  max_idx = 0
  max = A[0]
  for i in range(len(A)-1,-1,-1):
    max = A[i]
    max_idx = i
    #finding the maximum value
    for j in range(0,i):
      if(A[j]>max):
        max = A[j]
        max_idx = j
    #swapping
    temp = A[max_idx]
    A[max_idx]=A[i]
    A[i]=temp
  print(A)

#insertion sort
def insertion_sort(A):

  for i in range(0,len(A)):
    for j in range(i-1,-1,-1):
      if(A[j]>A[j+1]):
        temp = A[j]
        A[j]=A[j+1]
        A[j+1]=temp
      else:
        break
  print(A)  

#search
#linear search 
def linear_search(A, value):

  for i in range(0,len(A)):
    if(A[i]==value):
      return i
  return -1

#Binary search
def binary_search(A, val):

  L = 0
  R = len(A)-1
  while(L<=R):
    M = (L+R)//2
    if(val == A[M]):
      return M
    elif (val > A[M]):
      L = M + 1
    else:
      R = M - 1
  return -1


  


#tester 
print(length_of_string("abcdefgh"))
print(sum_of_integers(6))
print(exponent(2,7))
print(bin_to_dec("1011011",0,0))
print(sum_of_digits(5012,0))
print(fact(6))

 
#[Memoization]
print(fibonacci(4))
#sort
s=[2,5,8,7,6,1,0,569,65]
bubble_sort(s)
s=[2,5,8,7,6,1,0,569,65]
selection_sort(s)
s=[2,5,8,7,6,1,0,569,65]
insertion_sort(s)
#search
s=[2,5,8,7,6,1,0,569,65]
print(linear_search(s,569))
s=[2,5,8,7,6,1,0,569,65]
print(binary_search(s,569))

#recursive sort
#selection sort
po=[13,25,0,-4,7,-1,18,9,-6,21]

selection_sort(po)
print(po)
#insertion sort
#Tester
A=[22,5,14,2,7,1]
i=1
insertion_sort(A,i)
print(A)