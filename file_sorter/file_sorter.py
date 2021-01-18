import pyinputplus as pyip
import os
import os.path
import time
import subprocess
from datetime import datetime, timedelta, date
from pathlib import Path

os.chdir('/Users/terrelljackson/')
homedir = os.listdir()
py_list = []
file_count = 0
for name in homedir:  # Looping through home directory to search for certain files
    print(name)
    if name.endswith('.py'):  # Get all files in root directory that ends in .py
        py_list.append(name)

file_count += len(py_list)
print()
print(py_list)
print()
print(file_count)
print()


# print(len(py_list))
for f in py_list:  # script gets created dates for file in the py_list path
    print(f"{f} Was created on: {time.ctime(os.path.getctime(f))}\n")
    print(f"{f} Last modification date for file: {time.ctime(os.path.getmtime(f))}\n")

    # less_than_thirty_days = datetime.now() - timedelta(days=30)
    # old_files = datetime.fromtimestamp(os.path.getmtime(f))
    # if old_files < less_than_thirty_days:
    #     print(f"{f} has not been modified in the last 30 days")


def old_file():
    thirty_days = datetime.now() - timedelta(days=30)
    old_files = datetime.fromtimestamp(os.path.getmtime(f))
    for py in py_list:
        if old_files < thirty_days:
            print(f"{py} has not been modified in the last 30 days")
    print(thirty_days)
    print(old_files)
    # print(py)


old_file()
print(os.getcwd())  # Print current directory
