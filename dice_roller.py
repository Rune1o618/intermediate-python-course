import random #Generating Random Numbers



def main():
  dice_sum  = 0  
  dice_rolls = 2
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    dice_sum = dice_sum + roll
    print("You have rolled a {0}.".format(roll))
    print("You have a total dice sum of {0}!".format(dice_sum))
    

if __name__== "__main__":
  main()
