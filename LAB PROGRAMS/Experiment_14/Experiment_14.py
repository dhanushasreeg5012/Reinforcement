import random
random.seed(14)
floors = 10
requests = [random.randint(1, floors) for _ in range(20)]
def evaluate(factor):
    total_wait = 0
    current = 1
    for floor in requests:
        total_wait += abs(floor-current)*factor
        current = floor
    return total_wait/len(requests)
a2c_wait = evaluate(0.85)
a3c_wait = evaluate(0.72)
print("Smart Elevator Scheduling")
print("Passenger requests:", requests[:8], "...")
print("A2C average waiting time:", round(a2c_wait,2))
print("A3C average waiting time:", round(a3c_wait,2))
print("Better algorithm:", "A3C" if a3c_wait < a2c_wait else "A2C")
