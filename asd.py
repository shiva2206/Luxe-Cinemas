def gridChallenge(grid):
    # Write your code here
    
    for i in range(len(grid)):
        a=list(grid[i])
        a.sort()
        j=""
        for k in a:
            j=j+k
        grid[i]=j
    print("grid:",grid)    
    c=[grid[i][0] for i in range(len(grid))]
    c.sort()
    print("c",c)
    for h in range(len(c)):
        for p in grid:
            if c[h]==p[0]:
                c[h]=p
                break
    print("c",c)
    for m in range(len(c)):
        q=[c[i][m] for i in range(len(c))]
        r=q+[]
        r.sort()
        if r != q:
              return "NO"
                              
    else:
        return "YES"
            

t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())

    grid = []

    for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

    result = gridChallenge(grid)
    print(result)

