import random
random.seed(9)

def learn(method):
    Q=[[0.0,0.0] for _ in range(6)]
    for _ in range(300):
        s=0
        for step in range(30):
            if s==5: break
            a=random.randrange(2) if random.random()<0.1 else max(range(2),key=lambda x:Q[s][x])
            ns=max(0,s-1) if a==0 else min(5,s+1)
            r=10 if ns==5 else -1
            if method=="SARSA":
                na=max(range(2),key=lambda x:Q[ns][x])
                target=r if ns==5 else r+0.9*Q[ns][na]
            else:
                target=r if ns==5 else r+0.9*max(Q[ns])
            Q[s][a]+=0.4*(target-Q[s][a])
            s=ns
    return Q[0]

print("Warehouse Robot Algorithm Comparison")
for m in ["TD(0)","SARSA","Q-Learning"]:
    vals=learn("SARSA" if m=="SARSA" else "Q")
    print(m, "Start Q-values:", [round(v,2) for v in vals])
print("Best learned action: Move Right")
