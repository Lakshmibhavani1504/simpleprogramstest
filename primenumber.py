n=int(input("Enter the number to find if its a prime number"))
for i in range(2,n):
    if n%i==0:
        print("Number is not prime number")
else:
    print("Number is prime")
