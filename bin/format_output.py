import glob
import os
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

path = os.getcwd()
try:
    os.mkdir("output_aln")
except:
    os.system("rm -r output_aln")
    os.mkdir("output_aln")

filenames = glob.glob(path + "/output_efa/*.efa")
# print(len(filenames))

for filename in filenames:

    records = SeqIO.parse(filename, "fasta")
    new_filename = "/".join(filename.split("/")[:-2]) + "/output_aln/" + \
        (filename.split("/")[-1]).split(".")[0] + ".aln"
    try:
        SeqIO.write(records, new_filename, "clustal")
    except:
        out = SeqRecord(Seq("A"))
        out.id = "NO SEQUENCE FOUND"
        SeqIO.write(out, new_filename, "clustal")