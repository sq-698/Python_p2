import glob

list_of_files = glob.glob('files/*.txt')
for AF in list_of_files:
    with open(AF, "r") as f:
         poem = f.read()
    if poem == "0":
        print(poem)
        print(AF)



