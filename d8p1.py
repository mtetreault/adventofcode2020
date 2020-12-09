#!/usr/bin/env python3

print("adventofcode2020 d8")

payload_file = open('inputd8.txt', 'r')
dataset = payload_file.read().splitlines()

def loop_finder(data):
    cmd_history = []
    current_idx = 0
    accumulator = 0

    for i in range(len(data)):
        cmd,val = data[current_idx].split()
        if current_idx in cmd_history:
            print("LOOP", accumulator)
            return False

        cmd_history.append(current_idx)
        if (cmd == 'acc'):
            current_idx = current_idx + 1
            accumulator = accumulator + int(val)
        elif (cmd == 'jmp'):
            next_idx = current_idx + int(val)
            if (next_idx >= 0 and next_idx <= len(data) - 1):
                current_idx = current_idx + int(val)
            else:
                return accumulator
        else:
            current_idx = current_idx + 1

    return accumulator

for i in range(len(dataset)):
    new_data = dataset.copy()
    cmd, val = new_data[i].split()

    if cmd == 'nop':
        cmd = 'jmp'
    elif cmd == 'jmp':
        cmd = 'nop'
    
    new_data[i] = " ".join((cmd, val))
    if (loop_finder(new_data)):
        print('-------------found')

