# taking Testcases
for Iterate in range(int(input())):

	# taking input 
	Length = int(input())
	Arr = list(map(int, input().split()))
	
	#storing -1,0,1 values
	Count = [Arr.count(-1), Arr.count(0), Arr.count(1)]
	Value= len(Arr) - sum(Count)
	
	#check the array conditions
	if Value> 1:
		print("no")
	else:
	
		#else condion and check the proper valid which  we need to print
		if Value and Count[0]:
			print("no")
		elif (Count[0]>1 and Count[2] == 0) :
			print("no")
		else:
			print("yes")
			
			
	
