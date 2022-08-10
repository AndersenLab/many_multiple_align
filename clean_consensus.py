import os
import sys
from Bio import SeqIO, Align, AlignIO
from Bio.Seq import Seq

file_path = sys.argv[1]
out_path = "/".join(file_path.split("/")[:-1]) + "/cleaned_all_consensus.fa"

try:
    remove_threshold = float(sys.argv[2])
except:
    remove_threshold = 0.3


ambiguous = 'N'


print("\n\nCleaning file: " + os.path.basename(file_path))
print("\n\nRemoving sequences containing > " + str(remove_threshold*100) + \
    "% ambiguous nucleotides\n\n")

records = SeqIO.parse(file_path, "fasta")
out_recs = []
for record in records:
    if record.seq.count(ambiguous) > len(record.seq) * remove_threshold:
        print("Removing sequence: " + record.id)
    else:
        out_recs.append(record)

with open(out_path, "w") as output_handle:
    SeqIO.write(out_recs, output_handle, "fasta")