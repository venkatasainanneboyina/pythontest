# program to reverse numbers
n = int(input("Please give a number: "))
print("Before reverse your number is : %d" %n)
reverse = 0
while n!=0:
    reverse = reverse*10 + n%10       
    n = (n//10)
print("After reverse : %d" %reverse) 

#2 progam to reverse numbers
num = int(input("Please give a number: "))
print("Before reverse your number is : %d" %num)
rev = int(str(num)[::-1])
print("After reverse the number:", rev)

# program to reverse numbers
def reverse(num):
    if num < 10:
        return num
    else:
        return (num % 10) * 10**(len(str(num))-1) + reverse(num // 10)
num = int(input("Please enter a number: "))
print("Before reverse your number is : %d" %num)
rev = reverse(num)
print("After reverse the number:", rev)

#program to fibonacci numbers
n = int(input("please give a number for fibonacci series : "))
first,second=0,1
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        result=i
    else:
      result = first + second;
      first = second;
      second = result;
    print(result)

    #program find greatest 
    n1 = int(input("please give first number n1: "))
n2 = int(input("please give second number n2: "))
n3 = int(input("please give third number n3: "))
if n1>=n2 and n1>=n3: 
	print(" n1 is greatest");
if n2>=n1 and n2>=n3:
	print(" n2 is greatest");
if n3>=n1 and n3>=n2:
	print("n3 is greatest");

#program to swap numbers
a = int(input("please give first number a: "))
b = int(input("please give second number b: "))
a=a-b
b=a+b
a=b-a
print("After swapping")
print("value of a is : ", a);
print("value of b is : ", b); 

#program to check number perfect number or not in python
num = int(input("please give a number: "))
sum=0
for i in range(1,(num//2)+1):
    remainder = num % i
    if remainder == 0:
        sum = sum + i
if sum == num:
    print("given input is perfect number")
else:
    print("given input is not a perfect number") 