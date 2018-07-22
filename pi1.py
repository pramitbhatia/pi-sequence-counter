'''

In this algorithm we calculate the occurrence of all 2 digit
combinations and store the counts in a nested (2D) list. The
data can be accessed later by simply accessing the structure
using the correct indices.

This implementation is made keeping reusability in mind. For
the fixed number of digits, we can access the counts easily.

'''

from profilehooks import timecall
from math import pi,trunc

@timecall
def func():
    a = pi*10   # 31.4 ... Helps eliminate the 3 in units place
    b = []
    N = 300     # The number of decimal places to be accounted
    X = "02"    # The sequence to be found

    for i in range(N):
        b.append(trunc(a%10))
        a *= 10
    
    count2 = []
    for i in range(0,10):
        temp = [0,0,0,0,0,0,0,0,0,0]
        for j in range(0,len(b)-1):
            if b[j] == i:
                temp[b[j+1]] += 1
        count2.append(temp)

    return count2[int(X[0])][int(X[1])]
    
if __name__ == '__main__':
    print(func())
