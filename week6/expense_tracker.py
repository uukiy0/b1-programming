# Exercise 3: Personal Expense Tracker

# Initialize data structures
# expense_records will store each expense as a tuple category, amount, date
expense_records = []

# category_totals will store total spending for each category
category_totals = {}

# unique_categories will store distinct categories so no duplicates lol
unique_categories = set()

print("=== PERSONAL EXPENSE TRACKER ===")

# Collect expense data,5 expenses
for i in range(1, 6):
    # Get category name 
    category = input(f"Enter expense {i} category: ")
    
    # Convert input into a float for decimal values
    amount = float(input(f"Enter expense {i} amount: "))
    
    # Store date as a string in YYYY-MM-DD format
    date = input(f"Enter expense {i} date (YYYY-MM-DD): ")
    
    # Add the expense as a tuple into the list
    expense_records.append((category, amount, date))


# Process expenses to calculate totals and unique categories
for category, amount, date in expense_records:
    
    # Add category to the set (sets automatically remove duplicates)
    unique_categories.add(category)
    
    # Add amount to the correct category total
    # If category does not exist, start from 0
    category_totals[category] = category_totals.get(category, 0) + amount


# Extract only amounts using list comprehension
all_amounts = [amount for category, amount, date in expense_records]

# Calculate total spending
total_spending = sum(all_amounts)

# Calculate average expense (avoid division by zero)
average_expense = total_spending / len(all_amounts) if all_amounts else 0

# Find the expense record with the highest amount
# lambda x: x[1] tells Python to compare using the amount value
highest_expense_record = max(expense_records, key=lambda x: x[1]) if expense_records else None

# Find the expense record with the lowest amount
lowest_expense_record = min(expense_records, key=lambda x: x[1]) if expense_records else None

# Store statistics inside a dictionary
overall_stats = {
    "total_spending": total_spending,
    "average_expense": average_expense,
    "highest_expense": highest_expense_record,
    "lowest_expense": lowest_expense_record
}

# Generate report
print("\n=== OVERALL SPENDING SUMMARY ===")

print(f"Total Spending: ${overall_stats['total_spending']:.2f}")
print(f"Average Expense: ${overall_stats['average_expense']:.2f}")

# Display highest expense with category and date
if overall_stats["highest_expense"]:
    print(f"Highest Expense: ${overall_stats['highest_expense'][1]:.2f} "
          f"(Category: {overall_stats['highest_expense'][0]}, "
          f"Date: {overall_stats['highest_expense'][2]})")

# Display lowest expense
if overall_stats["lowest_expense"]:
    print(f"Lowest Expense: ${overall_stats['lowest_expense'][1]:.2f} "
          f"(Category: {overall_stats['lowest_expense'][0]}, "
          f"Date: {overall_stats['lowest_expense'][2]})")

print("\n=== UNIQUE CATEGORIES SPENT ON ===")

# Print the set of unique categories
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")

# Loop through each category and display total spending
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")
