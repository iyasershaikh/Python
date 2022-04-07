# Input height and weight
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Convert to required data type
h = float(height)
w = float(weight)

# Calculate BMI
bmi = w / h ** 2

print (int(bmi)) # Using Int Data type conversion will eliminate decimal values