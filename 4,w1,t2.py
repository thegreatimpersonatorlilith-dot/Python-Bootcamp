price=int(input("whats the price? "))
off=int(input("how much of a discount? "))
total_price=float(price-(price*(off/100)))
print(f"the total price is {total_price}")