import glob
import os
import sys

try:
    os.mkdir("data")
except:
    os.system("rm -r data")
    os.mkdir("data")

dir_path = sys.argv[1]
filenames = glob.glob(dir_path + "/*")

for filename in filenames:
    path = filename.split("/")[:-1]
    path = "/".join(path) + "/"
    if ".fa" in filename.split("/")[-1]:
        new_name = "data/" + (filename.split("/")[-1]).split(".")[0] + ".fa"
        os.system("cp " + filename + " " + new_name)
    else:
        pass