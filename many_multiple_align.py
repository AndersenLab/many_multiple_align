import glob
import os
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from datetime import timedelta, date
import time

t = time.time()
d = date.today()

dir_path = sys.argv[1]
path = os.getcwd()
output_path = "muscle_" + d.strftime("%m%d%y")

os.system("chmod +x bin/muscle_v5")

print("\nCOPYING DATA\n")
os.system("python3 bin/copy_data.py " + dir_path)

filenames = glob.glob(path + "/data/*.fa")

try:
    os.mkdir("output_efa")
except:
    os.system("rm -r output_efa")
    os.mkdir("output_efa")

try:
    os.mkdir(output_path)
except:
    os.system("rm -r " + output_path)
    os.mkdir(output_path)

print("\nRUNNING MUSCLE\n")
for filename in filenames:
    new_name = path + "/output_efa/" + \
    os.path.basename(filename).split(".")[0] + ".efa"
    os.system(path + "/bin/" + "muscle_v5 " + "-align " + filename + 
    " -output " + new_name)
    print("\nTime elapsed:", timedelta(seconds= time.time() - t))

print("\nFORMATTING DATA\n")
os.system("python3 bin/format_output.py")

os.system("mv data " + output_path)
os.system("mv output_aln " + output_path)
os.system("mv output_efa " + output_path)

print("Alignments can be found in the directory named: " + output_path)
print("\nTime elapsed:", timedelta(seconds= time.time() - t))
