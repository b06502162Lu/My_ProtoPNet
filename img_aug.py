import Augmentor
import os


"""

data_dir = "./datasets/cub200_cropped/train_cropped/" 
target_dir = "./datasets/cub200_cropped/train_cropped_augmented/" 
"""
#print(len(os.listdir(data_dir)))
folders = []
img_dir = []
for i in os.listdir(os.getcwd()) :
    folders.append(i)
    img_dir.append(i)
#print(len(folders))



for i in range(len(folders)):
    fd = folders[i]
    tfd = img_dir[i]
    print(fd)
    print(tfd)
    # rotation
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.rotate(probability=1, max_left_rotation=15, max_right_rotation=15)
    p.flip_left_right(probability=0.5)
    for i in range(10):
        p.process()
    del p
    print("finish rotation")
    # skew
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.skew(probability=1, magnitude=0.2)  # max 45 degrees
    p.flip_left_right(probability=0.5)
    for i in range(10):
        p.process()
    del p
    print("finish skew")
    # shear
    p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    p.shear(probability=1, max_shear_left=10, max_shear_right=10)
    p.flip_left_right(probability=0.5)
    for i in range(10):
        p.process()
    del p
    print("finish shear")
    # random_distortion
    #p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
    #p.random_distortion(probability=1.0, grid_width=10, grid_height=10, magnitude=5)
    #p.flip_left_right(probability=0.5)
    #for i in range(10):
    #    p.process()
    #del p
print("finish image augmentation")
