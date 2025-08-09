import math
number = float(input("Enter a  number : "))
if number <= 0:
    print(" enter a number greater than 0 ")
else:
    s = math.sqrt(number)
    l = math.log(number)
    print(f"Square root of {number} = {s}")
    print(f"Natural log of {number} = {l}")
b = math.radians(number)
f = math.sin(b)

print(f"Sine of {number} = {f}")