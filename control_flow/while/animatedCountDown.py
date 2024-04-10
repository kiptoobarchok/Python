#!/usr/bin/python3
"program to countdown to 0 from user input"

import time

start = int(input("Countdown from: "))

print(f'Blastoff in {start} seconds!!')

while start >= 0:
    time.sleep(1)
    print(f"T-{start}")
    start -= 1

time.sleep(1)
print('BLASTOFF')