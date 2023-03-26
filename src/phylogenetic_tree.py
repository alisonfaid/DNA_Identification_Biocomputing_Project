from Bio import AlignIO
from Bio import SeqIO
from Bio import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib.pyplot as plt
import matplotlib as mpl

mystery_file = 'data/mystery.fa'
dog_breeds_file = 'data/dog_breeds.fa'

alignment = AlignIO.read(dog_breeds_file, 'fasta')
mystery_seq = SeqIO.read(mystery_file, 'fasta')
alignment.append(mystery_seq)

def phylogenetic_tree(alignment_file):
    """
    Creates phylogenetic tree from alignment file and plots it using matplotlib

    Args:
        alignment_file (_type_): _description_
    """
    # Create distance calculator 
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)
    
    # Create phylogenetic tree
    constructor = DistanceTreeConstructor(calculator)
    tree = constructor.build_tree(alignment)
    
    # Plot tree
    fig = plt.figure(figsize=(15, 7.5), dpi=100) 
    plt.rc('font', size=6)             
    plt.rc('xtick', labelsize=10)       
    plt.rc('ytick', labelsize=10)    
    plt.rc('axes', titlesize=14) 
    tree.ladderize()		   
    axes = fig.add_subplot(1, 1, 1)
    
    return Phylo.draw(tree, axes=axes)



phylogenetic_tree(alignment)


    





