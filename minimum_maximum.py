#print first line of input
testCase=int(input())
for iterate in range(testCase):
    length=int(input())
    Arr=list(map(int,input().split()))
    Min=min(l)
# print next line input N space
    print(Min*(length-1))
