import os
import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

file_path = sys.argv[1]
out_path = sys.argv[2]

records = SeqIO.parse(file_path, "fasta")
try:
    SeqIO.write(records, out_path, "clustal")
except:
    out = SeqRecord(Seq("A"))
    SeqIO.write(out, out_path, "clustal")