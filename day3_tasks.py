# P001 - Day 3
#1
# numbers=input("Enter 4 numbers: ").split()
# a,b,c,d=map(float,numbers)
# avg=a*b*c*d/4
# print(f"Average is: {avg:.2f}")

#2
# hours=float(input("Please enter the number of hours: "))
# minutes= hours*60
# seconds=hours*3600
# print(f"{hours} hours {minutes} minutes and {seconds} seconds.")

#3
# base1 = float(input("Enter the length of the first base: "))
# base2 = float(input("Enter the length of the second base: "))
# height = float(input("Enter the height: "))
# area = (base1 + base2) * height / 2

# print(f"The area of the trapezoid is: {area}")

#4
# r= float(input("Enter the radius of the cylinder: "))
# h = float(input("Enter the height of the cylinder: "))

# pi = 3.14159
# volume = pi * (r ** 2) * h

# print(f"The volume of the cylinder is: {volume}")

#5
# numbers=input("Enter 3 numbers: ").split()
# num1, num2, num3=map(float,numbers)

# total_sum = num1 + num2 + num3
# average = total_sum / 3

# print(f"The sum is: {total_sum}")
# print(f"The average is: {average}")

# #6
# price = float(input("Enter the price: "))
# discount = float(input("Enter the discount percentage: "))
# tax = float(input("Enter the tax percentage: "))

# final_price = price - (price * discount / 100) + (price * tax / 100)

# print(f"Final price: {final_price:.2f}")

# #7
# meters = float(input("Enter in meters: "))

# centimeters = meters * 100
# millimeters = meters * 1000
# kilometers = meters * 0.001

# print(f"Centimeters: {centimeters}")
# print(f"Millimeters: {millimeters}")
# print(f"Kilometers: {kilometers}")

# #8
# side = float(input("Enter the side length of the cube: "))

# s = 6 * (side * side)
# volume = side * side * side

# print(f"Total surface area: {s:.3f}")
# print(f"Volume: {volume:.3f}")

# #9
# distance = float(input("Enter the total distance (km): "))
# time = float(input("Enter the total time (hours): "))

# average_speed = distance / time

# print(f"Average speed: {average_speed:.2f} km/h")

#10
weight = float(input("Enter your weight (kg): "))
height_cm = float(input("Enter your height (cm): "))

height_m = height_cm / 100

bmi = weight / (height_m * height_m)

print(f"BMI: {bmi:.2f}")
