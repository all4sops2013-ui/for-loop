# Write a program to print the numbers in reverse order beginning from the number entered by the user.

num = int(input("Enter a number: "))
for i in range(1,9,1):
    num = num - 1
    print(num)



i=1
while i<=14:
    print(i)
    i+=1
print('Done !!')



# WAP to take a number from the user and print the number of digits in that number using a while loop

num = int(input("Enter a number: "))
count = 0
while num!= 0:
    num=num//10
    count=count+1
print(count)
