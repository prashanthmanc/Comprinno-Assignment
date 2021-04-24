# iterrate though strips 
strips = int(input())
for strip in range(strips):
	# we will be reading lenth and the strips height
	length = int(input())
	heights = list(map(int,input().split()))
	
	# check base conditions
	if len(heights)%2==0 or heights[0]!=1:
		print("no")
		continue
		
	# now check the values from 1 to half lenth
	flag=0
	for height in range(1,length//2):
		
		# if the diff is not 1 then we will break
		if heights[height]-heights[height-1]!=1:
			flag=1
			break
	if flag:
		
		# we will print no and go to the next strip
		print("no")
		continue
		
	# now check the values from half to its total lenth
	for height in range((length+1)//2,length):
		
		# if the diff is not 1 then we will break
		if heights[height-1]-heights[height]!=1:
			flag=1
			break
	if flag:
		
		# we will print no and go to the next strip
		print("no")
		continue
	
	# if the condition satifies then print "yes"
	print("yes")
	
	
	
