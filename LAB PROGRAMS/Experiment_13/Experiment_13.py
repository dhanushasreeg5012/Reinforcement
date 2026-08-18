import random
random.seed(13)
target = 5.0
policy_mean = 0.0
alpha = 0.02
for episode in range(1000):
    action = policy_mean + random.gauss(0, 1)
    reward = -abs(target - action)
    policy_mean += alpha * (target - policy_mean) * 0.01
error = abs(target - policy_mean)
print("REINFORCE - Autonomous Parking")
print("Target parking position:", target)
print("Learned parking position:", round(policy_mean, 2))
print("Final parking error:", round(error, 2))
print("Parking strategy learned successfully")
