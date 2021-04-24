# Iterate through every team
totalTeams = int(input())
for team in range(totalTeams):
	
	# Select 3 members as team and store in Team list as tuples
	Team = []
	for member in range(3):
		Team.append(tuple(map(int,input().split())))
		
	# sort the Team list using 1st index of tuples
	Team.sort(key=lambda memb:memb[0])
	
	#check the first two members in Team list are the valid or not
	if Team[1][0]-Team[0][0]+Team[1][1]-Team[0][1]+Team[1][2]-Team[0][2]>0:
		
		# check the 2nd and third members in Team list are the valid or not
		if Team[2][0]-Team[1][0]+Team[2][1]-Team[1][1]+Team[2][2]-Team[1][2]>0:
			
			# if both the conditions satisify then print "yes" and continue for the next team
			print("yes")
			continue
			
	# if any of the condition fails print "no"
	print("no")
