states=["A","B","C","D"]
edges={
    "A":{"B":2,"C":5},
    "B":{"C":1,"D":4},
    "C":{"D":1},
    "D":{}
}
V={"D":0}
policy={}

for s in ["C","B","A"]:
    nxt,c=min(edges[s].items(),key=lambda kv:kv[1]+V[kv[0]])
    V[s]=c+V[nxt]
    policy[s]=nxt

route=["A"]
while route[-1]!="D":
    route.append(policy[route[-1]])

print("Taxi Routing using Dynamic Programming")
print("Value Function:", V)
print("Optimal Policy:", policy)
print("Optimal Route:", " -> ".join(route))
print("Minimum Cost:", V["A"])
