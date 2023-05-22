n=int(input("Enter the number to find factorial :"))

fact = 0

while(n>0):
    fact *= n
    n -= 1

print(fact)
