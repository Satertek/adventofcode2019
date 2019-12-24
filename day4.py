import numpy as np
import sys

day4_in = np.loadtxt('day4_input.txt', dtype=int, delimiter='-')

PART_ONE = False

def has_adjacent_digits(password):
    password = str(password)
    for i in range(len(str(password))-1):
        if (password[i] == password[i+1]):
            if PART_ONE:
                return True
            return check_larger_group(password, password[i], i)
    return False

def has_increasing_digits(password):
    password = str(password)
    for i in range(len(str(password))-1):
        if int(password[i]) > int(password[i+1]):
            return False
    return True

def check_larger_group(password, match, match_pos):
    if (password.count(match) == 2):
        return True
    if password[match_pos+2] == match:
        j = match_pos
        while j < len(password):
            if password[j] == match:
                j += 1
            else:
                break
        remaining_password = password[:match_pos] + password[j:]
        return has_adjacent_digits(remaining_password) 

valid_passwords = 0

for password in range(day4_in[0], day4_in[1]):

    if has_increasing_digits(password) and has_adjacent_digits(password):
        valid_passwords += 1  

print(f"Range: {day4_in[0]} - {day4_in[1]}")
print(f"Valid Passwords: {valid_passwords}")