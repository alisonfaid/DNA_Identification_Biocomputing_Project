Project Title
==
DNA identification tool for comparing an unknown sequence to multiple sequences in a database 
==

Project Description
==
This is a program which compares an input sequence to a database containing multiple sequences of the same length. The program identifies which sequence in the database is most similar to the input sequence and outputs information about the most similar sequence, the percentage difference between the target and database sequence, and the matching sequence itself. 

The program will also use z-scores from the alignment scores generated to calculate p-values for all of the sequences in the database. 

A phylogenetic tree will also be created containing all the sequences in the database and the target sequence. The branch of the target sequence will be colored in red so it is easily seen by the user. 
==

How to run the program
==
Python modules used by this program:
    - Biopython
    - Numpy 
    - Matplotlib 
    - Scipy 

To run program, please ensure these have been installed, one method is via pip from the command line:

    pip install biopython
    pip install numpy
    pip install matplotlib
    pip install scipy
==

How to use the program 
==
There are 3 modules in the program: 
    - dna_identification
    - probabilities
    - phylogenetic_tree

All of these modules are ran in the main.py file to output the information stated in the project description.

This project is currently supported for files in .fasta format - please modify as needed for other file formats. 
The phylogenetic_tree module assumes the database sequences are already aligned and that the target sequence is of the same length as the database sequences. A multple sequence alignment function would need to be added for any sequences which are not already aligned, or an MSA would need to be done externally. 
This database has been tested with a database containing sequences for diferent dog breeds, therefore part of the output contains the dog breed name - if this is not wanted please remove from final_output function in dna_identification and from p-value function in probabilities. 
