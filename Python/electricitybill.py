unit=int(input("Enter the units : "))

if(unit<=100):
    amt=unit*1.5

elif(unit>100 and unit<=200):
    amt=(unit*1.5)+((unit-100)*2.5)

elif(unit>200 and unit<=300):
    amt=(unit*1.5) + ((200-100)*2.5 +(unit-200)*4)

elif(unit>300 and unit<=350):
    amt=(unit*1.5) + (200-100)*2.5 + (300-200)*4 + (unit - 350)*5

else:
    amt=1500

print(amt)