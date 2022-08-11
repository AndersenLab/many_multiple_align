import sys
import os

from Bio import SeqIO, Align, AlignIO
from Bio.Align import AlignInfo
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align.substitution_matrices import Array

file_path = sys.argv[1]
out_path = sys.argv[2]


if len(sys.argv) == 4:
    if sys.argv[3] == "dumb":
        dumb_cons = True
    else:
        dumb_cons = False
else:
    dumb_cons = False

### params
threshold = 0.7
ambiguous = "N"
remove_threshold = 0.8
# if 80% of nucleuotides are deletions, then will not consider that position


if dumb_cons:

    alignment = AlignIO.read(open(file_path), "fasta")

    summary_align = AlignInfo.SummaryInfo(alignment)

    consensus = summary_align.dumb_consensus(ambiguous=ambiguous)

    out_seqrec = SeqRecord(consensus)
    out_seqrec.id = os.path.basename(file_path).split(".")[0] + "_consensus"
    out_seqrec.description = out_seqrec.id + \
        " length=" + str(len(consensus)) + " num_parent_seqs=" + str(len(alignment))

    with open(out_path, "w") as output_handle:
        SeqIO.write(out_seqrec, output_handle, "fasta")






else:

    record_lst = []
    with open(file_path) as handle:
        for record in SeqIO.parse(handle, "fasta"):
            record_lst.append(record)

    length = len(record_lst[0])
    # print(length)

    consensus_str = ""

    for i in range(length):
        new_letters = []
        for record in record_lst:
            new_letters.append(record.seq[i])


        if new_letters.count("-") / len(new_letters) >= remove_threshold:

            majority_letter = ""

        else:

            new_letters = list(filter(lambda x: x != "-", new_letters))
            # print(new_letters)
            
            unique_letters = list(set(new_letters))

            majority_count = 0
            majority_letter = ""
            for letter in unique_letters:
                if new_letters.count(letter) > majority_count:
                    if new_letters.count(letter) / len(new_letters) >= threshold:
                        majority_letter = letter
                    else:
                        majority_letter = ambiguous
                    majority_count = new_letters.count(letter)
            
            consensus_str += majority_letter

    # consensus_str = consensus_str.replace("-", "")


    consensus = Seq(consensus_str)

    # print(consensus)


    out_seqrec = SeqRecord(consensus)
    out_seqrec.id = os.path.basename(file_path).split(".")[0] + "_consensus"
    out_seqrec.description = out_seqrec.id + \
        " length=" + str(len(consensus)) + " num_parent_seqs=" + str(len(record_lst))


    with open(out_path, "w") as output_handle:
        SeqIO.write(out_seqrec, output_handle, "fasta")