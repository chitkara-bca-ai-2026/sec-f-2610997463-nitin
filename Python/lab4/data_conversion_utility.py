#  Data Conversion Utility

print("========================================")
print("       DATA CONVERSION UTILITY")
print("========================================")

product_name = input("Enter Product Name : ") 
price = float(input("Enter Price        : ")) 
quantity = int(input("Enter Quantity     : ")) 

total_price = price * quantity 


amount_str = str(total_price) # str() se string me convert 

# type check of every variable
print("\n----------------------------------------")
print("        TYPE CASTING SUMMARY")
print("----------------------------------------")
print(f"product_name   {product_name}     {type(product_name)}") # type() for type 
print(f"price          {price}     {type(price)}")
print(f"quantity       {quantity}       {type(quantity)}")
print(f"total_price    {total_price}     {type(total_price)}")
print(f"amount_str     {amount_str}     {type(amount_str)}")

# display tax invoice 
print("\n----------------------------------------")
print("             TAX INVOICE")
print("----------------------------------------")
print(f"Product Name  : {product_name}")
print(f"Price per Unit: Rs. {price}")
print(f"Quantity      : {quantity}")
print(f"----------------------------------------")
print(f"Invoice Total : Rs. {amount_str}") # amount str for toal 
print("========================================")