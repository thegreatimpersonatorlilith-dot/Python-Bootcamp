# P001 - Task 3 (Week 3)
numbers=[]
seen=[]
dup=[]
while True:
    number=int(input("Enter number: "))

    if number==0:
        break
    else:
        numbers.append(number)

for num in numbers:
    if num not in seen:
        seen.append(num)
    elif num not in dup:
        dup.append(num)

for num in dup:
    print(f"{num} → {numbers.count(num)} times")

unique_numbers = list(set(numbers))
unique_count = len(unique_numbers)
most_repeated = None
max_count = 0

for num in dup:

    count = numbers.count(num)

    if count > max_count:
        max_count = count
        most_repeated = num

print("\nAnalysis Report")
print("------------------------------------")
print(f"Main list: {numbers}")
print(f"Total numbers: {len(numbers)}")

if dup:

    print("Duplicate numbers and their counts:")

    for num in dup:
        print(f"{num} → {numbers.count(num)} times")

    print(f"Most repeated number: {most_repeated} ({max_count} times)")

else:
    print("No duplicate numbers found")


print(f"List without duplicates: {unique_numbers}")
print(f"Number of unique numbers: {unique_count}")
