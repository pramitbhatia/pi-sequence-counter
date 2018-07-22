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
    
    ctr = 0
    for i in range(0,len(b)-1):
        if b[i] == int(X[0]):
            if b[i+1] == int(X[1]):
                ctr += 1
    
    return ctr

if __name__ == '__main__':
    print(func())

'''

In this algorithm, we are simply traversing the array of the
digits and comparing the sequence using nested if statements

Match each digit with the first digit of the sequence wanted
by the user. If match is found then check for the next digit
in the sequence. A complete match will trigger the increment
of the counter variable.

This implementation is made while keeping use-and-throw case
in mind. The count of the sequence is calculated fresh every
time the program is run.

'''
