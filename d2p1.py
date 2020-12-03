#!/usr/bin/env python3

import re

print("adventofcode2020 d2p1")

payload_file = open('inputd2.txt', 'r')
data = payload_file.read().splitlines()
payload_file.close()
validPwdCount = 0

for line in data:
    m = re.search(r'(\d*)-(\d*) (\w): (\w*)', line)
    min = int(m.group(1))
    max = int(m.group(2))
    char = m.group(3)
    passwd = m.group(4)

    occurence = passwd.count(char)
    if(occurence >= min and occurence <= max):
        print("valid")
        validPwdCount = validPwdCount + 1

print("We got: ",validPwdCount, "valid passwords")


