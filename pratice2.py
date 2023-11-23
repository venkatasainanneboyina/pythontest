# Python3 program to swap first

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping 
	temp = newList[0]
	newList[0] = newList[size - 1]
	newList[size - 1] = temp
	
	return newList
	
# Driver code
newList = [88, 68,34,44,21]

print(swapList(newList))

# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):
	
	list[pos1], list[pos2] = list[pos2], list[pos1]
	return list

# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))

# Python program to find the
# maximum of two numbers


def maximum(a, b):
	
	if a >= b:
		return a
	else:
		return b
	
# Driver code
a = 2
b = 4
print(maximum(a, b))

# Python program to demonstrate
# symmetry and palindrome of the
# string


# Function to check whether the
# string is palindrome or not
def palindrome(a):


	mid = (len(a)-1)//2	  
	start = 0			
	last = len(a)-1
	flag = 0

	while(start <= mid):

	
		if (a[start]== a[last]):
			
			start += 1
			last -= 1
			
		else:
			flag = 1
			break;
			

	if flag == 0:
		print("The entered string is palindrome")
	else:
		print("The entered string is not palindrome")
		
	 
def symmetry(a):
	
	n = len(a)
	flag = 0
	
	# Check if the string's length
	# is odd or even
	if n%2:
		mid = n//2 +1
	else:
		mid = n//2
		
	start1 = 0
	start2 = mid
	
	while(start1 < mid and start2 < n):
		
		if (a[start1]== a[start2]):
			start1 = start1 + 1
			start2 = start2 + 1
		else:
			flag = 1
			break
	
	# Checking the flag variable to 
	# check if the string is symmetrical
	# or not
	if flag == 0:
		print("The entered string is symmetrical")
	else:
		print("The entered string is not symmetrical")
		
# Driver code
string = 'madam'
palindrome(string)
symmetry(string)

# program to check two arrays equal or not
arr1=[1,2,3,4,5]
arr2=[1,3,4,5,7]
if len(arr1) == len(arr2):
    print("array is equal")
else:
    print("array is not equal") 


