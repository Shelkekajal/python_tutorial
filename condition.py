#if,elif,else
age=int(input("enter a age :"))
if(age<=13):
    print("child")
elif(age>=13 and age<=18):
    print("teenage")
else:
     print("adult")   


#2
username=input("enter username :")
password=input("enter password :")
if(username=="admin" and password=="pass"):
    print("LOGIN SUCCESSFULLY")
else:
    print("WRONG PASSWORD OR USERNAME") 


#3
number=int(input("Enter number :"))
if(number%2==0):
    print("Even number is :",number)
else:
    print("odd number :",number)    


#4 nested if else


age = 20
has_id = True

if age >= 18:
    print("You are an adult")

    if has_id:
        print("You can enter")
    else:
        print("ID is required")
else:
    print("You are under 18")