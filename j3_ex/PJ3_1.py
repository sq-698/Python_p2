import glob

list_of_files = glob.glob('files-new/*.txt')
for AF in list_of_files:
    with open(AF, "r") as f:
         txt_f = f.read()
    if txt_f == "0":
        print(txt_f)
        print(AF)
#GIT 3
#git4


