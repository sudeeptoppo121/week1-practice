def calculate_salary(basic_salary, bonus_percentage=5):
    bonus_amount = basic_salary * (bonus_percentage / 100)
    final_salary = basic_salary + bonus_amount
    return bonus_amount, final_salary


# Input Section
name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: "))

choice = (
    input("Does the employee have a special bonus percentage? (yes/no): ")
    .strip()
    .lower()
)

# Call function based on user choice
if choice == "yes":
    bonus_percentage = float(input("Enter Special Bonus Percentage: "))
    bonus_amount, final_salary = calculate_salary(
        basic_salary, bonus_percentage
    )
else:
    bonus_percentage = 5.0  # Default value used for display
    bonus_amount, final_salary = calculate_salary(basic_salary)

# Display Section
print("\n--- Employee Salary Details ---")
print(f"Employee Name: {name}")
print(f"Basic Salary: ₹{basic_salary:.2f}")
print(f"Bonus Percentage: {bonus_percentage}%")
print(f"Bonus Amount: ₹{bonus_amount:.2f}")
print(f"Final Salary: ₹{final_salary:.2f}")