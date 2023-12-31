import os

# folder path
dir_path = './data3'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
#print(res)
print(len(res))
print(res[0])
checker = True
pngcounter = 0
txtcounter = 0
for x in res:
    if x.endswith(".png"):
        pngcounter +=1
    if x.endswith(".txt"):
        txtcounter +=1
print(txtcounter)
print(pngcounter)
pngcounter = 0
txtcounter = 0
counter = 0
for x in res:
   if x.endswith(".png"):
        name = x[:-4]
        if (name+".txt") not in res:
            print(name)