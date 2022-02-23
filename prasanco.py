# Import required modules
import argparse 
import os

# Extract useful information for use downstream 
cwd = os.getcwd()

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

args = parser.parse_args()

#==================================
# PrAsAnCo initial_assembly command
#==================================

if args.command == 'initial_assembly':
	
	os.mkdir(args.out_dir) # Create an ouput directory for the initial assembly
	os.mkdir(f'{args.out_dir}/BatchScripts')
	os.mkdir(f'{args.out_dir}/BatchScripts/OutErr')
	
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
		f'trycycler subsample --reads {args.label1}_reads.fastq --out_dir {args.out_dir}/read_subsets_1\n' +
		f'trycycler subsample --reads {args.label2}_reads.fastq --out_dir {args.out_dir}/read_subsets_2\n\n' +
		f'mkdir {args.out_dir}/{args.label1}_assemblies\n' +
		f'mkdir {args.out_dir}/{args.label2}_assemblies\n' +
		f'flye --nano-hq {args.out_dir}/read_subsets_1/sample_01.fastq --threads {args.threads} --out-dir assembly01 && cp assembly01/assembly.fasta {args.out_dir}/{args.label1}_assemblies/assembly_01.fasta && rm -r assembly_01\n' +
		f'{cwd}/third_party/miniasm_and_minipolish.sh {args.out_dir}/read_subsets_1/sample_02.fastq {args.threads} > assembly_02.gfa && any2fasta assembly_02.gfa > {args.out_dir}/{args.label1}_assemblies/assembly_02.fastra && rm assembly_02.gfa\n' +
		f'raven --threads {args.threads} {args.out_dir}/read_subsets_1/sample_03.fastq > {args.out_dir}/{args.label1}_assemblies/assembly_03.fasta && rm raven.cereal')
	InitialAssembly_script.close()
	os.system(f'mv InitialAssembly.sh {args.out_dir}/BatchScripts')
	os.system(f'sbatch {args.out_dir}/InitialAssembly.sh') 