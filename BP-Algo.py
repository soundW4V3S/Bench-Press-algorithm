def algo(nums, inputNumber):
    # Now we begin
    

    # Using math to isolate one side of the bar. Given the bar is 25lbs, 
    # and our target is inputNums, we can create the function:
    # 
    # f(inputNumber) = (inputNumber - 25) / 2, 
    # 
    # where the division of 2 isolates to one side of the bar.
    # 
    # -- We use float division to ensure we don't round-down with integer division.
    
    isolatedSide = (inputNumber - 25.0) / 2.0

   
    print(f"\n\n-- Your side's target weight is: \"{isolatedSide}lbs\" --\n")
    

    # iterator
    i = 0
    
    while ((isolatedSide > 0) and (i < len(nums))):

        # If isolatedSide is divisible by number, but there is still a remainder
        if ( ((isolatedSide / nums[i]) > 0) and ((isolatedSide % nums[i]) > 0) ):
            
            # Avoiding printing "You can add 0 weights of (nums[i])"
            if ((int(isolatedSide / nums[i])) > 0):
                print(f"\nYou can add {int(isolatedSide / nums[i])} weight(s) of {nums[i]}lbs")
                # We need to cast to an int here to ensure we don't go straight to isolatedSide.
                # Fractional math, yo.
                isolatedSide = isolatedSide - (nums[i] * (int(isolatedSide / nums[i])))
        
        # If isolatedSide is evenly divisible by number found in list
        elif ( ((isolatedSide / nums[i]) > 0) and ((isolatedSide % nums[i]) == 0) ):
            print(f"\nYou can add {int(isolatedSide / nums[i])} weight(s) of {nums[i]}lbs")
            isolatedSide = isolatedSide - (nums[i] * (isolatedSide / nums[i]))


        i += 1


    # If weight still remains that can't be added to given our current weights
    if (isolatedSide > 0):
        print(f"\n\n{isolatedSide} total lbs remain (For this side of the bar). Thanks for using my algorithm!")

    else:
        print(f"\n\nThanks for using my algorithm!")
        


def inputting(target):

    # User entering custom weight numbers BELOW HERE


    # temp is for while loop and continuous weight-adding. 
    # weightNums is for weight numbers added
    temp = False
    weightNums = []

    
    # First initial input
    firstValue = input("Please enter your first (highest) available weight number: ")

    
    # Error testing
    while (1):

        # If first input cannot be a float
        try:
            floatValue = float(firstValue)
            
        except:
            # This is to restart the inputting process
            print("\n-- Error! Invalid input. Retry again. --\n")
            firstValue = input("Please enter your first (highest) available weight number: ")
            
        else: 
            # In the event this is a valid float
            weightNums.append(floatValue)
            break

    

    # If the user continues to add weight numbers
    while (temp == False):
        y = input("Please enter another weight or \"cancel\" to calculate your weights: ")


        # If input string is "cancel"
        if (y == "cancel"):
            algo(weightNums, target)
            # Cancel asking for more weights && enter algorithm function
            temp = True

        else:
            # If input string != "cancel", test to see if it's a valid float
            try:
                floatValue = float(y)
    
            except:
                # If not == "cancel", retry
                print("\n-- Invalid input! Retry. --\n")
                temp = True

            else:
                # Append newly input number (if is a valid float)
                weightNums.append(float(y))
            

def main():

    # JUST A REMINDER FOR ME:
    # Don't use integers. Use floats. Weights can be incremented by decimal numbers too.
    


    print("--++ Assuming the bar is 25lbs... ++--\n\n")    
    

    # Loop is to check to make sure input is valid
    while (1):
        # User-entered target weight
        x = input("Please enter your target bench press weight: ")


        # In the event someone enters something other than a float
        try:
            x = float(x)
            # Input is a valid float. Break from while loop.
            break
            
        except:
            # Not a float. Re-loops.
            print("\n-- Incorrect format! Try again. --\n")
    

    # This is just for formatting.
    print("\n\n--++== Please enter your available weights in descending order ==++--\n\n")
    
    
    # Will use this for inputting. Passing target weight as a float.
    inputting(x)
            

main() 
# Entry point
