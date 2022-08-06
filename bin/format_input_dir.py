import glob
import os
import sys

dir_path = sys.argv[1]
out_path = sys.argv[2]

try:
    os.mkdir(out_path)
except:
    os.system("rm -r " + out_path)
    os.mkdir(out_path)


filepaths = glob.glob(dir_path + "/*")


for filepath in filepaths:
    filename = os.path.basename(filepath)
    if ".fa" in filename:
        newpath = os.path.join(out_path, filename.split(".")[0] + ".fa")
        os.system("cp " + filepath + " " + newpath)
    else:
        pass