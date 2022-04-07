# Here we learn type conversion where in we convert one data type into another
name = input("What is your name? \n")
length = len(name) #length is an integer so we cannot use it directly to concatinate with a string
new_length = str(length)
print("Your name has " + new_length + " characters!")

# More examples of type conversion

a = 150
print(type(a))
print(a)

print(type(str(a)))
print(str(a))

print(type(float(a)))
print(float(a))
