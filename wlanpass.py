import os


def getlen(x):
    for i, j in enumerate(x):
        if j == "\n":
            return i
    return 0

def findstr(str, find):
    f = str.find(find)
    if f == -1:
        return 0, 0
    index = f + len(find)
    extra = index+getlen(str[index:])
    s = str[index:extra]
    return s, extra

def getpass(net):
    cmdret = os.popen(f'netsh wlan show profiles "{net}" key=clear').read()
    temp = 'Key Content            : '
    pas, ex = findstr(cmdret, temp)
    if ex == 0:
        return 0, False
    return pas, True

def getnetlist():
    cmdret = os.popen('netsh wlan show profiles').read()
    temp = "All User Profile     : "
    netlist = []
    while True:
        str, ex = findstr(cmdret, temp)
        if ex == 0:
            break
        cmdret = cmdret[ex:]
        netlist.append(str)
    return netlist

def prtline():
    print("----------------------------------------------------------")

def main():
    print("\nListing network profiles...\n")
    network_list = getnetlist()
    for i, j in enumerate(network_list):
        print(i+1, j)
    opt = int(input("\nSelect a network to show password (Select 0 to list all passwords)\n"))
    if opt == 0:
        print('\nListing all passwords...')
        count = 0
        prtline()
        for i in network_list:
            # thread = threading.Thread()
            pas, ret = getpass(i)
            print(i, "=>", end=" ")
            if not ret:
                print('Password not found')
                prtline()
            else:
                print(pas)
                count += 1
                prtline()
        print(f'\n{count} passwords found.')
    else:
        net = network_list[opt-1]
        print(f"\nSearching for password...\nNetwork > '{net}'")
        prtline()
        pas, ret = getpass(net)
        if not ret:
            print('Password not found')
            exit(0)
        print('Password =', pas)
        prtline()

# 10/4/2022
# Aswin-Koroth
main()

        
    

