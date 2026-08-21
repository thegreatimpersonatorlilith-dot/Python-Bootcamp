capital = float(input("Enter the capital: "))
AIR = float(input("Enter the annual interest rate (percentage): "))
years = int(input("Enter the number of years: "))
times = int(input("Enter the number of times interest is calculated per year: "))

final_amount = capital * (1 + AIR / (times * 100)) ** (times * years)

print(f"Final amount: {final_amount}")