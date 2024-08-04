# Author: Jacob Abts
# Submission Date: 7/21/2024
# CSU Global - CSC500-1

# Part 1
def salesTaxCalculator(charge):
    salesTax = round(charge * 0.07, 2)
    print(f"Sales Tax: ${salesTax:.2f}")
    return salesTax

def tipCalculator(charge):
    tip = round(charge * 0.18, 2)
    print(f"Tip: ${tip:.2f}")
    return tip

def part1():
    foodCharge = round(float(input("Please enter the cost of the food: ")), 2)
    tip = salesTaxCalculator(foodCharge)
    salesTax = tipCalculator(foodCharge)
    print(f"Total Price: ${foodCharge + tip + salesTax:.2f}")

# Part 2
def part2():
    currentTime = int(input("Enter the current time (only hours and 24 hour time): "))
    timeTillAlarm = int(input("Enter hours till alarm: "))
    fullTime = (timeTillAlarm + currentTime) % 24
    halfTime = (timeTillAlarm + currentTime) % 12
    if fullTime == halfTime:
        halfID = "am"
    else:
        halfID = "pm"
    if halfTime == 0:
        halfTime = 12
    print(f"Alarm Time: {fullTime} ({halfTime} {halfID})")

# Main Function
def main():
    part1()
    print()
    part2()

main()