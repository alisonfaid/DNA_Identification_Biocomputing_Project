from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import MafftCommandline


mystery_file = r'data/mystery.fa'
dog_breeds_file = r'data/dog_breeds.fa'

in_file = dog_breeds_file
mafft_cline = MafftCommandline(input=in_file)
print(mafft_cline)
stdout, stderr = mafft_cline()
with open("aligned.fasta", "w") as handle:
    handle.write(stdout)
align = AlignIO.read("aligned.fasta", "fasta")

        
    





