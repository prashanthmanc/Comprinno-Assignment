# iterate over the test cases

for _ in range(int(input())):
	#first line take N integer input
    n=int(input())
    Arr=list(map(int,input().split()))
    Arr2=[]
    
    #creat an array
    Count=Counter()
    
    # iterate over ever element in Arr
    for iterate in Arr:
        Count[iterate]+=1
        
        # check the condition
        if((Count[iterate]%2)==0): Arr2.append(iterate)
        
	#maximum possible area for rectangle or -1
    if len(Arr2)<2: 
    	print(-1)
    else:
        Arr2.sort(reverse=True)
        print(Arr2[0]*Arr2[1])
