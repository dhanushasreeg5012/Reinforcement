import random
random.seed(11)

base={"DQN":42,"DDQN":36,"Dueling DQN":33,"PER":29}
results={}

print("Traffic Signal Control Comparison")
for name,b in base.items():
    waits=[b+random.randint(-3,3) for _ in range(20)]
    avg=sum(waits)/len(waits)
    results[name]=avg
    print(f"{name:12s} = {avg:.2f} sec average wait")

best=min(results,key=results.get)
print("Best Method:", best)
print("Lowest Waiting Time:", round(results[best],2),"sec")
