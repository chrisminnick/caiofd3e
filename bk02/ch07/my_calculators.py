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
