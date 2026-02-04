from pathlib import Path


def readFileandFolder():
    try:
        p= Path('')
        items= list(p.rglob('*'))
        
        print("Available Files")
        for i,items in enumerate(items):
            print(f"{i+1}: {items}")
    

    except Exception as err:
        print(err)


def createFileFunc():
    try:
        readFileandFolder()
        name= input("Set Name of Your File with extension:- ")
        p=Path(name)
        if not p.exists():
            with open(p,'w') as file:
                content= input("Add Some content if you want to ADD:- ")
                file.write(content)
            
            print("File Created Successfully")
        else:
            print("File Already Exists")
    except Exception as err:
        print(err)


    

  



print("Press 1 for Create New File Inside this folder: ")
print("Press 2 for Read  a File: ")
print("Press 3 for Update File: ")
print("Press 4 for Delete: ")


inpt= int(input("What you Want to Do: "))

if inpt==1:
    createFileFunc()