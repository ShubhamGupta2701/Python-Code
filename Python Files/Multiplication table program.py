# Program for Multiplication Table


num = int(input("Enter the Number : "))
print("Multipilcation table of ", num)
for i in range(1,11):
    print(num,'*',i,"=" ,num*i)
    