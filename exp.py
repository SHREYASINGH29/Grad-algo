import numpy as np
import pandas as pd

def random_walk(t):
    current_position = 0
    crosses = 0
    for i in range(t):
        # Generate a random step
        step = np.random.choice([1, -1])
        # Update current position
        current_position += step
        # Check if the particle has crossed the origin
        if current_position == 0:
            crosses += 1
    return crosses

def multiple_walks(t, n):
    total_crosses = 0
    for i in range(n):
        crosses = random_walk(t)
        total_crosses += crosses
    return total_crosses / n

for t in [4*10**4, 9*10**4, 16*10**4]:
    print(f"For t = {t}, the average number of times the particle crosses the origins is: {multiple_walks(t, 50)}")
