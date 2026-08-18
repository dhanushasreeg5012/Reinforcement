import random
random.seed(2)

grid = 4
goal = (3, 3)
moves = [(1,0),(-1,0),(0,1),(0,-1)]
Q = {(x,y): [0.0]*4 for x in range(grid) for y in range(grid)}

for _ in range(300):
    s = (0,0)
    for step in range(50):
        if s == goal:
            break
        a = random.randrange(4) if random.random() < 0.2 else max(range(4), key=lambda i: Q[s][i])
        ns = (min(3,max(0,s[0]+moves[a][0])), min(3,max(0,s[1]+moves[a][1])))
        r = 10 if ns == goal else -1
        Q[s][a] += 0.5*(r + 0.9*max(Q[ns]) - Q[s][a])
        s = ns

s=(0,0); path=[s]
for _ in range(12):
    if s==goal: break
    a=max(range(4), key=lambda i:Q[s][i])
    s=(min(3,max(0,s[0]+moves[a][0])), min(3,max(0,s[1]+moves[a][1])))
    path.append(s)

print("Smart Home Robot Navigation")
print("Learned Path:", path)
print("Goal Reached:", path[-1] == goal)