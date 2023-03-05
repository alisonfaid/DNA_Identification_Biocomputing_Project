
from Bio import SeqIO
from Bio import Align
from Bio.Seq import Seq

dog_breeds = 'data/dog_breeds.fa'
dog_breeds = SeqIO.parse(dog_breeds, 'fasta')
scores = [16695.0, 16689.0, 16688.0, 16689.0, 16706.0, 16706.0, 16688.0, 16709.0, 16705.0, 16690.0, 16688.0, 16704.0, 16704.0, 16704.0, 16704.0, 16704.0, 16704.0, 16704.0, 16704.0, 16704.0, 16687.0, 16689.0, 16687.0, 16687.0, 16689.0, 16687.0, 16704.0, 16707.0, 16686.0, 16688.0, 16688.0, 16688.0, 16707.0, 16688.0, 16702.0, 16696.0, 16694.0, 16706.0, 16704.0, 16703.0, 16706.0, 16693.0, 16705.0, 16705.0, 16703.0, 16703.0, 16703.0, 16693.0, 16693.0, 16693.0, 16693.0, 16693.0, 16704.0, 16704.0, 16704.0, 16702.0, 16702.0, 16702.0, 16702.0, 16691.0, 16692.0, 16692.0, 16701.0, 16693.0, 16703.0, 16701.0, 16703.0, 16703.0, 16701.0, 16701.0, 16701.0, 16701.0, 16703.0, 16691.0, 16691.0, 16700.0, 16700.0, 16692.0, 16692.0, 16702.0, 16700.0, 16702.0, 16695.0, 16699.0, 16699.0, 16691.0, 16699.0, 16688.0, 16683.0, 16690.0, 16704.0, 16689.0, 16689.0, 16711.0, 16688.0, 16685.0, 16688.0, 16686.0, 16683.0]


    
def seq_lens(database):
    lengths = []
    for i in database:
        seq_length = len(i)
        lengths.append(seq_length)
    return lengths

def p_identity(alignment_scores, db_lengths):
    ## DOCSTRING
    percent_id_list = []
    for s, l in zip(alignment_scores, db_lengths):
        perc_id =  s/ l * 100
        percent_id_list.append(perc_id) 
    return percent_id_list

sequence_lengths = seq_lens(dog_breeds)
percentage_identity = p_identity(scores, sequence_lengths)
print(percentage_identity)