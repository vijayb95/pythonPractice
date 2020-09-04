import shutil, os
from os import path

class color:
   PURPLE = '\033[95m'
   END = '\033[0m'

os.chdir('C:\\Gdrive\\Testplan')

def main():
    source = 'C:\\Gdrive\\Testplan'
    destination = 'E:\\Fdrive\\testplan'
    dest = destination
    copyFolder = list(map(str, input("Enter the folder you want to copied: ").split("\\")))

    for fol in copyFolder:
        source = source + '\\' + fol
        dest = dest + '\\' + fol

    if not path.exists(dest):
        print(f"Trying to copy: {source} to {dest}")
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
                    if not path.exists(destfilename):
                        print(f"copying {newfilename} to {dest}")
                        shutil.copy(newfilename, dest)
                    else:
                        print(color.PURPLE + 'Creating a Duplicates folder, manual verification is recommended'  + color.END)
                        print(f"{newfilename} already exists in {dest}. So creating a folder named 'duplicates' in {dest} and placing the file.")
                        dup = dest+'\\Duplicates'
                        if not path.exists(dup):
                            os.mkdir(dup)
                        print(f"New folder created {dup}")
                        shutil.copy(newfilename, dup)

if __name__ == "__main__":
    main()