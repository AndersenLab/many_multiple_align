# many_multiple_align
**many_multiple_align.py** is a simple tool for quickly performing many multiple sequence alignments at once using QUEST (or another Linux OS machine). The program repeatedly calls [Muscle5](https://drive5.com/muscle5/), a widely used multiple sequence alignment algorithm capable of running on multiple threads, on all FASTA files found in the input directory. **many_multiple_align.py** cannot be run locally on a macOS system.
## Installation

    git clone https://github.com/AndersenLab/many_multiple_align.git
    
    # test
    cd many_multiple_align
    python3 many_multiple_align.py test_data
    
The Muscle5 Linux binary is included in the installation and can be found in the **bin** directory.

The user should also have the [Biopython](https://biopython.org/) package present in their PATH. The following command will install Biopython.
    
    pip install biopython
    
## Usage
**many_multiple_align.py** requires one input directory/directory path. The directory should contain at least one FASTA-formatted file (.fa or .fasta).

    python3 many_multiple_align.py <input_directory_path>

It outputs a directory containing three subdirectories: **data**, **output_efa**, and **output_aln**. **data** contains copies of the FASTA files found in the input directory. **output_efa** contains multiple sequence alignments in [EFA](https://biopython.org/wiki/Download) format; within the context of **many_multiple_align.py**, there is no difference between the EFA format and the familiar FASTA format. **output_aln** contains multiple sequence alignments in the Clustal format.
