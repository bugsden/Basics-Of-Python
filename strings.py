#Converting a string to uppercase

intro = 'Hello There'
print(intro.upper())

#To find the index number of something in a string

y = input("What do you want to find from the string Hello There? ")
print(intro.find(y))

#But what if you just want to know if the y exists in the string

print(y in intro)

#Now say you want to replace variable y with something else

x = input("What do you want to replace it with? ")
print(intro.replace(y,x))


