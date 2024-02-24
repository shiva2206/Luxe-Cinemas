#Test case
t=int(input())
# loop for each test case
for tc in range(t):
    
    # int inputs in single line
    a,b,c,x,y = [ int(x) for x in input().split() ]
    
    if (a+b+c) != (x+y):
        print('NO')
        
    elif y< min (a, min(b,c)) or x<min(a,min(b,c)):
        print('NO')
        
    else:
        print('YES')