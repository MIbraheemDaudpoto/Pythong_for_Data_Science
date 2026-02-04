from pathlib import Path

def createAndReadFile():
    try:
        p= Path('')
        files= list(p.rglob('*'))


        for i, items in enumerate(files):
            print(f'{i+1}: {items}')
    except Exception as err:
        print(err)

  
def createFile():
    try:
        createAndReadFile()
        file= input("Add File name with extension:- ")

        p=Path(file)

        if  not p.exists():
            with open(file,'w') as File:
                content= input("Add Some content inside file:- ")
                File.write(content)
                print("FILE CREATED SUCCESSFULLY")
        else:
            print("File Already Exists with this name in this path")
            
    except Exception as err:
        print(err)





print("Press 1 for Create New File Inside this folder: ")
print("Press 2 for Read  a File: ")
print("Press 3 for Update File: ")
print("Press 4 for Delete: ")


inpt= int(input("What you Want to Do: "))

if inpt==1:
    createFile()