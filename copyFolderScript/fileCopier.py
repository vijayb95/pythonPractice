import shutil, os, time
from os import path

class color:
   PURPLE = '\033[95m'
   RED = '\033[91m'
   END = '\033[0m'

os.chdir('C:\\Gdrive\\Testplan')

def main():
    source = 'C:\\Gdrive\\Testplan'
    destination = 'E:\\Fdrive\\testplan'
    dest = destination
    copyFolder = list(map(str, input("Enter the folder you want to copied: ").split("\\")))
    overwrite = input("Do you want to overwrite existing files? ")
    if overwrite.lower() == 'y' or overwrite.lower() == 'yes':
        overwrite = True
    else:
        overwrite = False
        duplicateFolder = input("Press 'Y' if you want to create a duplicate folder and place files whenever there is a file with same name: ")
        if duplicateFolder.lower() == 'y' or duplicateFolder.lower() == 'yes':
            duplicateFolder = True
        else: duplicateFolder = False

    for fol in copyFolder:
        source = source + '\\' + fol
        dest = dest + '\\' + fol

    if not path.exists(dest):
        print(f"Trying to copy: {source} to {dest}")
        time.sleep(2)
        shutil.copytree(source, dest)
        print(f"Successfull copied from {source} to {dest}.")
    else:
        print(f"Failed to copy: {source} to {destination}, will be trying to copy the files and sub-directories.")
        for folderName, subfolders, filenames in os.walk(source):
            print('The current folder is ' + folderName)
            fol = folderName.split("Testplan")
            dest = destination + fol[1]
            if not path.exists(dest):
                print(f"Trying to copy: {folderName} to {dest}")
                shutil.copytree(folderName, dest)
                print(f"Successfull copied from {folderName} to {dest}.")
            else:
                for filename in filenames:
                    newfilename = folderName+'\\'+filename
                    destfilename = dest +'\\'+filename
                    if overwrite:
                        print(f"copying {newfilename} to {dest}")
                        shutil.copy(newfilename, dest)
                    else:
                        if not path.exists(destfilename):
                            print(f"copying {newfilename} to {dest}")
                            shutil.copy(newfilename, dest)
                        elif duplicateFolder:
                            print(color.RED + 'Creating a Duplicates folder because the same filename exists, manual verification is recommended'  + color.END)
                            print(f"{color.PURPLE}Creating a folder named 'Duplicates' in {dest} and placing the file '{filename}'.{color.END}")
                            dup = dest+'\\Duplicates'
                            if not path.exists(dup):
                                os.mkdir(dup)
                            print(f"New folder created {dup}")
                            shutil.copy(newfilename, dup)
                        else:
                            print(f"{color.PURPLE}{filename} is ignored, due to duplicate.{color.END}")
    ex = input("Press y to exit: ")
    if ex.lower() == 'y':
        exit()
    else:
        main()

if __name__ == "__main__":
    main()