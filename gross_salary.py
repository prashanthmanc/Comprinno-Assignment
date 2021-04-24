# iterate over test cases
TestCases=int(input())
for i in range(1,TestCases+1):

	# take the length input
     length =int(input())
     
    # check the length is < 1500
     if length<1500:
        height=0.10*length
        width=0.90*length
        total=length+width+height
        print(total)
    
    # check the length is >= 1500
     elif length>=1500:
         height=500
         width=0.98*length
         total=length+width+height
         print(total)
