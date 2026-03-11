from pathlib import Path




def readFileAndFolder():
    path= Path('')
    items= list(path.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

    

def createFile():
    try:
        print("Here is your folder structure")
        readFileAndFolder()
        name= input("What Should be your File Name: ")
        p= Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data= input("Enter Data: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")        
        else: 
            print("File Already Exists!")
    except Exception as err:
        print(err)




def readFile():
    try:
        print("Here is Complete Folder Structure: ")
        readFileAndFolder()
        fName= input("Enter file Name: ")
        p= Path(fName)
        if p.exists() and p.is_file():
            with open(p) as fs:
                data= fs.read()
                print(data)
            print("File Read Successfully")
        else:
            print("File is incorrect")
    except Exception as err:
        print(f"err")



# Update

def updateFile():
    try:
        print("Here is your Folder Structure :)")
        readFileAndFolder()
        name= str(input("Enter Your File Name: "))
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 For Change your File Name: ")
            print("Press 2 for OverWritting  File: ")
            print("Press 3 for Appending some Data: ")

            response= int(input("Enter Your Response:) "))
            if response==1:
                name2= input("Enter Your New File Name:) ")
                p2= Path(name2)
                if not p2.exists():
                    p.rename(p2)
                else: 
                    print("This File Already Exists")
            elif response==2:
                with open(p,"w") as fs:
                    data=input("Enter Your New Content:) ")
                    fs.write(data)
            elif response==3:
                with open(p,'a') as fs:
                    data=input("Enter other Data you want to append:) ")
                    fs.write(" "+ data)       

    except Exception as err:
        print(f"err")

print("Press 1 for Create a New File")
print("Press 2 for Read File")
print("Press 3 for update File")
print("Press 4 for Delete File")


check= int(input("Enter Your Choice: "))


if check==1:
    createFile()
elif check==2:
    readFile()
elif check==3:
    updateFile()