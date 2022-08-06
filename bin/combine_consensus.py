import sys
import os
import glob
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

dir_path = sys.argv[1]
out_path = sys.argv[2]

filepaths = glob.glob(dir_path + "/*.fa")

seqrec_list = []
for filepath in filepaths:
    records = SeqIO.parse(filepath, "fasta")
    seqrec_list.extend(records)

try:
    SeqIO.write(seqrec_list, out_path, "fasta")
except:
    out = SeqRecord(Seq("A"))
    SeqIO.write(out, out_path, "fasta")