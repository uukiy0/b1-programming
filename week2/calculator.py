#A calculator that accepts user input, performs calculations and displays formatted results with proper error handling and documentation.# 

#Get revenue from user

revenue = float(input("Enter total revenue: $"))
#Get costs from user

costs = float(input("Enter total costs: $"))

#Ensure correct input as costs cannot be negative
while costs < 0: 
    print("Invalid input only positive numbers accepted")

    costs = float(input("Enter total costs: $"))

#Calculate profit

profit = revenue - costs

#Calculate profit margin percentage 

margin = (profit/revenue) * 100

#Display results

print("\n--- Finacial Summary ---")
print(f" Revenue: ${revenue:,.2f}")
print(f"Costs: ${costs:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:.1f}%")
