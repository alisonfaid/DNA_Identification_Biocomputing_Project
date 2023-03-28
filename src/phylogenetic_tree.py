from Bio import AlignIO
from Bio import SeqIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib.pyplot as plt

def create_alignment(database, target_seq):
    """
    Summary:
    - Reads in aligned database file and target seq file 
    - Appends the target seq file to the database alignment

    Args:
        database (.fasta file): File containing multiple sequences which are already aligned
        target_seq (.fasta file): File containing the target sequence
    
    Returns: Bio.Align.MultipleSeqAlignment: Containing the database sequences and 
        target sequence

    """
    alignment = AlignIO.read(database, 'fasta')
    seq = SeqIO.read(target_seq, 'fasta')
    alignment.append(seq)
    
    return alignment

def phylogenetic_tree(alignment):
    """
    Summary:
    - Creates phylogenetic tree from alignment file and plots it using matplotlib.

    Args:
        alignment (Bio.Align.MultipleSequenceAlignment): Multiple sequence alignment 
            containing target sequence and database
    
    Return:
        matplotlib.figure.Figure: Phylogenetic tree of all sequences in the alignment with
            the target sequence highlighted in red.
    """
    # Create distance calculator 
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)
    
    # Construct phylogenetic tree
    constructor = DistanceTreeConstructor(calculator)
    tree = constructor.build_tree(alignment)
    
    # Plot tree using matplotlib 
    fig = plt.figure(figsize=(20, 7.5), dpi=100) 
    axes = fig.add_subplot(1, 1, 1)
    plt.rc('font', size=6)             
    plt.rc('xtick', labelsize=10)       
    plt.rc('ytick', labelsize=10)  
    plt.rc('axes', titlesize=10)
    plt.title('Phylogenetic Tree of Dog Breeds')  
    tree.ladderize()
    # Colour the branch of the target sequence red
    for clade in tree.get_terminals():
        if 'gb|KM061522.1|' in clade.name:
            clade.color = 'red'
    
    return Phylo.draw(tree, axes=axes)





    





