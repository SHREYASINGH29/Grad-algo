import numpy as np

population = np.array([1]*520000 + [-1]*480000)
np.random.shuffle(population)

def voting_experiment(sample_size, num_runs=100):
    counts = 0
    for _ in range(num_runs):
        sample = np.random.choice(population, size=sample_size)
        if np.sum(sample) > 0:  # count positive majorities
            counts += 1
    return counts / num_runs

for sample_size in [20, 100, 400]:
    print(f"Sample size: {sample_size}, Probability: {voting_experiment(sample_size)}")

sample_size = 1
while True:
    p = voting_experiment(sample_size)
    if p >= 0.9:
        break
    sample_size += 1
print(f"Required sample size: {sample_size}")

