numbers = input("Enter 3 numbers: ").split()

a, b, c = map(float, numbers)

total = a + b + c
average = total / 3

print(f"Sum: {total}")
print(f"Average: {average}")