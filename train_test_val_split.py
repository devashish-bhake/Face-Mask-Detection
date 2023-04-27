import os

images_dir = "./images"
files = open("files.txt", "w")

for images in os.listdir(images_dir):
    # read the names of all the images and store in files.txt
    # print(images.split(".")[0])
    files.write(images.split(".")[0] + "\n")
print("File Creation Done")
files.close()
# split the contents of file.txt into train.txt, test.txt and val.txt with precentager 80%, 10% and 10% respectively
import random

# Set the paths for the files
files_path = r"C:\Users\Shrikant\Desktop\github_profile\face_mask_detection\files.txt"
train_path = "./train.txt"
val_path = "./val.txt"
test_path = "./test.txt"

# Set the split ratios
train_split = 0.8
val_split = 0.1
test_split = 0.1

files = open("./files.txt", "r")
# Read the list of files
files_list = files.readlines()

# Shuffle the list of files
# random.shuffle(files_list)

# Split the files into train, val, and test sets
num_files = len(files_list)
print(num_files)
num_train = int(num_files * train_split)
num_val = int(num_files * val_split)
num_test = int(num_files * test_split)

train_files = files_list[:num_train]
val_files = files_list[num_train:num_train+num_val]
test_files = files_list[num_train+num_val:]

# Write the train, val, and test files to their respective files
with open(train_path, "w") as f:
    f.writelines(train_files)

with open(val_path, "w") as f:
    f.writelines(val_files)

with open(test_path, "w") as f:
    f.writelines(test_files)

print("Train, Test and Val Split Done")