# taking testcases
test=int(input())
for testcase in range(test):
	
	# take total cookies and milk input
    n=int(input())
    items =list(input().split())
    
    # iterate through the items
    k=0
    for item in range(n):
		# if last item is a cookie the it will surely be "no"
        if(item==n-1 and items[i]=='cookie'):
            k=1
            break
        # if item cookie has no following milk, then it will be "no"
        if(items[i]=='cookie' and items[i+1]!='milk'):
            k=1
            break
            
    if(k==1):
        print("NO")
        continue
    
    # if all cases satisify then "yes"
    print("YES")
        
      
