from pathlib import Path






print("Press 1 for Create New File Inside this folder: ")
print("Press 2 for Read  a File: ")
print("Press 3 for Update File: ")
print("Press 4 for Delete: ")


inpt= int(input("What you Want to Do: "))

if inpt==1:
    createFile()