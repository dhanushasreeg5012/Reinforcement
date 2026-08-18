import random
random.seed(6)

goal=5
Q=[[0.0,0.0] for _ in range(goal+1)]

for _ in range(300):
    s=0
    for step in range(30):
        if s==goal: break
        a=random.randrange(2) if random.random()<0.2 else max(range(2),key=lambda x:Q[s][x])
        ns=max(0,s-1) if a==0 else min(goal,s+1)
        r=10 if ns==goal else -1
        Q[s][a]+=0.5*(r+0.9*max(Q[ns])-Q[s][a])
        s=ns

path=[0]; s=0
for _ in range(10):
    if s==goal: break
    a=max(range(2),key=lambda x:Q[s][x])
    s=max(0,s-1) if a==0 else min(goal,s+1)
    path.append(s)

print("Autonomous Robot RL Model")
print("Learned Route:", path)
print("Goal Reached:", path[-1]==goal)
print("Framework concept: OpenAI Gym + TensorFlow/Keras")
