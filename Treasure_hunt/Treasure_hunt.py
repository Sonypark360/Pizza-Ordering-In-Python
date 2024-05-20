print('''   __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
      
      ''')

print("Welcome to Treasure Hunt. \n Your mission is to find the treasure.")
direction = input("Left or Right?\n").lower()

if direction == "left" :
   swim_wait = input("Swim or Wait?\n").lower()

   if swim_wait == "wait" :
      door = input("Now your here. Which Door? Red, Blue or Yellow?\n").lower()
      if door == "red" :
         print("Burned by Fire. \n Your dead")
      if door == "blue" :
         print("Eaten by Beast. \n your dead")
      if door == "yellow" :
         print ("Congratulations. You Found the quest!")
      else:
         print ("Game Over")        

   else :
      print("Attacked by a Crocodie.\n Your Dead")  
else :
   print("Fall into a hole. \n Game Over.") 
