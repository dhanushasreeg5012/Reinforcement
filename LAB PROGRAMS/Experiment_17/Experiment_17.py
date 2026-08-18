tasks={
"Clean Room":["Move to room","Detect dirt","Vacuum"],
"Bring Water":["Go to kitchen","Pick bottle","Deliver bottle"],
"Charge":["Find dock","Move to dock","Recharge"]
}
ham_time={"Clean Room":6,"Bring Water":5,"Charge":4}
maxq_time={"Clean Room":5,"Bring Water":4,"Charge":3}
print("Hierarchical RL - Household Robot")
print("Available high-level tasks:", list(tasks.keys()))
for task in tasks:
    print(task, "subtasks:", " -> ".join(tasks[task]))
print("HAM total task cost:", sum(ham_time.values()))
print("MAXQ total task cost:", sum(maxq_time.values()))
print("More efficient hierarchy: MAXQ")
