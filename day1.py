import numpy as np

PART_ONE = False

def calculate_fuel(x):
     return np.floor(x / 3) - 2

input = np.loadtxt("day1_input.txt")
total = 0

for line in input:
    fuel = calculate_fuel(line) # Calculate fuel for a module
    total += fuel
    # Calculate fuel for fuel (for fuel) for a module
    while not PART_ONE:
        fuel = calculate_fuel(fuel) 
        if fuel < 0:
            break
        total += fuel

print(f"Total Fuel Mass Required: [{total} kg]")