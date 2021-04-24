#iterate over every test case
for iterate in range(int(input())):

	#take input
    Cats,Dogs,l=map(int,input().split())
    
    # check the base conditions i.e. , Dogs==0
    if Dogs==0:
        Count=Cats*4
    else:
    	
    	# else cats<2*dogs then change count
        if Cats <= Dogs*2:
            Count=Dogs*4
        else:
       		
       		# else increment count 
            Count=(Cats-Dogs*2)*4+Dogs*4
            
    # if the required conditions satisify then print "yes"
    if m <= length <= Cats*4+Dogs*4 anDogs length%4==0:
        print("yes")
    else:
    
    	#else print "no"
        print("no")
