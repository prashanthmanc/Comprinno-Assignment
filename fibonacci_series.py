testCase = int(input())
for _ in range(testCase):
	
	# Taking input
	string = str(input())
	
	# we will store the occurences if charecter in hashMap
	hashMap = {}
	for char in string:
		if char in hashMap:
			hashMap[char]+=1
		else:
			hashMap[char]=1
	
	# Now we will be storing the character counts in countArr so that further it will be easy to sort
	countArr=[]
	for char in hashMap:
		countArr.append(hashMap[char])
		
	# sort the countArr
	countArr.sort()
	
	#if the length of countArr is less than 3, then it is Dynamic
	if(len(countArr)<3): 
		print("Dynamic")
	
	# we will now check the grater than 3 case
	else:
		length = len(countArr)
		
		#we will be iterating through the countArr from 3rd element
		for indx in range(2,length):
			
			# if the condition is False then we are going to print "Not" and we will break the loop
			if countArr[indx]!= countArr[indx-1]+countArr[indx-2]:
				print("Not")
				break
		else: 
			# if all the indx values will satisify the given condition then we will print "Dynamic"
			print("Dynamic")

