print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
full_name = name1 + name2
lowercase_name = full_name.lower()
t = lowercase_name.count("t")
r = lowercase_name.count("r")
u = lowercase_name.count("u")   
e = lowercase_name.count("e")
true_total = t+r+u+e 

l = lowercase_name.count("l")
o = lowercase_name.count("o")
v = lowercase_name.count("v")
e = lowercase_name.count("e")
love_total = l+o+v+e

total_score = int(str(true_total) + str(love_total))
if (total_score < 10) or (total_score > 90):
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
  print(f"Your score is {total_score}, you are alright together.")
else:
 print(f"Your love score is {total_score} .")
