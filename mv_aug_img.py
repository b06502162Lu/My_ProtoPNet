import os
folders = []
img_dir = []
for i in os.listdir(os.getcwd()) :
    folders.append(i)
    img_dir.append(i)

for i in range(len(folders)):
    
    fd = folders[i]+"/"+img_dir[i]
    if len(fd) == 0 :
        print(fd,"$$$$$$$$$$$$$")
    print(folders[i],"  :  ",len(fd))
    cmd = "mv "+fd+" "+"../train_cropped_augmented"
    fp = os.popen(cmd)