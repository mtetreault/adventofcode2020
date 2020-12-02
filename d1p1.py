#!/usr/bin/env python3

print("adventofcode2020 d1p1")
SUM=2020
data = []
payload_file = open('inputd1p1.txt', 'r')
for line in payload_file:
    data.append(int(line))
payload_file.close()
data.sort()

for i in range(len(data)):
    for j in range (i+1, len(data)):
        if (data[i] + data[j] == SUM):
            print("Got it:", data[i], data[j], data[i]*data[j])
            break
