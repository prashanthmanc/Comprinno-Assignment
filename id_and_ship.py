# take the length input

length = int(input())
for iterate in range(length):

	# iterate over every value and read the char
    current_value  = input()
    
    #check all possible condtions using if ladder and print 	   required output
    if current_value  == "B" or current_value  == "b":
        print("BattleShip")
    else if current_value  == "C" or current_value  == "c" :
        print("Cruiser")
    else if current_value  == "D" or current_value  == "d":
        print("Destroyer")
    else:
       print("Frigate")
