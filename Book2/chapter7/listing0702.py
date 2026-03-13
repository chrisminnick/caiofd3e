def calculate_total(price):
  
    # Calculate 7% tax
    tax = price * 0.07
  
    # Is the price at least $50?
    if price >= 50:
  
        # If so, charge a flat rate for shipping
        shipping = 5.00
    else:
  
        # Otherwise, charge 10% of the price for shipping
        shipping = price * 0.1
  
    # Calculate the total
    total = price + tax + shipping
  
    # Return the total
    return total
  
counter = 0
  
while (counter < 3):
    # Get the price
    price = float(input("Enter the price: "))
  
    # Get the total with tax and shipping
    total = calculate_total(price)
  
    print(f"Total with tax and shipping: ${total:.2f}")
  
    counter += 1
