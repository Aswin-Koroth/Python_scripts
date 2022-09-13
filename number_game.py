import math
import os

LIMIT = 100

def org_prt(n):
    l = len(str(LIMIT))
    num_len = len(n)
    # if num_len < l:
    print((l-num_len)*" "+n, end=' ')
    # else:
    #     print(n, end=' ')

def num_prt(a):
    r = list(range(a, LIMIT+1))
    j = 0
    for count in list(map(r.index, r)):
        if j % a == 0 and j != 0:
            j += a
        if j >= len(r):
            break
        org_prt(str(r[j]))
        j += 1
        if (count+1) % int(math.sqrt(LIMIT/2)) == 0 and count != 0:
            print('')

def numlist():
    ls = [1]
    j = 1
    for i in range(int(LIMIT / 2)):
        j += j
        ls.append(j)
        if j > LIMIT / 2:
            break
    return ls

def main():
    # print('Think of a number between 1 and 50\n')
    os.system('echo off')
    os.system('cls')
    input(f'Think of a number between 0 and {LIMIT}\n(press enter to continue...\n')
    num = 0
    for i in numlist():
        num_prt(i)
        inp = input('\n\nIs your number here? (Y or N) ')
        if inp.lower() == 'y':
            num += i
        os.system('cls')


    print(f"Your number is : {num}")

# 20/3/2022
# Aswin Koroth
main()
