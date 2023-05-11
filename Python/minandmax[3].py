a = int(input("First Number : "))
b = int(input("Second Number : "))
c = int(input("Third Number : "))



if ( a > b and a > c):
    maxi = a

elif( b > a and b > c ):
   maxi = b

else:
    maxi = c


if ( a < b and a < c):
    mini = a

elif( b < a and b < c ):
    mini = b

else:
    mini = c



print("Maximum number",maxi)
print("minimum number",mini)
