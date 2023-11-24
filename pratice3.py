# Python len()
li = [10, 20, 30]
n = len(li)
print("The length of list is: ", n)

# Python program to find the
# minimum of two numbers
 
 
def minimum(a, b):
     
    if a <= b:
        return a
    else:
        return b
     
# Driver code
a = 2
b = 4
print(minimum(a, b))

#recursive function to print even length words
def PrintEvenLengthWord(itr,list1):
  if itr == len(list1):
    return
  if len(list1[itr])%2 == 0:
    print(list1[itr])
  PrintEvenLengthWord(itr+1,list1)
  return
str = "geeks for geek"
l=[i for i in str.split()]
PrintEvenLengthWord(0,l)

def summation(test_tup):
 
    # Converting into list
    test = list(test_tup)
 
    # Initializing count
    count = 0
 
    # for loop
    for i in test:
        count += i
    return count
 
 
# Initializing test_tup
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))

test_list = [[('Gfg', 3)], [('best', 1)]]
cus_eles = [1, 2]
result_list = []
for i, row in enumerate(test_list):
    result_list.append(list(map(lambda x: x+(cus_eles[i],), row)))
print(result_list)

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)

# function calling
def dictionairy():
 
    # Declaring the hash function
    key_value = {}
 
# Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
     
    print("key_value",key_value)
 
    print("Task 2:-\nKeys and Values sorted in",
          "alphabetical order by the key  ")
     
 
    # sorted(key_value) returns a sorted list
    # of the Dictionary’s keys.
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")
 
 
def main():
        # function calling
    dictionairy()
 
 
# main function calling
if __name__ == "__main__":
    main()

ele = {'a': 5, 'c': 8, 'e': 2}
if "q" in ele:
    print(ele["d"])
else:
    print("Key not found")

    # Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


# Creating a set using string
test_set = set("geEks")

iter_gen = iter(test_set)

while True:
	try:
		# get the next item
		print(next(iter_gen))
		
		''' do something with element '''
		
	except StopIteration:
		# if StopIteration is raised,
		# break from loop
		break

def GFG(name, num): 
    print("Hello from ", name + ', ' + num) 
  
  
GFG("geeks for geeks", "25") 