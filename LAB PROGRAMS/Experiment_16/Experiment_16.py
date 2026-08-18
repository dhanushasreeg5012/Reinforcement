import random
random.seed(16)
methods={"REINFORCE":0.82,"Actor-Critic":0.90,"PPO":0.95}
print("Autonomous Lane-Keeping Comparison")
best=None
for name,base_score in methods.items():
    scores=[base_score+random.uniform(-0.03,0.03) for _ in range(30)]
    avg=sum(scores)/len(scores)
    print(f"{name:14s} Stability Score = {avg:.3f}")
    if best is None or avg>best[1]:
        best=(name,avg)
print("Best Policy Gradient Method:", best[0])
print("Highest Stability Score:", round(best[1],3))
