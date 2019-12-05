import numpy as np

day3_in = np.loadtxt('day3_input.txt', dtype=str, delimiter=',')
wire_data = []
for wire in day3_in:
    current_pos = [0,0]
    position_history = []
    for command in wire:
        direction = command[0]
        distance = int(command[1:])
        while distance > 0:
            if direction == "L":
                current_pos[0] += -1
            elif direction == "R":
                current_pos[0] += 1
            elif direction == "U":
                current_pos[1] += 1
            elif direction == "D":
                current_pos[1] += -1


        print(f"Position history length: {len(position_history)}")
    wire_data.append(position_history.copy())
