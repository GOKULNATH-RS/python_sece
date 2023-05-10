n=int(input("Enter number"))

fact = 0

while(n>0):
    fact *= n
    n -= 1

print(fact)