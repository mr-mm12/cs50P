def main():
    # Convert user input (meal cost) to dollars as float
    dollars = dtf(input("How much was the meal? "))
    # Convert user input (percentage) to decimal as float
    percent = ptf(input("What percentage would you like to tip? "))
    # Calculate the tip
    tip = dollars * percent
    # Print the result with two decimal places
    print(f"Leave ${tip:.2f}")


def dtf(d):
    # TODO
    # Remove the "$" sign and convert string to float
    D = float(d.strip("$"))
    return D
# or we can
"""
return flaot(d.strip("$"))
"""

def ptf(p):
    # TODO
    # Remove the "%" sign, convert string to float,
    # then divide by 100 to turn percentage into decimal
    P = float(p.strip("%")) / 100
    return P
# or we can
"""
return flaot(p.strip("%"))
"""
main()

# Mohammad_Reza_Mokhtari_Kia
