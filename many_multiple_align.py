import sys
import os
from datetime import timedelta, date
import time
import glob

t = time.time()
d = date.today()

path = os.getcwd()

output_path = os.path.join(path, "mmalign_" + d.strftime("%m%d%y"))

dir_path = sys.argv[1]

mac_arm = False
mac_intel = False
dumb_cons = False

if len(sys.argv) < 2:
    sys.exit("Please provide a directory as input.")
elif len(sys.argv) == 2:
    pass
elif len(sys.argv) == 3:
    third_arg = sys.argv[2]
    if "macarm" in third_arg:
        mac_arm = True
    elif "macintel" in third_arg:
        mac_intel = True
    elif "dumb" in third_arg:
        dumb_cons = True
elif len(sys.argv) == 4:
    third_fourth_args = sys.argv[2:4]
    if "macarm" in third_fourth_args:
        mac_arm = True
    elif "macintel" in third_fourth_args:
        mac_intel = True
    elif "dumb" in third_fourth_args:
        dumb_cons = True

if mac_arm:
    os.system("chmod +x bin/muscle_v5_macos_arm")
elif mac_intel:
    os.system("chmod +x bin/muscle_v5_macos_intel")
else:
    os.system("chmod +x bin/muscle_v5_linux")

try:
    os.mkdir(output_path)
except:
    os.system("rm -r " + output_path)
    os.mkdir(output_path)

try:
    os.mkdir(os.path.join(output_path, "alignment_fa"))
except:
    os.system("rm -r " + os.path.join(output_path, "alignment_fa"))
    os.mkdir(os.path.join(output_path, "alignment_fa"))

try:
    os.mkdir(os.path.join(output_path, "alignment"))
except:
    os.system("rm -r " + os.path.join(output_path, "alignment"))
    os.mkdir(os.path.join(output_path, "alignment"))

try:
    os.mkdir(os.path.join(output_path, "consensus"))
except:
    os.system("rm -r " + os.path.join(output_path, "consensus"))
    os.mkdir(os.path.join(output_path, "consensus"))

try:
    os.mkdir(os.path.join(output_path, "input_data"))
except:
    os.system("rm -r " + os.path.join(output_path, "input_data"))
    os.mkdir(os.path.join(output_path, "input_data"))

print("\nReformatting Input\n")


input_data_path = output_path + "/input_data"
os.system("python3 bin/format_input_dir.py " + dir_path + " " + input_data_path)

filenames = glob.glob(input_data_path + "/*.fa")

for filename in filenames:
    print("\nAligning: " + filename + "\n")
    base_name = os.path.basename(filename).split(".")[0]
    new_efa_name = os.path.join(output_path, "alignment_fa", \
        base_name + ".efa")

    if mac_arm:
        os.system(os.path.join(path, "bin", "muscle_v5_macos_arm") + \
            " -align " + filename + " -output " + new_efa_name)
    elif mac_intel:
        os.system(os.path.join(path, "bin", "muscle_v5_macos_intel") + \
            " -align " + filename + " -output " + new_efa_name)
    else:
        os.system(os.path.join(path, "bin", "muscle_v5_linux") + " -align " + \
            filename + " -output " + new_efa_name)

    os.system("python3 " + os.path.join(path, "bin", "format_output.py") + \
        " " + new_efa_name + " " + \
            os.path.join(output_path, "alignment", base_name + ".aln"))
    if dumb_cons:
        os.system("python3 " + os.path.join(path, "bin", "make_consensus.py") + \
            " " + os.path.join(output_path, "alignment_fa", base_name + ".efa") + \
            " " + \
            os.path.join(output_path, "consensus", base_name + "_consensus.fa") + \
            " dumb")
    else:
        os.system("python3 " + os.path.join(path, "bin", "make_consensus.py") + \
            " " + os.path.join(output_path, "alignment_fa", base_name + ".efa") + \
            " " + \
            os.path.join(output_path, "consensus", base_name + "_consensus.fa"))

# os.system("rm -r " + os.path.join(output_path, "alignment_fa"))
os.system("python3 " + os.path.join(path, "bin", "combine_consensus.py") + \
    " " + os.path.join(output_path, "consensus") + " " + \
    os.path.join(output_path, "all_consensus.fa"))