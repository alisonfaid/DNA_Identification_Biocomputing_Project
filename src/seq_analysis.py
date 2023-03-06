from Bio import SeqIO
from Bio import Align

def alignment(seq, database):
## Creates an alignment of the target sequence to each sequence in the database
## Calculates a score for the number of matches between the target sequence and the database 
## Stores the scores in a list 
    aligner = Align.PairwiseAligner(match_score = 1.0)
    alignments = []
    for i in database:
        score = aligner.score(seq, i)
        alignments.append(score)
    return alignments


def seq_lens(database):
## Calculates the length of each sequence in the reference database and stores them in a list
    lengths = []
    for i in database:
        print(i)
        seq_length = len(i)
        lengths.append(seq_length)
    return lengths


def p_identity(alignment_scores, db_lengths):
    ## Calculates the percentage identity of the target to each sequence in the database
    ## Takes the alignent scores from the alignment function and the sequence lengths from the 
    ## seq_lens function
    percent_id_list = []
    for s, l in zip(alignment_scores, db_lengths):
        perc_id =  s/ l * 100
        percent_id_list.append(perc_id) 
    return percent_id_list

def final_output():
## Find the highest sequence identity and return the resulting sequence along with the dog breed
    
    return






            



