# many_multiple_align
**many_multiple_align.nf** is a pipeline for quickly performing many multiple sequence alignments; **many_multiple_align.nf** can align 100+ FASTA files containing 100+ sequences each in minutes. The program repeatedly calls [Muscle5](https://drive5.com/muscle5/), a widely used multiple sequence alignment algorithm capable of running on multiple threads, on all FASTA files found in the input directory. **many_multiple_align.nf** cannot be run locally on a macOS system.

## Installation

    git clone https://github.com/AndersenLab/many_multiple_align.git
    
    # test
    cd many_multiple_align
    nextflow many_multiple_align.nf --in test_data
    
The Muscle5 binaries are included in the installation and can be found in the **bin** directory.

In addition to Nextflow, the user should have the [Biopython](https://biopython.org/) package present in their PATH. The following command will install Biopython.
    
    pip install biopython
    
## Usage
**many_multiple_align.nf** requires one input directory path. The directory should contain at least one FASTA-formatted file (.fa or .fasta). The sequences in each FASTA file will be aligned, and a concensus sequence will be generated.

    nextflow many_multiple_align.nf --in <input_directory_path>
    
For smaller tasks, **many_multiple_align.py** can be used in place of **many_multiple_align.nf** to avoid unnecessarily overloading QUEST with job submissions. Unlike **many_multiple_align.nf**, **many_multiple_align.py** can be run locally on a macOS system.

    python3 many_multiple_align.py <input_directory_path>               # Linux OS
    python3 many_multiple_align.py <input_directory_path> -macintel     # Mac OS Intel
    python3 many_multiple_align.py <input_directory_path> -macarm       # Mac OS ARM (M1+)
    
The output directory will contain three subdirectories. **input_data** contains the original input FASTA files. **alignment** contains multiple sequence alignments in Clustal format. **consensus** contains FASTA files, each containing one consensus sequence for every input FASTA file. **all_consensus.fa** is a FASTA file that contains all consensus sequences.
