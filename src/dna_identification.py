from Bio import SeqIO
from Bio import Align

def read_target_file(target_seq):
    """ Reads the file containing the target sequence

    Args:
        target_seq (.fasta file): target sequence file in fasta format

    Returns:
        SeqRecord: target sequence
    """
    seq = SeqIO.read(target_seq, 'fasta')
    return seq

def parse_database_file(database):
    """Reads in the database file and creates FastaIterator

    Args:
        database (.fasta file): file containing multiple sequences to compare to the target
            sequence

    Returns:
        FastaIterator: database sequences
    """
    data = SeqIO.parse(database, 'fasta')
    return data 



def alignment(unknown_seq, database):
    """
    Summary:
    - Creates alignments of the target sequence to each sequence in the database
    - Calculates a score for the number of aligned amino acids between the 
      target sequence and the database 
    - Stores the scores in a list 

    Args:
        unknown_seq (SeqRecord): sequence to compare to sequences in the database
        database (FastaIterator): file containing multiple sequences to compare the 
            unknown_seq to 

    Returns:
        list: alignment scores for each alignment
    """
    aligner = Align.PairwiseAligner(match_score = 1.0)
    alignments = []
    for i in database:
        score = aligner.score(unknown_seq, i)
        alignments.append(score)
    return alignments


def seq_lens(database):
    """
    Summary:
    Calculates the length of each sequence in the database and stores them in a list

    Args:
        database (.fasta file): file containing multiple sequences to compare the 
            unknown_seq to 

    Returns:
        list: lengths of each sequence in the database 
    """
    lengths = []
    for i in database:
        seq_length = len(i)
        lengths.append(seq_length)
    return lengths


def percent_id(alignment_scores, seq_lengths):
    """
    Summary:
    - Calculates the percentage identity of the target to each sequence in the database
    - Takes the alignent scores from the alignment function and the sequence lengths 
      from the seq_lens function
    

    Args:
        alignment_scores (list): list of alignment scores generated by alignment function
        seq_lengths (list): sequence lengths of all sequences in the database

    Returns:
        list: percentage identities for the target to each of the sequences in the database
    """
    percent_id_list = []
    for s, l in zip(alignment_scores, seq_lengths):
        p_id =  s/ l * 100
        percent_id_list.append(p_id) 
    return percent_id_list

def final_output(percent_id_list, database):
    """
    Summary:
    - Finds the alignment with the highest sequence identity 
    - Calculates the percentage difference  

    Args:
        percent_id_list (list): Percentage identities for each alignment generated by 
            percentage identity function
        database (.fasta file): file containing multiple sequences to compare the 
            unknown_seq to

    Returns:
        string: Contains information about the closest matching dog breed, percentage
            difference, and the sequence of the closest matching breed. 
    """
    max_p_id = max(percent_id_list)
    max_index = percent_id_list.index(max_p_id)
    percentage_difference = 100 - max_p_id
    for i, record in enumerate(SeqIO.parse(database, "fasta")):
        if i == max_index: 
            description = record.description
            split = description.split(']')
            breed = split[6]
            breed = breed[8:]
            new_line = '\n'
            return f'ID: {record.id}{new_line}Closest Matching Dog Breed:{breed}{new_line}Percentage Difference:{percentage_difference}%{new_line}{breed} Sequence:{record.seq[:30]}.....{record.seq[-5:]}'





