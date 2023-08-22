name = input("What is your name ")
birth_year = int(input("What is your birth year "))
age = 2023 - birth_year
is_new = True
print("Hello ", name)
print("Here are your details of")
print( "Name = ",name,"Age =",age)
if (is_new==True):
    print("The patient is new")
else:
    print("This is an old patient")
