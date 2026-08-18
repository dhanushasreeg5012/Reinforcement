cost = [[1,3,1],[2,5,2],[4,2,1]]
V = [[0]*3 for _ in range(3)]
V[2][2] = 1

for i in range(2,-1,-1):
    for j in range(2,-1,-1):
        if (i,j)==(2,2): continue
        nxt=[]
        if i<2: nxt.append(V[i+1][j])
        if j<2: nxt.append(V[i][j+1])
        V[i][j] = cost[i][j] + min(nxt)

print("Bellman Equation - Delivery Robot")
for row in V:
    print(row)
print("Minimum Travel Cost:", V[0][0])
print("Optimal Path: Right -> Right -> Down -> Down")
