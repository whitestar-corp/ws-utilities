import os
import shutil
import os.path

srcpath = r"./unsorted"
srcfiles = os.listdir(srcpath)

destpath = r"./sorted"

# extracts the twnshp/range from filenames and filter out duplicates
#destdirs = list(set([filename[6:13] for filename in srcfiles]))
for srcfile in srcfiles:
    state = srcfile[:2]
    meridian = srcfile[2:4]
    townrange = srcfile.split('_')[1]

    dest = os.path.join(destpath, state, meridian, townrange)

    if not os.path.exists(dest):
        os.makedirs(dest)
    
    filename = os.path.basename(srcfile)

    # add filename to destination path
    dest = os.path.join(dest, filename)
    src = os.path.join(srcpath, srcfile)
    os.rename(src, dest)    