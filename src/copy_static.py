from os.path import exists, join, isfile
from os import listdir, mkdir
from shutil import copy, rmtree

def copy_dir(src: str, dest: str):
    dir_list: list[str] = listdir(src)
    print(dir_list)
    for dir in dir_list:
        if isfile(join(src, dir)):
            if not exists(join(dest, dir)):
                print(f"{join(src, dir)} is a file and copied to {join(dest, dir)}")
                copy(join(src, dir), join(dest, dir))
        else:
            print(f"{join(src, dir)} is not a file")
            if not exists(join(dest, dir)):
                mkdir(join(dest, dir))
                print(f"{join(dest, dir)} is created")
                copy_dir(src=join(src, dir), dest=join(dest, dir))

def copy_static():
    if exists("public"):
        print("Removing old public dir")
        rmtree("public")

    print("Creating new public dir")
    mkdir("public")
    copy_dir(src="static", dest="public")