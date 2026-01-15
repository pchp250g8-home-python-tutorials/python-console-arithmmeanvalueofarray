# -- encoding:utf-8 --

import array
import os
import random

os.system("cls")
print("Input a count of elements")
nElems = int(input())
iArray = array.array("i")
nSum = 0
for i in range(0, nElems):
    nItem = random.randint(1, 100)
    iArray.append(nItem)
print("Generated Array:")
for i in range(0, nElems):
    nSum += iArray[i]
    print(iArray[i], end=" ")
fltVal = nSum / nElems
print(f"\r\nThe Sum of {nElems} elements of the array is:{nSum}")
print(f"The Mean Value of {nElems} elements of the array is:{fltVal}")