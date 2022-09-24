#!/usr/bin/env python3
# prime.py
# Author : Shipra
import time
def primeOrnot(numb):
    if numb < 2:
        return False
    if numb == 2:
        return True
    if numb % 2 == 0:
        return False
    else:
        divisor = numb//2
        for i in range(3,divisor,2):
            if numb % i == 0:
                return False
    return True


numb = 80380509999928600597
t0 = time.time()
print(primeOrnot(numb))

t1 = time.time()
print("Time required :", t1 - t0)