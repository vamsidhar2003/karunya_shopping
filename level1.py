print("the karunya shopping website")
print("done by the team")
print("kakani vamsidhar - URK21EC5003")
print("k. rajdev - URK21EC6024")
print("m.kesava reddy - URK21EC6019")
print("thrithwik - URK21EC6036")

def print_item_info(item_code, description, quality, qty, cost_item):
    print("THE ITEM CODE:", item_code)
    print("Description:", description)
    print("Quality:", quality)
    print("Quantity:", qty)
    print("Item Cost:", cost_item)

def cart():
    print("The total items in the cart are", n)

def calculating_cost(n, cost_item):
    cost = n * cost_item
    print("The total cost of the items is", cost)
    return cost

def membership(cost):
    name = input("Enter your name: ")
    print("Choose the type of membership")
    i = input("silver, gold, or platinum: ")
    if i == 'silver':
        cost1 = cost - 0.05 * cost
        print("The total cost is", cost1)
    elif i == 'gold':
        cost1 = cost - 0.1 * cost
        print("The total cost is", cost1)
    elif i == 'platinum':
        cost1 = cost - 0.2 * cost
        print("The total cost is", cost1)
    return cost1

def gst_calculation(cost):
    import math
    tax = math.ceil((cost + 0.06) * 0.07)
    print("GST amount is", tax)
    final_amount = cost + tax
    print("Final amount before surcharge and convenience fee:", final_amount)
    return final_amount

def platform_fee(final_amount):
    fee = final_amount * 0.2
    print("Platform charge is $", fee)
    return fee

def generate_invoice(final_amount, payment_mode):
    if final_amount < 1000 and payment_mode.lower() == "card":
        surcharge = final_amount * 0.025
        final_amount += surcharge
        print("Surcharge (2.5%) applied for card payment. New total:", final_amount)
    else:
        convenience_fee = final_amount * 0.01
        final_amount += convenience_fee
        print("Convenience fee (1%) applied for other payment modes. New total:", final_amount)

    print("Final Invoice Total (including charges):", final_amount)
    print("Invoice generated. Payment received.")

# Example usage
item_code = int(input("Enter the item code: "))
description = input("Enter the description: ")
qty = int(input("Enter the quantity: "))
cost_item = float(input("Enter the cost: "))
n = int(input("Enter the total quantity: "))

print_item_info(item_code, description, qty, cost_item, n)

total_cost = calculating_cost(n, cost_item)

membership_discounted_cost = membership(total_cost)

gst_total = gst_calculation(membership_discounted_cost)

platform_charge = platform_fee(gst_total)

payment_mode = input("Enter the payment mode (card or other): ")
generate_invoice(gst_total, payment_mode)
