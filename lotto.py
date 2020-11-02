import random

nums = list(range(1, 36))
jackpot = random.sample(nums, k=5)
print("Power ball numbers are >")
for x in jackpot:
    random.choice(jackpot)
    print(x)
power_num = random.randint(1, 10)
print(f"Power number = {power_num}")
nums2 = list(range(1, 33))
mega_6 = random.sample(nums2, k=6)
print(f"Mega 6 numbers are: {mega_6}")

