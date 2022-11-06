# to find the sum of odd numbers between 0 to 'n'S
n=int(input("Enter the number : "))
s=0
for i in range(1,n+1):
    if i%2!=0:
        s+=i
print(s)