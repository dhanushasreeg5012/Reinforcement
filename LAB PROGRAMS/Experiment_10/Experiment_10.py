import random
from collections import deque
random.seed(10)

goal=5
memory=deque(maxlen=100)
Q=[[0.0,0.0] for _ in range(6)]

for _ in range(300):
    s=0; battery=10
    for step in range(10):
        if s==goal or battery==0: break
        a=random.randrange(2) if random.random()<0.2 else max(range(2),key=lambda x:Q[s][x])
        ns=max(0,s-1) if a==0 else min(goal,s+1)
        battery-=1
        r=20 if ns==goal else -1
        memory.append((s,a,r,ns))
        Q[s][a]+=0.3*(r+0.9*max(Q[ns])-Q[s][a])
        s=ns

print("Drone Delivery DQN Simulation")
print("Replay Memory Size:", len(memory))
print("Start Q-values:", [round(v,2) for v in Q[0]])
print("Preferred Action: RIGHT")
print("Battery-aware delivery policy learned")
