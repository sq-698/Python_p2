import glob

list_of_files = glob.glob('files-new/*.txt')
list_of_files_name = []
list_of_files_text = []
file_no_child = []


for AF in list_of_files:
    list_of_files_name.append(AF[10:20])

for AF in list_of_files:
    with open(AF, "r") as f:
        tf = f.read()
    list_of_files_text.append(tf)

for N in list_of_files_name:
    if not(N in list_of_files_text):
        file_no_child.append(N)


file_no_child.sort()

with open("no_children.txt", "w") as f:
    for CH in file_no_child:
        f.write(CH + "\n")

print("finish")





