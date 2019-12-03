import numpy as np
import sys

PART_ONE = False

input = np.loadtxt("day2_input.txt", dtype=int, delimiter=',')

if PART_ONE:
    noun = 12
    verb = 2
else:
    noun = 0
    verb = 0

while noun < 99:
    while verb < 99:   
        output = input.copy()
        output[1] = noun
        output[2] = verb
        i = 0
        while i < len(output):
            if output[i] == 1:
                output[output[i+3]] = output[output[i+1]] + output[output[i+2]]
            elif output[i] == 2:
                output[output[i+3]] = output[output[i+1]] * output[output[i+2]]
            elif output[i] == 99:
                verb += 1
                break
            else:
                print(f"ERROR: Unknown Intcode: {output[i]} (Noun: {noun}, Verb: {verb})")
                sys.exit()
            i += 4
        if output[0] == 19690720 or PART_ONE:
            print(f"Position [0] Result: {output[0]}")
            print(f"Position [1] Result: {output[1]}")
            print(f"Position [2] Result: {output[2]}")
            print(f"Final Output: {100 * output[1] + output[2]}")
            output[1] = 1e6
            output[2] = 1e6
            break
    if output[0] == 19690720 or PART_ONE:
        break
    verb = 0
    noun += 1