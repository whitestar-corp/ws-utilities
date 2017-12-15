import os
import sys
from shutil import copyfile

# Root folder to start walking subfolders and files
walk_dir = sys.argv[1]

limit = -1

imageSuffix = "JP2"
metadataSuffix = "JP2.xml"

templateFile = "template.xml"

# read the metadata template to use
with open(templateFile, "r") as inputFile:
    xmlData = inputFile.read()
    print("This template will be used: \n %s" % xmlData)

print(os.path.join(os.getcwd(), templateFile))

if(sys.argv.count > 1):
    limit = sys.argv[2]
    print('Limiting output to %s files' % limit)

# read the metadata template to use
#with open("template.xml", "r") as inputFile:
#    xmlData = inputFile.read()

print('Relocating and Creating Metadata files for: ' + os.path.abspath(walk_dir))

filecount = 0

for root, subdirs, files in os.walk(walk_dir):

    if(int(filecount) > int(limit)):
        print("hit limit")
        break

    for filename in files:
        
        filecount += 1
    
        file_path = os.path.join(root, filename)

        k = file_path.rfind(".")

        metadatafile = file_path[:k] + ".xml"

        splits = filename.split("_")

        if not len(splits) == 3:
            print("Skipping %s %d" % (filename, len(splits)))
            break

        outfolder = splits[0] + "_" + splits[1]

        if not os.path.exists(outfolder):
            os.mkdir(outfolder)

        print("Will save this as : %s/%s" % (outfolder, filename))

        if filename.endswith(metadataSuffix): 
            copyfile("template.xml",os.path.join(outfolder, filename))
        else:
            copyfile(file_path, os.path.join(outfolder, filename))