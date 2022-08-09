#!/usr/bin/env nextflow
date = new Date().format('MMddyy')
params.in = null
params.out = projectDir + "/mmalign_${date}"
params.cons = ""


new_dir = file(params.out)
new_dir.mkdir()

cleaned_input_dir = new_dir + "/input_data"
cleaned_input_dir.mkdir()

efa_dir = new_dir + "/alignment_efa"
efa_dir.mkdir()

aln_dir = new_dir + "/alignment"
aln_dir.mkdir()

consensus_dir = new_dir + "/consensus"
consensus_dir.mkdir()


"chmod +x bin/muscle_v5_linux".execute()
muscle_path = projectDir + "/bin/muscle_v5_linux"


println "\nReformatting Input\n"
"python3 bin/format_input_dir.py ${params.in} ${cleaned_input_dir}".execute()
int waitFor = 10;
Thread.sleep(waitFor * 1000);


println "\nAlignment\n"

workflow{
    Channel.fromPath("${cleaned_input_dir}/*.fa") | align
    align.out.collect() | consensus

}

workflow.onComplete {
    println "Pipeline completed at: $workflow.complete"
    println "Execution status: ${ workflow.success ? 'OK' : 'failed' }"
}

process align{
    cpus 8
    memory '16 GB'

    input:
    file fast
    
    output:
    stdout

    
    script:

    """
    #!/usr/bin/env python
    import sys
    import os

    base_name = str.split(os.path.basename("${fast}"), ".")[0]

    efa = os.path.join("${efa_dir}", base_name + ".efa")
    aln = os.path.join("${aln_dir}", base_name + ".aln")
    cons = os.path.join("${consensus_dir}", base_name + "_consensus.fa")

    os.system("${muscle_path} -super5 ${fast} -output " + efa)
    os.system("python3 ${projectDir}/bin/format_output.py " + efa + " " + aln)
    os.system("python3 ${projectDir}/bin/make_consensus.py " + efa + " " + cons + " ${params.cons}")
    print("${fast}")
    """
}

process consensus{
    cpus 1
    memory '4 GB'

    input:
    stdin

    """
    python3 ${projectDir}/bin/combine_consensus.py ${consensus_dir} ${new_dir}/all_consensus.fa
    exit
    """
}