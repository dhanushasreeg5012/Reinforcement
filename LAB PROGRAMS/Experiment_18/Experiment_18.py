import random
random.seed(18)
tasks=["Pick","Place","Weld","Inspect"]
adaptation_steps={}
for task in tasks:
    base_steps=random.randint(15,25)
    meta_steps=max(3,base_steps-random.randint(8,14))
    adaptation_steps[task]=meta_steps
print("Meta-Reinforcement Learning - Industrial Robot")
for task,steps in adaptation_steps.items():
    print(f"{task:8s} adapted in {steps} steps")
avg=sum(adaptation_steps.values())/len(adaptation_steps)
print("Average adaptation steps:", round(avg,2))
print("Robot quickly adapted to new manufacturing tasks")
