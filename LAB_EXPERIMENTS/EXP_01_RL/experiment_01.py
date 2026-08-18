states = ["Start", "Center", "Attack", "Win"]
V = {s: 0.0 for s in states}
gamma = 0.9

for _ in range(10):
    V["Attack"] = 10
    V["Center"] = 2 + gamma * V["Attack"]
    V["Start"] = gamma * V["Center"]

print("Simplified Chess MDP")
print("State Values:", {k: round(v,2) for k,v in V.items()})
print("Optimal sequence: Start -> Center -> Attack -> Win")
print("Maximum Expected Reward:", round(V["Start"],2))