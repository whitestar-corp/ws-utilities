import os
import shutil
import os.path

srcpath = r"D:\OH\unsorted"
srcfiles = os.listdir(srcpath)

destpath = r"D:\OH\sorted"

# extracts the twnshp/range from filenames and filter out duplicates
destdirs = list(set([filename[6:13] for filename in srcfiles]))


def create(dirname, destpath):
    full_path = os.path.join(destpath, dirname)
    if os.path.isdir(full_path):
        os.mkdir(full_path)
    return full_path

def move(filename, dirpath):shutil.move(os.path.join(srcpath, filename),dirpath)

# create destination directories and store their names along with full paths
targets = [(folder, create(folder, destpath)) for folder in destdirs]

for dirname, full_path in targets:
    for filename in srcfiles:
        if dirname == filename[0:2]:
            move(filename, full_path)d