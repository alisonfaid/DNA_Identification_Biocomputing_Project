# def percent_id(database, unknown_seq):
## (create proper description later) - This function will read in both sequences,
## split the database into individual sequences and calculate the percentage identity of the 
## unknown sequence to each of the other sequences 

mystery = 'data/mystery.fa'
dog_breeds = 'data/dog_breeds.fa'


from Bio import SeqIO
from Bio import Align

## Function that asks for the target sequence and the database to compare to and reads them both in 
#def input_files(seq_file, database_file):
## DOCSTRING

unknown_seq = SeqIO.read(mystery, 'fasta')
dog_breeds = SeqIO.parse(dog_breeds, 'fasta')
    


## Function that creates an alignment of the target sequence to each sequence in the database 
def alignment(seq, database):
## DOCSTRING
    aligner = Align.PairwiseAligner(match_score = 1.0)
    alignments = []
    for i in database:
        score = aligner.score(seq, i)
        alignments.append(score)
        
    return alignments

## Function that calculates the length of each sequence and stores them in a list 
def seq_lens(database):
    lengths = []
    for i in database:
        seq_length = len(i)
        lengths.append(seq_length)
        
    return lengths
## Function that takes a list of alignment scores and calculates the percentage identity of the target to the database sequence 
def p_identity(alignment_scores, lengths):
    ## DOCSTRING
    percent_id_list = []
    for s, l in zip(alignment_scores, lengths):
        perc_id =  alignment_scores[s]/ lengths[l]
        percent_id_list.append(perc_id) 
    return percent_id_list

## Function that outputs the most similar sequence and the % difference between the target and database seq
def final_output():
    ## DOCSTRING
    return

alignments_output = alignment(unknown_seq, dog_breeds)
sequence_lengths = seq_lens(dog_breeds)
percentage_identity = p_identity(alignments_output, sequence_lengths) 

print(percentage_identity)


# Loop that calculates the percentage identity for each of the sequences
#match = 0
#perc_id_ls = []
#for seq in database:
#    for i in range(0, len(seq)):
#        if seq[i] == unknown_seq[i]:
#            match += 1
#        else:
 #           match += 0
#    perc_id = match / len(seq) 
#   perc_id_ls.append(perc_id)

#print(max(perc_id_ls))

            



