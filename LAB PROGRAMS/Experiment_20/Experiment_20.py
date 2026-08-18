states=["Victim Nearby","Victim Far"]
belief={"Victim Nearby":0.5,"Victim Far":0.5}
observation="Weak Signal"
if observation=="Strong Signal":
    belief["Victim Nearby"]=0.8
    belief["Victim Far"]=0.2
else:
    belief["Victim Nearby"]=0.35
    belief["Victim Far"]=0.65
action="Move Forward" if belief["Victim Far"]>belief["Victim Nearby"] else "Search Nearby"
print("Search-and-Rescue POMDP")
print("Observation:", observation)
print("Updated belief:", belief)
print("Selected action:", action)
print("Decision made under uncertainty")
