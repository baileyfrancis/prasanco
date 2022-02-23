# PRASANCO (Prokaryotic Assembly Annotation and Comparison Tool)
PrAsAnCo (**Pr**okaryotic **As**sembly **An**notation and **Co**mparison Tool) is a pipeline designed specifically for prokaryotic genome assembly, annotation and comparison of two input datasets. PrAsAnCo uses both short-read Illumina data and long-read Oxford Nanopore data to generate a polished assembly for both input samples using Trycycler. The quality and completeness of each assembly is then assessed using QUAST and BUSCO. Annotation of both assemblies is achieved using PROKKA. Finally, PrAsAnCo creates human readable comparison tables for the quality, completeness and annotations between the two assemblies. 

## Installation 

### Install PrAsAnCo with Conda 
Unfortunately, PrAsAnCo cannot be run using a single Conda environment. This is because third-party tools that PrAsAnCo uses require conflicting versions of Python. Therefore, before you run PrAsAnCo, you should create the two PrAsAnCo Conda environments using the commands shown below:

```
cd prasanco
conda env create --name prasanco_py3 --file ./conda/prasanco_py3.yml 
conda env create --name prasanco_py2 --file ./conda/prasanco_py2.yml
```

Due to PrAsAnCo using two different Conda environments, please ensure you provide PrAsAnCo with the path to your conda/miniconda directory using `prasanco --conda [path]`. This allows PrAsAnCo to activate each of its Conda environments when they are needed. 

## Usage 

### Step 1 - Initial assembly 
To assemble your long-read data, PrAsAnCo uses [Trycycler](https://github.com/rrwick/Trycycler). The first step in this Trycycler pipeline is to generate some initial assemblies for your genomes using [Flye](https://github.com/fenderglass/Flye), [Miniasm+Minipolish](https://github.com/rrwick/Minipolish) and [Raven](https://github.com/lbcb-sci/raven). These initial assemblies are then used by Trycycler to cluster your long reads into contigs - you will need these contigs for the next steps.

### Command
To run the initial assembly step please use the command shown here: (options are described in further detail below)

`[path to prasanco]/prasanco.py initial_assembly --label1 x --label2 x --reads1 x --reads2 x --threads x --conda x --out_dir x` 

#### Options 

