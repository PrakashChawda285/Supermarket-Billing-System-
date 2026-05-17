# # Supermarket Billing System
# 
# ## Overview
# This system allows a cashier to enter multiple items, specify quantities, 
#  apply discounts based on total purchase amount, and generate an itemized receipt.
# 
# ## Algorithm
# 1. Initialize empty lists to store item names, quantities, and prices
# 2. Loop to accept items until user chooses to finish
# 3. For each item, get name, quantity, unit price
# 4. Calculate item total = quantity × price
# 5. Store all information
# 6. Calculate subtotal = sum of all item totals
# 7. Apply discount based on subtotal using conditional statements
# 8. Calculate final total = subtotal - discount
# 9. Display itemized bill with all details
# 10. Show discount and final amount due

# ## Implementation
from datetime import datetime
def supermarket_billing_system():
    """
    Main function to run the supermarket billing system.
    Handles item input, discount calculation, and receipt generation.
    """
    
    # Initialize lists to store billing data
    items = []          # Store item names
    quantities = []     # Store quantities
    prices = []         # Store unit prices
    item_totals = []    # Store total for each item (quantity × price)
    date_time = datetime.now().strftime("%d/%m/%Y %H:%M")

    print("\n" + "="*50)
    print("     WELCOME TO SUPERMARKET BILLING SYSTEM")
    print("="*50)
    

    # Loop to accept multiple items (Key Requirement: Use loops for continuous input)
    while True:
        print("\n--- Enter Item Details ---")
        
        # Get item name
        item_name = input("Item name (or 'done' to finish): ").strip()
        
        # Check if user wants to finish billing
        if item_name.lower() == 'done':
            if len(items) == 0:
                print("\nNo items entered. Exiting system.")
                return
            break
        
        # Get quantity with validation
        while True:
            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Get unit price with validation
        while True:
            try:
                price = float(input("Unit price (₹): "))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid price.")
        
        # Calculate total for this item
        total = quantity * price
        
        # Store data
        items.append(item_name)
        quantities.append(quantity)
        prices.append(price)
        item_totals.append(total)
        
        print(f"✓ Added: {quantity} x {item_name} @ ₹{price:.2f} = ₹{total:.2f}")
    
    # Calculate subtotal
    subtotal = sum(item_totals)
    
    # Apply discounts based on total amount (Key Requirement: Conditional statements)
    discount_percentage = 0
    discount_amount = 0
    
    if subtotal >= 5000:
        discount_percentage = 15
        discount_amount = subtotal * 0.15
        discount_reason = "15% discount (Purchase above ₹5000)"
    elif subtotal >= 3000:
        discount_percentage = 10
        discount_amount = subtotal * 0.10
        discount_reason = "10% discount (Purchase above ₹3000)"
    elif subtotal >= 1500:
        discount_percentage = 5
        discount_amount = subtotal * 0.05
        discount_reason = "5% discount (Purchase above ₹1500)"
    elif subtotal >= 500:
        discount_percentage = 2
        discount_amount = subtotal * 0.02
        discount_reason = "2% discount (Purchase above ₹500)"
    else:
        discount_reason = "No discount applicable"
    
    # Calculate final total
    final_total = subtotal - discount_amount
    
    # Generate and display itemized receipt (Key Requirement: Itemized bill)
    print("\n" + "="*60)
    print("                     BILL RECEIPT")
    print("="*60)
    print(f"{'Item':<20} {'Qty':<6} {'Price(₹)':<10} {'Total(₹)':<12}")
    print("-"*60)
    
    for i in range(len(items)):
        print(f"{items[i]:<20} {quantities[i]:<6} ₹{prices[i]:<9.2f} ₹{item_totals[i]:<11.2f}")
    
    print("-"*60)
    print(f"{'Subtotal':<36} ₹{subtotal:<11.2f}")
    print(f"{discount_reason:<36} -₹{discount_amount:<10.2f}")
    print("-"*60)
    print(f"{'FINAL AMOUNT DUE':<36} ₹{final_total:<11.2f}")
    print("="*60)
    
    # Payment processing
    print("\n--- Payment ---")
    while True:
        try:
            amount_paid = float(input("Amount paid (₹): "))
            if amount_paid < final_total:
                print(f"Insufficient amount. Need ₹{final_total - amount_paid:.2f} more.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    
    change = amount_paid - final_total
    print(f"\nChange to return: ₹{change:.2f}")
    print("\n" + "="*60)
    print("     THANK YOU FOR SHOPPING WITH US!")
    print("     Please visit again!")
    # ("PRAKASH CHAWDA")
    print("Date" , date_time)
    print("="*60 + "\n")

# Run the billing system
if __name__ == "__main__":
    supermarket_billing_system()