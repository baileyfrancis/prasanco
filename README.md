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

### Third-party tools 
To function properly, PrAsAnCo depends on some third-party tools to carry out particular tasks. These third-party tools must be installed before you use PrAsAnCo. Installation instructions for each of the required tools can be found below: 

#### Filtlong
[Filtlong](https://github.com/rrwick/Filtlong#installation) is a tool that PrAsAnCo uses to quality check the long-read Oxford Nanopore data as part of its Trycycler hybrid assembly. To install Filtlong, use the commands down below 

```
cd prasanco (if you are not already in the prasanco directory) 
cd tools 
git clone https://github.com/rrwick/Filtlong.git
cd Filtlong
make -j
```
To ensure the Filtlong executable works correctly ****please copy it to a directory in your PATH****:

For example:

`cp bin/filtlong /usr/local/bin`

OR

`cp bin/filtlong [path to your prasanco_py3 Conda environment]/bin` 

