states = ["A", "B", "C", "Goal"]
transition = {
    ("A","Forward"):("B",0.9),
    ("A","Right"):("C",0.8),
    ("B","Forward"):("Goal",0.95),
    ("C","Forward"):("Goal",0.85)
}
reward = {"A":-1, "B":-1, "C":-2, "Goal":20}

print("Warehouse Robot MDP")
for k,v in transition.items():
    print(k, "->", v)
print("Best route: A -> B -> Goal")
print("Total Reward:", reward["A"]+reward["B"]+reward["Goal"])
