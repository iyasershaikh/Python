# If we want to concatinate different data types while printing something we had to convert each into string
# To this solution we get f-String function which does all the hard work
# Let's take an example

a = 1       #Integer
b = 1.5     #Float 
c = "Yaser" #String

print(f"Hi {c} your height is {b}m and you are {a} of a kind")