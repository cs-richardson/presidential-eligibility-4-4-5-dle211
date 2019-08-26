"""
This program checks for the user's eligibility to run for president based on
their age, citizenship, and years of residency.
"""

# Asks the user for their age, citizenship, and years of residency.
age = int(input("Age: "))
citizen = input("Born in the U.S.? (Yes/No): ")
residency = int(input("Years of Residency: "))

# If the user is at least 35 years old, is a U.S. citizen, and lived in the U.S.
# for at least 14 years, they are eligible to run for president.
if age >= 35 and citizen == "Yes" and residency >= 14:
    print("You are eligible to run for president!")

# Otherwise, they are not eligible to run for president.
else:
    print("You are not eligible to run for president.")

# Tells the user what qualities they're missing to be eligible to run for
# president.
if age < 35:
    print("You are too young. Youmust be at least 35 years old.")
if citizen != "Yes":
    print("You must be born in the U.S. to run for president.")
if residency < 14:
    print("You have not been a resident for long enough.")
