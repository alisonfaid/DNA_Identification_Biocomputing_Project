import seq_analysis as sa
from Bio import SeqIO
from Bio import Align

mystery_file = 'data/mystery.fa'
dog_breeds_file = 'data/dog_breeds.fa'
dog_breeds_2_file = 'data/dog_breeds.fa'

mystery = SeqIO.read(mystery_file, 'fasta')
dog_breeds = SeqIO.parse(dog_breeds_file, 'fasta')
dog_breeds_2 = SeqIO.parse(dog_breeds_2_file, 'fasta')

alignments = sa.alignment(mystery, dog_breeds)
sequence_lengths = sa.seq_lens(dog_breeds_2)
percentage_id = sa.percent_id(alignments, sequence_lengths)
final = sa.final_output(percentage_id, dog_breeds_file)
print(final)