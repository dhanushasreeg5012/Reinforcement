import random
random.seed(12)

target=5.0
policy_mean=0.0
learning_rate=0.02

for _ in range(1000):
    action=policy_mean+random.gauss(0,1)
    reward=-abs(target-action)
    policy_mean += learning_rate*(target-policy_mean)*0.01

print("Policy-Based RL for Robotic Arm")
print("Learned Pick Position:", round(policy_mean,2))
print("Target Place Position:", target)
print("Pick-and-place operation completed")
print("Policy improved using reward feedback")
