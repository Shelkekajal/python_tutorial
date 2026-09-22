#average of two number
'''a=int(input("enter number a :"))
b=int(input("enter number b :"))
avg=(a+b)/2
print("average :",int(avg))'''

# Write a program that asks the user for their name and age, then prints 

'''a=str(input("enter name :"))
b=int(input("enter age :"))
print("Hello",a,"you are ",b,"years old!")'''

#Take two numbers as input from the user and print their sum, difference, product  and quotient
'''num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
print("sum :",num1+num2)
print("Difference :",num1-num2)
print("product :",num1*num2)
print("quotient :",num1/num2)'''


#Ask the user to enter two integers and one float. Convert them all to floats and print their average.
'''a=12
b=32
c=12.1
print(float(a),"and",float(b))
print("average :",(a+b+c)/3)'''


#The user enters a string containing a number (e.g., ). Convert it to:Q4 "45"• an integer• a float • a string again
#Print all three values with their types.
from streamlit import user


num="45"
print(int(num),"type :",type(int(num)))
print(float(num),"type :",type(float(num)))
print(str(num),"type :",type(str(num)))

# Evaluate and print the result of the following expression: x = 10 + 3 * 2 ** 2
#Based on what you learnt in the lecture explain why the output is what it is

x = 10 + 3 * 2 ** 2
print(x)


#Write a program to swap  values of two numbers entered by the user
a=10
b=11
temp=a
a=b
b=temp
print("a :",a)
print("b :",b)

#'''Ask the user for a temperature in Celsius (string input). Convert it to ,then calculate and print temperature in Fahrenheit.float
#Conversion formula: F ahrenheitT emp = (CelsiusT emp ∗ (9/5)) +32

temp=float(input("enter temp in celsius :"))
fahrenheit=(temp*(9/5))+32
print("fahrenheit :",fahrenheit)

#Take the radius ( ) as user input and print the area.Q8 r
#Use the formula: π * (value of π = 3.14)Area = r2
r=int(input("enter the radius :"))
Area=3.14*r*r
print("area of radius :",Area)


#Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and compute simple interest: float
#SI = (P ∗ R ∗ T )/100

p=12
r=11
t=10
SI=(p*r*t)/100
print("SIMPLE INTEREST IS :",float(SI))