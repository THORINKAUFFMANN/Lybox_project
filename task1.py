# lib
import numpy as np
import array as array

# Exemple :
arr = array.array("i", [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13])
n1 = 2
n2 = 5

#fontion :
def calculate (arr,n1,n2):
    res = 0;
    i = 0;

    for i in range(n1, n2 + 1, 1):
        res = res + arr[i]
    return res

#main
if(0 <= n1 <= n2 <= len(arr)):
    print(calculate(arr,n1,n2))
else: print("the rule was not respected")
