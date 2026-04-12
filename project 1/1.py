from pathlib import Path

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i + 1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("pls tell your file name :- ")
        p = Path(name)

        if not p.exists() and p.is_file:
            with open(p, "w") as fs:
                data = input("what you want to write in this file: ")
                fs.write(data)
            print("file created successfully")
        else:
            print("this file already exists")

    except Exception as err:
        print(f"an error occurred: {err}")

def readfile():
    try:
     readfileandfolder()
     name = input("which file u want to read")
     p = Path(name)
     if p.exists() and p.is_file():
        with open(p , 'r') as fs:
            data = fs.read()
            print(data)
        print("readed succesfully")
     else:
        print("the file does not exist")
    except Exception as err:
        print(f"error is there named as {err}")

def updatefile():
    readfileandfolder()
    name = input("which file u want to update")
    p = Path(name)
    if p.exists() and p.is_file():
        print("press 1 for changing the name of file")
        print("press 2 for adding content to the file")
        print("press 3 for appending content to the file")
        choice = int(input("enter your choice: "))
        if choice == 1:
            new_name = input("enter the new name for the file: ")
            new_p = Path(new_name)
            if not new_p.exists():
                p.rename(new_p)
                print("file renamed successfully")
            else:
                print("a file with that name already exists")
        elif choice == 2:
            with open(p, 'a') as fs:
                data = input("enter the content you want to add: ")
                fs.write(data)
            print("content added successfully")
    else:
        print("the file does not exist")
        if choice == 3:
            with open(p, 'a') as fs:
                data = input("enter the content you want to append: ")
                fs.write(data)
            print("content appended successfully")
def deletefile():
    readfileandfolder()
    name = input("which file u want to delete")
    p = Path(name)
    if p.exists() and p.is_file():
        p.unlink()
        print("file deleted successfully")
    else:
        print("the file does not exist")

print("print 1 for creating a file")
print("print 2 for reading a file")
print("print 3 for updating a file")
print("print 4 for deleting a file")

check = int(input("pls tell your response: "))

if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()