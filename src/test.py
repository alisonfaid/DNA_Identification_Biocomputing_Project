
from Bio import SeqIO
from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dog_breeds_file = 'data/dog_breeds.fa'
#dog_breeds = SeqIO.parse(dog_breeds_file, 'fasta')

mystery = 'data/mystery.fa'
mystery_seq = SeqIO.read(mystery, 'fasta')
print(mystery_seq)

for i, seq_record in enumerate(SeqIO.parse(dog_breeds_file, "fasta")):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))


#seq_file = SeqIO.write([mystery_seq, dog_breeds], 'seq_file.fasta', 'fasta')
    