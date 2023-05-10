num1 = int(input("First Number : "))
num2 = int(input("Second Number : "))


maximum = 0
minimum = 0

if(num1 == num2):
    print("Equal")
else:
    if(num1 < num2):
        maximum = num2 
        minimum = num1
        print("max", maximum)
        print("min", minimum)
    else:
        maximum = num1
        minimum = num2
        print("max", maximum)
        print("min", minimum)


