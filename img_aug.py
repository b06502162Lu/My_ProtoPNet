import Augmentor
import os
def makedir(path):
    '''
    if path does not exist in the file system, create it
    '''
    if not os.path.exists(path):
        os.makedirs(path)

datasets_root_dir = './datasets/cub200_cropped/'
dir_ = datasets_root_dir + 'train_cropped/'
target_dir = datasets_root_dir + 'train_cropped_augmented/'

folders = list()
target_folders = list()
for name in os.listdir(dir_) :
    path = os.path.join(dir_,name)
    list.append(path)

for name in os.listdir(target_dir) :
    path = os.path.join(target_dir,name)
    list.append(path)

for i in range(10) :
    print("This is folder ",i," ",folders[i])
print("final",folders[-1])
#print("This is target:  ",target_folders)
print("\n\n\n\n")
"""
#makedir(target_dir)
folders = [os.path.join(dir, folder) for folder in next(os.walk(dir))[1]]
target_folders = [os.path.join(target_dir, folder) for folder in next(os.walk(dir))[1]]
for i in range(10) :
    print("This is folder ",i," ",folders[i])
print("final",folders[-1])
#print("This is target:  ",target_folders)
print("\n\n\n\n")
"""



for i in range(len(folders)):
    fd = folders[i]
    tfd = target_folders[i]

    #print("This is fd:  ",fd)
    #print("This is tfd:  ",tfd)
    #print("\n\n\n\n")

    # rotation
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.rotate(probability=1, max_left_rotation=15, max_right_rotation=15)
    p.flip_left_right(probability=0.5)
    for i in range(10):
        p.process()
    del p
    # skew
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.skew(probability=1, magnitude=0.2)  # max 45 degrees
    p.flip_left_right(probability=0.5)
    for i in range(10):
        p.process()
    del p
    # shear
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.shear(probability=1, max_shear_left=10, max_shear_right=10)
    p.flip_left_right(probability=0.5)
    for i in range(10):
        p.process()
    del p
    # random_distortion
    #p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    #p.random_distortion(probability=1.0, grid_width=10, grid_height=10, magnitude=5)
    #p.flip_left_right(probability=0.5)
    #for i in range(10):
    #    p.process()
    #del p
