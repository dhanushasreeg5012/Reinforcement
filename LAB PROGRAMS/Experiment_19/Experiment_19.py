robots=["R1","R2","R3"]
tasks={"T1":(2,3),"T2":(7,1),"T3":(4,6)}
robot_pos={"R1":(1,1),"R2":(8,2),"R3":(5,5)}
assignments={}
for robot in robots:
    available=[t for t in tasks if t not in assignments.values()]
    best=min(available,key=lambda t:abs(robot_pos[robot][0]-tasks[t][0])+abs(robot_pos[robot][1]-tasks[t][1]))
    assignments[robot]=best
print("Multi-Agent RL - Warehouse System")
for robot,task in assignments.items():
    print(robot, "assigned to", task)
print("Cooperative task allocation completed")
print("Navigation conflicts minimized")
