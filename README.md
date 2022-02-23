# PRASANCO (Prokaryotic Assembly Annotation and Comparison Tool)
PrAsAnCo (**Pr**okaryotic **As**sembly **An**notation and **Co**mparison Tool) is a pipeline designed specifically for prokaryotic genome assembly, annotation and comparison of two input datasets. PrAsAnCo uses both short-read Illumina data and long-read Oxford Nanopore data to generate a polished assembly for both input samples using Trycycler. The quality and completeness of each assembly is then assessed using QUAST and BUSCO. Annotation of both assemblies is achieved using PROKKA. Finally, PrAsAnCo creates human readable comparison tables for the quality, completeness and annotations between the two assemblies. 

## Installation 

### Install PrAsAnCo on your machine 
To install PrAsAnCo, move into the directory in which you would like PrAsAnCO to be installed and simply enter the commands below in to the command-line:

```
git clone https://github.com/baileyfrancis/prasanco
cd prasanco 
chmod +x ./install.sh 
./install.sh 

```
You are now ready to use PrAsAnCo. Before you do, please ensure you have created the required Conda environments as described below.

### Install PrAsAnCo Conda environment  
Unfortunately, PrAsAnCo cannot be run using a single Conda environment. This is because third-party tools that PrAsAnCo uses require conflicting versions of Python. Therefore, before you run PrAsAnCo, you should create the two PrAsAnCo Conda environments using the commands shown below:

```
cd prasanco
conda env create --name prasanco_py3 --file ./conda/prasanco_py3.yml 
conda env create --name prasanco_py2 --file ./conda/prasanco_py2.yml
```

Due to PrAsAnCo using two different Conda environments, please ensure you provide PrAsAnCo with the path to your conda envs/ directory using `prasanco --conda [path]`. This allows PrAsAnCo to activate each of its Conda environments when they are needed. 

## Usage 

### Step 1 - Initial assembly 
To assemble your long-read data, PrAsAnCo uses [Trycycler](https://github.com/rrwick/Trycycler). The first step in this Trycycler pipeline is to generate some initial assemblies for your genomes using [Flye](https://github.com/fenderglass/Flye), [Miniasm+Minipolish](https://github.com/rrwick/Minipolish) and [Raven](https://github.com/lbcb-sci/raven). These initial assemblies are then used by Trycycler to cluster your long reads into contigs - you will need these contigs for the next steps.

#### Command
To run the initial assembly step please use the command shown here: (options are described in further detail below)

`[path to prasanco]/prasanco.py initial_assembly --label1 x --label2 x --reads1 x --reads2 x --threads x --conda x --out_dir x` 

#### Options 
Option    | Description
--------  | -----------
--label1  | Name given to all files relating to your first sample. ***Example*** --label1 SampleA -> SampleA_reads.fastq (**To avoid confusion, please keep consistent throughout the PrAsAnCo pipeline**)
--label2  | Name given to all files relating to your second sample. ***Example*** --label2 SampleB -> SampleB_reads.fastq (**To avoid confusion, please keep consistent throughout the PrAsAnCo pipeline**)
--reads1  | A single file containing Oxford Nanopore long-reads for your first sample.
--reads2  | A single file containing Oxford Nanopore long-reads for your second sample.
--threads | The number of threads to allocate to this task. **Recommended = 8**
--conda   | The absolute path to your Conda /envs directory. ***Example*** /shared/home/mbxbf2/miniconda3/envs/
--out_dir | The name given to the PrAsAnCo output directory. 

#### Outputs
When the `initial_assembly` command is run it will create a new output directory within the current working directory (This new directory will have the name assigned to it by the `--out_dir` option. 

Inside this directory you will find various ouputs: 
* **BatchScripts/** directory = directory containing all scripts PrAsAnCo uses to run. If you wish to look at the SLURM outputs for these scripts, they can be found in BatchScripts/OutErr
* **[label1]_reads.fastq** = reads for your first sample after filtering by Filtlong
* **[label2]_reads.fastq** = reads for your second sample after filtering by Filtlong
* **[label1]_assemblies/** directory = directory containing all Flye, Miniasm+Minipolish and Raven assemblies for your first sample. If everything has worked correctly, this directory should contain 12 assemblies labelled assembly_**
* **[label2]_assemblies/** directory = directory containing all Flye, Miniasm+Minipolish and Raven assemblies for your second sample. If everything has worked correctly, this directory should contain 12 assemblies labelled assembly_**
* **[label1]_trycycler/** = trycycler output directory containing contigs for your first sample
* **[label2]_trycycler/** = trycycler output directory containing contigs for your second sample

***Please ensure you have all outputs before moving on to Step 2***

#### Checking your clusters 
At this stage, you need to have a look at your clusters of contigs and assess how good they are. You can do this by viewing the phylogenetic tree of your clusters (produced by Trycycler) - this can be found in the `trycycler` directories for your samples in the `contigs.newick` file. This file can be viewed using any phylogenetic tree visualisation tool e.g. [Dendroscope](https://uni-tuebingen.de/en/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/algorithms-in-bioinformatics/software/dendroscope/).

In short, good clusters contain many contigs that are closely related to eachother, wheras a bad cluster contains few contigs. For full instructions on selecting good contigs see [this page](https://github.com/rrwick/Trycycler/wiki/Clustering-contigs) (under the 'Choose your clusters heading) . If you have any bad clusters, please rename the directory (with the mv command) e.g. `cluster_02` will become `bad_cluster_02`. Again, for further details [refer here](https://github.com/baileyfrancis/prasanco/edit/main/README.md).

***Once you have done this, please move on to Step 2***

### Step 2 - Reconciliate clusters 
After you have hand-picked your good clusters, you are ready to reconcile the contigs within them. This step of the pipeline uses the Trycycler reconile command which: checks that contigs are sufficiently similar to eachother, (if applicable) attempts to circularise them and then performs a final alignment to ensure these circular contigs are similar enough for the next step. For further details on Trycycler reconicilation, [visit this page](https://github.com/rrwick/Trycycler/wiki/Reconciling-contigs)

#### Command 
To run the PrAsAnCo reconicle step, simply navigate to your **--out_dir** from the previous step and enter the command shown below in to the command line: (options are described in further detail below)

`python [path to prasanco]/prasanco.py reconcile --label1 x --label2 x --clusters1 x --clusters2 x`

#### Options 

Option   | Description
---------|------------
--label1 | Label for the first sample. **(Please use the same label as you did for Step 1)**
--label2 |  Label for the second sample. **(Please use the same label as you did for Step 1)**
--clusters1 | Specify the clusters from your first sample you wish to reconicle e.g. --clusters1 cluster_01 cluster_03
--clusters2 | Specify the clusters from your second sample you wish to reconicle e.g. --clusters1 cluster_01 cluster_03

### First reconcile round 
This reconicilation stage may take multiple rounds to complete correctly and requires you to inspect the output of each round and assess whether you should keep/discard particular contigs. However, for the first round of this stage we want to try and reconcicle all clusters from all samples.

We can do this with the following command (in your --out_dir:

`python [path to prasanco]/prasanco.py reconcile --label1 Sample1 --label2 Sample2 --clusters1 cluster_01 cluster_02 cluster_03 ... --clusters2 cluster_01 cluster_02 cluster_03 ...`

### Additional reconcile rounds
After this reconcile round has completed, have a look at the output (found in BatchScripts/OutErr/Reconcile.err).
At this stage, you will need to decide which contigs to keep and which to discard (if needed). In general, you should remove a contig if it recieves an error message of **'unable to circularise'** or if it creates a large number of indels (both of these can be deduced from the Reconcile.err file). If a contig fufils any of these scenarios, you should navigate to its given cluster directory/1_contigs and rename it like so:

`mv A_contig.fasta A_contig.bad` 

This will remove the bad contig from the next round of reconciliation. When all the bad contigs are removed, you should see a file named `2_all_seqs.fasta` in all of your cluster's directories.

You should keep repeating this process of reconcilation, removing bad contigs, reconciliation, removing bad contigs until you have these files. I strongly recommend that you look up this reconciliation step [here](https://github.com/rrwick/Trycycler/wiki/Reconciling-contigs) to familiarise yourself with this process.

Once you have all of yout `2_all_seqs.fasta` files, you can move on to the next step. 
