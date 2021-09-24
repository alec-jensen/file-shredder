import os
import sys
from termcolor import colored
import colorama

colorama.init()
success = True


def secure_delete(path, passes=5):
    global success
    with open(path, "ba+") as delfile:
        length = delfile.tell()
    with open(path, "br+") as delfile:
        for i in range(passes):
            try:
                delfile.seek(0)
                delfile.write(os.urandom(length))
                print(colored(f'PASS {i + 1} SUCCESS', 'green'))
            except:
                print(colored(f'PASS {i + 1} FAILED', 'red'))
                success = False
    try:
        os.remove(path)
        print(colored('FILE DELETED SUCCESSFULLY.', 'green'))
    except:
        print(colored('FILE DELETION ERROR. FILE MAY STILL BE SHREDDED.', 'red'))
        success = False


file = sys.argv[1]

print(colored('ARE YOU SURE YOU WANT TO CONTINUE WITH SHREDDING? Y/N', 'yellow'))
check = bool(input())

if check:
    print(colored('SHREDDING FILE', 'yellow'))
    secure_delete(file)
    if success:
        print(colored('SHRED SUCCESSFUL. PRESS ANY KEY TO CONTINUE.', 'green'))
        input()
    else:
        print(colored('ONE OR MORE ELEMENTS HAVE FAILED. PLEASE TRY AGAIN.', 'red'))
        input()
