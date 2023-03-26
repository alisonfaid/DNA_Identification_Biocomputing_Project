from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib.pyplot as plt
import matplotlib as mpl

mystery_file = 'data/mystery.fa'
dog_breeds_file = 'data/dog_breeds.fa'


alignment = AlignIO.read(dog_breeds_file, 'fasta')


calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)


constructor = DistanceTreeConstructor(calculator)
tree = constructor.build_tree(alignment)



fig = plt.figure(figsize=(13, 20), dpi=100) # create figure & set the size 
plt.rc('font', size=12)             # fontsize of the leaf and node labels 
plt.rc('xtick', labelsize=10)       # fontsize of the tick labels
plt.rc('ytick', labelsize=10)       # fontsize of the tick labels
#turtle_tree.ladderize()		   # optional way to reformat your tree 
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(tree, axes=axes)
#fig.savefig("turtles_cladogram")
    





