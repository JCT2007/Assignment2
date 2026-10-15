"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
MCDONALD_BURGER = 2.99


def cost_per_semester(annual_cost):
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    return annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)


def cost_per_credit(annual_cost, credits):
    return (annual_cost / SEMESTERS_PER_YEAR) / credits


def cost_per_class(annual_cost, credits):
    return (((annual_cost / SEMESTERS_PER_YEAR) / credits) * CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER


def fast_food(annual_cost):
    return int(annual_cost / MCDONALD_BURGER)


def main():
    annual_cost = float(input("Enter total cost for one year: "))
    credits = float(input("Enter credits this semester: "))

    while True:
        print("1: Cost per semester")
        print("2: Cost per month")
        print("3: Cost per day")
        print("4: Cost per credit")
        print("5: Cost per class")
        print("6: Bonus")
        print("Q: Exit")
        choice = str(input("Choose an option: "))

        if choice == "Q":
            break
        elif choice == "1":
            semester_price = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${semester_price:.2f}")
        elif choice == "2":
            month_price = cost_per_month(annual_cost)
            print(f"Monthly cost: ${month_price:.2f}")
        elif choice == "3":
            day_cost = cost_per_day(annual_cost)
            print(f"Daily cost: ${day_cost:.2f}")
        elif choice == "4":
            credit_cost = cost_per_credit(annual_cost, credits)
            print(f"Per credit cost: ${credit_cost:.2f}")
        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"Each CS1430 class is: ${class_cost:.2f}")
        elif choice == "6":
            burger_amount = fast_food(annual_cost)
            print(f"You could buy {burger_amount} McDonald's cheeseburgers instead")
        else: print("Invalid option")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
