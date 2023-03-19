from Bio import SeqIO
from Bio import Align


def alignment(seq, database):
    """
    - Input: an unknown sequence in fasta format, and a database of known sequence as a fasta iterator
    
    - Creates alignments of the target sequence to each sequence in the database
    - Calculates a score for the number of aligned amino acids between the target sequence and the database 
    - Stores the scores in a list 
    
    - Output: a list of alignment scores 
    """
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
        seq_length = len(i)
        lengths.append(seq_length)
    return lengths


def percent_id(alignment_scores, db_lengths):
    ## Calculates the percentage identity of the target to each sequence in the database
    ## Takes the alignent scores from the alignment function and the sequence lengths from the 
    ## seq_lens function
    percent_id_list = []
    for s, l in zip(alignment_scores, db_lengths):
        perc_id =  s/ l * 100
        percent_id_list.append(perc_id) 
    return percent_id_list

def final_output(p_id_list, database_file):
## Find the highest sequence identity and return the resulting sequence along with the dog breed
    max_p_id = max(p_id_list)
    max_index = p_id_list.index(max_p_id)
    percentage_difference = 100 - max_p_id
    for i, record in enumerate(SeqIO.parse(database_file, "fasta")):
        if i == max_index: 
            description = record.description
            split = description.split(']')
            breed = split[6]
            breed = breed[8:]
            new_line = '\n'
            return f'Closest matching dog breed:{breed}{new_line}% difference:{percentage_difference}{new_line}sequence of matching breed:{record.seq}'


database = 'data/dog_breeds.fa'
print(final_output([99, 50, 25], database))


            



