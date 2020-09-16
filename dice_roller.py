import random #Generating Random Numbers



def main():
  
    
  dice_rolls = int(input("How many die would you like to roll?\n"))
  dice_size = int(input("What is the size of the dice that you would like to roll?\n"))
  dice_sum = 0 
  for i in range(0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum = dice_sum + roll
    if roll == 1:
      print("You have rolled a {0}! Critical Fail\n".format(roll))
    elif roll == 6:
      print("You have rolled a {0}! Critical Success\n".format(roll))
    else:
      print("You have rolled a {0}!\n".format(roll))
      
    
  
  print("You have a total dice sum of {0}!".format(dice_sum))
    

if __name__== "__main__":
  main()
