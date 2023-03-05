import seq_analysis as sa
from Bio import SeqIO
from Bio import Align

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'
dog_breeds_2 = 'data/dog_breeds.fa'

mystery = SeqIO.read(mystery, 'fasta')
dog_breeds = SeqIO.parse(dog_breeds, 'fasta')
dog_breeds_2 = SeqIO.parse(dog_breeds_2, 'fasta')

alignments = sa.alignment(mystery, dog_breeds)
sequence_lengths = sa.seq_lens(dog_breeds_2)
percentage_id = sa.p_identity(alignments, sequence_lengths)

print(percentage_id)