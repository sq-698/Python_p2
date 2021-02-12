import glob

list_of_files = glob.glob('files-new/*.txt')
list_of_files_name = []
list_of_files_text = []
file_no_child = []


for AF in list_of_files:
    list_of_files_name.append(AF[10:20])

for AF in list_of_files:
    with open(AF, "r") as f:
        txt = f.read()
    list_of_files_text.append(txt)

for N in list_of_files_name:
    if not(N in list_of_files_text):
        file_no_child.append(N)



l1 = []
for e in file_no_child:
    fn = e
    i = 0
    i = i + 1
    l2 = [fn]
    while fn != "0":
        ee = "files-new/" + fn + ".txt"
        with open(ee, "r") as f:
            fn = f.read()
            l2.append(fn)

    if len(l2) > len(l1):
        l1 = list(l2)

print("Items in Root:")
for j in l1:
    print(j)

print(f'the length Root= {len(l1)}')


























