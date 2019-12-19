# Functional Genomic Experiments Utilities

A set of python modules to parse and process data
from different types of Functional Genomic Experiments

Some modules can be invoked on the command line as a script. 

```
Example - running the gen_matrix module 
    python -m matrix.gen_matrix  -i "path2/*file_suffix" -j index
    python -m matrix.gen_matrix -h # for details
```

## Install

You have two options - either you git clone the repos or you use pip install

### PIP Install
```
  - Test Version: pip install -i https://test.pypi.org/simple/ fungene-mdibl
```
### Git Clone
```
  1) git clone https://github.com/mdibl/fungene.git
  2) then cd to fungene
```

## Current Modules

### Runs As A Script from a command line
- [Matrix Generator](#gen_matrix)

### Runs trough import
- [Matrix Module](#matrix)

## gen_matrix

This tool generates a matrix given and  input array of text files and the target
column index and stored the resulting matrix file under the specified destdir.
If the destdir is not specified, the resulting files are stored in the the program's
base directory(program working directory)

In addition the the matrix file, the tool also generates a log
file that contains a summary of the process.

### Dependencies
 - Pandas 
 - Numpy

### Usage

```
 Usage: PROG [-h] --infiles="files" --outdir=path2/output_prefix --jindex=indexOfColumnValues 
        [--prefix=results_prefix] [--vindex=indexOfRowIDs] [--round]

 Where:
     -h To show the usage
     -i path2/files Or --infiles=path2/files  ... required, 
        specifies a commas-separated(or a wildcard)list of input files (takes wildcard)
     -o path2/output_dir Or  --outdir=path2/output_dir ... required, 
        default results dir is working directory
     -j indexOfColumnValues or --jindex=indexOfColumnValues ... required, 
        specifies the column index of the values 
     -p result_prefix  Or --prefix=results_prefix  ... optional default gen_matrix
        specifies the the name of the results file
     -v indexOfRowIDs or --vindex=indexOfRowIDs ... optional default first column(index=0)  
     --round or -r   
      
 Notes: You MUST enclose the input files argument within the "" since it could 
        contain wildcard or space between files.

 Output: Generate a matrix file under the path2 part of --outdir - 
         where the format of the results file is output_prefix.jindex_column_name.matrix.txt 

 Example running from a git cloned/exported repos: 
       python PROG  -i "input_path2/project1/*.genes.resutls" -o out_path2/project1/genes --prefix=genes_matrix -j 4 
       OR 
       python PROG --infiles="input_path2/project1/*.genes.results" --outdir=out_path2/project1/genes -p genes_matrix --jindex=4
       OR
       python PROG  -i "input_patH2/f1.genes.resutls,input_patH2/f1.genes.resutls" -o out_path2/project1/genes -p genes_matrix -j 4 
           
  Where:
  - if running as a script from git repos, PROG is "gen_matrix.py" 
  - if running as a module from pip install, PROG is "-m gen_matrix" 

 ASSUMPTIONS: 
       1) User has full permission to create the results directory specified in destdir
       2) Note that the input files argument MUST be enclosed within the quote ""
```


