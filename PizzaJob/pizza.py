print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
price = int(0)
if size == "S" :
   price = int(15) 
if size == "M" :
   price = int(20)
if size == "L" :
   price = int(25) 

if add_pepperoni == "Y" :
   if size == "S" :   
     price += 2 
   if size == "M" :
    price += 3 
   if size == "L" :
     price += 3
if extra_cheese == "Y" :
   price += 1
print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: {price}")
