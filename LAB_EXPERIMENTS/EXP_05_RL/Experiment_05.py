import random
random.seed(5)

rates=[0.05,0.08,0.12,0.10]
counts=[0]*4
values=[0.0]*4
epsilon=0.1

for _ in range(3000):
    arm=random.randrange(4) if random.random()<epsilon else max(range(4),key=lambda i:values[i])
    reward=1 if random.random()<rates[arm] else 0
    counts[arm]+=1
    values[arm]+=(reward-values[arm])/counts[arm]

best=max(range(4),key=lambda i:values[i])
print("Epsilon-Greedy Advertisement System")
print("Selections:", counts)
print("Estimated Rates:", [round(v,3) for v in values])
print("Best Advertisement: Ad", best+1)
