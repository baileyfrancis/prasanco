# Import required modules
import argparse 
import os

# Extract useful information for use downstream 
prasanco_path = os.path.dirname(os.path.realpath(__file__))

#================================================================
# Create arguments to be passed to the command line using argparse
#================================================================
parser=argparse.ArgumentParser(description='PrAsAnCo will assemble, annotate and compare two prokaryotic genomes using both Illumina short-read and Oxford Nanopore long-read data as inputs')

subparsers = parser.add_subparsers(title='Commands', dest='command')

# Create PrAsAnCo initial_assembly command
InitialAssembly_parser = subparsers.add_parser('initial_assembly', help='create initial assemblys for both of your samples using Oxford Nanopore long-read data. This step will take your long-reads, assemble them and attempt to cluster them in to contigs')
InitialAssembly_parser.add_argument('--label1', metavar='Label for your first sample', type=str, help='This label will be applied to all files relating to your first sample', required=True)
InitialAssembly_parser.add_argument('--label2', metavar='Label for your second sample', type=str, help='This label will be applied to all files relating to your second sample', required=True)
InitialAssembly_parser.add_argument('--reads1', metavar='Long reads for your first sample', type=str, help='Please provide a single file containing all your Oxford Nanopore long-reads for your first sample', required=True)
InitialAssembly_parser.add_argument('--reads2', metavar='Long reads for your second sample', type=str, help='Please provide a single file containing all your Oxford Nanopore long-reads for your second sample', required=True)
InitialAssembly_parser.add_argument('--threads', metavar='Number of threads', type=str, help='Specify the number of threads you wish to allocate to this job. Recommended = 8', required=True)
InitialAssembly_parser.add_argument('--conda', metavar='Path to your Conda/Miniconda environment directory', type=str, help='Please procide the absolute path to your Conda/Miniconda environments directory e.g. /shared/home/mbxbf2/miniconda3/envs', required=True)
InitialAssembly_parser.add_argument('--out_dir', metavar='Output directory', type=str, help='Output directory for your initial assemblies')

# Create PrAsAnCo reconcile command
Reconcile_parser = subparsers.add_parser('reconcile', help='Perform the Trycycler reconciliation step for each of your samples')
Reconcile_parser.add_argument('--clusters1', nargs='*', metavar='Clusters for your first sample', type=str, help='Specify the clusters you wish to reconcile for your first sample. E.g. --clusters1 cluster_001 cluster_002 cluster_003')
Reconcile_parser.add_argument('--clusters2', nargs='*', metavar='Clusters for your second sample', type=str, help='Specify the clusters you wish to reconcile for your second sample. E.g. --clusters1 cluster_001 cluster_002 cluster_003')
Reconcile_parser.add_argument('--label1', metavar='Label for your first sample', type=str, help='Please provide the same label for your first sample as you used for Step 1', required=True)
Reconcile_parser.add_argument('--label2', metavar='Label for your second sample', type=str, help='Please provide the same label for your second sample as you used for Step 1', required=True)
Reconcile_parser.add_argument('--prasanco_dir', metavar='Path to your PrAsAnCo output directory', type=str, help='Please provide the path to your PrAsAnCo output directory', required=True)
Reconcile_parser.add_argument.add_argument('--conda', metavar="path to your conda /envs directory", type=str, help='Please provide the absolute path to your conda /envs directory e.g. /shared/home/mbxbf2/miniconda3/envs')

# Create PrAsAnCo msa command 
MSA_parser = subparsers.add_parser('msa', help = 'Perform a multiple sequence alignment for each of your samples contigs')
MSA_parser.add_argument('--label1', metavar='Label for your first sample', type=str, help='Please provide the same label for your first sample as you used for Step 1 and 2', required=True)
MSA_parser.add_argument('--label2', metavar='Label for your second sample', type=str, help='Please provide the same label for your second sample as you used for Step 1 and 2', required=True)
MSA_parser.add_argument('--clusters1', nargs='*', metavar='Clusters for your first sample', type=str, help='Specify the clusters you wish to align for your first sample. E.g. --clusters1 cluster_001 cluster_002 cluster_003')
MSA_parser.add_argument('--clusters2', nargs='*', metavar='Clusters for your second sample', type=str, help='Specify the clusters you wish to align for your second sample. E.g. --clusters1 cluster_001 cluster_002 cluster_003')
MSA_parser.add_argument('--prasanco_dir', metavar='Path to your PrAsAnCo output directory', type=str, help='Please provide the path to your PrAsAnCo output directory', required=True)
MSA_parser.add_argument.add_argument('--conda', metavar="path to your conda /envs directory", type=str, help='Please provide the absolute path to your conda /envs directory e.g. /shared/home/mbxbf2/miniconda3/envs/', required=True)

#Create PrAsAnCo final_assembly command
FinalAssembly_parser = subparsers.add_parser('final_assembly', help='Finish the Trycycler assemblies for both of your samples and polish them.')
FinalAssembly_parser.add_argument('--label1', metavar='Label for your first sample', type=str, help='Please proved the same label for your first sample as you used in Steps 1, 2 and 3', required=True)
FinalAssembly_parser.add_argument('--label2', metavar='Label for your second sample', type=str, help='Please proved the same label for your second sample as you used in Steps 1, 2 and 3', required=True)
FinalAssembly_parser.add_argument('--long1', metavar='Long reads for your first sample', type=str, help='Please provide the path to your filtered long reads for your first sample produced in Step 1. These should be named [label1]_reads.fastq', required=True)
FinalAssembly_parser.add_argument('--long1', metavar='Long reads for your second sample', type=str, help='Please provide the path to your filtered long reads for your second sample produced in Step 1. These should be named [label2]_reads.fastq', required=True)
FinalAssembly_parser.add_argument('--short1_R1', metavar='R1 short reads for your first sample', type=str, help='A single file containing your R1 Illumina short-reads for your first sample', required=True)
FinalAssembly_parser.add_argument('--short1_R2', metavar='R2 short reads for your first sample', type=str, help='A single file containing your R2 Illumina short-reads for your first sample', required=True)
FinalAssembly_parser.add_argument('--short2_R1', metavar='R1 short reads for your second sample', type=str, help='A single file containing your R1 Illumina short-reads for your second sample', required=True)
FinalAssembly_parser.add_argument('--short2_R2', metavar='R2 short reads for your second sample', type=str, help='A single file containing your R2 Illumina short-reads for your second sample', required=True)
FinalAssembly_parser.add_argument('--clusters1', nargs='*', metavar='Clusters for your first sample', type=str, help='Please specify the clusters for your first sample e.g. cluster_01 cluster_02 cluster_03', required=True)
FinalAssembly_parser.add_argument('--clusters1', nargs='*', metavar='Clusters for your second sample', type=str, help='Please specify the clusters for your second sample e.g. cluster_01 cluster_02 cluster_03', required=True)
FinalAssembly_parser.add_argument('--prasanco_dir', metavar='Path to your PrAsAnCo output directory', type=str, help='Please provide the path to your PrAsAnCo output directory', required=True)
FinalAssembly_parser.add_argument('--threads', metavar='Number of threads', type=str, help='Specify the number of threads you wish to allocate. Recommended = 8', required=True)
FinalAssembly_parser.add_argument('--conda', metavar="path to your conda /envs directory", type=str, help='Please provide the absolute path to your conda /envs directory e.g. /shared/home/mbxbf2/miniconda3/envs', required=True)

#Create PrAsAnCo QC command 
QC_parser = subparsers.add_parser('QC', help='Perform QC on your final assemblies for your two samples')
QC_parser.add_argument('--label1', metavar='Label for your first sample', type=str, help='This label will be applied to all files relating to your first sample', required=True)
QC_parser.add_argument('--label2', metavar='Label for your second sample', type=str, help='This label will be applied to all files relating to your second sample', required=True)
QC_parser.add_argument('--reference', metavar='Reference assembly for your sample', type=str, help='Please provide a reference assembly for your samples', required=True)
QC_parser.add_argument('--prasanco_dir', metavar='Path to your PrAsAnCo output directory', type=str, help='Please provide the path to your PrAsAnCo output directory', required=True)
QC_parser.add_argument('--conda', metavar="path to your conda /envs directory", type=str, help='Please provide the absolute path to your conda /envs directory e.g. /shared/home/mbxbf2/miniconda3/envs')

# Create PrAsAnCo annotate command 
Annotate_parser = subparsers.add_parser('annotate', help='Annotate both of your samples using PROKKA')
Annotate_parser.add_argument('--label1', metavar='Label for your first sample', type=str, help='Please provide a label for your first sample. This name will be added to all output files relating to your first sample', required=True)
Annotate_parser.add_argument('--label2', metavar='Label for your second sample', type=str, help='Please provide a label for your second sample. This name will be added to all output files relating to your second sample', required=True)
Annotate_parser.add_argument('--assembly1' metavar='Final assembly for your first sample', type=str, help='Please provide the path to your final PrAsAnCo assembly for your first sample. This should be named [label1]_final_assembly.fasta', required=True)
Annotate_parser.add_argument('--assembly2' metavar='Final assembly for your second sample', type=str, help='Please provide the path to your final PrAsAnCo assembly for your second sample. This should be named [label2]_final_assembly.fasta', required=True)
Annotate_parser.add_argument('--reference', metavar='Reference assembly for your sample', type=str, help='Please provide a reference assembly for your samples')
Annotate_parser.add_argument('--kingdom', metavar='Kingdom name for your samples', type=str, help='Please provide the kingdom name for your samples e.g. Archaea')
Annotate_parser.add_argument('--genus', metavar='Genus name for your samples', type=str, help='Please provide the genus name for your samples e.g. Haloferax', required=True)
Annotate_parser.add_argument('--species', metavar='Species name for your samples', type=str, help='Please provide the species name for your samples e.g. volcanii', required=True)
Annotate_parser.add_argument('--prasanco_dir', metavar='Path to your PrAsAnCo output directory', type=str, help='Please provide the path to your PrAsAnCo output directory', required=True)
Annotate_parser.add_argument.add_argument('--conda', metavar="path to your conda /envs directory", type=str, help='Please provide the absolute path to your conda /envs directory e.g. /shared/home/mbxbf2/miniconda3/envs')

args = parser.parse_args()

#==================================
# PrAsAnCo initial_assembly command
#==================================

if args.command == 'initial_assembly':
	
	os.mkdir(args.out_dir) # Create an ouput directory for the initial assembly
	os.mkdir(f'{args.out_dir}/BatchScripts')
	os.mkdir(f'{args.out_dir}/BatchScripts/OutErr')
	
	if args.conda.endswith('/') == False:
		args.conda = args.conda + '/'

	InitialAssembly_script = open('InitialAssembly.sh', 'w+')
	InitialAssembly_script.write('#!/bin/bash\n' +
		'#SBATCH --job-name=InitialAssembly\n' +
		'#SBATCH --nodes=1\n' +
		'#SBATCH --tasks-per-node=1\n' +
		'#SBATCH --cpus-per-task=4\n' +
		'#SBATCH --mem=15g\n' +
		'#SBATCH --time=48:00:00\n' +
		f'#SBATCH --output={args.out_dir}/BatchScripts/OutErr/%x.out\n' +
		f'#SBATCH --error={args.out_dir}/BatchScripts/OutErr/%x.err\n\n' +
		'source $HOME/.bash_profile\n' +
		f'conda activate {args.conda}prasanco_py3\n\n' +
		f'filtlong --min_length 1000 --keep_percent 95 {args.reads1} > {args.label1}_reads.fastq\n' +
		f'filtlong --min_length 1000 --keep_percent 95 {args.reads2} > {args.label2}_reads.fastq\n' +
		f'mv {args.label1}_reads.fastq {args.out_dir}\n' +
		f'mv {args.label2}_reads.fastq {args.out_dir}\n\n' +
		f'trycycler subsample --reads {args.out_dir}/{args.label1}_reads.fastq --out_dir {args.out_dir}/read_subsets_1\n' +
		f'trycycler subsample --reads {args.out_dir}/{args.label2}_reads.fastq --out_dir {args.out_dir}/read_subsets_2\n\n' +
		f'mkdir {args.out_dir}/{args.label1}_assemblies\n' +
		f'mkdir {args.out_dir}/{args.label2}_assemblies\n\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_1/sample_01.fastq --threads {args.threads} --out-dir assembly_01 && cp assembly_01/assembly.fasta {args.out_dir}/{args.label1}_assemblies/assembly_01.fasta && rm -r assembly_01\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_1/sample_02.fastq {args.threads} > assembly_02.gfa && any2fasta assembly_02.gfa > {args.out_dir}/{args.label1}_assemblies/assembly_02.fasta && rm assembly_02.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_1/sample_03.fastq > {args.out_dir}/{args.label1}_assemblies/assembly_03.fasta && rm raven.cereal\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_1/sample_04.fastq --threads {args.threads} --out-dir assembly_04 && cp assembly_04/assembly.fasta {args.out_dir}/{args.label1}_assemblies/assembly_04.fasta && rm -r assembly_04\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_1/sample_05.fastq {args.threads} > assembly_05.gfa && any2fasta assembly_05.gfa > {args.out_dir}/{args.label1}_assemblies/assembly_05.fasta && rm assembly_05.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_1/sample_06.fastq > {args.out_dir}/{args.label1}_assemblies/assembly_06.fasta && rm raven.cereal\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_1/sample_07.fastq --threads {args.threads} --out-dir assembly_07 && cp assembly_07/assembly.fasta {args.out_dir}/{args.label1}_assemblies/assembly_07.fasta && rm -r assembly_07\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_1/sample_08.fastq {args.threads} > assembly_08.gfa && any2fasta assembly_08.gfa > {args.out_dir}/{args.label1}_assemblies/assembly_08.fasta && rm assembly_08.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_1/sample_09.fastq > {args.out_dir}/{args.label1}_assemblies/assembly_09.fasta && rm raven.cereal\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_1/sample_10.fastq --threads {args.threads} --out-dir assembly_10 && cp assembly_10/assembly.fasta {args.out_dir}/{args.label1}_assemblies/assembly_10.fasta && rm -r assembly_10\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_1/sample_11.fastq {args.threads} > assembly_11.gfa && any2fasta assembly_11.gfa > {args.out_dir}/{args.label1}_assemblies/assembly_11.fasta && rm assembly_11.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_1/sample_12.fastq > {args.out_dir}/{args.label1}_assemblies/assembly_12.fasta && rm raven.cereal\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_2/sample_01.fastq --threads {args.threads} --out-dir assembly_01 && cp assembly_01/assembly.fasta {args.out_dir}/{args.label2}_assemblies/assembly_01.fasta && rm -r assembly_01\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_2/sample_02.fastq {args.threads} > assembly_02.gfa && any2fasta assembly_02.gfa > {args.out_dir}/{args.label2}_assemblies/assembly_02.fasta && rm assembly_02.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_2/sample_03.fastq > {args.out_dir}/{args.label2}_assemblies/assembly_03.fasta && rm raven.cereal\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_2/sample_04.fastq --threads {args.threads} --out-dir assembly_04 && cp assembly_04/assembly.fasta {args.out_dir}/{args.label2}_assemblies/assembly_04.fasta && rm -r assembly_04\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_2/sample_05.fastq {args.threads} > assembly_05.gfa && any2fasta assembly_05.gfa > {args.out_dir}/{args.label2}_assemblies/assembly_05.fasta && rm assembly_05.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_2/sample_06.fastq > {args.out_dir}/{args.label2}_assemblies/assembly_06.fasta && rm raven.cereal' +
		f'flye --nano-hq {args.out_dir}/read_subsets_2/sample_07.fastq --threads {args.threads} --out-dir assembly_07 && cp assembly_07/assembly.fasta {args.out_dir}/{args.label2}_assemblies/assembly_07.fasta && rm -r assembly_07\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_2/sample_08.fastq {args.threads} > assembly_08.gfa && any2fasta assembly_08.gfa > {args.out_dir}/{args.label2}_assemblies/assembly_08.fasta && rm assembly_08.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_2/sample_09.fastq > {args.out_dir}/{args.label2}_assemblies/assembly_09.fasta && rm raven.cereal\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_2/sample_10.fastq --threads {args.threads} --out-dir assembly_10 && cp assembly_10/assembly.fasta {args.out_dir}/{args.label2}_assemblies/assembly_10.fasta && rm -r assembly_10\n' +
		f'{prasanco_path}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_2/sample_11.fastq {args.threads} > assembly_11.gfa && any2fasta assembly_11.gfa > {args.out_dir}/{args.label2}_assemblies/assembly_11.fasta && rm assembly_11.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_2/sample_12.fastq > {args.out_dir}/{args.label2}_assemblies/assembly_12.fasta && rm raven.cereal\n\n' +
		f'trycycler cluster --assemblies {args.out_dir}/{args.label1}_assemblies/*.fasta --reads {args.out_dir}/{args.label1}_reads.fastq --out_dir {args.label1}_trycycler\n' +
		f'trycycler cluster --assemblies {args.out_dir}/{args.label2}_assemblies/*.fasta --reads {args.out_dir}/{args.label2}_reads.fastq --out_dir {args.label2}_trycycler\n\n' +
		f'rm -r {args.out_dir}/read_subsets_1\n' +
		f'rm -r {args.out_dir}/read_subsets_2')
	InitialAssembly_script.close()
	os.system(f'mv InitialAssembly.sh {args.out_dir}/BatchScripts')
	os.system(f'sbatch {args.out_dir}/BatchScripts/InitialAssembly.sh')  

#===========================
# PrAsAnCo reconcile command
#===========================

if args.command == 'reconcile':
	
	if args.conda.endswith('/') == False:
		args.conda = args.conda + '/'

	if args.prasanco_dir.endswith('/') == False:
		args.prasanco_dir = args.prasanco_dir + '/'

	ReconcileScript= open('Reconcile.sh', 'w+')
	ReconcileScript.write('#!/bin/bash\n' +
		'#SBATCH --job-name=Reconcile\n' +
		'#SBATCH --nodes=1\n' +
		'#SBATCH --tasks-per-node=1\n' +
		'#SBATCH --cpus-per-task=4\n' +
		'#SBATCH --mem=15g\n' +
		'#SBATCH --time=48:00:00\n' +
		f'#SBATCH --output={args.prasanco_dir}BatchScripts/OutErr/%x.out\n' +
		f'#SBATCH --error={args.prasanco_dir}BatchScripts/OutErr/%x.err\n\n' +
		'source $HOME/.bash_profile\n' +
		f'conda activate {args.conda}prasanco_py3\n\n')
	ReconcileScript.close()

	if type(args.clusters1) is list:
		for cluster in args.clusters1:
			AppendClusters1 = open('Reconcile.sh', 'a')
			AppendClusters1.write(f'trycycler --reads {args.prasanco_dir}{args.label1}_reads.fastq --cluster_dir {args.prasanco_dir}/{args.label1}_trycycler/{cluster}\n')
			AppendClusters1.close()

	if type(args.clusters2) is list:
		for cluster in args.clusters2:
			AppendClusters2 = open('Reconcile.sh', 'a')
			AppendClusters2.write(f'trycycler --reads {args.prasanco_dir}{args.label2} --cluster_dir {args.prasanco_dir}{args.label2}_trycycler/{cluster}\n')
			AppendClusters2.close()

	os.system('sbatch Reconcile.sh')
	os.system(f'mv Reconcile.sh {args.prasanco_dir}BatchScripts')

#=====================
# PrAsAnCo msa command
#=====================

if args.command == 'msa':

	if args.conda.endswith('/') == False:
		args.conda = args.conda + '/'

	if args.prasanco_dir.endswith('/') == False:
		args.prasanco_dir = args.prasanco_dir + '/'

    MSA_script = open('MSA.sh', 'w+')
    MSA_script.write('#!/bin/bash\n' +
        '#SBATCH --job-name=MSA\n' +
        '#SBATCH --nodes=1\n' +
        '#SBATCH --tasks-per-node=1\n' +
        '#SBATCH --cpus-per-task=4\n' +
        '#SBATCH --mem=15g\n' +
        '#SBATCH --time=48:00:00\n' +
        f'#SBATCH --output={args.prasanco_dir}BatchScripts/OutErr/%x.out\n' +
        f'#SBATCH --error={args.prasanco_dir}BatchScripts/OutErr/%x.err\n\n' +
        'source $HOME/.bash_profile\n' +
        f'conda activate {args.conda}prasanco_py3\n\n')
    MSA_script.close()

    if type(args.clusters1) is list:
        for cluster in args.clusters1:
            MSA_AppendClusters1 = open('MSA.sh', 'a')
            MSA_AppendClusters1.write(f'trycycler msa --cluster_dir {args.prasanco_dir}{args.label1}_trycycler/{cluster}\n')
            MSA_AppendClusters1.close()

    if type(args.clusters2) is list:
        for cluster in args.clusters2:
            MSA_AppendClusters2 = open('MSA.sh', 'a')
            MSA_AppendClusters2.write(f'trycycler msa --cluster_dir {args.prasanco_dir}{args.label2}_trycycler/{cluster}\n')
            MSA_AppendClusters2.close()

    os.system('sbatch MSA.sh')
    os.system(f'mv MSA.sh {args.prasanco_dir}BatchScripts')

#================================
# PrAsAnCo final_assembly command
#================================

if args.command == 'final_assembly':

	if args.conda.endswith('/') == False:
		args.conda = args.conda + '/'

	if args.prasanco_dir.endswith('/') == False:
		args.prasanco_dir = args.prasanco_dir + '/'

	FinalAssemblyScript = open('FinalAssembly.sh', 'w+')
	FinalAssemblyScript.write('#!/bin/bash\n' +
		'#SBATCH --job-name=FinalAssembly\n' +
		'#SBATCH --nodes=1\n' +
		'#SBATCH --tasks-per-node=1\n' +
		'#SBATCH --cpus-per-task=4\n' +
		'#SBATCH --mem=15g\n' +
		'#SBATCH --time=48:00:00\n' +
		f'#SBATCH --output={args.prasanco_dir}BatchScripts/OutErr/%x.out\n' +
		f'#SBATCH --error={args.prasanco_dir}BatchScripts/OutErr/%x.err\n\n' +
		'source $HOME/.bash_profile\n' +
		f'conda activate {args.conda}prasanco_py3\n\n' +
		f'trycycler partition --reads {args.prasanco_dir}{args.label1}_reads.fastq --cluster_dirs {args.prasanco_dir}{label1}_trycycler/cluster_*\n' +
		f'trycycler partition --reads {args.prasanco_dir}{args.label2}_reads.fastq --cluster_dirs {args.prasanco_dir}{label2}_trycycler/cluster_*\n\n')
	FinalAssemblyScript.close()

	for cluster in args.cluster1:
		FinalAssembly_AppendClusters1 = open('FinalAssembly.sh', 'a')
		FinalAssembly_AppendClusters1.write(f'trycycler consensus --cluster_dir {args.prasanco_dir}{label1}_trycycler/{cluster} --threads {args.threads}\n')
		FinalAssembly_AppendClusters1.close()

	for cluster in args.cluster2:
		FinalAssembly_AppendClusters2 = open('FinalAssembly.sh', 'a')
		FinalAssembly_AppendClusters2.write(f'trycycler consensus --cluster_dir {args.prasanco_dir}{label2}_trycycler/{cluster} --threads {args.threads}\n')
		FinalAssembly_AppendClusters2.close()

	FinalAssemblyScript2 = open('FinalAssembly.sh', 'a')
	FinalAssemblyScript2.write('\n' +
		f'cat {args.prasanco_dir}{label1}_trycycler/cluster_*/7_final_consensus.fasta > {args.prasanco_dir}{label1}_trycycler/consensus.fasta\n' +
		f'cat {args.prasanco_dir}{label2}_trycycler/cluster_*/7_final_consensus.fasta > {args.prasanco_dir}{label2}_trycycler/consensus.fasta\n\n' +
		'conda deactivate\n' +
		f'conda activate {args.conda}/prasanco_py2\n\n' +
		f'for c in {args.prasanco_dir}{label1}_trycycler/cluster_*; do\n' +
		'medaka_consensus -i "$c"/4_reads.fastq -d "$c"/7_final_consensus.fasta -o "$c"/medaka -m r941_min_sup_g507 -t 12\n' +
		'mv "$c"/medaka/consensus.fasta "$c"/8_medaka.fasta\n' +
		'rm -r "$c"/medaka "$c"/*.fai "$c"/*.mmi\n' +
		'done\n\n' +
		f'for c in {args.prasanco_dir}{label2}_trycycler/cluster_*; do\n' +
		'medaka_consensus -i "$c"/4_reads.fastq -d "$c"/7_final_consensus.fasta -o "$c"/medaka -m r941_min_sup_g507 -t 12\n' +
		'mv "$c"/medaka/consensus.fasta "$c"/8_medaka.fasta\n' +
		'rm -r "$c"/medaka "$c"/*.fai "$c"/*.mmi\n' +
		'done\n\n' + 
		f'cat {args.prasanco_dir}{args.label1}_trycycler/cluster_*/8_medaka.fasta > {args.prasanco_dir}{args,label1}_trycycler/consensus.fasta\n' +
		f'cat {args.prasanco_dir}{args.label2}_trycycler/cluster_*/8_medaka.fasta > {args.prasanco_dir}{args,label2}_trycycler/consensus.fasta\n\n' +
		'conda deactivate\n' +
		f'conda activate {args.conda}/prasanco_py3'
		f'fastp --in1 {args.short1_R1} --in2 {args.short1_R2} --out1 {args.prasanco_dir}{args.label1}_1.fastq.gz --out2 {args.prasanco_dir}{args.label1}_2.fastq.gz --unpaired1 {args.prasanco_dir}{args.label1}_u.fastq.gz --unpaired2 {args.prasanco_dir}{args.label1}_u.fastq.gz \n' +
		f'fastp --in1 {args.short2_R1} --in2 {args.short2_R2} --out1 {args.prasanco_dir}{args.label2}_1.fastq.gz --out2 {args.prasanco_dir}{args.label2}_2.fastq.gz --unpaired1 {args.prasanco_dir}{args.label2}_u.fastq.gz --unpaired2 {args.prasanco_dir}{args.label2}_u.fastq.gz \n\n' +
		f'bwa index {args.prasanco_dir}{args.label1}_trycycler/consensus.fasta\n' +
		f'bwa mem -t 16 -a {args.prasanco_dir}{args.label1}_trycycler/consensus.fasta {args.prasanco_dir}{args.label1}_1.fastq.gz > {args.prasanco_dir}{args.label1}_alignments_1.sam\n' +
		f'bwa mem -t 16 -a {args.prasanco_dir}{args.label1}_trycycler/consensus.fasta {args.prasanco_dir}{args.label1}_2.fastq.gz > {args.prasanco_dir}{args.label1}_alignments_2.sam\n' +
		f'{prasanco_path}/third_party/polypolish {args.prasanco_dir}{args.label1}_trycycler/consensus.fasta {args.prasanco_dir}{args.label1}_alignments_1.sam {args.prasanco_dir}{args.label2}_alignments_2.sam > {args.prasanco_dir}{args.label1}_polypolish.fasta\n' +
		f'bwa index {args.prasanco_dir}{args.label2}_trycycler/consensus.fasta\n' +
		f'bwa mem -t 16 -a {args.prasanco_dir}{args.label2}_trycycler/consensus.fasta {args.prasanco_dir}{args.label2}_1.fastq.gz > {args.prasanco_dir}{args.label2}_alignments_1.sam\n' +
		f'bwa mem -t 16 -a {args.prasanco_dir}{args.label2}_trycycler/consensus.fasta {args.prasanco_dir}{args.label2}_2.fastq.gz > {args.prasanco_dir}{args.label2}_alignments_2.sam\n' +
		f'{prasanco_path}/third_party/polypolish {args.prasanco_dir}{args.label2}_trycycler/consensus.fasta {args.prasanco_dir}{args.label2}_alignments_1.sam {args.prasanco_dir}{args.label2}_alignments_2.sam > {args.prasanco_dir}{args.label2}_polypolish.fasta\n\n' +
		f'polca.sh -a {args.prasanco_dir}{args.label1}_polypolish.fasta -r "{args.prasanco_dir}{args.label1}_1.fastq.gz {args.prasanco_dir}{args.label1}_2.fastq.gz" -t 16 -m 1G\n' +
		f'mv .PolcaCorrected.fa {args.prasanco_dir}{args.label1}_final_assembly.fasta\n' +
		f'polca.sh -a {args.prasanco_dir}{args.label2}_polypolish.fasta -r "{args.prasanco_dir}{args.label2}_1.fastq.gz {args.prasanco_dir}{args.label2}_2.fastq.gz" -t 16 -m 1G\n' +
		f'mv *.PolcaCorrected.fa {args.prasanco_dir}{args.label2}_final_assembly.fasta')
	FinalAssemblyScript.close()

	os.system('sbatch FinalAssembly.sh')
	os.system(f'mv FinalAssembly.sh {args.prasanco_dir}/BatchScripts')

#====================
# PrAsAnCo QC command
#====================

if args.command == 'QC':

	if args.conda.endswith('/') == False:
		args.conda = args.conda + '/'

	if args.prasanco_dir.endswith('/') == False:
		args.prasanco_dir = args.prasanco_dir + '/'

	os.system(f'mkdir {args.prasanco_dir}QC')

	QC_Script = open('QC.sh', 'w+')
	QC_Script.write('#!/bin/bash\n' +
		'#SBATCH --job-name=QC\n' +
		'#SBATCH --nodes=1\n' +
		'#SBATCH --tasks-per-node=1\n' +
		'#SBATCH --cpus-per-task=4\n' +
		'#SBATCH --mem=15g\n' +
		'#SBATCH --time=48:00:00\n' +
		f'#SBATCH --output={args.prasanco_dir}BatchScripts/OutErr/%x.out\n' +
		f'#SBATCH --error={args.prasanco_dir}BatchScripts/OutErr/%x.err\n\n' +
		'source $HOME/.bash_profile\n' +
		f'conda activate {args.conda}prasanco_py2\n\n' +
		f'quast -o {args.prasanco_dir}QC/{args.label1}_QUAST -r {args.reference} --glimmer {args.prasanco_dir}{args.label1}_final_assembly.fasta\n' +
		f'quast -o {args.prasanco_dir}QC/{args.label2}_QUAST -r {args.reference} --glimmer {args.prasanco_dir}{args.label2}_final_assembly.fasta\n\n' +
		'conda deactivate\n' +
		f'conda activate {args.conda}prasanco_py3' +
		f'busco -m genome -i {args.prasanco_dir}{args.label1}_final_assembly.fasta -o {args.prasanco_dir}QC/{args.label1}_BUSCO --auto-lineage-prok --out-path {args.prasanco_dir}QC --update-data\n' +
		f'busco -m genome -i {args.prasanco_dir}{args.label2}_final_assembly.fasta -o {args.prasanco_dir}QC/{args.label2}_BUSCO --auto-lineage-prok --out-path {args.prasanco_dir}QC --update-data')
	QC_Script.close()

	os.system('sbatch QC.sh')
	os.system(f'mv QC.sh {args.prasanco_dir}BatchScripts')

#==========================
# PrAsAnCo annotate command
#==========================

if args.command == 'annotate':
	
	if args.conda.endswith('/') == False:
		args.conda = args.conda + '/'

	if args.prasanco_dir.endswith('/') == False:
		args.prasanco_dir = args.prasanco_dir + '/'

	AnnotateScript= open('Annotate.sh', 'w+')
	AnnotateScript.write('#!/bin/bash\n' +
		'#SBATCH --job-name=Annotate\n' +
		'#SBATCH --nodes=1\n' +
		'#SBATCH --tasks-per-node=1\n' +
		'#SBATCH --cpus-per-task=4\n' +
		'#SBATCH --mem=15g\n' +
		'#SBATCH --time=48:00:00\n' +
		f'#SBATCH --output={args.prasanco_dir}BatchScripts/OutErr/%x.out\n' +
		f'#SBATCH --error={args.prasanco_dir}BatchScripts/OutErr/%x.err\n\n' +
		'source $HOME/.bash_profile\n' +
		f'conda activate {args.conda}prasanco_py3\n\n' +
		f'prokka --outdir {args.prasanco_dir}{args.label1}_PROKKA --force --prefix {args.label1} --kingdom {args.kingdom} --genus {args.genus} --species {args.species} --usegenus {args.assembly1}\n' +
		f'prokka --outdir {args.prasanco_dir}{args.label2}_PROKKA --force --prefix {args.label2} --kingdom {args.kingdom} --genus {args.genus} --species {args.species} --usegenus {args.assembly2}\n')
	AnnotateScript.close()

	os.system('sbatch Annotate.sh')
	os.system(f'mv Annotate.sh {args.prasanco_dir}BatchScripts')
	
