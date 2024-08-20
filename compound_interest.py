principle = 0
rate = 0
time = 0

# OPTIONAL: Change how many times interest is applied per time period (default is once per year)
#applied = 1

while principle <= 0:
    principle = float(input("Enter principle amount: "))
    if principle <= 0:
        print("You can't get interest on 0 or less")

while rate <= 0:
    rate = float(input("Enter interest rate %: "))
    if rate <= 0:
        print("You can't get interest that is 0 or less")

while time <= 0:
    time = float(input("Enter time period in years: "))
    if time <= 0:
        print("Time period can't be 0 or less")

#while applied <= 0:
#    applied = float(input("Enter how many times interest is applied per year: "))
#    if applied <= 0:
#        print("What's the point of this calculator if you aren't applying interest?")

compound_interest = principle * (1 + rate / 100) ** time
#compound_interest_applied = principle * (1 + ((rate / 100) / applied)) ** (applied * time)

print(f"Value after {time} years: ₤{compound_interest:.2f}")
#print(f"Value after {time} years being applied {applied} times/year: ₤{compound_interest_applied:.2f}")
