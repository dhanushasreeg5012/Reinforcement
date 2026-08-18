rooms=["A","B","C","D"]
dirt={"A":4,"B":2,"C":5,"D":3}
energy_cost=1

values={r:dirt[r]-energy_cost for r in rooms}
policy=sorted(rooms,key=lambda r:values[r],reverse=True)
total=sum(values[r] for r in policy)

print("Monte Carlo Vacuum Cleaner")
print("Estimated Room Values:", values)
print("Learned Cleaning Policy:", " -> ".join(policy))
print("Expected Net Reward:", total)
