#Print contains of the first line input
for i in range(int(input())):
	#test case contains 3 integers a,b,n
    a,b,n = map(int, input().split())
    #Print N turns
    if n%2==1:
        a*=2
    print(max(a,b)//min(a,b))
