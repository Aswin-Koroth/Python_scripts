import os
import shutil
from termcolor import colored

def listext(fle):
    elist = []
    for f in fle:
        elist.append(f.rsplit(".")[-1])
    return list(dict.fromkeys(elist))  # remove duplicates

def onlyfolders(fle):
    folderlist = []
    for f in fle:
        isdir = os.path.isdir(os.path.join(root, f))
        if isdir:
            folderlist.append(f)
    return folderlist

def onlyfiles(fle):
    filelist = []
    for f in fle:
        isdir = os.path.isdir(os.path.join(root, f))
        if isdir:
            continue
        filelist.append(f)
    return filelist


def printall(lst):
    for f in lst:
        print(colored(f, "green"))


def organize():
    ext = listext(onlyfiles(dirlist))
    for e in ext:
        if os.path.exists(os.path.join(root, e)):
            continue
        os.makedirs(os.path.join(root, e))

    for f in onlyfiles(dirlist):
        for e in ext:
            if f.endswith(e):
                os.replace(os.path.join(root, f), os.path.join(root, e, f))
    print("\n"+colored("Files oraganized\n", "green"), colored(str(len(ext))+" folder(s) created", "yellow"))


def delete():
    extention = "." + input("extention to delete (jpg, mp3, xml ...)(Type . to delete every folder)(Type * to delete everything)\n")
    count = 0
    print("\n")
    if extention == "..":
        for f in onlyfolders(dirlist):
            shutil.rmtree(os.path.join(root, f))
            print(colored(f, "yellow"))
            count += 1
        print(colored(f"{str(count)} folder(s) deleted", "red"))
    elif extention == '.*':
        try:
            shutil.rmtree(root)
        except:
            print(colored("Contents in folder deleted", "red"))
    else:
        for fl in onlyfiles(dirlist):
            if fl.endswith(extention):
                os.remove(os.path.join(root, fl))
                print(colored(fl, "yellow"))
                count += 1
        print(colored(str(count)+" file(s) deleted", "red"))

os.system('color')
os.system('echo off')
os.system('cls')
root = ""
dirlist = []


def main():
    global root
    root = os.path.join(os.getcwd(), input(colored("Enter folder path\n", 'yellow')))
    # print(root)
    # print(os.getcwd())
    global dirlist
    dirlist = os.listdir(root)
    if len(dirlist) == 0:
        print(colored("Folder is empty", "yellow"))
        exit(0)
    print(colored("\nFILES", "yellow"))
    printall(dirlist)
    opt = int(input("\n1. Delete \n2. Organize\n"))
    if opt == 1:
        delete()
    elif opt == 2:
        organize()
    elif opt == 3:
        printall(dirlist)
    elif opt == 4:
        printall(onlyfolders(dirlist))

# 17/2/2022
# Aswin Koroth
if __name__ == "__main__":
    main()
