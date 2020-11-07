from shutil import copyfile

with open("index.php", "r") as to_check, open("index_compare.php") as to_compare:
    if to_check.read() != to_compare.read():
        copyfile("index_compare.php", "index.php")
