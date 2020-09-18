import random #Generating Random Numbers
def main():
  
    
  dice_rolls = int(input("How many die would you like to roll?\n"))
  dice_size = int(input("What is the size of the dice that you would like to roll?\n"))
  dice_sum = 0 
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    print("You have rolled {0}".format(roll))
  dice_sum = dice_sum + roll
  return dice_sum

result = main()
while result == 6:
  print("Amazing you rolled a perfect{0}! Gods have granted you entry into Valhallah!Entry\n".format(result))
else:
     print("You have rolled a {0}!! Alas! You shall Not Passss!!!\n".format(result))
     user_input = input("Would you like to try again? Select [y] to continue! [n] to give up!\n")
     while (user_input.lower() != 'y' and user_input.lower() != 'n' ):
       user_input = input("Wrong Input Idiot: Try Again! Press Y/N to continue/stop")
     if (user_input.lower() == 'y'):
       main()
     else:
       print("You live to try another day!")
    
    
    
    
#if result == 6:
 # print("Amazing you rolled a perfect{0}! Gods have granted you entry into Valhallah!Entry\n".format(result))
#else:
 # print("You have rolled a {0}!! Alas! You shall Not Passss!!!\n".format(result))

if __name__== "__main__":
  main()


  
