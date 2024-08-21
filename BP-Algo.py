# WELCOME TO MY BENCH PRESS PROGRAM/ALGORITHM
# 2 || 3 improvements to come.
#
# 1: weight number on each side to target weight
# 2: Planet Fitness standard weights (to reduce time taken by typing out 45, 25...)
# 3: 45lb bar in the event there's a bigger bar and a different gym (e.g. LA/The Edge)
#
# UPDATE 1.1: COMPLETED ABOVE-LISTED FEATURES. FASTER OVERALL FUNCTIONALITY W/ LESS REQUIRED TYPING.


def algo(nums, inputNumber, pfTrueInput2):
    # Now we begin
    

    # Using math to isolate one side of the bar. Given the bar is 25lbs, 
    # and our target is inputNums, we can create the function:
    # 
    # f(inputNumber) = (inputNumber - 25) / 2, 
    # 
    # where the division of 2 isolates to one side of the bar.
    # 
    # -- We use float division to ensure we don't round-down with integer division.


    
    # If at Planet Fitness, use 25.0 bar weight
    if (pfTrueInput2 == "y"):
        isolatedSide = (inputNumber - 25.0) / 2.0

    # Else we're not at Planet Fitness, use a 45.0 lb bar weight
    else:
        isolatedSide = (inputNumber - 45.0) / 2.0

    
   
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


    return
        

def racking(pfTrueInput2):

    # Racking function. Here you can see how much you're racking in total.

    # Total amount racked so far. Variable used for tracking.
    # If at Planet Fitness, initial Bar weight is 25.0 lbs
    if (pfTrueInput2 == "y"):
        sum = 25.0
    # Else (base case is "n"), it is 45.0 lbs
    else:
        sum = 45.0


    print()   # Newline
        

    
    while (1):
        # User input for adding a weight

        temp = input("\nPlease enter a weight (\"c\" to cancel): ")
        
        if (temp == "c"):
            break
            
        else:
            try:
                # Input is not a valid float, but is also not "c"
                temp = float(temp)
    
            except:
                print("\nError! Invalid weight.")
                
            else:
                # If we were to add the total weight of the variable "temp" on both sides of the bar
                sum += (temp * 2)


    # Once loop is broken, state total weight racked.
    print(f"\n\nYou're racking {sum} in total.\n\n\nThank you for using my program!")

    
    return
    

def inputting(target, pfTrueInput):

    # User entering custom weight numbers BELOW HERE


    # weightNums is for weight numbers added
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
    while (1):
        y = input("\nPlease enter another weight or \"c\" to calculate your weights: ")


        # If input string is "c"
        if (y == "c"):
            algo(weightNums, target, pfTrueInput)
            # Cancel asking for more weights && enter algorithm function
            break

        else:
            # If input string != "c", test to see if it's a valid float
            try:
                floatValue = float(y)
    
            except:
                # If not == "c", retry
                print("\n-- Invalid input! Retry. --")

            else:
                # Append newly input number (if is a valid float)
                weightNums.append(float(y))


    return



def main():

    # JUST A REMINDER FOR ME:
    # Don't use integers. Use floats. Weights can be incremented by decimal numbers too.
    
    
    
    # If user is at Planet Fitness (45.0, 25.0, 10.0, 5.0, 2.5 lb standard)
    pfTrue = None   # NULL temporarily. More used to C++.
    while (1):
        pfTrue = input("Are you at Planet Fitness? (y/n): ")
        if (pfTrue == "y"):
            print("\n")
            break
        elif (pfTrue == "n"):
            print("\n")
            break


    
    # Letting the User decide their input type. Since my friend and I usually say; 
    # "Rack on a 45", or "Rack on a 25", this calculator will have 2 uses. 1 for checking
    # how much you're racking, and 1 for hitting a target weight.
    calculationType = None
    while (1):
        calculationType = input("See how much you're racking? Or calculate a goal? (s/c): ")
        if (calculationType == "s"):
            # Call racking function to see how much you're racking in total && Send PF boolean state
            racking(pfTrue)
            # End program once complete
            return
        elif(calculationType == "c"):
            # Continue with standard algorithm sequence
            break
        

    print("\n")  # Newlines
    

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


    
    # If User is at planet fitness. Uses PF standard weights.
    # Sends common PF weights && target weight
    if (pfTrue == "y"):
        algo([45.0, 25.0, 10.0, 5.0, 2.5], x, pfTrue)
        # Return to exit program
        return
    
    

    # This is just for formatting.
    print("\n\n--++== Please enter your available weights in descending order ==++--\n\n")
    
    
    # Will use this for inputting. Passing target weight as a float.
    inputting(x, pfTrue)
            

main() 
# Entry point
