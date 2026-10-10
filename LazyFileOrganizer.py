import os 
import shutil


path = input("Enter the Folder Path to Organize: "  )
files = os.listdir(path)
for file in files:
    Filename,extension = os.path.splitext(file)
    extensions = extension[1:]

    if os.path.exists(path + "/" + extensions):
        shutil.move(path + "/" + file, path + "/" + extensions + "/" + file)
    else:
        os.makedirs(path + "/" + extensions)
        shutil.move(path + "/" + file, path + "/" + extensions + "/" + file) 