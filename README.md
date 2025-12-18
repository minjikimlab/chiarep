# HiChIA-Rep
A package for quantifying the similarity between chromatin interactions data enriched for protein binding sites or open chromatin regions (e.g. ChIA-PET, HiChIP, ChIATAC, HiCAR and related data).

    
## Methods Overview 
### Data

**Chromatin Structure**\
The chromatin structure is assumed to be a `.hic` file (with normalization="NONE" available) or a `.bedpe` file that is commonly used to store the "loops" of processed ChIA-PET experiments. The toggle between these two files is available as the parameter `use_bedpe` in the `commands.py make-sample-input-file` program. The program bins the chromatin structure data at a specified resolution into an $N \times N$ adjacency matrix with $N$ being the number of nodes, that is the number of bins in a given window. The adjacency matrix $A$ should contain *integer counts* where $A_{ij}$ is the number of inter-ligated fragments captured between binned genomic loci $i$ and $j$. This matrix is symmetric and non-negative and may contain isolated nodes due to centromeres and telomeres. 

**Binding Affinity**\
The binding affinity data is assumed to be a `.bedgraph` file and represents either the protein enrichment level (e.g. ChIA-PET) or the level of accessibility (e.g. ChIATAC). The program bins the binding affinity data at a specified resolution into an $N$-dimensional vector with $N$ being the number of nodes, that is the number of bins in a given window. This vector $b$ should similarly contain *integer counts* where $b_i$ is the number of captured fragments aligning to binned genomic locus $i$. This vector is non-negative. If the values are not integer counts and contain floating point values between 0 and 1, then it is recommended to multiply the binding affinity values by a large fixed constant, which can be specified via the `ba_mult` parameter. 

### Preprocessing  
- TODO
    
### Graph signal processing comparison
- TODO
    
### Example
- TODO


## Results
- HiChIA-Rep can clearly distinguish between replicates and non-replicates
- For a threshold, we recommend (?)
    
## Usage 
### Dependencies:
Make a conda environment using `environment.yml`.
```
name: hichia-env
channels:
  - conda-forge
dependencies:
  - python=3.10
  - numpy>=2.2,<2.3
  - scipy>=1.15,<1.16
  - matplotlib>=3.10,<3.11
  - click
  - pybedgraph>=0.5
  - pybedtools>=0.12
  - sphinx # Just for building docs
  - pip
  - pip:
      - hic-straw==1.3
```
### Installation: 
- TODO

```bash    
# Install from github
git clone https://github.com/c0ver/chia_rep.git    
pip3 install chia_rep/

# Install from pypi
pip3 install chia_rep
```

### Create Input files
- TODO

With `example/sample_list.txt` containing the following:
```
LHH0048H
LHH0054H
LHH0084H
LHH0086V
...
```
and `data/` containing bedgraph, peak, and loop files
```bash
cd example
python commands.py --help
python commands.py make-pairs --help
python commands.py make-sample-input-file --help

python commands.py make-pairs sample_list.txt pairs.txt

# Assumes (letter case doesn't matter)
# bedgraph file extension: .bedgraph
# peak files extension: .broadpeak
# loop files extension: .cis.be3
# Creates sample_input_file.txt
python commands.py make-sample-input-file sample_list.txt sample_input_file.txt data/
```

    
### Run script
- TODO

Example script is included in `example/script.py`.
```bash
cd example
python script.py --help

# Example usages
python script.py sample_input_file.txt hg38.chrom.sizes pairs.txt 3000000 5000 chr1
python script.py sample_input_file.txt hg38.chrom.sizes pairs.txt 3000000 5000 all
python script.py sample_input_file.txt hg38.chrom.sizes pairs.txt 3000000 5000 chr1 chr2
```

### Documentation
Included in docs/build/html

## Contact
Contact Minji (minjilab@umich.edu) for general questions or Sion (sionkim@umich.edu). 
