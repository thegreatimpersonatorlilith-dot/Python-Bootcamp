side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

s = (side1 + side2 + side3) / 2

area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5

print(f"Area: {area}")