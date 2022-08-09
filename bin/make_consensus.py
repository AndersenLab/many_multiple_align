import sys
import os

from Bio import SeqIO, Align, AlignIO
from Bio.Align import AlignInfo
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align.substitution_matrices import Array

file_path = sys.argv[1]
out_path = sys.argv[2]

alignment = AlignIO.read(open(file_path), "clustal")

summary_align = AlignInfo.SummaryInfo(alignment)

consensus = summary_align.dumb_consensus(ambiguous='N')

out_seqrec = SeqRecord(consensus)
out_seqrec.id = os.path.basename(file_path).split(".")[0] + "_consensus"
out_seqrec.description = out_seqrec.id + \
    " length=" + str(len(consensus)) + " num_parent_seqs=" + str(len(alignment))

with open(out_path, "w") as output_handle:
    SeqIO.write(out_seqrec, output_handle, "fasta")