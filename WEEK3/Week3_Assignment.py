#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (discount_percent/100 * price)
    else:
        final_price = price

    return f"The Final Price after a discount of {discount_percent}% is: {final_price}"
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.   

price = float(input("Enter the Original Price:"))
discount_percent = float(input("Enter the Discount percentage(Don't put  the percentage sign):"))
print(calculate_discount(price, discount_percent))

