principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can't be less than or equal to zero.")

'''
while True:
    principal = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principle can't be less than Zero")
    else:
        break'''

while rate <= 0:
    rate = float(input("Enter the rate percentage: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero.")
# Compound interest formula: A = P * (1 + r/100) ** t
total = principal * pow(1 + rate / 100, time)
print(f"Balance after {time} year(s): {total:.2f}")
